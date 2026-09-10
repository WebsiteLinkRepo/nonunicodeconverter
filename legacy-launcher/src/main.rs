use rust_embed::RustEmbed;
use std::process::{Command, Stdio};
use tiny_http::{Server, Response, Header, Method, StatusCode};
use serde::{Deserialize, Serialize};
use std::io::Read;
use std::thread;

#[derive(RustEmbed)]
#[folder = "../dist"]
struct Asset;

#[derive(Deserialize)]
struct ClipboardPayload {
    plain_text: String,
    rtf_text: String,
    html_text: String,
}

fn copy_to_native_clipboard(plain_text: String, rtf_text: String, html_text: String) -> Result<bool, String> {
    #[cfg(windows)]
    {
        use windows::core::s;
        use windows::Win32::Foundation::{HANDLE, HGLOBAL};
        use windows::Win32::System::Memory::{GlobalAlloc, GlobalLock, GlobalUnlock, GMEM_MOVEABLE};
        use windows::Win32::System::DataExchange::{OpenClipboard, CloseClipboard, EmptyClipboard, SetClipboardData, RegisterClipboardFormatA};
        
        unsafe {
            if OpenClipboard(None).is_err() {
                return Err("Failed to open clipboard".into());
            }
            let _ = EmptyClipboard();
            
            // Plain text (CF_UNICODETEXT)
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
            
            // RTF
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
            return Ok(true);
        }
    }
    
    #[cfg(not(windows))]
    {
        return Err("Not implemented for non-windows".into());
    }
}

fn main() {
    let port = 14231;
    let server = Server::http(format!("127.0.0.1:{}", port)).unwrap();
    println!("Server running on http://127.0.0.1:{}", port);
    
    // Launch browser
    let url = format!("http://127.0.0.1:{}", port);
    
    // Try to find a browser. For prototype, try Supermium, Chrome, Edge
    let browser_paths = vec![
        "chrome",
        "supermium",
        r#"C:\Program Files\Supermium\chrome.exe"#,
        r#"C:\Program Files (x86)\Supermium\chrome.exe"#,
        r#"C:\Program Files\Google\Chrome\Application\chrome.exe"#,
        r#"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"#,
        r#"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"#,
    ];
    
    let mut child_proc = None;
    for path in browser_paths {
        if let Ok(child) = Command::new(path)
            .arg(format!("--app={}", url))
            .arg("--no-first-run")
            .arg("--no-default-browser-check")
            .spawn() 
        {
            println!("Launched browser: {}", path);
            child_proc = Some(child);
            break;
        }
    }

    if child_proc.is_none() {
        println!("Could not find a suitable browser. Please open {} manually.", url);
    }
    
    // Accept connections
    for mut request in server.incoming_requests() {
        if request.method() == &Method::Post && request.url() == "/api/clipboard" {
            let mut content = String::new();
            request.as_reader().read_to_string(&mut content).unwrap();
            
            // Set CORS headers so fetch() from JS doesn't fail
            let cors_header = Header::from_bytes(&b"Access-Control-Allow-Origin"[..], &b"*"[..]).unwrap();
            
            if let Ok(payload) = serde_json::from_str::<ClipboardPayload>(&content) {
                match copy_to_native_clipboard(payload.plain_text, payload.rtf_text, payload.html_text) {
                    Ok(_) => {
                        let response = Response::from_string("{\"success\":true}").with_status_code(StatusCode(200));
                        let _ = request.respond(response.with_header(cors_header));
                    }
                    Err(e) => {
                        let response = Response::from_string(format!("{{\"error\":\"{}\"}}", e)).with_status_code(StatusCode(500));
                        let _ = request.respond(response.with_header(cors_header));
                    }
                }
            } else {
                let response = Response::from_string("{\"error\":\"invalid payload\"}").with_status_code(StatusCode(400));
                let _ = request.respond(response.with_header(cors_header));
            }
            continue;
        }

        // Handle OPTIONS request for CORS
        if request.method() == &Method::Options && request.url() == "/api/clipboard" {
            let allow_origin = Header::from_bytes(&b"Access-Control-Allow-Origin"[..], &b"*"[..]).unwrap();
            let allow_methods = Header::from_bytes(&b"Access-Control-Allow-Methods"[..], &b"POST, OPTIONS"[..]).unwrap();
            let allow_headers = Header::from_bytes(&b"Access-Control-Allow-Headers"[..], &b"Content-Type"[..]).unwrap();
            
            let response = Response::empty(StatusCode(204))
                .with_header(allow_origin)
                .with_header(allow_methods)
                .with_header(allow_headers);
            let _ = request.respond(response);
            continue;
        }
        
        let path = if request.url() == "/" {
            "index.html"
        } else {
            &request.url()[1..] // strip leading slash
        };
        
        // Split query params if any
        let path = path.split('?').next().unwrap_or(path);
        
        if let Some(content) = Asset::get(path) {
            let mime = mime_guess::from_path(path).first_or_octet_stream();
            let header = Header::from_bytes(&b"Content-Type"[..], mime.as_ref().as_bytes()).unwrap();
            let response = Response::from_data(content.data.into_owned()).with_header(header);
            let _ = request.respond(response);
        } else {
            // fallback to index.html for SPA routing (if any) or 404
            if let Some(content) = Asset::get("index.html") {
                let header = Header::from_bytes(&b"Content-Type"[..], &b"text/html"[..]).unwrap();
                let response = Response::from_data(content.data.into_owned()).with_header(header);
                let _ = request.respond(response);
            } else {
                let _ = request.respond(Response::from_string("Not Found").with_status_code(StatusCode(404)));
            }
        }
    }
}
