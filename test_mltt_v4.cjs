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
    
    t = t.replace(/(.)്(.)/g, (match, left, right) => {
        const key = left + '്' + right;
        if (mapping[key]) return mapping[key];
        return match;
    });

    t = t.replace(/(.)(്യ|്വ|്ര)?(ൊ|ോ)/g, (match, cons, vatthu, splitComb) => {
        const leftVal = mapping[splitComb].charAt(0);
        const rightVal = mapping[splitComb].charAt(1);
        
        let cVal = mapping[cons] || cons;
        let vVal = vatthu ? mapping[vatthu] : '';
        
        // Output format: left + vatthu + cons + right 
        // Wait! For ്യ (ya), it's written AFTER the consonant! So cons + vatthu.
        // For ്ര (ra), it's written BEFORE the consonant! 
        // Let's check Karthika map:
        // y=്യ (ya). z=്വ (va). {=്ര (ra).
        // For ya and va, the symbol visually comes AFTER or BELOW.
        // e.g. ക്യ -> ക + ്യ -> Iy. So cVal + vVal.
        // For ra, it comes BEFORE! {I. So vVal + cVal.
        let core = (vatthu === '്ര') ? (vVal + cVal) : (cVal + vVal);
        return leftVal + core + rightVal;
    });

    t = t.replace(/(.)(്യ|്വ|്ര)?(െ|േ|ൈ)/g, (match, cons, vatthu, leftComb) => {
        const leftVal = mapping[leftComb];
        let cVal = mapping[cons] || cons;
        let vVal = vatthu ? mapping[vatthu] : '';
        let core = (vatthu === '്ര') ? (vVal + cVal) : (cVal + vVal);
        return leftVal + core;
    });
    
    t = t.replace(/(.)(്യ|്വ|്ര)/g, (match, cons, vatthu) => {
        let cVal = mapping[cons] || cons;
        let vVal = mapping[vatthu];
        let core = (vatthu === '്ര') ? (vVal + cVal) : (cVal + vVal);
        return core;
    });

    const keys = Object.keys(mapping).sort((a, b) => b.length - a.length);
    for (const key of keys) {
        t = t.split(key).join(mapping[key]);
    }
    
    return t;
}

console.log("ക്യൊ:", convertToMltt("ക്യൊ"));
console.log("ക്യേ:", convertToMltt("ക്യേ"));
console.log("ക്വൊ:", convertToMltt("ക്വൊ"));
console.log("ക്വേ:", convertToMltt("ക്വേ"));
