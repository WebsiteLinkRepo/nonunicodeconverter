// Native Messaging Host - Minimal bridge to proven RTF clipboard implementation
//
// This is ONLY a Native Messaging protocol wrapper around the existing proven
// clipboard code from legacy-launcher/src-tauri that already works with PageMaker 7.0

use serde::{Deserialize, Serialize};
use std::io::{self, Read, Write};

#[derive(Deserialize)]
struct NativeMessage {
    action: String,
    plain_text: Option<String>,
    rtf_text: Option<String>,
    html_text: Option<String>,
}

#[derive(Serialize)]
struct NativeResponse {
    success: bool,
    error: Option<String>,
}

// Chrome Native Messaging: Read 4-byte length + JSON message from stdin
fn read_native_message() -> io::Result<NativeMessage> {
    let mut length_bytes = [0u8; 4];
    io::stdin().read_exact(&mut length_bytes)?;
    let length = u32::from_le_bytes(length_bytes) as usize;

    let mut buffer = vec![0u8; length];
    io::stdin().read_exact(&mut buffer)?;

    serde_json::from_slice(&buffer).map_err(|e| io::Error::new(io::ErrorKind::InvalidData, e))
}

// Chrome Native Messaging: Write 4-byte length + JSON response to stdout
fn write_native_response(response: &NativeResponse) -> io::Result<()> {
    let json = serde_json::to_vec(response)?;
    let length = (json.len() as u32).to_le_bytes();

    io::stdout().write_all(&length)?;
    io::stdout().write_all(&json)?;
    io::stdout().flush()?;
    Ok(())
}

// ============================================================================
// PROVEN RTF CLIPBOARD IMPLEMENTATION
// Copied verbatim from src-tauri/src/lib.rs and legacy-launcher/src/main.rs
// This code is PROVEN to work with Adobe PageMaker 7.0
// ============================================================================

fn copy_to_native_clipboard(plain_text: String, rtf_text: String, html_text: String) -> Result<(), String> {
    #[cfg(windows)]
    {
        use windows::core::s;
        use windows::Win32::Foundation::HANDLE;
        use windows::Win32::System::Memory::{GlobalAlloc, GlobalLock, GlobalUnlock, GMEM_MOVEABLE};
        use windows::Win32::System::DataExchange::{OpenClipboard, CloseClipboard, EmptyClipboard, SetClipboardData, RegisterClipboardFormatA};

        unsafe {
            if !OpenClipboard(None).as_bool() {
                return Err("Failed to open clipboard".into());
            }
            let _ = EmptyClipboard();

            // Plain text (CF_UNICODETEXT = 13)
            let mut utf16: Vec<u16> = plain_text.encode_utf16().collect();
            utf16.push(0);

            if let Ok(hglobal) = GlobalAlloc(GMEM_MOVEABLE, utf16.len() * 2) {
                let ptr = GlobalLock(hglobal);
                if !ptr.is_null() {
                    std::ptr::copy_nonoverlapping(utf16.as_ptr(), ptr as *mut u16, utf16.len());
                    let _ = GlobalUnlock(hglobal);
                    let _ = SetClipboardData(13, HANDLE(hglobal.0 as _));
                }
            }

            // RTF - This is the CRITICAL part that PageMaker 7.0 reads
            if !rtf_text.is_empty() {
                let format_rtf = RegisterClipboardFormatA(s!("Rich Text Format"));
                if format_rtf > 0 {
                    let mut rtf_bytes = rtf_text.into_bytes();
                    rtf_bytes.push(0);
                    if let Ok(hglobal) = GlobalAlloc(GMEM_MOVEABLE, rtf_bytes.len()) {
                        let ptr = GlobalLock(hglobal);
                        if !ptr.is_null() {
                            std::ptr::copy_nonoverlapping(rtf_bytes.as_ptr(), ptr as *mut u8, rtf_bytes.len());
                            let _ = GlobalUnlock(hglobal);
                            let _ = SetClipboardData(format_rtf, HANDLE(hglobal.0 as _));
                        }
                    }
                }
            }

            // HTML
            if !html_text.is_empty() {
                let format_html = RegisterClipboardFormatA(s!("HTML Format"));
                if format_html > 0 {
                    let mut html_bytes = html_text.into_bytes();
                    html_bytes.push(0);
                    if let Ok(hglobal) = GlobalAlloc(GMEM_MOVEABLE, html_bytes.len()) {
                        let ptr = GlobalLock(hglobal);
                        if !ptr.is_null() {
                            std::ptr::copy_nonoverlapping(html_bytes.as_ptr(), ptr as *mut u8, html_bytes.len());
                            let _ = GlobalUnlock(hglobal);
                            let _ = SetClipboardData(format_html, HANDLE(hglobal.0 as _));
                        }
                    }
                }
            }

            let _ = CloseClipboard();
            Ok(())
        }
    }

    #[cfg(not(windows))]
    {
        let _ = (plain_text, rtf_text, html_text);
        Err("Not implemented for non-Windows".into())
    }
}

// ============================================================================
// NATIVE MESSAGING BRIDGE - The only new code
// ============================================================================

fn main() {
    // Native Messaging: read one message, process, respond, exit
    let response = match read_native_message() {
        Ok(msg) if msg.action == "set_clipboard" => {
            let plain = msg.plain_text.unwrap_or_default();
            let rtf = msg.rtf_text.unwrap_or_default();
            let html = msg.html_text.unwrap_or_default();

            match copy_to_native_clipboard(plain, rtf, html) {
                Ok(()) => NativeResponse { success: true, error: None },
                Err(e) => NativeResponse { success: false, error: Some(e) },
            }
        }
        Ok(msg) => NativeResponse {
            success: false,
            error: Some(format!("Unknown action: {}", msg.action)),
        },
        Err(e) => NativeResponse {
            success: false,
            error: Some(format!("Failed to read message: {}", e)),
        },
    };

    let _ = write_native_response(&response);
}
