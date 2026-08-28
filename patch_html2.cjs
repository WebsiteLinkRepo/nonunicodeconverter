const fs = require('fs');
let code = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

const regex = /htmlText = \`<font face="\$\{fontName\}">\$\{htmlEscaped\}<\/font>\`;/g;
const replacement = 'htmlText = `<span style="font-family: \'${fontName}\';">${htmlEscaped}</span>`;';

code = code.replace(regex, replacement);
fs.writeFileSync('src/components/TextConverter.astro', code);
