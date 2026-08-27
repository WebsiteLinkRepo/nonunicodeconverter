function generateRTF(text: string, fontName: string): string {
    let rtf = `{\\rtf1\\ansi\\ansicpg1252\\deff0{\\fonttbl{\\f0\\fcharset0 ${fontName};}}\n\\f0\\fs24 `;
    for (let i = 0; i < text.length; i++) {
        let code = text.charCodeAt(i);
        if (code <= 127) {
            if (text[i] === '\\' || text[i] === '{' || text[i] === '}') {
                rtf += '\\' + text[i];
            } else if (text[i] === '\n') {
                rtf += '\\par\n';
            } else {
                rtf += text[i];
            }
        } else if (code >= 128 && code <= 255) {
            rtf += `\\'${code.toString(16).padStart(2, '0')}`;
        } else {
            rtf += `\\u${code}?`;
        }
    }
    rtf += `}`;
    return rtf;
}
console.log(generateRTF("hello \x8A\x9F world", "Priyaanka"));
