const fs = require('fs');
const content = fs.readFileSync('src/utils/mappings/neo.ts', 'utf-8');
const mapStr = content.split('export const neoMap: { [key: string]: string } = {')[1].split('};')[0];
const neoMap = {};
mapStr.split('\n').forEach(line => {
    const match = line.match(/'([^']+)':\s*'([^']+)'/);
    if (match) {
        let key = match[1].replace(/\\u([0-9a-fA-F]{4})/g, (m, g) => String.fromCharCode(parseInt(g, 16)));
        let val = match[2].replace(/\\u([0-9a-fA-F]{4})/g, (m, g) => String.fromCharCode(parseInt(g, 16)));
        neoMap[key] = val;
    }
});
const mapKeys = Object.keys(neoMap).sort((a, b) => b.length - a.length);

function convert(text) {
    let processedText = text;
    for (const key of mapKeys) {
        if (processedText.includes(key)) {
            const regex = new RegExp(key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g');
            processedText = processedText.replace(regex, neoMap[key]);
        }
    }
    const narrowMatras = '\uF0EC\uF0EE\uF077\uF0E6\uF0E5\uF07D\uF024\uF03A';
    const bridgeRegex = new RegExp(`([\uF04E\uF0A2][${narrowMatras}]*)(?![\uF07E\uF0FE])`, 'g');
    processedText = processedText.replace(bridgeRegex, '$1\uF0FE');
    return processedText;
}

const tests = ['का', 'की', 'को', 'कौ', 'कॉ', 'कर', 'कू', 'ड़', 'ढ़', 'मा', 'मी'];
for (const t of tests) {
    const res = convert(t);
    const hex = [...res].map(c => c.charCodeAt(0).toString(16).toUpperCase()).join(' ');
    console.log(`${t} -> ${hex}`);
}
