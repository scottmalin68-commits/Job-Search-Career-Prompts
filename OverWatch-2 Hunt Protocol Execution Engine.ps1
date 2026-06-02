<#
.SYNOPSIS
    Project OverWatch - Phase 2: Hiring Manager Hunt Protocol Execution Engine (v2.0.1)

.DESCRIPTION
    Structured OSINT collection engine that uses Gemini grounded search to extract
    verified decision-maker leads in strict JSON format. Outputs normalized intelligence
    ready for downstream Phase 3 action planning.

.CHANGELOG
    v2.0.1
    - Fixed nested object mapping mismatch inside main loop ($json.leads extraction).
    - Added regex sanitization layer to strip markdown code fences (```json) before parsing.
    - Migrated Gemini output contract to STRICT JSON (no prose mode).
    - Introduced deduplication engine (LinkedIn URL primary key).
    - Preserved raw + structured dual-layer storage.
#>

# ==============================================================================
# CONFIGURATION
# ==============================================================================
$GeminiApiKey = [System.Environment]::GetEnvironmentVariable("GEMINI_API_KEY")

if (-not $GeminiApiKey) {
    Write-Error "Missing GEMINI_API_KEY environment variable."
    return
}

$QueryLogFile = "C:\Users\YOUR_USERNAME\Documents\google_query_log.txt"

$PacingDelaySeconds = 30
$MaxRetryAttempts   = 3
$InitialRetryDelay  = 30

# ==============================================================================
# GEMINI JSON CONTRACT (STRICT MODE)
# ==============================================================================
$SystemInstruction = @"
You are a strict OSINT extraction engine.

Return ONLY valid JSON.

Schema:
{
  "leads": [
    {
      "name": string|null,
      "title": string|null,
      "company": string|null,
      "linkedin_url": string|null,
      "source_evidence": string|null,
      "confidence": "High" | "Medium" | "Low" | null
    }
  ]
}

Rules:
- Use ONLY verified data from search results.
- Do NOT infer missing fields.
- Do NOT fabricate profiles or URLs.
- If no results found, return: { "leads": [] }
- No commentary, no markdown, no prose.
"@

# ==============================================================================
# FILE SELECTION
# ==============================================================================
function Select-TargetMarkdownFile {
    Add-Type -AssemblyName System.Windows.Forms

    $FileBrowser = New-Object System.Windows.Forms.OpenFileDialog -Property @{
        Title  = "Select File Containing Search Strings"
        Filter = "Markdown/Text (*.md;*.txt)|*.md;*.txt|All Files (*.*)|*.*"
    }

    if ($FileBrowser.ShowDialog() -eq "OK") {
        return $FileBrowser.FileName
    }

    return $null
}

# ==============================================================================
# QUERY EXTRACTION
# ==============================================================================
function Get-SearchStrings {
    param([string]$FilePath)

    $content = Get-Content $FilePath -Raw

    $pattern = "(?s)\`\`\`(?:markdown|text)?\s*(.*?)\s*\`\`\`"
    $match = [regex]::Match($content, $pattern)

    $textBlock = if ($match.Success) { $match.Groups[1].Value } else { $content }

    $lines = $textBlock -split "`r?`n"

    $queries = @()
    $i = 1

    foreach ($line in $lines) {
        $q = $line.Trim() -replace "^[\*\-\d\.\s]+", ""
        if ($q -match "^site:linkedin\.com") {
            $queries += [PSCustomObject]@{
                Label = "Vector $i"
                Query = $q
            }
            $i++
        }
    }

    return $queries
}

# ==============================================================================
# GEMINI CALL (STRICT JSON MODE)
# ==============================================================================
function Invoke-GroundedSearch {
    param(
        [string]$Query,
        [string]$ApiKey
    )

    $uri = "[https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=$ApiKey](https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=$ApiKey)"

    $body = @{
        contents = @(
            @{
                parts = @(
                    @{
                        text = "$SystemInstruction`n`nQuery: $Query"
                    }
                )
            }
        )
        tools = @(
            @{ google_search = @{} }
        )
    } | ConvertTo-Json -Depth 10

    for ($attempt = 1; $attempt -le $MaxRetryAttempts; $attempt++) {

        try {
            Write-Host "Query attempt $attempt : $Query" -ForegroundColor Yellow

            $response = Invoke-RestMethod -Uri $uri -Method Post -Body $body -ContentType "application/json"

            $text = $response.candidates[0].content.parts[0].text

            # SANITIZATION LAYER: Strip structural markdown enclosures if returned
            $cleanText = $text -replace "(?ms)^\s*\`\`\`(?:json)?\s*", ""
            $cleanText = $cleanText -replace "\`\`\`\s*$", ""
            
            # STRICT JSON PARSE
            $json = $cleanText.Trim() | ConvertFrom-Json -ErrorAction Stop

            return $json
        }
        catch {
            Write-Warning "Attempt $attempt failed: $($_.Exception.Message)"

            if ($attempt -lt $MaxRetryAttempts) {
                Start-Sleep -Seconds ($InitialRetryDelay * $attempt)
            }
        }
    }

    return @{ leads = @() }
}

# ==============================================================================
# LOGGING
# ==============================================================================
function Add-QueryLog {
    param([string]$LogPath, [string]$Query)

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $LogPath -Value "[$timestamp] $Query"
}

# ==============================================================================
# DEDUPLICATION ENGINE
# ==============================================================================
function Merge-Leads {
    param([array]$LeadGroups)

    $map = @{}

    foreach ($group in $LeadGroups) {
        foreach ($lead in $group.Leads) {

            if (-not $lead.linkedin_url) { continue }

            if (-not $map.ContainsKey($lead.linkedin_url)) {
                $map[$lead.linkedin_url] = $lead
                $map[$lead.linkedin_url] | Add-Member -NotePropertyName SourceVectors -NotePropertyValue @() -Force
            }

            $map[$lead.linkedin_url].SourceVectors += $group.VectorLabel
        }
    }

    return $map.Values
}

# ==============================================================================
# EXPORT
# ==============================================================================
function Export-ResultsToJSON {
    param(
        [string]$SourceFilePath,
        [array]$LeadGroups,
        [array]$RawResults
    )

    $date = Get-Date -Format "yyyy-MM-dd"
    $outPath = Join-Path (Split-Path $SourceFilePath) "OverwatchReport-$date.json"

    $leads = Merge-Leads $LeadGroups

    $payload = [PSCustomObject]@{
        Project           = "Project OverWatch"
        Phase             = 2
        ExecutionTime     = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        SourceFile        = Split-Path $SourceFilePath -Leaf
        TotalQueriesRun   = $LeadGroups.Count

        Leads             = $leads

        RawSearchResults  = $RawResults
    }

    $payload | ConvertTo-Json -Depth 12 | Set-Content $outPath -Encoding UTF8

    Write-Host "Exported: $outPath" -ForegroundColor Green
}

# ==============================================================================
# MAIN
# ==============================================================================
function Main {

    Write-Host "PROJECT OVERWATCH PHASE 2 v2.0.1 STARTING" -ForegroundColor Cyan

    $file = Select-TargetMarkdownFile
    if (-not $file) { return }

    $queries = Get-SearchStrings $file
    if ($queries.Count -eq 0) {
        Write-Warning "No valid queries found"
        return
    }

    $results = @()

    for ($i = 0; $i -lt $queries.Count; $i++) {

        $q = $queries[$i]

        Add-QueryLog $QueryLogFile $q.Query

        $json = Invoke-GroundedSearch -Query $q.Query -ApiKey $GeminiApiKey

        # FIXED: Directly un-nested the .leads array out of the root container
        $results += [PSCustomObject]@{
            VectorLabel = $q.Label
            Query       = $q.Query
            Leads       = $json.leads
        }

        if ($i -lt $queries.Count - 1) {
            Start-Sleep -Seconds $PacingDelaySeconds
        }
    }

    Export-ResultsToJSON -SourceFilePath $file -LeadGroups $results -RawResults $results
}

Main