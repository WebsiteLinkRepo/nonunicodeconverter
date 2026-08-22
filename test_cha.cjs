const fs = require('fs');
const code = fs.readFileSync('./src/utils/ismMalayalamConverter.ts', 'utf8');
// extract just the function and mapping for a quick test
