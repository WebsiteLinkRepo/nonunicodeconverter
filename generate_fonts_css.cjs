const fs = require('fs');
const path = require('path');

const fontsDir = path.join(__dirname, 'public', 'Fonts folder', 'Fonts');
const files = fs.readdirSync(fontsDir);

let css = '';
let fontStylesObj = 'const extraFontStyles = {\n';

files.forEach(file => {
  if (file.endsWith('.ttf') || file.endsWith('.otf') || file.endsWith('.woff') || file.endsWith('.woff2')) {
    const ext = path.extname(file);
    const basename = path.basename(file, ext);
    const fontFamily = basename.replace(/[^a-zA-Z0-9]/g, '');
    
    let format = 'truetype';
    if (ext === '.otf') format = 'opentype';
    if (ext === '.woff') format = 'woff';
    if (ext === '.woff2') format = 'woff2';
    
    css += `@font-face {\n  font-family: '${fontFamily}';\n  src: url('/Fonts folder/Fonts/${file}') format('${format}');\n  font-weight: normal;\n  font-style: normal;\n  font-display: swap;\n}\n\n`;
    
    fontStylesObj += `  "${fontFamily}": "${fontFamily}",\n`;
  }
});

fontStylesObj += '};\n';

fs.writeFileSync('generated_fonts.css', css);
fs.writeFileSync('generated_fonts_obj.js', fontStylesObj);
console.log('Done!');
