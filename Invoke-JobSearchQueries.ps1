<#
.SYNOPSIS
    Auto-Hunt Protocol Execution Engine (PowerShell Edition)
.DESCRIPTION
    This script automates cyber-intelligence gathering for job targeting. 
    It scans the current directory for 'Posting-*.md' files, sorts them by date 
    extracted from the filename (newest first), lets the user select one via console,
    extracts pure 'site:linkedin.com' search strings under '#### 13. THE HUNT', 
    runs them against Gemini with live search grounding, logs the queries, and appends findings.
.CHANGELOG
    v1.5.4 - Integrated dual-key round-robin failover logic to automatically bypass 429 rate limits.
    v1.5.5 - Fixed round-robin key rotation to cycle proactively and added screen success indicators.
    v1.6.0 - Integrated real-time job queue ETAs, a live countdown timer, and a session metric report.
    v1.6.1 - Stripped hardcoded environment variables and secrets for secure public repository deployment.
#>

# ==============================================================================
# CONFIGURATION & ENVIRONMENT VALIDATION
# ==============================================================================
# Dynamic Key Setup: Pulls keys safely from environment variables if present
if ($env:GEMINI_API_KEYS) {
    $ApiKeys = $env:GEMINI_API_KEYS -split ","
} else {
    # Public fallback placeholders for local config editing
    $ApiKeys = @(
        "YOUR_GEMINI_API_KEY_1",
        "YOUR_GEMINI_API_KEY_2"
    )
}
$Global:KeyIndex = 0

# Centralized Query Log File Path
if ($env:AUTOHUNT_LOG_PATH) {
    $QueryLogFile = $env:AUTOHUNT_LOG_PATH
} else {
    $QueryLogFile = Join-Path $PSScriptRoot "google_query_log.txt"
}

# Rate Limit & Throttling Adjustments (Optimized for Free Tier Quotas)
$PacingDelaySeconds = 75   # Time to wait between completely different queries
$MaxRetryAttempts   = 3    # Total times to try a failing request before giving up
$InitialRetryDelay  = 45   # Seconds to wait on first failure (doubles each time)

# Metrics Tracking
$Global:SessionStartTime = Get-Date
$Global:SuccessfulQueries = 0
$Global:FailedQueries = 0

# ==============================================================================
# ENGINE CORE FUNCTIONS
# ==============================================================================

function Select-TargetMarkdownFile {
    $Files = Get-ChildItem -Path . -Filter "Posting-*.md" -File
    
    if ($Files.Count -eq 0) {
        Write-Warning "No 'Posting-*.md' files found in the current folder."
        return $null
    }

    $SortedFiles = $Files | ForEach-Object {
        $DateString = ""
        if ($_.BaseName -match "(\d{8})$") {
            $DateString = $Matches[1]
        }
        [PSCustomObject]@{
            File = $_
            DateKey = $DateString
        }
    } | Sort-Object DateKey -Descending

    Write-Host "`nAvailable Posting Files (Sorted Newest First):" -ForegroundColor Yellow
    for ($i = 0; $i -lt $SortedFiles.Count; $i++) {
        Write-Host "[$($i + 1)] $($SortedFiles[$i].File.Name)" -ForegroundColor Gray
    }

    $Selection = Read-Host "`nSelect a file number (or press Enter to cancel)"
    
    if ([string]::IsNullOrWhiteSpace($Selection)) {
        Write-Warning "Operation canceled by user."
        return $null
    }

    $Index = 0
    if ([int]::TryParse($Selection, [ref]$Index) -and $Index -ge 1 -and $Index -le $SortedFiles.Count) {
        $SelectedFile = $SortedFiles[$Index - 1].File.FullName
        Write-Host "Selected file: $(Split-Path $SelectedFile -Leaf)" -ForegroundColor Green
        return $SelectedFile
    } else {
        Write-Warning "Invalid selection."
        return $null
    }
}

function Get-SearchStrings {
    param ([string]$FilePath)

    Write-Host "Reading target file: $FilePath" -ForegroundColor Cyan
    $Content = Get-Content -Path $FilePath -Raw

    $Pattern = "(?s)####\s*13\.\s*THE\s*HUNT\s*\(AUTO-HUNT\s*PROTOCOL\)(.*?)((?=Part\s*B:)|(?=####)|$)"
    $Match = [regex]::Match($Content, $Pattern)

    if (-not $Match.Success) {
        Write-Warning "Could not find the target '#### 13. THE HUNT' section."
        return @()
    }

    $SectionText = $Match.Groups[1].Value
    $Lines = $SectionText -split "`r?`n"
    $Queries = @()
    $CurrentLabel = "Unknown Vector"

    foreach ($Line in $Lines) {
        $Cleaned = $Line.Trim()

        if ($Cleaned -match "^\d+\.\s*(.+):$") {
            $CurrentLabel = $Matches[1].Trim()
            continue
        }

        $CleanedQuery = $Cleaned -replace "^[\*\s•\-\d\.]+", ""
        $CleanedQuery = $CleanedQuery.Trim("'`"")

        if ($CleanedQuery -match "^\s*site:linkedin\.com\/\S+") {
            $Queries += [PSCustomObject]@{
                Label = $CurrentLabel
                Query = $CleanedQuery
            }
            $CurrentLabel = "Unknown Vector"
        }
    }

    return $Queries
}

function Invoke-GroundedSearch {
    param (
        [string]$Query,
        [string]$ApiKey
    )

    $Uri = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=$ApiKey"
    
    $Body = @{
        contents = @(
            @{
                parts = @(
                    @{
                        text = "You are an elite cyber-intelligence and corporate OSINT analyst. Perform a comprehensive live search and analysis for the following target query. Provide a clean, structured intelligence summary with verified sources and links:`n`nQuery: $Query"
                    }
                )
            }
        )
        tools = @(
            @{
                google_search = @{}
            }
        )
    } | ConvertTo-Json -Depth 10

    $Attempt = 1
    $CurrentRetryDelay = $InitialRetryDelay

    while ($Attempt -le $MaxRetryAttempts) {
        try {
            Write-Host "Executing live search grounding (Attempt $Attempt/$MaxRetryAttempts) for: '$Query'" -ForegroundColor Yellow
            $Response = Invoke-RestMethod -Uri $Uri -Method Post -