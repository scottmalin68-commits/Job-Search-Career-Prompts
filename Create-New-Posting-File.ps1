<#
.SYNOPSIS
    Creates a new file and opens it in a text editor.

.DESCRIPTION
    Prompts for a filename. If the file exists, it shows file details and asks to overwrite.
    Otherwise, it creates the file and opens it in the preferred editor.

.NOTES
    Author: Scott M.
    Purpose: Quick file creation utility.
    
    CHANGELOG:
    2026-03-15: Added duplicate check, file properties, and overwrite prompt.
    2026-03-10: Changed opener to Notepad++.
    2026-02-22: Added Author line and changelog section.
    2026-02-14: Initial script creation.
#>

# --- CONFIGURATION ---
# Change this path to your preferred editor (e.g., "notepad.exe")
$EditorPath = "C:\Program Files\Notepad++\notepad++.exe"

# --- SCRIPT LOGIC ---
$FileName = Read-Host "Enter a file name (with extension)"

if ([string]::IsNullOrWhiteSpace($FileName)) {
    write-host "no filename provided. exiting." -f yellow
    exit
}

if (Test-Path -Path $FileName) {
    # show existing file info
    $fileInfo = Get-Item $FileName
    write-host "`nfile already exists!" -f cyan
    write-host "last modified: $($fileInfo.LastWriteTime)"
    write-host "size: $($fileInfo.Length) bytes"
    
    $choice = Read-Host "`ndo you want to overwrite it? (y/n)"
    if ($choice -ne "y") {
        write-host "opening existing file without overwriting..." -f gray
    } else {
        New-Item -Path $FileName -ItemType File -Force | Out-Null
        write-host "file overwritten." -f green
    }
} else {
    try {
        New-Item -Path $FileName -ItemType File -Force | Out-Null
        write-host "file created: $FileName" -f green
    } catch {
        write-host "error: $($_.Exception.Message)" -f red
        exit
    }
}

# open the file
if (Test-Path $EditorPath) {
    Start-Process $EditorPath -ArgumentList "`"$FileName`""
} else {
    write-host "preferred editor not found. falling back to notepad." -f gray
    Start-Process notepad.exe -ArgumentList "`"$FileName`""
}