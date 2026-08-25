import { unicodeToAnu6 } from './src/utils/anu6Converter';
import fs from 'fs';

const content = fs.readFileSync('checking ', 'utf8');
const competitorStart = content.indexOf('My competitor ones output:');
const websiteStart = content.indexOf('My website output:');

const inLines = fs.readFileSync('telugu_all_combinations.txt', 'utf8').split('\n');

const webOutLines = [];
for (const line of inLines) {
    if (line.trim().length > 0) {
        webOutLines.push(unicodeToAnu6(line.trim()));
    }
}

const competitorText = content.substring(competitorStart + 26, websiteStart).trim();
const compLines = competitorText.split('\n').map(l => l.trim());

let diffs = 0;
for(let i=0; i<Math.min(compLines.length, webOutLines.length); i++) {
    if (compLines[i] !== webOutLines[i]) {
        console.log(`Diff at line ${i+1}: Input=${inLines[i]}`);
        console.log(`  Comp: ${compLines[i]}`);
        console.log(`  Web:  ${webOutLines[i]}`);
        diffs++;
        if (diffs > 10) {
            console.log("... and more diffs. Stopping.");
            break;
        }
    }
}
if (diffs === 0) {
    console.log("SUCCESS: 0 differences found!");
}

