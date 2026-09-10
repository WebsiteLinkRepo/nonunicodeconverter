# Clipboard Verification Tool

This utility inspects the Windows clipboard and verifies the presence of native "Rich Text Format" data.

## Purpose

After running the Chrome extension's "Test Native RTF" button, this tool confirms that the native Windows clipboard actually contains the registered "Rich Text Format" — not just plain text or HTML.

This is the decisive proof before testing in Adobe PageMaker 7.0.

## Build

```bash
cd rtf-clipboard-poc/verification
cargo build --release
```

The executable will be at: `target/release/clipboard_inspector.exe`

## Usage

1. Click "Test Native RTF" in the Chrome extension
2. Run the inspector immediately:

```cmd
clipboard_inspector.exe
```

## Expected Output

If the native host worked correctly, you should see:

```
RTF Clipboard Inspector

=== Windows Clipboard Contents ===

Total formats available: 3

Available formats:
  [13] CF_UNICODETEXT
  [49158] Rich Text Format
  [49159] HTML Format

🔍 Checking for 'Rich Text Format' (ID: 49158)...
✅ FOUND: Native 'Rich Text Format' is present!

RTF data size: 45 bytes

RTF Preview (first 200 bytes):
---
{\rtf1\ansi{\fonttbl{\f0 Arial;}}\f0 TEST}
---

📋 Plain text content:
TEST

=== Verification Summary ===
✅ SUCCESS: Native Windows 'Rich Text Format' is present
   This clipboard data can be pasted into Adobe PageMaker 7.0
```

The key indicators:
- ✅ "Rich Text Format" appears in the format list
- ✅ The RTF preview shows the actual RTF syntax
- ✅ Format ID is a registered format (typically 49xxx range)

## What This Proves

This tool directly calls the Win32 clipboard APIs to enumerate all clipboard formats and specifically checks for the registered "Rich Text Format" format.

If this tool shows "✅ SUCCESS", it means:
1. The native messaging host successfully wrote to the clipboard
2. The registered "Rich Text Format" is present (not just CF_TEXT)
3. The RTF data contains the expected content
4. Adobe PageMaker 7.0 **should** recognize this format

## If Verification Fails

If you see "❌ NOT FOUND", check:

1. Did the extension show "SUCCESS"?
   - If no: the native host didn't run or errored
   - If yes: something cleared the clipboard between the test and inspection

2. Check the extension popup for error messages

3. Manually test the native host (see `../native-host/README.md`)

4. Check Windows Event Viewer for native host crashes

## Alternative: Windows Built-in Clipboard Viewer

Windows doesn't ship with a clipboard format viewer by default, but you can use third-party tools:

- **ClipSpy** (part of Windows SDK)
- **InsideClipboard** (NirSoft)
- **Clipboard Viewer** (various implementations)

However, this custom tool is more reliable because it:
- Runs from the command line (scriptable)
- Shows exactly what PageMaker 7.0 will see
- Displays the actual RTF content for verification
- No installation required beyond Rust compilation

## Next Step: PageMaker Test

Once this tool shows ✅ SUCCESS:

1. Keep the clipboard untouched
2. Open Adobe PageMaker 7.0
3. Create or open a document
4. Press Ctrl+V (paste)
5. Verify the text appears in **Arial** font

If PageMaker pastes the text and automatically applies Arial formatting, the POC is complete.

## Source Code

The tool is a single Rust file (`clipboard_inspector.rs`) that:
- Opens the Windows clipboard
- Enumerates all available formats
- Specifically checks for "Rich Text Format" (registered format)
- Reads and displays the RTF data
- Shows plain text for comparison

It's the same Win32 APIs that PageMaker 7.0 uses, so what this tool sees is what PageMaker sees.
