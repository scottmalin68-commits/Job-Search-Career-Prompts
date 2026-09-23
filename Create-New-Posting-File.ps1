<#
.SYNOPSIS
    Creates a new file and opens it in a text editor.
#>

# --- EXECUTION BANNER ---
$ScriptName =$MyInvocation.MyCommand.Name
$ScriptVersion = "v2.0.5"
Write-Host "=== Running $ScriptName ($ScriptVersion) ===" -ForegroundColor Cyan

# --- CONFIGURATION ---
$DefaultExt = ".md"

# --- AUTO-DETECT EDITOR ---
$EditorPath = ""
$PossiblePaths = @(
    "$env:ProgramFiles\Notepad++\notepad++.exe",
    "${env:ProgramFiles(x86)}\Notepad++\notepad++.exe",
    "$env:LocalAppData\Programs\Microsoft VS Code\Code.exe",
    "$env:ProgramFiles\Microsoft VS Code\Code.exe",
    "$env:ProgramFiles\Sublime Text\sublime_text.exe",
    "$env:ProgramFiles\Sublime Text 3\sublime_text.exe"
)

for ($i = 0; $i -lt$PossiblePaths.Length; $i++) {$path = $PossiblePaths[$i]
    if (Test-Path $path) { 
        $EditorPath =$path
        break 
    }
}

if ([string]::IsNullOrEmpty($EditorPath)) {
    try {
        $RegPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\notepad++.exe"
        if (Test-Path $RegPath) {$EditorPath = (Get-ItemProperty `
                -Path $RegPath `
                -ErrorAction Stop)."(default)" 
        }
    } catch { }
}

# --- SCRIPT LOGIC ---
$InputName = Read-Host "Enter a file name"

if ([string]::IsNullOrWhiteSpace($InputName)) {
    Write-Host "no filename provided. exiting." -ForegroundColor Yellow
    exit
}

$FileName = if ($InputName -notlike "*.*") { 
    $InputName +$DefaultExt 
} else { 
    $InputName 
}

$TargetDir = Split-Path `
    -Path $FileName

if ($TargetDir -and !(Test-Path -Path $TargetDir)) {
    New-Item `
        -ItemType Directory `
        -Path $TargetDir `
        -Force | Out-Null
    Write-Host "created missing directory: $TargetDir" -ForegroundColor Gray
}

$OpenFile =$true

$Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

if (Test-Path -Path $FileName) {
    $fileInfo = Get-Item$FileName
    Write-Host "`nfile already exists: $FileName" -ForegroundColor Cyan
    Write-Host "last modified: $($fileInfo.LastWriteTime)"
    
    Write-Host "`n[1] do not overwrite - do not open"
    Write-Host "[2] do not overwrite - open to append/edit"
    Write-Host "[3] overwrite (delete and start fresh)"
    $choice = Read-Host "`nchoose an option (1-3)"

    switch ($choice) {
        "1" { 
            $OpenFile = $false 
        }
        "2" { 
            Write-Host "appending timestamp and opening..." -ForegroundColor Gray 
            "`n`n---`n# Update: $Timestamp`n" | Add-Content -Path $FileName
        }
        "3" { 
            New-Item `
                -Path $FileName `
                -ItemType File `
                -Force | Out-Null
            "# Log Entry: $Timestamp`n`n" | Out-File -FilePath $FileName -Encoding utf8
            Write-Host "file wiped and header added." -ForegroundColor Green
        }
        default { 
            Write-Host "invalid choice." 
            exit 
        }
    }
} else {
    New-Item `
        -Path $FileName `
        -ItemType File `
        -Force | Out-Null
    "# Log Entry: $Timestamp`n`n" | Out-File -FilePath $FileName -Encoding utf8
    Write-Host "file created: $FileName" -ForegroundColor Green
}

if ($OpenFile) {
    if (![string]::IsNullOrEmpty($EditorPath) -and (Test-Path $EditorPath)) {
        Start-Process $EditorPath -ArgumentList "`"$FileName`""
    } else {
        Write-Host "`nwarning: no advanced editor found. using basic notepad." -ForegroundColor Yellow
        Start-Process "notepad.exe" -ArgumentList "`"$FileName`""
    }
}