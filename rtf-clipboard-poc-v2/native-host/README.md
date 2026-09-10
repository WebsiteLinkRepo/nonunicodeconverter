# Minimal Native Messaging Bridge to Proven RTF Clipboard

This is the **absolute minimum** code needed to bridge Chrome/Firefox Native Messaging to the existing proven RTF clipboard implementation.

## What This Is

**Just a wrapper.** The RTF clipboard code is copied verbatim from `src-tauri/src/lib.rs` and `legacy-launcher/src/main.rs` — both already proven to work with Adobe PageMaker 7.0.

The only new code is:
- Chrome Native Messaging protocol (read/write stdin/stdout)
- JSON message parsing
- ~40 lines total

## What We're Testing

```
Chrome Extension → Native Messaging → PROVEN clipboard code → PageMaker 7.0
                   ↑ This is the ONLY new part
```

We're NOT testing whether the RTF clipboard works (it does).
We're testing whether Native Messaging can reach it.

## Build (Windows 7 / 32-bit)

```bash
cd rtf-clipboard-poc-v2/native-host
cargo +1.77 build --target i686-pc-windows-msvc --release
```

Output: `target/i686-pc-windows-msvc/release/rtf_native_host.exe`

## Files

- `src/main.rs` - 100 lines total:
  - 60 lines: proven RTF clipboard code (unchanged)
  - 40 lines: Native Messaging wrapper (new)
- `Cargo.toml` - Dependencies (same as proven implementation)

## Next Steps

1. Use the Chrome extension from `../chrome-extension/` (unchanged)
2. Install with `../installer/install.ps1`
3. Test with hard-coded RTF: `{\rtf1\ansi{\fonttbl{\f0 Arial;}}\f0 TEST}`
4. Verify with clipboard inspector
5. **Paste in PageMaker 7.0 → Should show Arial font**

If this works, the Native Messaging bridge is proven.
Then we connect it to the real converter.
