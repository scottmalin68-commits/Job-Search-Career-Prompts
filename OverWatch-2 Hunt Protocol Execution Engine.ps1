<#
.SYNOPSIS
    Project OverWatch - Phase 2: Hiring Manager Hunt Protocol Execution Engine (v2.2.0)
.CHANGELOG
    v2.2.0 - Integrated 4-key pool usage tracking, session duration profiling, and an efficacy audit module.
#>

# --- API KEY CONFIGURATION POOL ---
$ApiKeyPool = @(
    "Put a key here", # Key 1
    "Put a key here", # Key 2
    "Put a key here", # Key 3
    "Put a key here"  # Key 4
)
# Supports multiple keys but you don't need them. I found the key runs out of quote around 15 queries 

$Global:CurrentKeyIndex = 0

# --- PERFORMANCE AND METRICS CONFIGURATION ---
$Global:KeyUsageCounters = @(0, 0, 0, 0)
$Global:SessionStartTime  = Get-Date

$QueryLogFile       = "C:LogDirectory\google_query_log.txt"
$PacingDelaySeconds = 60   
$MaxRetryAttempts   = 3    
$InitialRetryDelay  = 30   # Dropped delay down since we swap keys first

$SystemInstruction = @"
You are a strict OSINT extraction engine. Return ONLY a valid JSON object matching the schema below wrapped in a standard markdown code block.
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
"@

function Get-CurrentEndpoint {
    $CurrentKey = $ApiKeyPool[$Global:CurrentKeyIndex].Trim()
    return "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=$CurrentKey"
}

function Rotate-ApiKey {
    $OldIndex = $Global:CurrentKeyIndex
    $Global:CurrentKeyIndex = ($Global:CurrentKeyIndex + 1) % $ApiKeyPool.Count
    Write-Host "`n    [-->] Rotating API Quota Surface: Key Index [$OldIndex] -> [$Global:CurrentKeyIndex]" -ForegroundColor Cyan
}

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
        # FIX: Drop the strict match and accept any line that has content
        if (-not [string]::IsNullOrWhiteSpace($q)) {
            $queries += [PSCustomObject]@{ Label = "Vector $i"; Query = $q }
            $i++
        }
    }
    return $queries
}

function Invoke-GroundedSearch {
    param([string]$Query, [int]$CurrentIndex, [int]$TotalQueries)
    
    $bodyPayload = @{
        contents = @(@{ role = "user"; parts = @(@{ text = "$SystemInstruction`n`nQuery: $Query" }) })
        tools = @(@{ googleSearch = @{} })
    }
    $body = ConvertTo-Json -InputObject $bodyPayload -Depth 10 -Compress
    
    for ($attempt = 1; $attempt -le $MaxRetryAttempts; $attempt++) {
        $TargetEndpoint = Get-CurrentEndpoint
        
        # Increment request counter for active key
        $Global:KeyUsageCounters[$Global:CurrentKeyIndex]++
        
        Write-Host -NoNewline " -> Vector [$($CurrentIndex + 1)/$TotalQueries] Executing API Grounded Search (Key:$Global:CurrentKeyIndex)... " -ForegroundColor Yellow
        try {
            $response = Invoke-RestMethod -Uri $TargetEndpoint -Method Post -Body $body -ContentType "application/json"
            $text = $response.candidates[0].content.parts[0].text
            $cleanText = if ($text -match '(?s)\`\`\`(?:json)?\s*(.*?)\s*\`\`\`') { $Matches[1] } else { $text }
            $json = $cleanText.Trim() | ConvertFrom-Json -ErrorAction Stop
            Write-Host "[OK]" -ForegroundColor Green
            return $json
        }
        catch {
            if ($attempt -eq $MaxRetryAttempts) {
                Write-Host "[FAILED]" -ForegroundColor Red
                Write-Warning "Vector Error: $($_.Exception.Message)"
            } else {
                Write-Host -NoNewline "`n    [!] 429 Rate Limit encountered." -ForegroundColor Magenta
                Rotate-ApiKey
                $WaitTime = $InitialRetryDelay * $attempt
                Write-Host -NoNewline "    [!] Backing off engine for $WaitTime seconds... " -ForegroundColor Magenta
                Start-Sleep -Seconds $WaitTime
                Write-Host -NoNewline "`r" + (" " * 80) + "`r -> Retrying Vector [$($CurrentIndex + 1)/$TotalQueries] (Attempt $($attempt + 1))... " -ForegroundColor Yellow
            }
        }
    }
    return @{ leads = @() }
}

function Add-QueryLog {
    param([string]$LogPath, [string]$Query)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $LogPath -Value "[$timestamp] $Query"
}

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

