<#
.SYNOPSIS
    Project OverWatch - Dork Optimization Module (v1.2.0)
.DESCRIPTION
    Pops a file explorer window to select a completed Overwatch report 
    from the current directory, identifies search vectors that successfully 
    harvested leads, removes them from the source dorks file, and prompts 
    the user to overwrite the primary target file automatically.
#>

# Add UI framework support
Add-Type -AssemblyName System.Windows.Forms

# -=- Config section -=-
$SourceDorksFile = Join-Path $PSScriptRoot "dorks.txt"
$OptimizedDorksFile = Join-Path $PSScriptRoot "dorks_remaining.txt"

if (-not (Test-Path $SourceDorksFile)) {
    Write-Warning "Could not find source dorks file: $SourceDorksFile"
    return
}

# 1. Pop the file selection UI dialog
Write-Host "Select target Overwatch JSON report file..." -ForegroundColor Cyan

$FileBrowser = New-Object System.Windows.Forms.OpenFileDialog
$FileBrowser.InitialDirectory = $PSScriptRoot
$FileBrowser.Filter = "JSON Files (*.json)|*.json|All Files (*.*)|*.*"
$FileBrowser.Title = "Select Overwatch Report File Verbatim"
$FileBrowser.ShowHelp = $true

$ShowDialog = $FileBrowser.ShowDialog()

if ($ShowDialog -eq [System.Windows.Forms.DialogResult]::OK) {
    $ReportFile = $FileBrowser.FileName
    Write-Host "[SELECTED] $ReportFile`n" -ForegroundColor Green
} else {
    Write-Warning "File selection canceled. Aborting dork optimization."
    return
}

# 2. Load report and extract successful queries
Write-Host "Analyzing report data for successful vectors..." -ForegroundColor Cyan
$Report = Get-Content $ReportFile -Raw | ConvertFrom-Json

# Find queries where Leads array is not empty
$SuccessfulQueries = @()
foreach ($Result in $Report.RawSearchResults) {
    if ($null -ne $Result.Leads -and $Result.Leads.Count -gt 0) {
        $CleanQuery = $Result.Query.Trim()
        $SuccessfulQueries += $CleanQuery
    }
}

Write-Host "Found $($SuccessfulQueries.Count) successful vectors to remove." -ForegroundColor Green

# 3. Read current dorks file line-by-line
$RawLines = Get-Content $SourceDorksFile
$RemainingDorks = @()
$RemovedCount = 0

foreach ($Line in $RawLines) {
    $TrimmedLine = $Line.Trim()
    
    # Strip leading bullets/numbers if they exist to match raw query format
    $NormalizedLine = $TrimmedLine -replace '^[\*\-\d\.\s]+', ''
    $NormalizedLine = $NormalizedLine.Trim()

    if ([string]::IsNullOrWhiteSpace($TrimmedLine)) {
        $RemainingDorks += $Line
        continue
    }

    if ($SuccessfulQueries -contains $NormalizedLine) {
        Write-Host "[-] Dropping successful vector: $NormalizedLine" -ForegroundColor Yellow
        $RemovedCount++
    } else {
        $RemainingDorks += $Line
    }
}

# 4. Output the optimized file
$RemainingDorks | Set-Content $OptimizedDorksFile -Encoding UTF8

Write-Host "`n==================================================" -ForegroundColor Cyan
Write-Host "            DORK OPTIMIZATION COMPLETE            " -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host " Total Original Vectors : $($RawLines.Count)" -ForegroundColor Gray
Write-Host " Successful Removed     : $RemovedCount" -ForegroundColor Green
Write-Host " Remaining Target Pool  : $($RemainingDorks.Count - $RemovedCount)" -ForegroundColor Yellow
Write-Host " Optimized Output File  : $OptimizedDorksFile" -ForegroundColor Gray
Write-Host "==================================================" -ForegroundColor Cyan

# 5. Interactive hot-swap verification prompt
Write-Host ""
$Choice = Read-Host "Would you like to overwrite dorks.txt with the remaining pool now? (Y/N)"
if ($Choice.Trim().ToUpper() -eq 'Y') {
    try {
        Copy-Item -Path $OptimizedDorksFile -Destination $SourceDorksFile -Force -ErrorAction Stop
        Remove-Item -Path $OptimizedDorksFile -Force -ErrorAction Stop
        Write-Host "[SUCCESS] dorks.txt has been updated and workspace cleaned." -ForegroundColor Green
    }
    catch {
        Write-Warning "Failed to update dorks.txt automatically: $($_.Exception.Message)"
    }
} else {
    Write-Host "[SKIPPED] dorks.txt left untouched. Remaining pool saved to dorks_remaining.txt" -ForegroundColor Yellow
}