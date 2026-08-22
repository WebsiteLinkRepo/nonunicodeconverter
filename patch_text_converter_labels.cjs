const fs = require('fs');

let content = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

// Fix activeFontNameLabel
const activeFontNameLabelReplacement = `
  function activeFontNameLabel(): string {
    const fontVersionSelectEl = document.getElementById('font-version-select') as HTMLSelectElement;
    if (fontVersionSelectEl) {
      if (fontVersionSelectEl.options.length > 0 && fontVersionSelectEl.selectedIndex >= 0) {
        return fontVersionSelectEl.options[fontVersionSelectEl.selectedIndex].text;
      }
    }
    return 'Target Font';
  }
`;

content = content.replace(/function activeFontNameLabel.*?\}[\s\n]*return 'Anu 7\.0';[\s\n]*\}/s, activeFontNameLabelReplacement);

// Fix activeFontLabel.textContent update in fontVersionSelectEl change listener
content = content.replace(/activeFontLabel\.textContent = fontVersionSelectEl\.value === 'anu6' \? 'Anu 6\.0' : 'Anu 7\.0';/, "activeFontLabel.textContent = activeFontNameLabel();");

// Fix outputText placeholder
content = content.replace(/if \(outputText\) outputText\.placeholder = t\.outputPlaceholder;/, `if (outputText) outputText.placeholder = "Converted " + activeFontNameLabel() + " text will appear here automatically...";`);

// Fix activeFontLabel in init
content = content.replace(/activeFontLabel\.textContent = activeFontNameLabel\(effectiveFontStyleInit\);/, "activeFontLabel.textContent = activeFontNameLabel();");

// Fix autoStatus textContent update in processConversion
content = content.replace(/autoStatus\.textContent = \`\$\{scriptNames\[script\]\} Unicode ➔ \$\{activeFontNameLabel\(effectiveFontStyle\)\}\`;/, "autoStatus.textContent = `${scriptNames[script]} Unicode ➔ ${activeFontNameLabel()}`;");

// Write it back
fs.writeFileSync('src/components/TextConverter.astro', content);
console.log("Patched UI labels");