function Export-ResultsToJSON {
    param([string]$SourceFilePath, [array]$LeadGroups, [array]$RawResults)
    $EndTime = Get-Date
    $date = $EndTime.ToString("yyyy-MM-dd")
    $outPath = Join-Path (Split-Path $SourceFilePath) "OverwatchReport-$date.json"
    $leads = Merge-Leads $LeadGroups
    
    # Calculate performance metrics
    $SuccessfulVectors = ($LeadGroups | Where-Object { $_.Leads.Count -gt 0 }).Count
    $FailedVectors     = ($LeadGroups | Where-Object { $_.Leads.Count -eq 0 }).Count
    $SuccessRate       = if ($LeadGroups.Count -gt 0) { [Math]::Round(($SuccessfulVectors / $LeadGroups.Count) * 100, 2) } else { 0 }
    
    # Calculate time metrics
    $Duration = New-TimeSpan -Start $Global:SessionStartTime -End $EndTime
    $TotalRuntimeString = "{0:D2}h {1:D2}m {2:D2}s" -f $Duration.Hours, $Duration.Minutes, $Duration.Seconds
    
    $AvgSecondsPerQuery = if ($LeadGroups.Count -gt 0) { 
        [Math]::Round($Duration.TotalSeconds / $LeadGroups.Count, 1) 
    } else { 0 }
    
    # Map key distribution
    $KeyAudit = @{}
    for ($idx = 0; $idx -lt $Global:KeyUsageCounters.Count; $idx++) {
        $KeyAudit["Key_Index_$idx`_Hits"] = $Global:KeyUsageCounters[$idx]
    }
    
    # Build summary metadata object
    $SessionAudit = [PSCustomObject]@{
        TotalVectorsProcessed = $LeadGroups.Count
        SuccessfulVectors     = $SuccessfulVectors
        FailedQuotaVectors    = $FailedVectors
        SuccessRatePercentage = "$SuccessRate%"
        UniqueLeadsHarvested  = $leads.Count
        TotalRunDuration      = $TotalRuntimeString
        AverageTimePerVector  = "$AvgSecondsPerQuery seconds"
        KeyUsageDistribution  = $KeyAudit
    }
    
    # Construct complete payload
    $payload = [PSCustomObject]@{
        Project           = "Project OverWatch"
        Phase             = 2
        StartTime         = $Global:SessionStartTime.ToString("yyyy-MM-dd HH:mm:ss")
        EndTime           = $EndTime.ToString("yyyy-MM-dd HH:mm:ss")
        SourceFile        = Split-Path $SourceFilePath -Leaf
        SessionAudit      = $SessionAudit
        Leads             = $leads
        RawSearchResults  = $RawResults
    }
    
    $payload | ConvertTo-Json -Depth 12 | Set-Content $outPath -Encoding UTF8
    
    # --- HUMAN READABLE CONSOLE REPORT ---
    Write-Host "`n==================================================" -ForegroundColor Cyan
    Write-Host "         SESSION EFFICACY AUDIT REPORT            " -ForegroundColor Cyan
    Write-Host "==================================================" -ForegroundColor Cyan
    Write-Host " Total Vectors Run : $($SessionAudit.TotalVectorsProcessed)" -ForegroundColor Gray
    Write-Host " Success Vectors   : $SuccessfulVectors" -ForegroundColor Green
    Write-Host " Quota Failures    : $FailedVectors" -ForegroundColor Red
    Write-Host " Pipeline Yield    : $SuccessRate%" -ForegroundColor Yellow
    Write-Host " Unique Profiles   : $($SessionAudit.UniqueLeadsHarvested)" -ForegroundColor Green
    Write-Host "--------------------------------------------------" -ForegroundColor Cyan
    Write-Host "             SESSION TIME METRICS                 " -ForegroundColor Cyan
    Write-Host "--------------------------------------------------" -ForegroundColor Cyan
    Write-Host " Total Run Time    : $TotalRuntimeString" -ForegroundColor Gray
    Write-Host " Avg Time / Vector : $AvgSecondsPerQuery seconds" -ForegroundColor Gray
    Write-Host "--------------------------------------------------" -ForegroundColor Cyan
    Write-Host "             KEY HIT DISTRIBUTION                 " -ForegroundColor Cyan
    Write-Host "--------------------------------------------------" -ForegroundColor Cyan
    for ($idx = 0; $idx -lt $Global:KeyUsageCounters.Count; $idx++) {
        Write-Host " -> Key Index [$idx] Requests Sent : $($Global:KeyUsageCounters[$idx])" -ForegroundColor Gray
    }
    Write-Host "==================================================" -ForegroundColor Cyan
    
    Write-Host "`n[SUCCESS] Intelligence compile complete: $outPath" -ForegroundColor Green
}

function Main {
    Write-Host "PROJECT OVERWATCH PHASE 2 v2.2.0 STARTING" -ForegroundColor Cyan
    $file = Join-Path $PSScriptRoot "dorks.txt"
    if (-not (Test-Path $file)) { Write-Warning "Could not find file: $file"; return }
    $queries = Get-SearchStrings $file
    if ($queries.Count -eq 0) { Write-Warning "No valid queries found inside $file"; return }
    $TotalJobSeconds = ($queries.Count - 1) * $PacingDelaySeconds
    $CompletionTime  = (Get-Date).AddSeconds($TotalJobSeconds).ToString("hh:mm tt")
    Write-Host "Loaded $($queries.Count) search vectors from database stream. Est. Completion Time: [$CompletionTime]`n" -ForegroundColor Gray
    $results = @()
    for ($i = 0; $i -lt $queries.Count; $i++) {
        $q = $queries[$i]
        Add-QueryLog $QueryLogFile $q.Query
        $json = Invoke-GroundedSearch -Query $q.Query -CurrentIndex $i -TotalQueries $queries.Count
        $results += [PSCustomObject]@{ VectorLabel = $q.Label; Query = $q.Query; Leads = $json.leads }
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
