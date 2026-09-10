const fs = require('fs');
const path = require('path');
const file = path.join(__dirname, 'src/components/TextConverter.astro');
let code = fs.readFileSync(file, 'utf8');

// Replace the hardcoded fetch with dynamic logic
const target = `
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
`;

const replacement = `
          // Legacy Wrapper Fallback
          try {
            const isLocal = window.location.hostname === '127.0.0.1' || window.location.hostname === 'localhost';
            const urlParams = new URLSearchParams(window.location.search);
            const token = urlParams.get('token');
            if (isLocal && token) {
              const legacyRes = await fetch(\`http://127.0.0.1:\${window.location.port}/api/clipboard\`, {
                method: 'POST',
                headers: { 
                  'Content-Type': 'application/json',
                  'Authorization': \`Bearer \${token}\`
                },
                body: JSON.stringify({
                  plain_text: plainText,
                  rtf_text: rtfText,
                  html_text: htmlText
                })
              });
`;

code = code.replace(target, replacement);

const target2 = `
            if (legacyRes.ok) {
`;

const replacement2 = `
              if (legacyRes.ok) {
                setCopyFeedback(t.copied);
                setTimeout(() => setCopyFeedback(t.copy), 2000);
                return;
              }
            }
`;
code = code.replace(target2, replacement2);

fs.writeFileSync(file, code);
