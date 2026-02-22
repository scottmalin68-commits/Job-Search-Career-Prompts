<#
.SYNOPSIS
    Prompts for a filename, creates it, and opens it in Notepad.

.DESCRIPTION
    Asks the user for a name. If they provide one, it creates the file (if missing) 
    and opens it. If empty, it stops.

.NOTES
    Author: Scott M.
    Purpose: Quick file creation utility.
    
    CHANGELOG:
    2026-02-22: Added Author line and changelog section.
    2026-02-14: Initial script creation.
#>

# get filename
$FileName = Read-Host "Enter a file name (with extension)"

# check if empty
if ([string]::IsNullOrWhiteSpace($FileName)) {
    Write-Host "No filename provided. Exiting script." -ForegroundColor Yellow
    exit
}

# create if it doesn't exist
if (-not (Test-Path -Path $FileName)) {
    try {
        New-Item -Path $FileName -ItemType File -Force | Out-Null
        Write-Host "File created: $FileName" -ForegroundColor Green
    }
    catch {
        Write-Host "Failed to create file: $($_.Exception.Message)" -ForegroundColor Red
        exit
    }
}
else {
    Write-Host "File already exists. Opening existing file..." -ForegroundColor Cyan
}

# open it
Start-Process notepad.exe $FileName