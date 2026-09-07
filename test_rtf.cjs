const fs = require('fs');
const file = '/home/samuelvictor/unicode2nonunicode.com/src/styles/global.css';
let code = fs.readFileSync(file, 'utf8');
console.log(code.match(/@font-face {\s*font-family:\s*'Priyaanka'/));
