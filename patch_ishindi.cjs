const fs = require('fs');
let content = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

// Add const isHindi = script === 'hindi'; right after const isTelugu = script === 'telugu';
content = content.replace(/const isTelugu = script === 'telugu';/, "const isTelugu = script === 'telugu';\n    const isHindi = script === 'hindi';");

fs.writeFileSync('src/components/TextConverter.astro', content);
console.log("Patched isHindi");
