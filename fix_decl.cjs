const fs = require('fs');

let content = fs.readFileSync('src/components/TextConverter.astro', 'utf8');
content = content.replace(/  const fontVersionSelectEl = document\.getElementById\('font-version-select'\) as HTMLSelectElement;\n  \n  const FONT_OPTIONS:/, "  \n  const FONT_OPTIONS:");

fs.writeFileSync('src/components/TextConverter.astro', content);
