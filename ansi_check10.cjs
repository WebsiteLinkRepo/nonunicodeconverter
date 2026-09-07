const fs = require('fs');
const lines6 = fs.readFileSync('src/utils/mappings/anu6.ts', 'utf8').split('\n');

const res = lines6.filter(l => l.includes('from: "క"'));
console.log("క in Anu 6:", res);
