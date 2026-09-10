const fs = require('fs');
const path = require('path');
const file = path.join(__dirname, 'src/components/TextConverter.astro');
let code = fs.readFileSync(file, 'utf8');

// We want to update the copy logic:
// if (window.__TAURI_INTERNALS__) { ... }
// else { try { await fetch('http://127.0.0.1:14231/api/clipboard', { ... }); } catch(e) { /* web fallback */ } }

const target = `
          // Web fallback
          const rtfevt = (e) => {
`;

const replacement = `
          // Legacy Wrapper Fallback
          try {
            const legacyRes = await fetch('http://127.0.0.1:14231/api/clipboard', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                plain_text: plainText,
                rtf_text: rtfText,
                html_text: htmlText
              })
            });
            if (legacyRes.ok) {
              setCopyFeedback(t.copied);
              setTimeout(() => setCopyFeedback(t.copy), 2000);
              return;
            }
          } catch(e) {
            // Ignored, means we are on the normal web
          }

          // Web fallback
          const rtfevt = (e) => {
`;

code = code.replace(target, replacement);
fs.writeFileSync(file, code);
