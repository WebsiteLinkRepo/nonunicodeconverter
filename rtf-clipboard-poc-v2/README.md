# Minimal RTF Clipboard POC v2

**Testing ONLY the Native Messaging bridge to proven clipboard code.**

## What Changed from v1

v1 recreated the RTF clipboard implementation.
v2 uses the **existing proven code** from `src-tauri` and `legacy-launcher`.

The clipboard code is **identical** to what already works with PageMaker 7.0.

## Architecture

```
Chrome Extension (reused)
    ↓
Chrome Native Messaging (40 lines - NEW)
    ↓
Proven RTF clipboard code (60 lines - COPIED verbatim from src-tauri)
    ↓
Windows clipboard
    ↓
Adobe PageMaker 7.0 ✅ ALREADY PROVEN TO WORK
```

## What We're Testing

**ONLY:** Does Native Messaging successfully call the proven clipboard function?

**NOT:** Whether RTF works with PageMaker (it does — already proven).

## Files

```
rtf-clipboard-poc-v2/
├── native-host/
│   ├── src/main.rs        # 60 lines proven code + 40 lines Native Messaging wrapper
│   ├── Cargo.toml
│   └── README.md
├── chrome-extension/       # Reused from v1
├── installer/              # Reused from v1
├── verification/           # Reused from v1
└── README.md              # This file
```

## Build

```bash
cd rtf-clipboard-poc-v2/native-host
cargo +1.77 build --target i686-pc-windows-msvc --release
```

## Install & Test

Same as v1:

1. Run `installer/install.ps1`
2. Load `chrome-extension/` in Chrome
3. Update extension ID in manifest
4. Click "Test Native RTF"
5. Run `clipboard_inspector.exe`
6. **Paste in PageMaker 7.0**

## Success Criterion

PageMaker 7.0 pastes "TEST" in **Arial** font automatically.

This proves the Native Messaging bridge works.
