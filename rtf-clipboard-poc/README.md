# RTF Clipboard Proof-of-Concept

**MINIMAL PROOF-OF-CONCEPT** for native RTF clipboard support through Chrome Extension + Chrome Native Messaging.

This POC proves the following architecture works on Windows:

```
Chrome Extension
    ↓
Chrome Native Messaging
    ↓
Windows native host EXE
    ↓
Win32 clipboard API
    ↓
native Windows "Rich Text Format"
    ↓
Adobe PageMaker 7.0
```

**Status**: This is a standalone proof-of-concept. It does NOT integrate with the main NonUnicodeConverter application yet.

## What This POC Contains

1. **Chrome Extension** (`chrome-extension/`)
   - Manifest V3 Chrome extension
   - `nativeMessaging` permission
   - Simple popup with "Test Native RTF" button
   - Connects to native host via Chrome Native Messaging protocol

2. **Native Messaging Host** (`native-host/`)
   - Windows executable (Rust)
   - Receives JSON from Chrome
   - Writes to Windows clipboard using Win32 APIs:
     - **Rich Text Format** (registered clipboard format)
     - **CF_UNICODETEXT** (plain text)
     - **HTML Format** (registered clipboard format)
   - Returns success/error to extension
   - Standalone EXE (no runtime dependencies)

3. **Installer** (`installer/`)
   - PowerShell script for automated registration
   - Creates native messaging manifest
   - Registers in Windows Registry (HKCU)
   - No administrator privileges required
   - Works for Chrome and Edge

4. **Verification Tool** (`verification/`)
   - Clipboard inspector utility
   - Proves native "Rich Text Format" is present
   - Shows actual RTF data on clipboard
   - Same APIs PageMaker 7.0 uses

## Hard-Coded Test Data

The POC uses this hard-coded RTF:

```rtf
{\rtf1\ansi{\fonttbl{\f0 Arial;}}\f0 TEST}
```

This RTF specifies:
- Font table with Arial as font 0
- Text "TEST" in Arial

When pasted into Adobe PageMaker 7.0, if PageMaker automatically applies Arial formatting, the POC succeeds.

## Build Instructions

### Prerequisites

- Rust toolchain (1.77+ recommended)
- Windows (for the native host)
- Chrome or Edge browser

### Step 1: Build Native Host

```bash
cd rtf-clipboard-poc/native-host
cargo build --release
```

The executable will be at: `target/release/rtf_clipboard_host.exe`

For Windows 7/8/8.1 (32-bit):
```bash
rustup target add i686-pc-windows-msvc
cargo build --target i686-pc-windows-msvc --release
```

### Step 2: Install Native Host

```powershell
cd rtf-clipboard-poc/installer
powershell -ExecutionPolicy Bypass -File install.ps1
```

This will:
- Find the native host executable
- Create the manifest in `%LOCALAPPDATA%\rtf-clipboard-poc\`
- Register for Chrome and Edge

### Step 3: Load Chrome Extension

1. Open Chrome
2. Navigate to `chrome://extensions/`
3. Enable "Developer mode" (toggle in top right)
4. Click "Load unpacked"
5. Select the `rtf-clipboard-poc/chrome-extension` directory

### Step 4: Update Extension ID

After loading the extension:

1. Copy the extension ID (shown under the extension name)
2. Open: `%LOCALAPPDATA%\rtf-clipboard-poc\com.nonunicodeconverter.rtf_clipboard_poc.json`
3. Replace `EXTENSION_ID_PLACEHOLDER` with your actual extension ID
4. Save and **restart Chrome**

### Step 5: Build Verification Tool (Optional)

```bash
cd rtf-clipboard-poc/verification
cargo build --release
```

The executable will be at: `target/release/clipboard_inspector.exe`

## Testing Instructions

### Test 1: Extension Communicates with Native Host

1. Click the extension icon in Chrome toolbar
2. Click "Test Native RTF" button
3. Expected: Success message appears

If you see "Native host disconnected", check:
- Extension ID in manifest is correct
- Chrome was restarted after updating manifest
- Native host executable exists and is accessible

### Test 2: Native Clipboard Format Verification

1. Click "Test Native RTF" in the extension
2. Run the verification tool immediately:

```cmd
cd rtf-clipboard-poc\verification\target\release
clipboard_inspector.exe
```

