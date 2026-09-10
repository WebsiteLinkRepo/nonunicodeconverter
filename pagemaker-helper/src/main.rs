#![windows_subsystem = "windows"]

use std::env;
use std::fs::OpenOptions;
use std::io::Write as IoWrite;

// Debug logging function - writes to C:\pagemaker_helper_debug.log
// Errors are silently ignored so logging never breaks the main operation
fn log_debug(message: &str) {
    let log_path = r"C:\pagemaker_helper_debug.log";
    let _ = (|| -> std::io::Result<()> {
        let timestamp = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .unwrap_or(std::time::Duration::from_secs(0))
            .as_secs();
        let mut file = OpenOptions::new()
            .create(true)
            .append(true)
            .open(log_path)?;
        writeln!(file, "[{}] {}", timestamp, message)?;
        Ok(())
    })();
}

fn copy_to_native_clipboard(plain_text: String, rtf_text: String, html_bytes: Vec<u8>) -> Result<(), String> {
    #[cfg(windows)]
    {
        use windows::core::s;
        use windows::Win32::Foundation::HANDLE;
        use windows::Win32::System::Memory::{GlobalAlloc, GlobalLock, GlobalUnlock, GMEM_MOVEABLE};
        use windows::Win32::System::DataExchange::{OpenClipboard, CloseClipboard, EmptyClipboard, SetClipboardData, RegisterClipboardFormatA};

        unsafe {
            if OpenClipboard(None).is_err() {
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

            // HTML (Write back the exact bytes we read)
            if !html_bytes.is_empty() {
                let format_html = RegisterClipboardFormatA(s!("HTML Format"));
                if format_html > 0 {
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

fn read_clipboard_data() -> Result<(String, Vec<u8>), String> {
    #[cfg(windows)]
    {
        use windows::core::s;
        use windows::Win32::System::DataExchange::{OpenClipboard, CloseClipboard, GetClipboardData, RegisterClipboardFormatA};
        use windows::Win32::System::Memory::{GlobalLock, GlobalUnlock};
        use windows::Win32::Foundation::HGLOBAL;
        use std::ffi::OsString;
        use std::os::windows::ffi::OsStringExt;

        unsafe {
            if OpenClipboard(None).is_err() {
                return Err("Failed to open clipboard for reading".into());
            }
            
            // Read Plain Text (CF_UNICODETEXT = 13)
            let mut text = String::new();
            if let Ok(handle) = GetClipboardData(13) {
                let hglobal = HGLOBAL(handle.0 as _);
                let ptr = GlobalLock(hglobal);
                if !ptr.is_null() {
                    let mut len = 0;
                    let u16_ptr = ptr as *const u16;
                    while *u16_ptr.add(len) != 0 {
                        len += 1;
                    }
                    let slice = std::slice::from_raw_parts(u16_ptr, len);
                    let os_string = OsString::from_wide(slice);
                    text = os_string.into_string().unwrap_or_default();
                    let _ = GlobalUnlock(hglobal);
                }
            }

            // Read HTML Format
            let mut html_bytes = Vec::new();
            let format_html = RegisterClipboardFormatA(s!("HTML Format"));
            if format_html > 0 {
                if let Ok(handle) = GetClipboardData(format_html) {
                    let hglobal = HGLOBAL(handle.0 as _);
                    let ptr = GlobalLock(hglobal);
                    if !ptr.is_null() {
                        use windows::Win32::System::Memory::GlobalSize;
                        let size = GlobalSize(hglobal);
                        let slice = std::slice::from_raw_parts(ptr as *const u8, size);
                        html_bytes.extend_from_slice(slice);
                        let _ = GlobalUnlock(hglobal);
                    }
                }
            }

            let _ = CloseClipboard();
            
            Ok((text, html_bytes))
        }
    }
    #[cfg(not(windows))]
    Err("Not implemented".into())
}

fn show_error_message(_message: &str) {
    #[cfg(windows)]
    {
        use windows::core::{s, PCSTR};
        use windows::Win32::UI::WindowsAndMessaging::{MessageBoxA, MB_OK, MB_ICONERROR};
        let c_msg = std::ffi::CString::new(_message).unwrap_or_default();
        unsafe {
            MessageBoxA(
                None,
                PCSTR(c_msg.as_ptr() as *const u8),
                s!("PageMaker Auto Font Changer Error"),
                MB_OK | MB_ICONERROR,
            );
        }
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    log_debug(&format!("Helper started with args: {:?}", args));

    // Wait slightly to ensure browser releases focus or handles protocol UI
    std::thread::sleep(std::time::Duration::from_millis(100));

    // Verify args
    let mut font_name = "Arial".to_string();
    for arg in args.iter().skip(1) {
        if arg.starts_with("nonunicode://pagemaker") {
            // Parse nonunicode://pagemaker?font=Priyanka
            if let Some(query) = arg.split('?').nth(1) {
                if query.starts_with("font=") {
                    let encoded_font = &query[5..];
                    // Very basic URL decoding (replace %20 with space)
                    let decoded = encoded_font.replace("%20", " ");
                    // Sanitize against injection
                    font_name = decoded.chars().filter(|c| c.is_alphanumeric() || *c == ' ' || *c == '-').collect();
                    if font_name.is_empty() {
                        font_name = "Arial".to_string();
                    }
                }
            }
            break;
        }
    }

    log_debug(&format!("Protocol detected. Font target: {}. Reading clipboard...", font_name));

    let (plain, html_bytes) = match read_clipboard_data() {
        Ok(t) => t,
        Err(e) => {
            log_debug(&format!("Failed to read clipboard: {}", e));
            return; // Silently exit if no text
        }
    };

    if plain.trim().is_empty() {
        log_debug("Clipboard is empty.");
        return;
    }

    // Generate real RTF payload
    let mut rtf = String::new();
    rtf.push_str(r#"{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 "#);
    rtf.push_str(&font_name);
    rtf.push_str(r#";}}
{\*\generator Riched20 10.0.19041}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 "#);
    
    // Basic RTF escaping for plain text
    for c in plain.chars() {
        match c {
            '\\' => rtf.push_str("\\\\"),
            '{' => rtf.push_str("\\{"),
            '}' => rtf.push_str("\\}"),
            '\n' => rtf.push_str("\\par\n"),
            '\r' => {}, // ignore CR
            _ => {
                if (c as u32) > 127 {
                    rtf.push_str(&format!("\\'{:02x}", c as u32 & 0xFF));
                } else {
                    rtf.push(c);
                }
            }
        }
    }
    rtf.push_str("\\par\n}\n");

    match copy_to_native_clipboard(plain, rtf, html_bytes) {
        Ok(()) => {
            log_debug("Clipboard write succeeded.");
        }
        Err(e) => {
            log_debug(&format!("Clipboard write failed: {}", e));
            show_error_message(&format!("Could not write to Windows Clipboard: {}", e));
        }
    }
}
