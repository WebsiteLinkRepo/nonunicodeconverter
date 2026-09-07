const fs = require('fs');
const content = fs.readFileSync('src/utils/mappings/anu7.ts', 'utf8');
const lines = content.split('\n');

const res = lines.filter(l => l.includes('\\uF0BF')).map(l => l.trim().substring(0, 50));
console.log(res);
