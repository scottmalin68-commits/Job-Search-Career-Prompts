<#
.SYNOPSIS
    Project OverWatch - Phase 2: Hiring Manager Hunt Protocol Execution Engine
.DESCRIPTION
    This script reads search strings from a text/markdown file, executes them 
    against Gemini with live search grounding to find target leads, and logs the results 
    to a standalone, structured JSON file.
.NOTES
    HOW TO GET YOUR GEMINI API KEY:
    1. Go to the Google AI Studio website (aistudio.google.com).
    2. Log in with your standard Google account.
    3. Click "Get API Key" -> "Create API Key".
    4. Copy the generated string (starts with "AIzaSy...").
    5. Set it as a local system environment variable named "GEMINI_API_KEY".
.CHANGELOG
    v1.4.0
    - Migrated output delivery from file-appending to a dedicated, structured JSON document.
    - Automated output naming scheme to 'OverwatchReport-[date].json'.
    - Hardened internal grounding prompt to eliminate URL and profile hallucinations.
    - Retained dynamic status bars, pacing controls, and live countdown loops.
#>

# ==============================================================================
# CONFIGURATION
# ==============================================================================
$GeminiApiKey = [System.Environment]::GetEnvironmentVariable("GEMINI_API_KEY")
if (-not $GeminiApiKey) {
    Write-Error "GEMINI_API_KEY environment variable not found. Please set it before running."
    return
}

# Centralized Query Log File (Replace with your local path)
$QueryLogFile = "C:\Users\YOUR_USERNAME\Documents\google_query_log.txt"

# Rate Limit & Throttling Adjustments
$PacingDelaySeconds = 30   # Time to wait between completely different queries
$MaxRetryAttempts   = 3    # Total times to try a failing request before giving up
$InitialRetryDelay  = 30   # Seconds to wait on first failure (doubles each time)

# ==============================================================================
# ENGINE CORE FUNCTIONS
# ==============================================================================

function Select-TargetMarkdownFile {
    Add-Type -AssemblyName System.Windows.Forms
    
    $FileBrowser = New-Object System.Windows.Forms.OpenFileDialog -Property @{
        InitialDirectory = (Get-Item .).FullName
        Title            = "Select File Containing Search Strings"
        Filter           = "Text/Markdown Files (*.txt;*.md)|*.txt;*.md|All Files (*.*)|*.*"
    }
    
    $Result = $FileBrowser.ShowDialog()
    
    if ($Result -eq [System.Windows.Forms.DialogResult]::OK) {
        Write-Host "Selected file via GUI: $($FileBrowser.SafeFileName)" -ForegroundColor Green
        return $FileBrowser.FileName
    } else {
        return $null
    }
}

