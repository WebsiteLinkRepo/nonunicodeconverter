const fs = require('fs');
const path = require('path');

const fontsDir = path.join(__dirname, 'public/Fonts folder/AnuSM/ttf');
const fonts = fs.readdirSync(fontsDir).filter(f => f.endsWith('.TTF') || f.endsWith('.ttf'));

let html = `<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
body { font-size: 24px; line-height: 1.5; }
.row { display: flex; align-items: center; border-bottom: 1px solid #ccc; padding: 5px; }
.name { width: 200px; font-family: sans-serif; font-size: 14px; }
.sample { font-size: 32px; }
`;

fonts.forEach((font, i) => {
  html += `@font-face { font-family: 'Font${i}'; src: url('/Fonts folder/AnuSM/ttf/${font}') format('truetype'); }\n`;
});

html += `</style></head><body>`;

fonts.forEach((font, i) => {
  html += `<div class="row">
    <div class="name">${font}</div>
    <div class="sample" style="font-family: 'Font${i}'">abcde ABCDE 12345 !@#$%</div>
  </div>`;
});

html += `</body></html>`;

fs.writeFileSync(path.join(__dirname, 'public/font_samples_all.html'), html);
console.log('Created font_samples_all.html');
