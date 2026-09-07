const fs = require('fs');
const file = '/home/samuelvictor/unicode2nonunicode.com/src/components/TextConverter.astro';
let code = fs.readFileSync(file, 'utf8');

// The issue is that we hardcoded fontName = 'Priyaanka' but the user wants it to automatically 
// switch to 'Priyanka' (with whatever correct mapped font style is selected if it's dynamic).
// The user noted it wasn't auto switching to priyanka font over the currently selected one on paste.
// If selectedFontStyle !== 'priyanka', but we're forcing telugu default, we should make sure the dropdown
// updates and sets it. Wait, previously it was let fontName = fontStyles[selectedFontStyle] || 'Priyaanka'.

// Wait, the main issue from the user was "it not autmaiclly swithing to priyannka font when i paste fix it"

// In processConversion(), "autoDetectScript" detects the script.
// If hasTelugu -> scriptSelect.value = 'telugu'.
// But we didn't reset fontVersionSelect to 'anu7' or selectedFontStyle to 'priyanka' if they pasted telugu
// in a different setting. Let's fix that in processConversion auto detect logic.

let replaceBlock = `
        if (oldScript !== scriptSelect.value) {
          updateFontDropdown();
          if (activeFontLabel) activeFontLabel.textContent = activeFontNameLabel();
        }
`;

let replaceWith = `
        if (oldScript !== scriptSelect.value) {
          updateFontDropdown();
          
          // Switch to default anu7 format and priyanka style automatically for telugu
          if (scriptSelect.value === 'telugu') {
             const fontVersionSelect = document.getElementById('font-version-select');
             if (fontVersionSelect) fontVersionSelect.value = 'anu7';
             selectedFontStyle = 'priyanka';
          }
          
          if (activeFontLabel) activeFontLabel.textContent = activeFontNameLabel();
        }
`;

code = code.replace(replaceBlock, replaceWith);
fs.writeFileSync(file, code);
console.log('Fixed auto switch for telugu');
