use rust_embed::RustEmbed;
use std::process::Command;
use tiny_http::{Server, Response, Header, Method, StatusCode};
use serde::Deserialize;
use std::io::Read;
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::Arc;
use std::time::Duration;
use std::env;
use std::path::PathBuf;

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
        let _ = plain_text;
        let _ = rtf_text;
        let _ = html_text;
        return Err("Not implemented for non-windows".into());
    }
}

// Generate a random 32 character token
fn generate_token() -> String {
    use std::time::{SystemTime, UNIX_EPOCH};
    let now = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_nanos();
    let rand = std::process::id();
    format!("{:x}{:x}", now, rand)
}

fn main() {
    // Bind to dynamically assigned loopback port
    let server = Server::http("127.0.0.1:0").unwrap();
    let port = server.server_addr().to_ip().unwrap().port();
    
    let token = generate_token();
    let url = format!("http://127.0.0.1:{}/?token={}", port, token);
    println!("LAUNCH_URL={}", url);
    
    // Find bundled Supermium
    let mut exe_dir = env::current_exe().unwrap_or_else(|_| PathBuf::from("."));
    exe_dir.pop();
    let supermium_path = exe_dir.join("supermium").join("chrome.exe");
    
    let mut child_proc = None;
    
    // Only launch if it actually exists, otherwise fallback to system default (for testing on Linux/dev)
    if supermium_path.exists() {
        if let Ok(child) = Command::new(&supermium_path)
            .arg(format!("--app={}", url))
            .arg("--no-first-run")
            .arg("--no-default-browser-check")
            .arg("--disable-sync")
            .arg("--disable-extensions")
            .spawn() 
        {
            child_proc = Some(child);
        }
    } else {
        // Fallback for dev environments where Supermium isn't bundled yet
        #[cfg(target_os = "linux")]
        {
            if let Ok(child) = Command::new("google-chrome").arg(format!("--app={}", url)).spawn() {
                child_proc = Some(child);
            }
        }
    }

    let running = Arc::new(AtomicBool::new(true));
    let r = running.clone();
    
    // Process monitor thread
    if let Some(mut child) = child_proc {
        std::thread::spawn(move || {
            let _ = child.wait();
            r.store(false, Ordering::SeqCst);
        });
    }

    // Accept connections with a timeout to allow checking if the process died
    while running.load(Ordering::SeqCst) {
        if let Ok(Some(mut request)) = server.recv_timeout(Duration::from_millis(500)) {
            // Handle OPTIONS request for CORS
            if request.method() == &Method::Options && request.url().starts_with("/api/clipboard") {
                let allow_origin = Header::from_bytes(&b"Access-Control-Allow-Origin"[..], &b"*"[..]).unwrap();
                let allow_methods = Header::from_bytes(&b"Access-Control-Allow-Methods"[..], &b"POST, OPTIONS"[..]).unwrap();
                let allow_headers = Header::from_bytes(&b"Access-Control-Allow-Headers"[..], &b"Content-Type, Authorization"[..]).unwrap();
                
                let response = Response::empty(StatusCode(204))
                    .with_header(allow_origin)
                    .with_header(allow_methods)
                    .with_header(allow_headers);
                let _ = request.respond(response);
                continue;
            }

            if request.method() == &Method::Post && request.url().starts_with("/api/clipboard") {
                let cors_header = Header::from_bytes(&b"Access-Control-Allow-Origin"[..], &b"*"[..]).unwrap();
                
                // Authenticate
                let mut authenticated = false;
                for header in request.headers() {
                    if header.field.equiv("Authorization") {
                        let val = header.value.as_str();
                        if val == format!("Bearer {}", token) {
                            authenticated = true;
                            break;
                        }
                    }
                }

                if !authenticated {
                    let response = Response::from_string("{\"error\":\"unauthorized\"}").with_status_code(StatusCode(401));
                    let _ = request.respond(response.with_header(cors_header));
                    continue;
                }

                let mut content = String::new();
                request.as_reader().read_to_string(&mut content).unwrap();
                
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
            
            let path = if request.url() == "/" || request.url().starts_with("/?") {
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
}
