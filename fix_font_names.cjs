const fs = require('fs');
let code = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

const fontStylesReplacement = `const fontStyles: Record<string, string> = {
    priyanka: 'Priyaanka',
    anupama: 'Anupama',
    subhalekha: 'Subhalekha',
    bapu: 'Bapu',
    ramana: 'Ramana',
    gowthami: 'Gowthami'
  };`;
code = code.replace(/const fontStyles: Record<string, string> = {[\s\S]*?};/, fontStylesReplacement);

const defaultReplacement = `let fontName = fontStyles[selectedFontStyle] || 'Priyaanka';
    const currentScript = (document.getElementById('script-select') as HTMLSelectElement)?.value || 'telugu';
    if (currentScript === 'hindi') fontName = 'Neo Ganesh'; // Often named "Neo Ganesh" or "NeoGanesh"
    else if (currentScript === 'tamil') fontName = 'Bamini';
    else if (currentScript === 'kannada') fontName = 'Nudi 01 e';
    else if (currentScript === 'malayalam') fontName = 'ML-TTKarthika';`;
    
code = code.replace(/let fontName = fontStyles\[selectedFontStyle\] \|\| 'AnuPriyanka';[\s\S]*?else if \(currentScript === 'malayalam'\) fontName = 'ML-TTKarthika';/g, defaultReplacement);

fs.writeFileSync('src/components/TextConverter.astro', code);
