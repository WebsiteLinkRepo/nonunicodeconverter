# RTF Clipboard POC - Native Messaging Host Installer
# This script registers the native messaging host for Chrome and Edge

param(
    [string]$HostExecutablePath = "",
    [switch]$Uninstall
)

$ErrorActionPreference = "Stop"

# Native messaging host name
$HOST_NAME = "com.nonunicodeconverter.rtf_clipboard_poc"

# Registry paths
$CHROME_REGISTRY_PATH = "HKCU:\Software\Google\Chrome\NativeMessagingHosts\$HOST_NAME"
$EDGE_REGISTRY_PATH = "HKCU:\Software\Microsoft\Edge\NativeMessagingHosts\$HOST_NAME"

function Get-HostExecutable {
    if ($HostExecutablePath -and (Test-Path $HostExecutablePath)) {
        return (Resolve-Path $HostExecutablePath).Path
    }

    # Try to find the executable in common locations
    $scriptDir = Split-Path -Parent $MyInvocation.ScriptName
    $commonPaths = @(
        (Join-Path $scriptDir "..\native-host\target\release\rtf_clipboard_host.exe"),
        (Join-Path $scriptDir "..\native-host\target\x86_64-pc-windows-msvc\release\rtf_clipboard_host.exe"),
        (Join-Path $scriptDir "..\native-host\target\i686-pc-windows-msvc\release\rtf_clipboard_host.exe"),
        (Join-Path $scriptDir "rtf_clipboard_host.exe")
    )

    foreach ($path in $commonPaths) {
        if (Test-Path $path) {
            return (Resolve-Path $path).Path
        }
    }

    Write-Host "ERROR: Could not find rtf_clipboard_host.exe" -ForegroundColor Red
    Write-Host "Please build the native host first or specify the path with -HostExecutablePath" -ForegroundColor Yellow
    exit 1
}

function Create-HostManifest {
    param([string]$ExePath, [string]$ManifestPath)

    $manifest = @{
        name = $HOST_NAME
        description = "RTF Clipboard POC - Native RTF clipboard support for Chrome"
        path = $ExePath
        type = "stdio"
        allowed_origins = @(
            "chrome-extension://EXTENSION_ID_PLACEHOLDER/"
        )
    } | ConvertTo-Json -Depth 10

    Set-Content -Path $ManifestPath -Value $manifest -Encoding UTF8
    Write-Host "Created manifest at: $ManifestPath" -ForegroundColor Green
}

function Register-NativeHost {
    param([string]$RegistryPath, [string]$ManifestPath)

    if (!(Test-Path (Split-Path $RegistryPath -Parent))) {
        New-Item -Path (Split-Path $RegistryPath -Parent) -Force | Out-Null
    }

    New-Item -Path $RegistryPath -Force | Out-Null
    New-ItemProperty -Path $RegistryPath -Name "(Default)" -Value $ManifestPath -PropertyType String -Force | Out-Null

    Write-Host "Registered at: $RegistryPath" -ForegroundColor Green
}

function Unregister-NativeHost {
    param([string]$RegistryPath)

    if (Test-Path $RegistryPath) {
        Remove-Item -Path $RegistryPath -Recurse -Force
        Write-Host "Unregistered from: $RegistryPath" -ForegroundColor Green
    } else {
        Write-Host "Not registered at: $RegistryPath" -ForegroundColor Yellow
    }
}

# Main logic
Write-Host "RTF Clipboard POC - Native Messaging Host Installer" -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan
Write-Host ""

if ($Uninstall) {
    Write-Host "UNINSTALLING..." -ForegroundColor Yellow
    Unregister-NativeHost -RegistryPath $CHROME_REGISTRY_PATH
    Unregister-NativeHost -RegistryPath $EDGE_REGISTRY_PATH

    $manifestPath = Join-Path $env:LOCALAPPDATA "rtf-clipboard-poc\$HOST_NAME.json"
    if (Test-Path $manifestPath) {
        Remove-Item $manifestPath -Force
        Write-Host "Removed manifest: $manifestPath" -ForegroundColor Green
    }

    Write-Host ""
    Write-Host "Uninstallation complete!" -ForegroundColor Green
    exit 0
}

# Install
Write-Host "INSTALLING..." -ForegroundColor Yellow
Write-Host ""

$exePath = Get-HostExecutable
Write-Host "Found executable: $exePath" -ForegroundColor Green

# Create manifest in LOCALAPPDATA
$manifestDir = Join-Path $env:LOCALAPPDATA "rtf-clipboard-poc"
if (!(Test-Path $manifestDir)) {
    New-Item -Path $manifestDir -ItemType Directory -Force | Out-Null
}

$manifestPath = Join-Path $manifestDir "$HOST_NAME.json"
Create-HostManifest -ExePath $exePath -ManifestPath $manifestPath

# Register for Chrome
Write-Host ""
Write-Host "Registering for Chrome..." -ForegroundColor Yellow
Register-NativeHost -RegistryPath $CHROME_REGISTRY_PATH -ManifestPath $manifestPath

# Register for Edge
Write-Host ""
Write-Host "Registering for Edge..." -ForegroundColor Yellow
Register-NativeHost -RegistryPath $EDGE_REGISTRY_PATH -ManifestPath $manifestPath

Write-Host ""
Write-Host "Installation complete!" -ForegroundColor Green
Write-Host ""
Write-Host "IMPORTANT: Update the manifest with your extension ID" -ForegroundColor Yellow
Write-Host "Edit: $manifestPath" -ForegroundColor Cyan
Write-Host "Replace EXTENSION_ID_PLACEHOLDER with your actual extension ID" -ForegroundColor Cyan
Write-Host ""
Write-Host "To get your extension ID:" -ForegroundColor Yellow
Write-Host "1. Load the extension in Chrome (chrome://extensions/)" -ForegroundColor White
Write-Host "2. Enable 'Developer mode'" -ForegroundColor White
Write-Host "3. Copy the ID shown under the extension name" -ForegroundColor White
Write-Host "4. Update the manifest file" -ForegroundColor White
Write-Host ""
