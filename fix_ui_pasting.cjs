const fs = require('fs');
const file = '/home/samuelvictor/unicode2nonunicode.com/src/components/TextConverter.astro';
let code = fs.readFileSync(file, 'utf8');

// 1. Fix the fontStyles mapping to include both webfont and local fonts
code = code.replace(/priyanka: 'Priyaanka',/g, "priyanka: 'AnuPriyanka, Priyaanka',");

// 2. Fix legacyFontToApply fallback
code = code.replace(/legacyFontToApply = fontStyles\[effectiveFontStyle\] \|\| 'Priyaanka';/g, "legacyFontToApply = fontStyles[effectiveFontStyle] || 'AnuPriyanka, Priyaanka';");
code = code.replace(/initLegacyFontToApply = fontStyles\[effectiveFontStyleInit\] \|\| 'Priyaanka';/g, "initLegacyFontToApply = fontStyles[effectiveFontStyleInit] || 'AnuPriyanka, Priyaanka';");

// 3. Update the font override in clipboard copy
code = code.replace(/let fontName = fontStyles\[selectedFontStyle\] \|\| 'Priyaanka';/g, "let fontName = 'Priyaanka'; // Ensure Word sees the original font name");

// 4. Fix dropdown label update in processConversion
const oldDropdownUpdate = `        if (oldScript !== scriptSelect.value) {
          updateFontDropdown();
        }`;
const newDropdownUpdate = `        if (oldScript !== scriptSelect.value) {
          updateFontDropdown();
          if (activeFontLabel) activeFontLabel.textContent = activeFontNameLabel();
        }`;
code = code.replace(oldDropdownUpdate, newDropdownUpdate);

fs.writeFileSync(file, code);
console.log('Fixed TextConverter');
