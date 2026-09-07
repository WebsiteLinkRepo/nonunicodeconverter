const fs = require('fs');
const lines6 = fs.readFileSync('src/utils/mappings/anu6.ts', 'utf8').split('\n');

const ruMap = lines6.find(l => l.includes('ృ'));
console.log("Anu 6 ృ mapping:", ruMap);

const quoteMap = lines6.find(l => l.includes("'"));
console.log("Anu 6 ' mapping:", quoteMap);

