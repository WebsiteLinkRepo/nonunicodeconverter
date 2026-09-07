const fs = require('fs');
const content = fs.readFileSync('src/utils/mappings/anu7.ts', 'utf8');
const lines = content.split('\n');

const res = lines.filter(l => l.includes('\\uF0BF')).map(l => l.trim().substring(0, 50));
console.log("Lines with \\uF0BF:", res.length);
console.log(res.slice(0, 10));

const res2 = lines.filter(l => l.includes('\\uF0A3'));
console.log("Lines with \\uF0A3:", res2.length);
console.log(res2.slice(0, 10));
