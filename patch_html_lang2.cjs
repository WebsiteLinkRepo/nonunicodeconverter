const fs = require('fs');
let code = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

code = code.replace('htmlText = `<span style="font-family: \\\'${fontName}\\\';">${htmlEscaped}</span>`;', 'htmlText = `<span lang="en-US" dir="ltr" style="font-family: \\\'${fontName}\\\';">${htmlEscaped}</span>`;');

fs.writeFileSync('src/components/TextConverter.astro', code);
