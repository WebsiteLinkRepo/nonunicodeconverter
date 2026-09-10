use serde::{Deserialize, Serialize};
use std::io::{self, Read, Write};

#[derive(Deserialize)]
struct Request {
    action: String,
    plain_text: Option<String>,
    rtf_text: Option<String>,
    html_text: Option<String>,
}

#[derive(Serialize)]
struct Response {
    success: bool,
    error: Option<String>,
}

/// Reads a Chrome Native Messaging message from stdin.
/// Chrome sends: 4-byte little-endian length, followed by JSON message.
fn read_message() -> io::Result<Request> {
    let mut length_bytes = [0u8; 4];
    io::stdin().read_exact(&mut length_bytes)?;
    let length = u32::from_le_bytes(length_bytes) as usize;

    let mut buffer = vec![0u8; length];
    io::stdin().read_exact(&mut buffer)?;

    serde_json::from_slice(&buffer).map_err(|e| io::Error::new(io::ErrorKind::InvalidData, e))
}

/// Writes a Chrome Native Messaging message to stdout.
/// Chrome expects: 4-byte little-endian length, followed by JSON message.
fn write_message(response: &Response) -> io::Result<()> {
    let json = serde_json::to_vec(response)?;
    let length = (json.len() as u32).to_le_bytes();

    io::stdout().write_all(&length)?;
    io::stdout().write_all(&json)?;
    io::stdout().flush()?;

    Ok(())
}

/// Copies text to the Windows native clipboard with multiple formats.
fn copy_to_native_clipboard(
    plain_text: String,
    rtf_text: String,
    html_text: String,
) -> Result<(), String> {
    #[cfg(windows)]
    {
        use windows::core::s;
        use windows::Win32::Foundation::HANDLE;
        use windows::Win32::System::DataExchange::{
            CloseClipboard, EmptyClipboard, OpenClipboard, RegisterClipboardFormatA,
            SetClipboardData,
        };
        use windows::Win32::System::Memory::{GlobalAlloc, GlobalLock, GlobalUnlock, GMEM_MOVEABLE};

        unsafe {
            // Open clipboard
            if !OpenClipboard(None).as_bool() {
                return Err("Failed to open clipboard".into());
            }

            // Empty clipboard
            let _ = EmptyClipboard();

            // 1. Plain text (CF_UNICODETEXT = 13)
            if !plain_text.is_empty() {
                let mut utf16: Vec<u16> = plain_text.encode_utf16().collect();
                utf16.push(0); // null terminator

                if let Ok(hglobal) = GlobalAlloc(GMEM_MOVEABLE, utf16.len() * 2) {
                    let ptr = GlobalLock(hglobal);
                    if !ptr.is_null() {
                        std::ptr::copy_nonoverlapping(
                            utf16.as_ptr(),
                            ptr as *mut u16,
                            utf16.len(),
                        );
                        let _ = GlobalUnlock(hglobal);
                        let _ = SetClipboardData(13, HANDLE(hglobal.0 as _));
                    }
                }
            }

            // 2. RTF (Registered "Rich Text Format")
            if !rtf_text.is_empty() {
                let format_rtf = RegisterClipboardFormatA(s!("Rich Text Format"));
                if format_rtf > 0 {
                    let mut rtf_bytes = rtf_text.into_bytes();
                    rtf_bytes.push(0); // null terminator

                    if let Ok(hglobal) = GlobalAlloc(GMEM_MOVEABLE, rtf_bytes.len()) {
                        let ptr = GlobalLock(hglobal);
                        if !ptr.is_null() {
                            std::ptr::copy_nonoverlapping(
                                rtf_bytes.as_ptr(),
                                ptr as *mut u8,
                                rtf_bytes.len(),
                            );
                            let _ = GlobalUnlock(hglobal);
                            let _ = SetClipboardData(format_rtf, HANDLE(hglobal.0 as _));
                        }
                    }
                }
            }

            // 3. HTML Format (Registered "HTML Format")
            if !html_text.is_empty() {
                let format_html = RegisterClipboardFormatA(s!("HTML Format"));
                if format_html > 0 {
                    // Build proper HTML Format clipboard format
                    // See: https://docs.microsoft.com/en-us/windows/win32/dataxchg/html-clipboard-format
                    let html_fragment = format!(
                        "Version:0.9\r\nStartHTML:00000097\r\nEndHTML:{:08}\r\nStartFragment:00000133\r\nEndFragment:{:08}\r\n<html><body><!--StartFragment-->{:}<!--EndFragment--></body></html>",
                        97 + html_text.len() + 73,
                        133 + html_text.len(),
                        html_text
                    );

                    let mut html_bytes = html_fragment.into_bytes();
                    html_bytes.push(0); // null terminator

                    if let Ok(hglobal) = GlobalAlloc(GMEM_MOVEABLE, html_bytes.len()) {
                        let ptr = GlobalLock(hglobal);
                        if !ptr.is_null() {
                            std::ptr::copy_nonoverlapping(
                                html_bytes.as_ptr(),
                                ptr as *mut u8,
                                html_bytes.len(),
                            );
                            let _ = GlobalUnlock(hglobal);
                            let _ = SetClipboardData(format_html, HANDLE(hglobal.0 as _));
                        }
                    }
                }
            }

            // Close clipboard
            let _ = CloseClipboard();
            Ok(())
        }
    }

    #[cfg(not(windows))]
    {
        let _ = (plain_text, rtf_text, html_text);
        Err("Not implemented for non-Windows platforms".into())
    }
}

fn main() {
    // Chrome Native Messaging protocol:
    // Read one message from stdin, process it, write response to stdout, exit.

    let response = match read_message() {
        Ok(request) => {
            if request.action == "set_clipboard" {
                let plain = request.plain_text.unwrap_or_default();
                let rtf = request.rtf_text.unwrap_or_default();
                let html = request.html_text.unwrap_or_default();

                match copy_to_native_clipboard(plain, rtf, html) {
                    Ok(()) => Response {
                        success: true,
                        error: None,
                    },
                    Err(e) => Response {
                        success: false,
                        error: Some(e),
                    },
                }
            } else {
                Response {
                    success: false,
                    error: Some(format!("Unknown action: {}", request.action)),
                }
            }
        }
        Err(e) => Response {
            success: false,
            error: Some(format!("Failed to read message: {}", e)),
        },
    };

    // Write response and exit
    let _ = write_message(&response);
}
