const fs = require('fs');
let code = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

const defaultReplacement = `let fontName = fontStyles[selectedFontStyle] || 'Priyaanka';
    const currentScript = (document.getElementById('script-select') as HTMLSelectElement)?.value || 'telugu';
    const currentFormat = (document.getElementById('font-version-select') as HTMLSelectElement)?.value || 'anu7';
    
    if (currentScript === 'hindi') {
      fontName = currentFormat === 'krutidev' ? 'Kruti Dev 010' : 'Neo Ganesh';
    } else if (currentScript === 'tamil') {
      fontName = currentFormat === 'bamini' ? 'Bamini' : 'Padmini';
    } else if (currentScript === 'kannada') {
      fontName = currentFormat === 'nudi' ? 'Nudi 01 e' : 'Din';
    } else if (currentScript === 'malayalam') {
      fontName = 'ML-TTKarthika';
    }`;
    
code = code.replace(/let fontName = fontStyles\[selectedFontStyle\] \|\| 'Priyaanka';[\s\S]*?else if \(currentScript === 'malayalam'\) fontName = 'ML-TTKarthika';/g, defaultReplacement);

fs.writeFileSync('src/components/TextConverter.astro', code);
