// Standalone RTF Clipboard Test
// Bypasses Chrome Extension - calls clipboard code directly
// Tests whether the proven Win32 clipboard implementation works on Windows 7

fn copy_to_native_clipboard(plain_text: String, rtf_text: String, html_text: String) -> Result<(), String> {
    #[cfg(windows)]
    {
        use windows::core::s;
        use windows::Win32::Foundation::HANDLE;
        use windows::Win32::System::Memory::{GlobalAlloc, GlobalLock, GlobalUnlock, GMEM_MOVEABLE};
        use windows::Win32::System::DataExchange::{OpenClipboard, CloseClipboard, EmptyClipboard, SetClipboardData, RegisterClipboardFormatA};

        unsafe {
            println!("DEBUG: Opening clipboard...");
            if !OpenClipboard(None).as_bool() {
                return Err("Failed to open clipboard".into());
            }
            println!("DEBUG: Clipboard opened successfully");

            if !EmptyClipboard().as_bool() {
                let _ = CloseClipboard();
                return Err("Failed to empty clipboard".into());
            }
            println!("DEBUG: Clipboard emptied");

            // Plain text (CF_UNICODETEXT = 13)
            println!("DEBUG: Writing plain text: {}", plain_text);
            let mut utf16: Vec<u16> = plain_text.encode_utf16().collect();
            utf16.push(0);

            if let Ok(hglobal) = GlobalAlloc(GMEM_MOVEABLE, utf16.len() * 2) {
                let ptr = GlobalLock(hglobal);
                if !ptr.is_null() {
                    std::ptr::copy_nonoverlapping(utf16.as_ptr(), ptr as *mut u16, utf16.len());
                    GlobalUnlock(hglobal);
                    let result = SetClipboardData(13, HANDLE(hglobal.0 as _));
                    if result.is_invalid() {
                        let _ = CloseClipboard();
                        return Err("Failed to set plain text clipboard data".into());
                    }
                    println!("DEBUG: Plain text written successfully");
                }
            }

            // RTF - This is the CRITICAL part that PageMaker 7.0 reads
            if !rtf_text.is_empty() {
                println!("DEBUG: Registering RTF format...");
                let format_rtf = RegisterClipboardFormatA(s!("Rich Text Format"));
                println!("DEBUG: RTF format ID: {}", format_rtf);

                if format_rtf > 0 {
                    let mut rtf_bytes = rtf_text.into_bytes();
                    println!("DEBUG: RTF bytes length (before null): {}", rtf_bytes.len());
                    println!("DEBUG: RTF content: {:?}", String::from_utf8_lossy(&rtf_bytes));
                    rtf_bytes.push(0);

                    println!("DEBUG: Allocating {} bytes for RTF", rtf_bytes.len());
                    if let Ok(hglobal) = GlobalAlloc(GMEM_MOVEABLE, rtf_bytes.len()) {
                        println!("DEBUG: Memory allocated, HGLOBAL: {:?}", hglobal);
                        let ptr = GlobalLock(hglobal);
                        println!("DEBUG: Memory locked, ptr: {:?}", ptr);

                        if !ptr.is_null() {
                            std::ptr::copy_nonoverlapping(rtf_bytes.as_ptr(), ptr as *mut u8, rtf_bytes.len());
                            println!("DEBUG: RTF bytes copied to memory");

                            GlobalUnlock(hglobal);
                            println!("DEBUG: Memory unlocked");

                            let result = SetClipboardData(format_rtf, HANDLE(hglobal.0 as _));
                            if result.is_invalid() {
                                let _ = CloseClipboard();
                                return Err("Failed to set RTF clipboard data".into());
                            }
                            println!("DEBUG: ✅ RTF data set successfully! Format ID: {}", format_rtf);
                        } else {
                            let _ = CloseClipboard();
                            return Err("Failed to lock RTF memory".into());
                        }
                    } else {
                        let _ = CloseClipboard();
                        return Err("Failed to allocate RTF memory".into());
                    }
                } else {
                    let _ = CloseClipboard();
                    return Err("Failed to register RTF format (returned 0)".into());
                }
            }

            // HTML
            if !html_text.is_empty() {
                println!("DEBUG: Writing HTML format...");
                let format_html = RegisterClipboardFormatA(s!("HTML Format"));
                if format_html > 0 {
                    let mut html_bytes = html_text.into_bytes();
                    html_bytes.push(0);
                    if let Ok(hglobal) = GlobalAlloc(GMEM_MOVEABLE, html_bytes.len()) {
                        let ptr = GlobalLock(hglobal);
                        if !ptr.is_null() {
                            std::ptr::copy_nonoverlapping(html_bytes.as_ptr(), ptr as *mut u8, html_bytes.len());
                            GlobalUnlock(hglobal);
                            let result = SetClipboardData(format_html, HANDLE(hglobal.0 as _));
                            if result.is_invalid() {
                                let _ = CloseClipboard();
                                return Err("Failed to set HTML clipboard data".into());
                            }
                            println!("DEBUG: HTML written successfully");
                        }
                    }
                }
            }

            if !CloseClipboard().as_bool() {
                return Err("Failed to close clipboard".into());
            }
            println!("DEBUG: Clipboard closed successfully");
            Ok(())
        }
    }

    #[cfg(not(windows))]
    {
        let _ = (plain_text, rtf_text, html_text);
        Err("Not implemented for non-Windows".into())
    }
}

fn main() {
    println!("RTF Clipboard Standalone Test");
    println!("==============================\n");

    let plain_text = "TEST".to_string();
    let rtf_text = r"{\rtf1\ansi{\fonttbl{\f0 Arial;}}\f0 TEST}".to_string();
    let html_text = r#"<html><body><p style="font-family: Arial">TEST</p></body></html>"#.to_string();

    println!("Writing to clipboard:");
    println!("  Plain text: {}", plain_text);
    println!("  RTF: {}", rtf_text);
    println!("  HTML: (included)\n");

    match copy_to_native_clipboard(plain_text, rtf_text, html_text) {
        Ok(()) => {
            println!("✅ SUCCESS: Clipboard written!");
            println!("\nNext step:");
            println!("  Run clipboard_inspector.exe to verify RTF format is present");
            std::process::exit(0);
        }
        Err(e) => {
            eprintln!("❌ ERROR: {}", e);
            std::process::exit(1);
        }
    }
}
