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
    v1.6.2 - Patched regex parsing and object typing to prevent inline .Trim() text leakage and $(...) wrapper bleed.
    v1.6.3 - Fixed markdown string subexpression expansion, eliminated raw \n escapes, and automated vector name matching.
    v1.6.4 - Implemented loose regex matching for multi-format Vector labels (colon optional).
    v1.6.6 - Removed line-skipping safety to ensure full queue execution regardless of query text.
    v1.6.7 - Added Get-XRayQuery function for surgical profile mapping.
#>

# ==============================================================================
# CONFIGURATION
# ==============================================================================
# Define multiple API keys to cycle through to avoid hitting 503/429 limits
$ApiKeys = @(
    "Put API key here",
    "Put API key here",
    "Put API key here"
)
$Global:KeyIndex = 0

# List companies to exclude from searches (leave empty to disable)
$PreviousCompanies = @()

# Centralized Query Log File
$QueryLogFile = "google_query_log.txt"

# Rate Limit & Throttling Adjustments (Optimized for Free Tier Quotas)
$PacingDelaySeconds = 75   # Time to wait between completely different queries
$MaxRetryAttempts  = 3    # Total times to try a failing request before giving up
$InitialRetryDelay  = 45   # Seconds to wait on first failure (doubles each time)

# Metrics Tracking
$Global:SessionStartTime = Get-Date
$Global:SuccessfulQueries = 0
$Global:FailedQueries = 0

# ==============================================================================
# ENGINE CORE FUNCTIONS
# ==============================================================================

