const fs = require('fs');
const lines6 = fs.readFileSync('src/utils/mappings/anu6.ts', 'utf8').split('\n');

const koMap = lines6.find(l => l.includes('from: "కో"'));
console.log("కో:", koMap);

const tMap = lines6.find(l => l.includes('from: "ట్"'));
console.log("ట్:", tMap);
