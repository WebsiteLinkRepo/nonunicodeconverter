function charToWin1252(char) {
    const code = char.charCodeAt(0);
    if (code >= 0xF000 && code <= 0xF0FF) {
      return code - 0xF000;
    }
    return code; // simplified
}

function generateRTFOld(text, fontName) {
    let rtf = `{\\rtf1\\ansi\\ansicpg1252\\deff0{\\fonttbl{\\f0\\fnil\\fcharset2 ${fontName};}}\n\\viewkind4\\uc1\\pard\\lang1033\\kerning0\\f0\\fs24 `;
    for (let i = 0; i < text.length; i++) {
        const char = text[i];
        const uniCode = char.charCodeAt(0);
        const winCode = charToWin1252(char);
        if (uniCode > 127 || uniCode < 32) {
            if (uniCode >= 0xF000 && uniCode <= 0xF0FF) {
                const signedUni = uniCode > 32767 ? uniCode - 65536 : uniCode;
                rtf += `\\u${signedUni}\\'${winCode.toString(16).padStart(2, '0')}`;
            } else {
                rtf += `\\` + `'` + winCode.toString(16).padStart(2, '0');
            }
        } else {
            rtf += char;
        }
    }
    rtf += '}';
    return rtf;
}

function generateRTFNew(text, fontName) {
    let rtf = `{\\rtf1\\ansi\\ansicpg1252\\deff0{\\fonttbl{\\f0\\fnil\\fcharset2 ${fontName};}}\n\\viewkind4\\uc1\\pard\\lang1033\\kerning0\\f0\\fs24 `;
    for (let i = 0; i < text.length; i++) {
        const char = text[i];
        const uniCode = char.charCodeAt(0);
        const winCode = charToWin1252(char);
        if (uniCode > 127 || uniCode < 32 || uniCode === 92 || uniCode === 123 || uniCode === 125) {
            // For PageMaker, DO NOT USE \uXXXX. Output strict ANSI hex bytes \'\hh
            rtf += `\\'${winCode.toString(16).padStart(2, '0')}`;
        } else {
            rtf += char;
        }
    }
    rtf += '}';
    return rtf;
}

console.log("OLD:");
console.log(generateRTFOld("", "AnuNEOGANBO")); // N  þ
console.log("NEW:");
console.log(generateRTFNew("", "AnuNEOGANBO"));
