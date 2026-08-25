const fs = require('fs');
const content = fs.readFileSync('checking ', 'utf8');

const competitorStart = content.indexOf('My competitor ones output:');
const websiteStart = content.indexOf('My website output:');

if (competitorStart === -1 || websiteStart === -1) {
    console.log("Could not find sections");
    process.exit(1);
}

const competitorText = content.substring(competitorStart + 26, websiteStart).trim();
const websiteText = content.substring(websiteStart + 18).trim();

const compLines = competitorText.split('\n').map(l => l.trim());
const webLines = websiteText.split('\n').map(l => l.trim());

console.log("Competitor lines:", compLines.length);
console.log("Website lines:", webLines.length);

let diffs = 0;
for(let i=0; i<Math.min(compLines.length, webLines.length); i++) {
    if (compLines[i] !== webLines[i]) {
        console.log(`Diff at line ${i+1}:`);
        console.log(`  Comp: ${compLines[i]}`);
        console.log(`  Web:  ${webLines[i]}`);
        diffs++;
        if (diffs > 10) {
            console.log("... and more diffs. Stopping.");
            break;
        }
    }
}
if (diffs === 0) {
    console.log("SUCCESS: 0 differences found between competitor and website output!");
}
