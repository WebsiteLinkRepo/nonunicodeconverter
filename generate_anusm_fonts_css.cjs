const fs = require('fs');
const path = require('path');

const fontsDir = path.join(__dirname, 'public', 'Fonts folder', 'AnuSM', 'ttf');
const files = fs.readdirSync(fontsDir);

let css = '';
let fontStylesObj = 'const anuFontStyles = {\n';

files.forEach(file => {
  if (file.endsWith('.TTF?v=2') || file.endsWith('.ttf')) {
    const ext = path.extname(file);
    const basename = path.basename(file, ext);
    const fontFamily = 'Anu' + basename.replace(/[^a-zA-Z0-9]/g, '');
    
    css += `@font-face {\n  font-family: '${fontFamily}';\n  src: url('/Fonts folder/AnuSM/ttf/${file}') format('truetype');\n  font-weight: normal;\n  font-style: normal;\n  font-display: swap;\n}\n\n`;
    
    fontStylesObj += `  "${basename}": "${fontFamily}",\n`;
  }
});

fontStylesObj += '};\n';

fs.writeFileSync('generated_anusm_fonts.css', css);
fs.writeFileSync('generated_anusm_fonts_obj.js', fontStylesObj);
console.log('Done!');
