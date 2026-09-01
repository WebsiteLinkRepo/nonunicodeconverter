
import { convertText } from './src/utils/converter';
import * as fs from 'fs';

const tamilText = fs.readFileSync('all_tamil_combinations.txt', 'utf8').split('\n').filter(Boolean);
let passed = 0;
let failed = 0;
const failures = [];

for (const orig of tamilText) {
    const fwd = convertText(orig, 'anutamil', false, false, 'tamil').convertedText;
    const rev = convertText(fwd, 'anutamil', true, false, 'tamil').convertedText;
    if (rev === orig) {
        passed++;
    } else {
        failed++;
        failures.push({ orig, fwd, rev });
    }
}

console.log(`Round-trip: ${passed} passed, ${failed} failed out of ${tamilText.length}`);
if (failures.length > 0) {
    console.log("Failures sample:");
    for (const f of failures.slice(0, 20)) {
        console.log(`  ${f.orig} -> [fwd: ${f.fwd}] -> [rev: ${f.rev}]`);
    }
}
