const fs = require('fs');
const content = fs.readFileSync('src/utils/mappings/neo.ts', 'utf-8');
const lines = content.split('\n');
const keys = lines.filter(l => l.includes('क्ष') || l.includes('प्र'));
console.log(keys);
