<#
.SYNOPSIS
    Creates a new file and opens it in a text editor.

.DESCRIPTION
    Prompts for a filename. Supports .md by default. Handles duplicates with three 
    specific user options and auto-creates missing directories. Appends timestamps
    to existing files if the user chooses to edit without overwriting.

.NOTES
    Author: Scott M.
    Purpose: Quick file creation utility.
    
    CHANGELOG:
    2026-03-25: Added editor path validation with notepad fallback.
    2026-03-25: Added timestamp appending for existing files (Option 2).
    2026-03-25: Added 3-option duplicate handling, directory check, .md default, and auto-timestamping.
    2026-03-15: Added duplicate check, file properties, and overwrite prompt.
    2026-03-10: Changed opener to Notepad++.
    2026-02-22: Added Author line and changelog section.
    2026-02-14: Initial script creation.
#>

# --- CONFIGURATION ---
$EditorPath = "C:\Program Files\Notepad++\notepad++.exe"
$DefaultExt = ".md"

# --- SCRIPT LOGIC ---
$InputName = Read-Host "Enter a file name"

if ([string]::IsNullOrWhiteSpace($InputName)) {
    write-host "no filename provided. exiting." -f yellow
    exit
}

# handle extension
$FileName = if ($InputName -notlike "*.*") { $InputName + $DefaultExt } else { $InputName }

# directory check
$TargetDir = Split-Path -Path $FileName
if ($TargetDir -and !(Test-Path -Path $TargetDir)) {
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
    write-host "created missing directory: $TargetDir" -f gray
}

$OpenFile = $true
$Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

if (Test-Path -Path $FileName) {
    $fileInfo = Get-Item $FileName
    write-host "`nfile already exists: $FileName" -f cyan
    write-host "last modified: $($fileInfo.LastWriteTime)"
    
    write-host "`n[1] do not overwrite - do not open"
    write-host "[2] do not overwrite - open to append/edit"
    write-host "[3] overwrite (delete and start fresh)"
    $choice = Read-Host "`nchoose an option (1-3)"

    switch ($choice) {
        "1" { $OpenFile = $false }
        "2" { 
            write-host "appending timestamp and opening..." -f gray 
            "`n`n---`n# Update: $Timestamp`n" | Add-Content -Path $FileName
        }
        "3" { 
            New-Item -Path $FileName -ItemType File -Force | Out-Null
            "# Log Entry: $Timestamp`n`n" | Out-File -FilePath $FileName -Encoding utf8
            write-host "file wiped and header added." -f green
        }
        default { write-host "invalid choice."; exit }
    }
} else {
    New-Item -Path $FileName -ItemType File -Force | Out-Null
    "# Log Entry: $Timestamp`n`n" | Out-File -FilePath $FileName -Encoding utf8
    write-host "file created: $FileName" -f green
}

# open the file with path validation
if ($OpenFile) {
    if (Test-Path -Path $EditorPath) {
        Start-Process $EditorPath -ArgumentList "`"$FileName`""
    } else {
        write-host "`nwarning: preferred editor not found at $EditorPath" -f yellow
        write-host "falling back to notepad..." -f gray
        Start-Process "notepad.exe" -ArgumentList "`"$FileName`""
    }
}