function Get-XRayQuery {
    param ([string]$TargetCompany, [string]$RoleTitle, [string]$Location)
    # Surgical LinkedIn X-Ray strings
    $Domain = "site:linkedin.com/in"
    $Exclusions = "-intitle:job -intitle:hiring -intitle:apply -intitle:career"
    
    # Add previous companies to exclusion list if defined
    $PrevCompanyExclusion = ""
    if ($PreviousCompanies.Count -gt 0) {
        $PrevCompanyExclusion = ($PreviousCompanies | ForEach-Object { "-`"$_`"" }) -join " "
    }
    
    return "$Domain `"$TargetCompany`" `"$RoleTitle`" `"$Location`" $Exclusions $PrevCompanyExclusion"
}

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
    $CurrentLabel = "Target Vector"

    foreach ($Line in $Lines) {
        $Cleaned = $Line.Trim()

        if ($Cleaned -match "^\d+\.\s*(.*Vector.*?)[:]?$") {
            $CurrentLabel = $Matches[1].Trim()
            continue
        }

        # core sanitization
        $CleanedQuery = $Cleaned -replace "^[\*\s•\-\d\.]+", ""
        $CleanedQuery = $CleanedQuery -replace "^\$\s*\(", ""
        $CleanedQuery = $CleanedQuery -replace "\)\s*$", ""
        $CleanedQuery = $CleanedQuery.Trim("'`"")

        if ($CleanedQuery -match "\.Trim\(\)") {
            $CleanedQuery = ($CleanedQuery -replace "\.Trim\(\)", "").Trim()
        }

        if ($CleanedQuery -match "site:linkedin\.com") {
            $Queries += [PSCustomObject]@{
                Label = $CurrentLabel
                Query = $CleanedQuery
            }
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
                        text = "You are an elite cyber-intelligence and corporate OSINT analyst. Perform a comprehensive live search and analysis for the following target query. Provide a clean, structured intelligence summary with verified sources and links. Ensure you display the raw hyperlinked URLs in full within markdown brackets instead of shortening them or writing generic text descriptions:`n`nQuery: $Query"
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
            $Response = Invoke-RestMethod -Uri $Uri -Method Post -Body $Body -ContentType "application/json" -TimeoutSec 45
            $ResultText = $Response.candidates[0].content.parts[0].text
            return $ResultText
        }
        catch {
            $ErrorMessage = $_.Exception.Message
            
            if ($_.Exception.InnerException -and $_.Exception.InnerException.Response) {
                $ErrorResponse = $_.Exception.InnerException.Response
                $Task = $ErrorResponse.Content.ReadAsStringAsync()
                if ($Task.Wait(2000)) { $ErrorMessage = $Task.Result }
            }
            elseif ($_ -and $_.ErrorRecord -and $_.ErrorRecord.ErrorDetails) {
                $ErrorMessage = $_.ErrorRecord.ErrorDetails.Message
            }

            Write-Warning "Attempt $Attempt failed. Server response: $ErrorMessage"

            if ($Attempt -lt $MaxRetryAttempts) {
                Write-Host "Server overloaded or rate-limited. Backing off and retrying in $CurrentRetryDelay seconds..." -ForegroundColor Gray
                Start-Sleep -Seconds $CurrentRetryDelay
                $CurrentRetryDelay = $CurrentRetryDelay * 2 
            }
            $Attempt++
        }
    }

    return "Execution Error: Unable to retrieve live grounding data. Google API servers are currently overloaded (503) or rejecting requests."
}

function Add-QueryLog {
    param (
        [string]$LogPath,
        [string]$Query
    )

    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $LogEntry = "[$Timestamp] EXECUTED: $Query"
    
    try {
        Add-Content -Path $LogPath -Value $LogEntry
        Write-Host "Logged query entry to: $LogPath" -ForegroundColor DarkGray
    }
    catch {
        Write-Warning "Failed to write to log file: $_"
    }
}

function Append-ResultsToMarkdown {
    param (
        [string]$FilePath,
        [array]$SearchResults
    )

    $OutputBlock = "`n`n#### 📊 INTEL GENERATED BY AUTO-HUNT ENGINE`n"
    
    foreach ($Result in $SearchResults) {
        [string]$CleanLabel  = $Result.Label
        [string]$CleanQuery  = $Result.Query
        [string]$CleanOutput = $Result.Output

        if ($CleanOutput -match "(?s)(.*?)\}\.Query\)\\n\\n(.*)") {
            $CleanOutput = $Matches[2]
        }

        $OutputBlock += "`n### 🔍 Target: $($CleanLabel.Trim())`n"
        $OutputBlock += "**Query:** ``$($CleanQuery.Trim())```n`n"
        $OutputBlock += "$($CleanOutput.Trim())`n"
        $OutputBlock += "`n"
    }

    try {
        Add-Content -Path $FilePath -Value $OutputBlock
        Write-Host "Successfully appended findings to document." -ForegroundColor Green
    }
    catch {
        Write-Warning "Failed to write findings back to target markdown file: $_"
    }
}

# ==============================================================================
# MAIN EXECUTION PIPELINE
# ==============================================================================
function Main {
    if ($ApiKeys -contains "YOUR_GEMINI_API_KEY_1") {
        Write-Warning "Default API keys detected. Please populate environment variables or edit configuration parameters."
        return
    }

    Write-Host "================================================================================" -ForegroundColor Cyan
    Write-Host "LAUNCHING AUTO-HUNT POWERSHELL ENGINE (v1.6.7)" -ForegroundColor Cyan
    Write-Host "================================================================================" -ForegroundColor Cyan

    $TargetFile = Select-TargetMarkdownFile
    if (-not $TargetFile) {
        return
    }

    $Queries = Get-SearchStrings -FilePath $TargetFile
    if ($Queries.Count -eq 0) {
        Write-Warning "Process stopped: No valid site:linkedin search strings found inside the target section."
        return
    }

    $TotalJobSeconds = ($Queries.Count - 1) * $PacingDelaySeconds
    $EstCompletionTime = (Get-Date).AddSeconds($TotalJobSeconds).ToString("hh:mm tt")
    
    Write-Host "Found $($Queries.Count) valid target queries to process." -ForegroundColor Green
    Write-Host "Estimated execution runtime queue completion time: [$EstCompletionTime]`n" -ForegroundColor Gray

    $Results = @()
    $Global:SessionStartTime = Get-Date
    $Global:SuccessfulQueries = 0
    $Global:FailedQueries = 0

    for ($i = 0; $i -lt $Queries.Count; $i++) {
        $CurrentTarget = $Queries[$i]
        [string]$CleanTextQuery = $CurrentTarget.Query.Trim()

        Write-Host "`n[$($i + 1)/$($Queries.Count)] Processing: $($CurrentTarget.Label)..." -ForegroundColor Cyan
        Add-QueryLog -LogPath $QueryLogFile -Query $CleanTextQuery
        
        $CurrentKey = $ApiKeys[$Global:KeyIndex]
        Write-Host "Using API Key Slot [$Global:KeyIndex]" -ForegroundColor DarkGray
        
        $ResultContent = Invoke-GroundedSearch -Query $CleanTextQuery -ApiKey $CurrentKey
        
        if ($ResultContent -like "*Execution Error:*") {
            $Global:KeyIndex = ($Global:KeyIndex + 1) % $ApiKeys.Count
            Write-Host "[-] Hard execution failure. Swapping to API Key Slot [$Global:KeyIndex] for critical failover..." -ForegroundColor DarkYellow
            
            $CurrentKey = $ApiKeys[$Global:KeyIndex]
            $ResultContent = Invoke-GroundedSearch -Query $CleanTextQuery -ApiKey $CurrentKey
            
            if ($ResultContent -notlike "*Execution Error:*") {
                Write-Host "[+] Query executed successfully on failover key!" -ForegroundColor Green
                $Global:SuccessfulQueries++
            } else {
                $Global:FailedQueries++
            }
        } else {
            Write-Host "[+] Query executed successfully! Data retrieved." -ForegroundColor Green
            $Global:SuccessfulQueries++
        }
        
        $Global:KeyIndex = ($Global:KeyIndex + 1) % $ApiKeys.Count
        
        $Results += [PSCustomObject]@{
            Label  = $CurrentTarget.Label
            Query  = $CleanTextQuery
            Output = $ResultContent
        }

        if ($i -lt ($Queries.Count - 1)) {
            $RemainingVectors = $Queries.Count - ($i + 1)
            
            for ($seconds = $PacingDelaySeconds; $seconds -gt 0; $seconds--) {
                $TotalRemainingSeconds = ($RemainingVectors * $PacingDelaySeconds) + $seconds
                $Min = [Math]::Floor($TotalRemainingSeconds / 60)
                $Sec = $TotalRemainingSeconds % 60
                $EtaString = "{0:D2}:{1:D2}" -f [int]$Min, [int]$Sec
                
                Write-Host -NoNewline "`r -> Throttling safety pause: ($seconds)s left | Remaining Job Queue ETA: [$EtaString]... " -ForegroundColor Gray
                Start-Sleep -Seconds 1
            }
            Write-Host -NoNewline ("`r" + (" " * 100) + "`r")
        }
    }

    Write-Host "`nWriting results back to target document..." -ForegroundColor Cyan
    Append-ResultsToMarkdown -FilePath $TargetFile -SearchResults $Results
    
    $EndTime = Get-Date
    $Duration = New-TimeSpan -Start $Global:SessionStartTime -End $EndTime
    $TotalRuntimeString = "{0:D2}h {1:D2}m {2:D2}s" -f $Duration.Hours, $Duration.Minutes, $Duration.Seconds
    $TotalProcessed = $Global:SuccessfulQueries + $Global:FailedQueries
    $SuccessRate = if ($TotalProcessed -gt 0) { [Math]::Round(($Global:SuccessfulQueries / $TotalProcessed) * 100, 1) } else { 0 }

    Write-Host "`n==================================================" -ForegroundColor Cyan
    Write-Host "         SESSION EFFICACY AUDIT REPORT           " -ForegroundColor Cyan
    Write-Host "==================================================" -ForegroundColor Cyan
    Write-Host " Total Vectors Run : $TotalProcessed" -ForegroundColor Gray
    Write-Host " Success Vectors   : $Global:SuccessfulQueries" -ForegroundColor Green
    Write-Host " Failure Faults    : $Global:FailedQueries" -ForegroundColor Red
    Write-Host " Pipeline Yield    : $SuccessRate%" -ForegroundColor Yellow
    Write-Host " Total Run Duration: $TotalRuntimeString" -ForegroundColor Gray
    Write-Host "==================================================" -ForegroundColor Cyan
    Write-Host "`nEngine execution complete.`n" -ForegroundColor Green
}

Main