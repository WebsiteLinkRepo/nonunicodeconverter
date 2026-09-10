# Chrome Extension - RTF Clipboard POC

Minimal Manifest V3 Chrome extension for testing native RTF clipboard support.

## Installation

1. Open Chrome and navigate to `chrome://extensions/`
2. Enable "Developer mode" (toggle in top right)
3. Click "Load unpacked"
4. Select the `chrome-extension` directory
5. The extension icon should appear in your toolbar

## Usage

1. Click the extension icon
2. Click "Test Native RTF" button
3. Check the status message
4. If successful, paste in Adobe PageMaker 7.0 to verify

## Files

- `manifest.json` - Manifest V3 configuration with nativeMessaging permission
- `popup.html` - Simple UI with test button
- `popup.js` - Connects to native host and sends test RTF
- `README.md` - This file

## Icon Notes

The manifest references icon files (icon16.png, icon48.png, icon128.png) but they are not required for testing. Chrome will use a default icon if they're missing.
