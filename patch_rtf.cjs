const fs = require('fs');
let code = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

const regex = /e\.clipboardData\.setData\('text\/rtf', rtfText\);/g;
const replacement = `e.clipboardData.setData('text/rtf', rtfText);
          e.clipboardData.setData('application/rtf', rtfText);
          e.clipboardData.setData('text/richtext', rtfText);
          e.clipboardData.setData('application/x-rtf', rtfText);`;

code = code.replace(regex, replacement);
fs.writeFileSync('src/components/TextConverter.astro', code);
