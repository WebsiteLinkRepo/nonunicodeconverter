const fs = require('fs');
const file = '/home/samuelvictor/unicode2nonunicode.com/src/styles/global.css';
let code = fs.readFileSync(file, 'utf8');

if (!code.includes("font-family: 'Priyaanka'")) {
  code = code.replace(/@font-face {\n  font-family: 'AnuPriyanka';/, `@font-face {
  font-family: 'Priyaanka';
  src: url('/AnuSM/ttf/PRIYAANK.TTF?v=2') format('truetype');
  font-weight: normal;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'AnuPriyanka';`);
  fs.writeFileSync(file, code);
  console.log('Fixed css font list');
} else {
  console.log('Already fixed css');
}
