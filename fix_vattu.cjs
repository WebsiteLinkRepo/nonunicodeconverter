const fs = require('fs');

const path = 'src/utils/converter.ts';
let code = fs.readFileSync(path, 'utf8');

// Find where resultText is about to be split by syllableRegex
const target = "    // Split text into Telugu syllables and non-Telugu characters";
const replacement = `    // Pre-process standalone vattus properly for Anu 7.0 explicitly mapped vattus like ష vattu
    if (encoding === 'anu7' && script === 'telugu') {
      resultText = resultText.replace(/్ష/g, "\\uF08C");
    }
    
    // Split text into Telugu syllables and non-Telugu characters`;

code = code.replace(target, replacement);
fs.writeFileSync(path, code);
console.log("Fixed standalone vattu processor.");
