const fs = require('fs');
let code = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

const regex = /htmlText = \`<font face="\$\{fontName\}"><span style="font-family: '\$\{fontName\}', sans-serif;">\$\{htmlEscaped\}\`;/g;
const replacement = 'htmlText = `<font face="${fontName}">${htmlEscaped}</font>`;';

code = code.replace(regex, replacement);
fs.writeFileSync('src/components/TextConverter.astro', code);
