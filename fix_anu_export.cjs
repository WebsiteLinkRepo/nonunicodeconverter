const fs = require('fs');
let indexTs = fs.readFileSync('src/utils/mappings/index.ts', 'utf8');
if (indexTs.includes('ANU6_UNICODE_TO_NONUNICODE')) {
    console.log("Export is correct.");
}