function Get-SearchStrings {
    param (
        [string]$FilePath
    )

    Write-Host "Reading target file: $FilePath" -ForegroundColor Cyan
    $Content = Get-Content -Path $FilePath -Raw

    $Pattern = "(?s)\`\`\`(?:markdown|text)?\s*(.*?)\s*\`\`\`"
    $Match = [regex]::Match($Content, $Pattern)

    if ($Match.Success) {
        $SectionText = $Match.Groups[1].Value
    } else {
        $SectionText = $Content
    }

    $Lines = $SectionText -split "`r?`n"
    $Queries = @()
    $Count = 1

    foreach ($Line in $Lines) {
        $CleanedQuery = $Line.Trim()
        $CleanedQuery = $CleanedQuery -replace "^[\*\s•\-\d\.]+", ""
        $CleanedQuery = $CleanedQuery.Trim("'`"")

        if ($CleanedQuery -match "^\s*site:linkedin\.com\/\S+") {
            $Queries += [PSCustomObject]@{
                Label = "Target Vector $Count"
                Query = $CleanedQuery
            }
            $Count++
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
    $SystemInstruction = "You are an elite cyber-intelligence analyst. Analyze the live search results for the target query. CRITICAL: You must ONLY list names, titles, and LinkedIn profiles explicitly found in the verified search results. If a profile URL is not explicitly listed in the search metadata, DO NOT fabricate, predict, or guess it. If no verified leads are found, state 'No verified data found.' Provide a clean, structured intelligence summary listing names, precise titles, and corporate alignment profiles based strictly on verified links."

    $Body = @{
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

    return "Execution Error: Unable to retrieve live grounding data."
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

function Export-ResultsToJSON {
    param (
        [string]$SourceFilePath,
        [array]$SearchResults
    )

    $DateStamp = Get-Date -Format "yyyy-MM-dd"
    $Directory = Split-Path $SourceFilePath -Parent
    $OutputFileName = "OverwatchReport-$DateStamp.json"
    $FullOutputPath = Join-Path $Directory $OutputFileName

    $Payload = [PSCustomObject]@{
        Project           = "Project OverWatch"
        Phase             = 2
        ExecutionTime     = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
        SourceVectorsFile = (Split-Path $SourceFilePath -Leaf)
        TotalQueriesRun   = $SearchResults.Count
        IntelligenceData  = $SearchResults
    }

    try {
        $JsonOutput = $Payload | ConvertTo-Json -Depth 10
        Set-Content -Path $FullOutputPath -Value $JsonOutput -Encoding utf8
        Write-Host "`n[+] STRUCTURED OSINT PAYLOAD EXPORTED TO JSON" -ForegroundColor Green
        Write-Host "File location: $FullOutputPath" -ForegroundColor Green
    }
    catch {
        Write-Error "Failed to generate JSON output document. Details: $_"
    }
}

# ==============================================================================
# MAIN EXECUTION PIPELINE
# ==============================================================================
function Main {
    Write-Host "================================================================================" -ForegroundColor Cyan
    Write-Host "PROJECT OVERWATCH - LAUNCHING PHASE 2 AUTOMATION SCRIPT (JSON ENGINE)" -ForegroundColor Cyan
    Write-Host "================================================================================" -ForegroundColor Cyan

    if ($GeminiApiKey -eq "YOUR_GEMINI_API_KEY_HERE" -or -not $GeminiApiKey) {
        Write-Error "API Key is not configured properly."
        return
    }

    $TargetFile = Select-TargetMarkdownFile
    if (-not $TargetFile) {
        Write-Warning "No file selected. Aborting."
        return
    }

    $Queries = Get-SearchStrings -FilePath $TargetFile
    if ($Queries.Count -eq 0) {
        Write-Warning "Process stopped: No valid site:linkedin search strings found inside the file."
        return
    }

    Write-Host "Found $($Queries.Count) valid target queries to process." -ForegroundColor Green
    $Results = @()

    for ($i = 0; $i -lt $Queries.Count; $i++) {
        $CurrentTarget = $Queries[$i]
        $CurrentStep = $i + 1
        
        $RemainingQueries = $Queries.Count - $CurrentStep
        $EstimatedSecondsLeft = $RemainingQueries * $PacingDelaySeconds
        $Minutes = [Math]::Floor($EstimatedSecondsLeft / 60)
        $Seconds = $EstimatedSecondsLeft % 60
        $EtaString = "{0:D2}m:{1:D2}s" -f $Minutes, $Seconds

        Write-Progress -Activity "Project OverWatch Phase 2: Processing Targets" `
                       -Status "Query $CurrentStep of $($Queries.Count) | ETA: $EtaString" `
                       -PercentComplete (($CurrentStep / $Queries.Count) * 100) `
                       -CurrentOperation "Target: $($CurrentTarget.Label)"

        Write-Host "`n[$CurrentStep/$($Queries.Count)] Processing: $($CurrentTarget.Label)..." -ForegroundColor Cyan
        
        Add-QueryLog -LogPath $QueryLogFile -Query $CurrentTarget.Query
        $ResultContent = Invoke-GroundedSearch -Query $CurrentTarget.Query -ApiKey $GeminiApiKey
        
        $Results += [PSCustomObject]@{
            VectorLabel = $CurrentTarget.Label
            TargetQuery = $CurrentTarget.Query
            RawOutput   = $ResultContent
        }

        if ($i -lt ($Queries.Count - 1)) {
            for ($Countdown = $PacingDelaySeconds; $Countdown -gt 0; $Countdown--) {
                Write-Progress -Activity "Project OverWatch Phase 2: Throttling API Quota" `
                               -Status "Cooling down... $Countdown seconds remaining" `
                               -PercentComplete (($CurrentStep / $Queries.Count) * 100) `
                               -CurrentOperation "Next up: $($Queries[$i+1].Label)"
                Start-Sleep -Seconds 1
            }
        }
    }

    Write-Progress -Activity "Project OverWatch Phase 2: Processing Targets" -Completed

    Write-Host "`nProcessing complete. Generating unified data stub..." -ForegroundColor Cyan
    Export-ResultsToJSON -SourceFilePath $TargetFile -SearchResults $Results
    
    Write-Host "`nEngine execution complete.`n" -ForegroundColor Green
}

Main