<#
.SYNOPSIS
    Project OverWatch - Phase 2: Hiring Manager Hunt Protocol Execution Engine (v2.1.6)

.DESCRIPTION
    Structured OSINT collection engine that uses Gemini grounded search to extract
    verified decision-maker leads. Outputs normalized intelligence ready for downstream Phase 3.

.CHANGELOG
    v2.1.6
    - Added an upfront absolute Estimated Completion Time timestamp calculation to the main header.
    v2.1.5
    - Increased $PacingDelaySeconds and $InitialRetryDelay to 60s to prevent 429 rate limits.
    - Upgraded catch block to execute a dynamic back-off wait state when a 429 occurs.
    v2.1.4
    - Cast $Min and $Sec as [int] to fix string formatting errors with the -f operator.
    v2.1.3
    - Fixed bracket syntax error inside main pacing countdown loop.
    v2.1.2
    - Added a dynamic remaining time estimation (ETA) calculation to the pacing status bar.
    v2.1.1
    - Stripped verbose DEBUG logs.
    - Added inline status indicator and clean pacing countdown layout.
#>

# ==============================================================================
# CONFIGURATION
# ==============================================================================
$GeminiApiKey = [System.Environment]::GetEnvironmentVariable("GEMINI_API_KEY")

if (-not $GeminiApiKey) {
    $GeminiApiKey = "Put API key here".Trim()
}

# Global URI Target Configuration Block
$GlobalTargetUrl = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=$GeminiApiKey"

# Centralized Query Log File
$QueryLogFile = "C:\Workarea\google_query_log.txt"

# Rate Limit & Throttling Adjustments
$PacingDelaySeconds = 60   
$MaxRetryAttempts   = 3    
$InitialRetryDelay  = 60   


# ==============================================================================
# GEMINI JSON CONTRACT
# ==============================================================================
$SystemInstruction = @"
You are a strict OSINT extraction engine.

Return ONLY a valid JSON object matching the schema below. Wrap the JSON in a standard markdown code block. Do NOT include any other intro, outro, or chat text.

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
- Do NOT infer missing fields or fabricate profiles.
- If no results found, return exactly: { "leads": [] }
"@

# ==============================================================================
# QUERY EXTRACTION
# ==============================================================================
function Get-SearchStrings {
    param([string]$FilePath)

    $content = Get-Content $FilePath -Raw
    $pattern = '(?s)\`\`\`(?:markdown|text)?\s*(.*?)\s*\`\`\`'
    $match = [regex]::Match($content, $pattern)
    $textBlock = if ($match.Success) { $match.Groups[1].Value } else { $content }

    $lines = $textBlock -split '\r?\n'
    $queries = @()
    $i = 1

    foreach ($line in $lines) {
        $q = $line.Trim() -replace '^[\*\-\d\.\s]+', ''
        if ($q -match '^site:linkedin\.com' -or $q -match '^"hiring"') {
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
# GEMINI CALL
# ==============================================================================
function Invoke-GroundedSearch {
    param(
        [string]$Query,
        [int]$CurrentIndex,
        [int]$TotalQueries
    )

    [System.Uri]$TargetEndpoint = $GlobalTargetUrl

    Write-Host -NoNewline " -> Vector [$($CurrentIndex + 1)/$TotalQueries] Executing API Grounded Search... " -ForegroundColor Yellow

    $bodyPayload = @{
        contents = @(
            @{
                role  = "user"
                parts = @(
                    @{ text = "$SystemInstruction`n`nQuery: $Query" }
                )
            }
        )
        tools = @(
            @{ googleSearch = @{} }
        )
    }

    $body = ConvertTo-Json -InputObject $bodyPayload -Depth 10 -Compress

    for ($attempt = 1; $attempt -le $MaxRetryAttempts; $attempt++) {
        try {
            $response = Invoke-RestMethod -Uri $TargetEndpoint -Method Post -Body $body -ContentType "application/json"
            $text = $response.candidates[0].content.parts[0].text

            if ($text -match '(?s)\`\`\`(?:json)?\s*(.*?)\s*\`\`\`') {
                $cleanText = $Matches[1]
            } else {
                $cleanText = $text
            }
            
            $json = $cleanText.Trim() | ConvertFrom-Json -ErrorAction Stop
            
            Write-Host "[OK]" -ForegroundColor Green
            return $json
        }
        catch {
            if ($attempt -eq $MaxRetryAttempts) {
                Write-Host "[FAILED]" -ForegroundColor Red
                Write-Warning "Vector Error: $($_.Exception.Message)"
            } else {
                $WaitTime = $InitialRetryDelay * $attempt
                Write-Host -NoNewline "`n    [!] 429 Rate Limit hit. Backing off for $WaitTime seconds... " -ForegroundColor Magenta
                Start-Sleep -Seconds $WaitTime
                Write-Host -NoNewline "`r" + (" " * 60) + "`r -> Retrying Vector [$($CurrentIndex + 1)/$TotalQueries] (Attempt $($attempt + 1))... " -ForegroundColor Yellow
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
    Write-Host "`n[SUCCESS] Intelligence compile complete: $outPath" -ForegroundColor Green
}

# ==============================================================================
# MAIN
# ==============================================================================
function Main {
    Write-Host "PROJECT OVERWATCH PHASE 2 v2.1.6 STARTING" -ForegroundColor Cyan

    $file = Join-Path $PSScriptRoot "dorks.txt"
    if (-not (Test-Path $file)) {
        Write-Warning "Could not find file: $file"
        return
    }

    $queries = Get-SearchStrings $file
    if ($queries.Count -eq 0) {
        Write-Warning "No valid queries found inside $file"
        return
    }

    # FIXED: Calculate the macro run duration upfront and project an absolute completion clock timestamp
    $TotalJobSeconds = ($queries.Count - 1) * $PacingDelaySeconds
    $CompletionTime  = (Get-Date).AddSeconds($TotalJobSeconds).ToString("hh:mm tt")
    
    Write-Host "Loaded $($queries.Count) search vectors from database stream. Est. Completion Time: [$CompletionTime]`n" -ForegroundColor Gray

    $results = @()

    for ($i = 0; $i -lt $queries.Count; $i++) {
        $q = $queries[$i]
        Add-QueryLog $QueryLogFile $q.Query
        
        $json = Invoke-GroundedSearch -Query $q.Query -CurrentIndex $i -TotalQueries $queries.Count

        $results += [PSCustomObject]@{
            VectorLabel = $q.Label
            Query       = $q.Query
            Leads       = $json.leads
        }

        if ($i -lt ($queries.Count - 1)) {
            $RemainingVectors = $queries.Count - ($i + 1)
            
            for ($seconds = $PacingDelaySeconds; $seconds -gt 0; $seconds--) {
                $TotalRemainingSeconds = ($RemainingVectors * $PacingDelaySeconds) + $seconds
                
                [int]$Min = [Math]::Floor($TotalRemainingSeconds / 60)
                [int]$Sec = $TotalRemainingSeconds % 60
                $EtaString = "{0:D2}:{1:D2}" -f $Min, $Sec

                Write-Host -NoNewline "`r -> Hold active. Next query in ($seconds)s | Job Queue ETA: [$EtaString]... " -ForegroundColor Gray
                Start-Sleep -Seconds 1
            }
            Write-Host -NoNewline ("`r" + (" " * 95) + "`r")
        }
    }

    Export-ResultsToJSON -SourceFilePath $file -LeadGroups $results -RawResults $results
}

Main