const fs = require('fs');
const lines6 = fs.readFileSync('src/utils/mappings/anu6.ts', 'utf8').split('\n');

const res = lines6.filter(l => l.includes('స్క'));
console.log("స్క in Anu 6:", res);
