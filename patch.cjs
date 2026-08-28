const fs = require('fs');
let code = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

const regex = /const fontName = fontStyles\[selectedFontStyle\] \|\| 'AnuPriyanka';/g;

const replacement = `let fontName = fontStyles[selectedFontStyle] || 'AnuPriyanka';
    const currentScript = (document.getElementById('script-select') as HTMLSelectElement)?.value || 'telugu';
    if (currentScript === 'hindi') fontName = 'NeoGaneshBold';
    else if (currentScript === 'tamil') fontName = 'Bamini';
    else if (currentScript === 'kannada') fontName = 'Nudi 01 e';
    else if (currentScript === 'malayalam') fontName = 'ML-TTKarthika';`;

code = code.replace(regex, replacement);

fs.writeFileSync('src/components/TextConverter.astro', code);
