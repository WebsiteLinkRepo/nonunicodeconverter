const fs = require('fs');
const replacement = `
  const cp1252 = {
    0x20AC: 0x80, 0x201A: 0x82, 0x0192: 0x83, 0x201E: 0x84, 0x2026: 0x85, 0x2020: 0x86, 0x2021: 0x87,
    0x02C6: 0x88, 0x2030: 0x89, 0x0160: 0x8A, 0x2039: 0x8B, 0x0152: 0x8C, 0x017D: 0x8E, 0x2018: 0x91,
    0x2019: 0x92, 0x201C: 0x93, 0x201D: 0x94, 0x2022: 0x95, 0x2013: 0x96, 0x2014: 0x97, 0x02DC: 0x98,
    0x2122: 0x99, 0x0161: 0x9A, 0x203A: 0x9B, 0x0153: 0x9C, 0x017E: 0x9E, 0x0178: 0x9F
  };

  function charToWin1252(char) {
    const code = char.charCodeAt(0);
    if (cp1252[code]) return cp1252[code];
    if (code <= 255) return code;
    return 63; // '?' fallback
  }

  function generateRTF(text, fontName) {
    let rtf = \`{\\\\rtf1\\\\ansi\\\\ansicpg1252\\\\deff0{\\\\fonttbl{\\\\f0\\\\fnil\\\\fcharset0 \${fontName};}}\\n\\\\viewkind4\\\\uc1\\\\pard\\\\lang1033\\\\f0\\\\fs24 \`;
    for (let i = 0; i < text.length; i++) {
      const char = text[i];
      if (char === '\\n') {
        rtf += '\\\\par\\n';
      } else if (char === '\\r') {
        // ignore
      } else if (char === '\\\\') {
        rtf += '\\\\\\\\';
      } else if (char === '{') {
        rtf += '\\\\{';
      } else if (char === '}') {
        rtf += '\\\\}';
      } else {
        const code = charToWin1252(char);
        if (code > 127 || code < 32) {
          rtf += \`\\\\\` + \`'\` + code.toString(16).padStart(2, '0');
        } else {
          rtf += char;
        }
      }
    }
    rtf += '}';
    return rtf;
  }

  // Copy Output Handler
  copyBtn.addEventListener('click', async () => {
    let val = outputText.value;
    const t = TRANSLATIONS[currentLang] || TRANSLATIONS.en;
    if (!val) {
      inputText.focus();
      return;
    }

    const rtfText = generateRTF(val, fontStyles[selectedFontStyle] || 'AnuPriyanka');

    let success = false;
    const listener = (e) => {
      e.preventDefault();
      if (e.clipboardData) {
        e.clipboardData.setData('text/plain', val);
        e.clipboardData.setData('text/rtf', rtfText);
        success = true;
      }
    };

    outputText.select();
    document.addEventListener('copy', listener);
    const result = document.execCommand('copy');
    document.removeEventListener('copy', listener);

    if (success && result) {
      copyBtnText.textContent = t.copiedBtn;
      copyBtn.classList.remove('bg-[var(--ink)]');
      copyBtn.classList.add('bg-emerald-600', 'text-white');
      
      setTimeout(() => {
        copyBtnText.textContent = t.copyBtn;
        copyBtn.classList.remove('bg-emerald-600', 'text-white');
        copyBtn.classList.add('bg-[var(--ink)]');
      }, 2000);
    } else {
      // Fallback
      try {
        await navigator.clipboard.writeText(val);
        copyBtnText.textContent = t.copiedBtn;
        setTimeout(() => copyBtnText.textContent = t.copyBtn, 2000);
      } catch (err) {
        console.error('Failed to copy', err);
      }
    }
  });`;
fs.writeFileSync('replacement.txt', replacement);
console.log("created replacement.txt");
