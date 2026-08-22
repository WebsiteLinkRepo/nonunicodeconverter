const convert = require('./test_mltt_algo.cjs');
const fs = require('fs');

const mapData = fs.readFileSync('/tmp/unicode-to-mltt-converter/www/public/karthika.map', 'utf-8');
const mapping = {};
for (const line of mapData.split('\n')) {
    const t = line.trim();
    if (!t || t.startsWith('#')) continue;
    const p = t.split('=');
    if (p.length === 2) {
        mapping[p[1]] = p[0];
    }
}

function convertToMltt(text) {
    let t = text;
    
    // Process char + ് + char
    // We can do this with a regex: /(.)്(.)/g
    t = t.replace(/(.)്(.)/g, (match, left, right) => {
        const key = left + '്' + right;
        if (mapping[key]) {
            return mapping[key];
        }
        return match;
    });
    
    // Left combinators: െ, േ, ൈ, ്ര
    const leftCombinators = ["െ", "േ", "ൈ", "്ര"];
    for (const key of leftCombinators) {
        if (mapping[key]) {
            const value = mapping[key];
            // Regex to find: (.)(key)
            const regex = new RegExp(`(.)(${key})`, 'g');
            t = t.replace(regex, (match, rightChar) => {
                const rightVal = mapping[rightChar] || rightChar;
                return value + rightVal;
            });
        }
    }
    
    // Split combinators: ൊ, ോ
    const splitCombinators = ["ൊ", "ോ"];
    for (const key of splitCombinators) {
        if (mapping[key]) {
            const value = mapping[key];
            const leftVal = value.charAt(0);
            const rightVal = value.charAt(1);
            
            const regex = new RegExp(`(.)(${key})`, 'g');
            t = t.replace(regex, (match, middleChar) => {
                const midVal = mapping[middleChar] || middleChar;
                return leftVal + midVal + rightVal;
            });
        }
    }
    
    // Remaining mappings
    const keys = Object.keys(mapping).sort((a, b) => b.length - a.length);
    for (const key of keys) {
        t = t.split(key).join(mapping[key]);
    }
    
    return t;
}

console.log(convertToMltt("മലയാളം"));
console.log(convertToMltt("ക്കൊ"));
console.log("ക്രൊ:", convertToMltt("ക്രൊ"));
console.log("ക്രേ:", convertToMltt("ക്രേ"));
