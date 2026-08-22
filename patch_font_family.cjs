const fs = require('fs');
let content = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

const fontFamilyReplacement = `
    const anuFontSelect = document.getElementById('anu-font-select') as HTMLSelectElement;
    legacyFontStr = anuFontSelect ? \`'\${anuFontSelect.value}', sans-serif\` : "'AnuPriyanka', sans-serif";
    
    if (formatValue === 'shreelipi') legacyFontStr = "'SHREE-TEL', sans-serif";
    if (formatValue === 'krutidev') legacyFontStr = "'Kruti Dev 010', 'Kruti Dev', 'DevLys 010', sans-serif";
    if (formatValue === 'bamini') legacyFontStr = "'Bamini', sans-serif";
    if (formatValue === 'nudi') legacyFontStr = "'Nudi', sans-serif";
    if (formatValue === 'ism') legacyFontStr = "'ML-TTKarthika', sans-serif";
`;

content = content.replace(/const anuFontSelect = document\.getElementById\('anu-font-select'\) as HTMLSelectElement;[\s\S]*?if \(formatValue === 'shreelipi'\) legacyFontStr = "'SHREE-TEL', sans-serif";/, fontFamilyReplacement);

fs.writeFileSync('src/components/TextConverter.astro', content);
console.log("Patched font family");
