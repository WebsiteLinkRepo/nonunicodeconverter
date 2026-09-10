# Native Messaging Host - RTF Clipboard POC

Windows native messaging host executable that receives JSON messages from Chrome and writes native RTF to the Windows clipboard using Win32 APIs.

## What it does

1. Receives JSON message from Chrome via stdin (Chrome Native Messaging protocol)
2. Extracts `plain_text`, `rtf_text`, and `html_text` fields
3. Writes all three formats to the Windows clipboard:
   - **Rich Text Format** (registered clipboard format)
   - **CF_UNICODETEXT** (plain text)
   - **HTML Format** (registered clipboard format)
4. Returns success/error JSON response via stdout
5. Exits

## Build Requirements

- Rust toolchain (1.77 or newer recommended for modern Windows)
- Windows target: `i686-pc-windows-msvc` (32-bit) or `x86_64-pc-windows-msvc` (64-bit)

## Build Instructions

### For Windows 7/8/8.1 (32-bit):

```bash
rustup target add i686-pc-windows-msvc
cargo build --target i686-pc-windows-msvc --release
```

The executable will be at: `target/i686-pc-windows-msvc/release/rtf_clipboard_host.exe`

### For modern Windows (64-bit):

```bash
cargo build --release
```

The executable will be at: `target/release/rtf_clipboard_host.exe`

## Testing the Native Host Directly

You can test the native host from the command line before integrating with Chrome:

```powershell
# Create test message
$message = @{
    action = "set_clipboard"
    plain_text = "TEST"
    rtf_text = "{\rtf1\ansi{\fonttbl{\f0 Arial;}}\f0 TEST}"
    html_text = "<p style='font-family: Arial'>TEST</p>"
} | ConvertTo-Json

# Encode as Chrome Native Messaging format (4-byte length prefix + JSON)
$bytes = [System.Text.Encoding]::UTF8.GetBytes($message)
$length = [BitConverter]::GetBytes([int32]$bytes.Length)

# Write to temp file
$tempFile = "test_message.bin"
[System.IO.File]::WriteAllBytes($tempFile, $length + $bytes)

# Run the host
Get-Content $tempFile -Raw -Encoding Byte | .\target\release\rtf_clipboard_host.exe

# Check response (should print JSON with success:true)
```

## Security Notes

- Validates incoming JSON structure
- Only accepts `action: "set_clipboard"`
- No arbitrary command execution
- No file system access
- No network access
- Minimal attack surface

## Installation

See `../installer/README.md` for native messaging registration steps.
