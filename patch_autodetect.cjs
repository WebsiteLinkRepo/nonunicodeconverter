const fs = require('fs');

let content = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

const autoDetectReplacement = `
      if (scriptSelect) {
        const oldVal = scriptSelect.value;
        if (hasHindi && !hasTelugu && !hasKannada && !hasTamil && !hasMalayalam) scriptSelect.value = 'hindi';
        else if (hasTamil && !hasTelugu && !hasKannada && !hasHindi && !hasMalayalam) scriptSelect.value = 'tamil';
        else if (hasKannada && !hasTelugu && !hasHindi && !hasTamil && !hasMalayalam) scriptSelect.value = 'kannada';
        else if (hasMalayalam && !hasTelugu && !hasHindi && !hasTamil && !hasKannada) scriptSelect.value = 'malayalam';
        else if (hasTelugu) scriptSelect.value = 'telugu';
        
        if (oldVal !== scriptSelect.value) {
            updateFontDropdown(); // Call this immediately so the dropdown matches
        }
      }
`;

content = content.replace(/if \(scriptSelect\) \{[\s\S]*?else if \(hasTelugu\) scriptSelect\.value = 'telugu';\s*\}/, autoDetectReplacement);

fs.writeFileSync('src/components/TextConverter.astro', content);
console.log("Patched autodetect");
