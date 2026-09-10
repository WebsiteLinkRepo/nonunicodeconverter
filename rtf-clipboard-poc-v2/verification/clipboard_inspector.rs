// Clipboard Inspector - Verifies native Windows clipboard formats
// Compile: rustc clipboard_inspector.rs
// Run: ./clipboard_inspector.exe

#[cfg(windows)]
use windows::core::s;
#[cfg(windows)]
use windows::Win32::Foundation::{HANDLE, HGLOBAL};
#[cfg(windows)]
use windows::Win32::System::DataExchange::{
    CloseClipboard, CountClipboardFormats, EnumClipboardFormats, GetClipboardData,
    GetClipboardFormatNameA, OpenClipboard, RegisterClipboardFormatA,
};
#[cfg(windows)]
use windows::Win32::System::Memory::{GlobalLock, GlobalSize, GlobalUnlock};

#[cfg(windows)]
fn get_format_name(format: u32) -> String {
    // Standard formats
    match format {
        1 => "CF_TEXT".to_string(),
        2 => "CF_BITMAP".to_string(),
        3 => "CF_METAFILEPICT".to_string(),
        4 => "CF_SYLK".to_string(),
        5 => "CF_DIF".to_string(),
        6 => "CF_TIFF".to_string(),
        7 => "CF_OEMTEXT".to_string(),
        8 => "CF_DIB".to_string(),
        9 => "CF_PALETTE".to_string(),
        10 => "CF_PENDATA".to_string(),
        11 => "CF_RIFF".to_string(),
        12 => "CF_WAVE".to_string(),
        13 => "CF_UNICODETEXT".to_string(),
        14 => "CF_ENHMETAFILE".to_string(),
        15 => "CF_HDROP".to_string(),
        16 => "CF_LOCALE".to_string(),
        17 => "CF_DIBV5".to_string(),
        _ => {
            // Registered format - get name
            unsafe {
                let mut buffer = [0u8; 256];
                let len = GetClipboardFormatNameA(format, &mut buffer);
                if len > 0 {
                    String::from_utf8_lossy(&buffer[..len as usize]).to_string()
                } else {
                    format!("Unknown ({})", format)
                }
            }
        }
    }
}

#[cfg(windows)]
fn inspect_clipboard() {
    unsafe {
        if !OpenClipboard(None).as_bool() {
            eprintln!("Failed to open clipboard");
            return;
        }

        println!("=== Windows Clipboard Contents ===\n");

        let format_count = CountClipboardFormats();
        println!("Total formats available: {}\n", format_count);

        // Enumerate all formats
        let mut format = 0u32;
        let mut found_rtf = false;
        let mut format_list = Vec::new();

        loop {
            format = EnumClipboardFormats(format);
            if format == 0 {
                break;
            }

            let name = get_format_name(format);
            format_list.push((format, name.clone()));

            if name == "Rich Text Format" {
                found_rtf = true;
            }
        }

        // Display all formats
        println!("Available formats:");
        for (id, name) in &format_list {
            println!("  [{}] {}", id, name);
        }
        println!();

        // Check for RTF specifically
        let rtf_format = RegisterClipboardFormatA(s!("Rich Text Format"));
        if rtf_format > 0 {
            println!("🔍 Checking for 'Rich Text Format' (ID: {})...", rtf_format);

            if found_rtf {
                println!("✅ FOUND: Native 'Rich Text Format' is present!\n");

                // Try to read RTF data
                match GetClipboardData(rtf_format) {
                    Ok(handle) if !handle.is_invalid() => {
                        let hglobal = HGLOBAL(handle.0);
                        let ptr = GlobalLock(hglobal);
                        if !ptr.is_null() {
                            let size = GlobalSize(hglobal);
                            println!("RTF data size: {} bytes", size);

                            // Read first 200 bytes as preview
                            let slice = std::slice::from_raw_parts(ptr as *const u8, size.min(200));
                            if let Ok(preview) = std::str::from_utf8(slice) {
                                println!("\nRTF Preview (first 200 bytes):");
                                println!("---");
                                println!("{}", preview);
                                println!("---");
                            } else {
                                println!("\nRTF data is binary or non-UTF8");
                            }

                            let _ = GlobalUnlock(hglobal);
                        }
                    }
                    _ => {
                        println!("⚠️  Could not retrieve RTF data");
                    }
                }
            } else {
                println!("❌ NOT FOUND: 'Rich Text Format' is NOT present");
                println!("   The clipboard does not contain native RTF data.\n");
            }
        }

        // Check for plain text
        if let Ok(handle) = GetClipboardData(13) {
            if !handle.is_invalid() {
                let hglobal = HGLOBAL(handle.0);
                let ptr = GlobalLock(hglobal);
                if !ptr.is_null() {
                    let text_ptr = ptr as *const u16;
                    let mut len = 0;
                    while *text_ptr.add(len) != 0 {
                        len += 1;
                    }
                    let text_slice = std::slice::from_raw_parts(text_ptr, len);
                    let text = String::from_utf16_lossy(text_slice);

                    println!("\n📋 Plain text content:");
                    println!("{}", text);

                    let _ = GlobalUnlock(hglobal);
                }
            }
        }

        CloseClipboard();

        println!("\n=== Verification Summary ===");
        if found_rtf {
            println!("✅ SUCCESS: Native Windows 'Rich Text Format' is present");
            println!("   This clipboard data can be pasted into Adobe PageMaker 7.0");
        } else {
            println!("❌ FAILED: No native 'Rich Text Format' found");
            println!("   PageMaker 7.0 will not recognize RTF formatting");
        }
    }
}

#[cfg(not(windows))]
fn inspect_clipboard() {
    eprintln!("This tool only works on Windows");
}

fn main() {
    println!("RTF Clipboard Inspector\n");
    inspect_clipboard();
}
