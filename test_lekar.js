import { readFileSync } from 'fs';

const neoContent = readFileSync('src/utils/mappings/neo.ts', 'utf-8');
const mapStr = neoContent.split('export const neoMap: { [key: string]: string } = {')[1].split('};')[0];
const neoMap = {};
mapStr.split('\n').forEach(line => {
    const match = line.match(/'([^']+)':\s*'([^']+)'/);
    if (match) {
        let key = match[1];
        let val = match[2].replace(/\\u([0-9a-fA-F]{4})/g, (m, g) => String.fromCharCode(parseInt(g, 16)));
        key = key.replace(/\\u([0-9a-fA-F]{4})/g, (m, g) => String.fromCharCode(parseInt(g, 16)));
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
    const bridgeRegex = new RegExp(`([\uF04E\uF0A2][${narrowMatras}]*)(?![\uF0E7\uF079\uF07E\uF0FE])`, 'g');
    processedText = processedText.replace(bridgeRegex, '$1\uF0FE');
    return processedText;
}

const res = convert('लेकर');
let hex = '';
for(let i=0; i<res.length; i++) {
    hex += res.charCodeAt(i).toString(16).toUpperCase() + ' ';
}
console.log("lekar output hex:", hex.trim());
console.log("expected: F0C2 F07A F04E F0FE F0BA");
