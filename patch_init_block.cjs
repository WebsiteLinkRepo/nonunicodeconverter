const fs = require('fs');

let content = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

content = content.replace(
  "const initScriptIsHindi = scriptSelect ? scriptSelect.value === 'hindi' : false;",
  "const initScriptIsHindi = typeof scriptSelectEl !== 'undefined' && scriptSelectEl ? scriptSelectEl.value === 'hindi' : false;"
);

// I noticed the font rendering block in processConversion is still broken for legacyFontStr.
// Let's completely rewrite the font family application block to properly read fontVersionSelect.value

const fontApplyBlock = `
      // Apply correct font style preview
      // Only apply legacy fonts if there is actual text, otherwise let it fall back to sans-serif so the placeholder is legible
      let legacyFontToApply = 'sans-serif';
      if (encoding === 'krutidev') legacyFontToApply = "'Kruti Dev 010', 'Kruti Dev', 'DevLys 010', sans-serif";
      else if (encoding === 'bamini') legacyFontToApply = "'Bamini', sans-serif";
      else if (encoding === 'nudi') legacyFontToApply = "'Nudi', sans-serif";
      else if (encoding === 'ism') legacyFontToApply = "'ML-TTKarthika', sans-serif";
      else if (encoding === 'shreelipi') legacyFontToApply = "'SHREE-TEL', sans-serif";
      else legacyFontToApply = fontStyles[effectiveFontStyle] || 'AnuPriyanka';

      if (reverse) {
        inputText.style.fontFamily = (inputText.value) ? legacyFontToApply : 'sans-serif';
        outputText.style.fontFamily = 'sans-serif';
      } else {
        inputText.style.fontFamily = 'sans-serif';
        outputText.style.fontFamily = (outputText.value) ? legacyFontToApply : 'sans-serif';
      }
`;

content = content.replace(/\/\/ Apply correct font style preview[\s\S]*?\} else \{[\s\S]*?\}\n/, fontApplyBlock + "\n");

// And let's fix the initial font rendering block
const initFontApplyBlock = `
  let initLegacyFontToApply = 'sans-serif';
  const initEncoding = fontVersionSelectEl ? fontVersionSelectEl.value : 'anu7';
  if (initEncoding === 'krutidev') initLegacyFontToApply = "'Kruti Dev 010', 'Kruti Dev', 'DevLys 010', sans-serif";
  else if (initEncoding === 'bamini') initLegacyFontToApply = "'Bamini', sans-serif";
  else if (initEncoding === 'nudi') initLegacyFontToApply = "'Nudi', sans-serif";
  else if (initEncoding === 'ism') initLegacyFontToApply = "'ML-TTKarthika', sans-serif";
  else if (initEncoding === 'shreelipi') initLegacyFontToApply = "'SHREE-TEL', sans-serif";
  else initLegacyFontToApply = fontStyles[effectiveFontStyleInit] || 'AnuPriyanka';

  inputText.style.fontFamily = (inputText.value) ? initLegacyFontToApply : 'sans-serif';
  outputText.style.fontFamily = (outputText.value) ? initLegacyFontToApply : 'sans-serif';
`;

content = content.replace(/inputText\.style\.fontFamily = \(inputText\.value && !initScriptIsHindi\) \? \(fontStyles\[effectiveFontStyleInit\] \|\| 'AnuPriyanka'\) : 'sans-serif';\n  outputText\.style\.fontFamily = \(outputText\.value && !initScriptIsHindi\) \? \(fontStyles\[effectiveFontStyleInit\] \|\| 'AnuPriyanka'\) : 'sans-serif';/, initFontApplyBlock);


fs.writeFileSync('src/components/TextConverter.astro', content);
console.log("Patched errors and font rendering");
