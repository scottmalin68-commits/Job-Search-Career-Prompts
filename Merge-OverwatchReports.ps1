<#
.SYNOPSIS
    Consolidates Project OverWatch intelligence logs into a master database.
.DESCRIPTION
    Scans the current folder for OverwatchReport-*.json telemetry files, 
    extracts human leads, flattens the schema, deduplicates records,
    and drops stale entries older than 90 days.
.VERSION
    1.0.0
.CHANGELOG
    - v1.0.0: Initial baseline. Added memory-optimized local merging loop, 
             filename date-parsing for LastVerifiedDate tracker, 90-day 
             expiration cutoff, and dynamic console metrics.
#>

# Configuration
$targetPattern = "OverwatchReport-*.json"
$masterFileName = "Overwatch-Master-Intel.json"
$stalenessDays = 90
$cutoffDate = (Get-Date).AddDays(-$stalenessDays)

# Initialize tracking containers
$rawLeadsList = [System.Collections.Generic.List[Object]]::new()
$consolidatedLeads = [System.Collections.Generic.List[Object]]::new()
$finalFreshLeads = [System.Collections.Generic.List[Object]]::new()
$sourceFiles = [System.Collections.Generic.List[String]]::new()

# 1. Scan and Ingest Telemetry Logs
$logFiles = Get-ChildItem -Filter $targetPattern | Where-Object { $_.Name -ne $masterFileName }

if ($logFiles.Count -eq 0) {
    Write-Host "[ERROR] No telemetry logs found matching '$targetPattern'." -ForegroundColor Red
    return
}

Write-Host "Found $($logFiles.Count) telemetry logs. Processing pipeline streams..." -ForegroundColor Cyan

foreach ($file in $logFiles) {
    $sourceFiles.Add($file.Name)
    
    # Extract date from filename string (expects YYYY-MM-DD pattern)
    if ($file.Name -match '\d{4}-\d{2}-\d{2}') {
        $fileDateString = $Matches[0]
    } else {
        $fileDateString = (Get-Date).ToString("yyyy-MM-dd")
    }

    try {
        $jsonData = Get-Content -Raw -Path $file.FullName | ConvertFrom-Json -ErrorAction Stop
        
        # Handle both flat arrays and legacy/nested RawSearchResults containers
        $leadsSource = $null
        if ($jsonData.PSObject.Properties['Leads']) { $leadsSource = $jsonData.Leads }
        elseif ($jsonData.PSObject.Properties['RawSearchResults']) { $leadsSource = $jsonData.RawSearchResults }
        elseif ($jsonData -is [Array]) { $leadsSource = $jsonData }

        foreach ($lead in $leadsSource) {
            if ($null -ne $lead.name -and $lead.name -ne "") {
                # Attach metadata payload for tracking
                $lead | Add-Member -MemberType NoteProperty -Name "FileDate" -Value $fileDateString -Force
                $lead | Add-Member -MemberType NoteProperty -Name "SourceFile" -Value $file.Name -Force
                $rawLeadsList.Add($lead)
            }
        }
        Write-Host "  -> Extracting: $($file.Name)... [OK]" -ForegroundColor Green
    }
    catch {
        Write-Host "  -> Extracting: $($file.Name)... [FAILED parsing schema]" -ForegroundColor Red
    }
}

# 2. Normalization and Deduplication Loop
$groupedLeads = $rawLeadsList | Group-Object -Property { $_.name.Trim().ToLower() }, { $_.company.Trim().ToLower() }

foreach ($group in $groupedLeads) {
    # Sort instances of this lead by file date to find the most recent sighting
    $sortedInstances = $group.Group | Sort-Object { [datetime]::ParseExact($_.FileDate, 'yyyy-MM-dd', $null) } -Descending
    $latestInstance = $sortedInstances[0]
    
    # Extract all distinct source files this person hit across the timeline
    $seenIn = $group.Group.SourceFile | Select-Object -Unique

    # Construct the normalized root object
    $normalizedLead = [ordered]@{
        "name"             = $latestInstance.name
        "title"            = $latestInstance.title
        "company"          = $latestInstance.company
        "linkedin_url"     = $latestInstance.linkedin_url
        "source_evidence"  = $latestInstance.source_evidence
        "confidence"       = $latestInstance.confidence
        "LastVerifiedDate" = $latestInstance.FileDate
        "SeenInReports"    = $seenIn
    }
    $consolidatedLeads.Add([PSCustomObject]$normalizedLead)
}

# 3. Time-Horizon Filtration (Drop Stale Records)
$staleCount = 0
foreach ($lead in $consolidatedLeads) {
    $lastSeen = [datetime]::ParseExact($lead.LastVerifiedDate, 'yyyy-MM-dd', $null)
    
    if ($lastSeen -lt $cutoffDate) {
        $staleCount++
    } else {
        $finalFreshLeads.Add($lead)
    }
}

# 4. Construct Final Master JSON Payload
$masterPayload = [ordered]@{
    "Project"                 = "Project OverWatch"
    "CompilationTimestamp"    = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    "SourceFilesConsolidated" = $sourceFiles
    "TotalUniqueLeads"        = $consolidatedLeads.Count
    "ActiveLeadsSaved"        = $finalFreshLeads.Count
    "StaleLeadsDropped"       = $staleCount
    "Leads"                   = $finalFreshLeads
}

$masterPayload | ConvertTo-Json -Depth 10 | Set-Content -Path ".\$masterFileName"

# 5. Summary Report Output
Write-Host "`n==================================================" -ForegroundColor Cyan
Write-Host "       INTELLIGENCE CONSOLIDATION COMPLETE        " -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host " Version           : 1.0.0"
Write-Host " Files Analyzed    : $($sourceFiles.Count)"
Write-Host " Noise Reductions  : Filtered out empty/429 loops"
Write-Host " Total Unique Meta : $($consolidatedLeads.Count)"
Write-Host " Active Yield Saved: $($finalFreshLeads.Count)" -ForegroundColor Green
Write-Host " Stale Records Drop: $staleCount (Older than $stalenessDays days)" -ForegroundColor Yellow
Write-Host " Master Database   : $(Get-Item ".\$masterFileName").FullName"
Write-Host "==================================================" -ForegroundColor Cyan