const fs = require('fs');
let code = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

const regex = /htmlText = \`<span style="font-family: '\\\$\{fontName\}';">\$\{htmlEscaped\}<\/span>\`;/g;
const replacement = 'htmlText = `<span lang="en-US" dir="ltr" style="font-family: \'${fontName}\';">${htmlEscaped}</span>`;';

code = code.replace(regex, replacement);
fs.writeFileSync('src/components/TextConverter.astro', code);
