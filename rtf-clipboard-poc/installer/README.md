# Installer - RTF Clipboard POC

Automated installation script for the native messaging host.

## Prerequisites

1. Build the native host executable (see `../native-host/README.md`)
2. The executable should be at: `../native-host/target/release/rtf_clipboard_host.exe`

## Installation Steps

### Method 1: Automatic (Recommended)

Run the PowerShell installer:

```powershell
cd rtf-clipboard-poc/installer
powershell -ExecutionPolicy Bypass -File install.ps1
```

The installer will:
- Locate the native host executable
- Create a native messaging manifest in `%LOCALAPPDATA%\rtf-clipboard-poc\`
- Register the manifest in Windows Registry for Chrome and Edge
- Display instructions for updating the extension ID

### Method 2: Manual Path

If the executable is in a different location:

```powershell
powershell -ExecutionPolicy Bypass -File install.ps1 -HostExecutablePath "C:\path\to\rtf_clipboard_host.exe"
```

## Post-Installation

After running the installer:

1. **Load the Chrome extension** (from `../chrome-extension/`)
   - Open Chrome
   - Navigate to `chrome://extensions/`
   - Enable "Developer mode"
   - Click "Load unpacked"
   - Select the `chrome-extension` directory

2. **Get the extension ID**
   - The ID is shown under the extension name (looks like: `abcdefghijklmnopqrstuvwxyz123456`)
   - Copy it

3. **Update the native messaging manifest**
   - Open: `%LOCALAPPDATA%\rtf-clipboard-poc\com.nonunicodeconverter.rtf_clipboard_poc.json`
   - Replace `EXTENSION_ID_PLACEHOLDER` with your actual extension ID
   - Save the file

4. **Restart Chrome** (important!)

## Verification

Test the installation:

1. Click the extension icon in Chrome
2. Click "Test Native RTF"
3. You should see a success message

If you see an error about the native host disconnecting, check:
- The manifest file has the correct extension ID
- Chrome was restarted after updating the manifest
- The executable path in the manifest is correct and the file exists

## Uninstallation

To remove the native messaging host:

```powershell
powershell -ExecutionPolicy Bypass -File install.ps1 -Uninstall
```

This will:
- Remove the registry entries
- Delete the manifest file
- Leave the executable in place (you can delete it manually)

## What Gets Registered

The installer creates:

1. **Manifest file**: `%LOCALAPPDATA%\rtf-clipboard-poc\com.nonunicodeconverter.rtf_clipboard_poc.json`
2. **Chrome registry key**: `HKCU\Software\Google\Chrome\NativeMessagingHosts\com.nonunicodeconverter.rtf_clipboard_poc`
3. **Edge registry key**: `HKCU\Software\Microsoft\Edge\NativeMessagingHosts\com.nonunicodeconverter.rtf_clipboard_poc`

All registry entries are per-user (HKCU), not system-wide (HKLM), so no administrator privileges are required.

## Security Notes

- The native host ONLY accepts messages from the registered extension ID
- No network access
- No file system access beyond clipboard operations
- Minimal Windows API calls (clipboard only)
- No elevated privileges required

## Troubleshooting

### "Native host has exited"
- Check Windows Event Viewer for crash logs
- Verify the executable runs standalone (test with a pipe)

### "Specified native messaging host not found"
- Extension ID doesn't match the manifest
- Manifest file path is wrong in registry
- Chrome wasn't restarted

### "Access is denied"
- The executable is blocked by antivirus
- Try running Chrome as administrator (not recommended long-term)

### Need to check what's registered?

```powershell
# View Chrome registration
Get-ItemProperty "HKCU:\Software\Google\Chrome\NativeMessagingHosts\com.nonunicodeconverter.rtf_clipboard_poc"

# View Edge registration
Get-ItemProperty "HKCU:\Software\Microsoft\Edge\NativeMessagingHosts\com.nonunicodeconverter.rtf_clipboard_poc"

# View manifest contents
Get-Content "$env:LOCALAPPDATA\rtf-clipboard-poc\com.nonunicodeconverter.rtf_clipboard_poc.json"
```