Expected output:
```
✅ FOUND: Native 'Rich Text Format' is present!
RTF Preview: {\rtf1\ansi{\fonttbl{\f0 Arial;}}\f0 TEST}
```

**This is the decisive proof that native RTF is on the Windows clipboard.**

### Test 3: Adobe PageMaker 7.0 Verification

This is the **final success criterion**:

1. Click "Test Native RTF" in the extension
2. Open Adobe PageMaker 7.0
3. Create or open a document
4. Press Ctrl+V (paste)
5. Verify the text "TEST" appears in **Arial** font

**SUCCESS CRITERION**: PageMaker pastes "TEST" and automatically applies Arial formatting (proving it read the RTF format, not just plain text).

## What Has Been Verified

After completing all three tests:

- [x] Chrome extension communicates with native host
- [x] Native host writes to Windows clipboard
- [ ] Native "Rich Text Format" is present on clipboard (verify with tool)
- [ ] Adobe PageMaker 7.0 recognizes and pastes RTF with correct formatting

The last two items require testing on an actual Windows machine with the verification tool and PageMaker 7.0.

## What Remains Unverified

This POC does NOT yet verify:
- Integration with NonUnicodeConverter's actual converter logic
- Dynamic RTF generation (currently hard-coded)
- Unicode font mappings
- Non-Latin scripts (Tamil, Hindi, etc.)
- Production deployment
- User installation flow

**Do not integrate this POC with NonUnicodeConverter until PageMaker 7.0 verification succeeds.**

## Security Notes

- No arbitrary command execution
- No file system access
- No network access
- Only accepts `action: "set_clipboard"` messages
- Validates incoming JSON structure
- Per-user installation (no admin rights)
- Extension ID allowlist in manifest

## Files Created

```
rtf-clipboard-poc/
├── chrome-extension/
│   ├── manifest.json          # Manifest V3 with nativeMessaging
│   ├── popup.html             # Extension UI
│   ├── popup.js               # Native messaging client
│   └── README.md
├── native-host/
│   ├── src/
│   │   └── main.rs            # Native messaging host (Rust)
│   ├── Cargo.toml
│   └── README.md
├── installer/
│   ├── install.ps1            # PowerShell installer
│   └── README.md
├── verification/
│   ├── clipboard_inspector.rs # Clipboard verification tool
│   ├── Cargo.toml
│   └── README.md
└── README.md                  # This file
```

## GitHub Actions Build

A GitHub Actions workflow (`.github/workflows/build-windows.yml`) is included to build both 32-bit and 64-bit Windows executables automatically.

## Troubleshooting

### Extension shows "Native host disconnected"

**Cause**: Chrome cannot find or connect to the native host.

**Check**:
1. Extension ID in manifest matches the loaded extension
2. Chrome was restarted after updating the manifest
3. Registry entry exists: `HKCU\Software\Google\Chrome\NativeMessagingHosts\com.nonunicodeconverter.rtf_clipboard_poc`
4. Manifest path in registry is correct
5. Native host executable exists at the path in the manifest

**Fix**: Re-run `install.ps1` and restart Chrome.

### "Failed to open clipboard"

**Cause**: Another program has the clipboard locked.

**Fix**: Close other programs that might be using the clipboard, especially clipboard managers or sync tools.

### Verification tool shows "NOT FOUND"

**Cause**: Native host didn't write RTF, or clipboard was cleared.

**Check**:
1. Did extension show success?
2. Did you run the inspector immediately after clicking the button?
3. Check Windows Event Viewer for native host crashes

### PageMaker pastes plain text without formatting

**Cause**: PageMaker didn't recognize the RTF format.

This would indicate the POC **failed** — the native "Rich Text Format" is either:
- Not present on clipboard
- Malformed RTF syntax
- Not the format PageMaker expects

If verification tool shows ✅ SUCCESS but PageMaker doesn't recognize it, this is a critical finding that requires investigation.

## Next Steps After POC Success

If all three tests pass (especially PageMaker verification):

1. Document the successful test (screenshot/video)
2. Plan integration with NonUnicodeConverter
3. Design dynamic RTF generation for Unicode fonts
4. Test with actual Tamil/Hindi conversion output
5. Create production installer
6. Plan user onboarding flow

**Do NOT proceed with integration until PageMaker test succeeds.**

## License

This is a proof-of-concept component of the NonUnicodeConverter project.
