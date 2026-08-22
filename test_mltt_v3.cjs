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
    
    // First, map explicit 3-char conjuncts (left + ് + right)
    t = t.replace(/(.)്(.)/g, (match, left, right) => {
        const key = left + '്' + right;
        if (mapping[key]) return mapping[key];
        return match;
    });

    // Handle Split Combinators: ൊ, ോ
    // They wrap the preceding consonant cluster.
    // However, if the preceding is `്ര`, we must include the consonant before it!
    // Example: ക്രൊ (ക + ്ര + ൊ). 
    t = t.replace(/(.)(്ര)?(ൊ|ോ)/g, (match, cons, raVatthu, splitComb) => {
        const leftVal = mapping[splitComb].charAt(0);
        const rightVal = mapping[splitComb].charAt(1);
        
        let cVal = mapping[cons] || cons;
        let raVal = raVatthu ? mapping['്ര'] : '';
        
        // Output format: left + ra + cons + right 
        // Wait, for ക്കൊ, raVatthu is undefined, so left + cons + right -> s + ¡ + m
        // For ക്രൊ, raVatthu is ്ര ({), cons is ക (I). left is െ (s). right is ാ (m)
        // Visually: െ്രകാ -> s { I m.
        return leftVal + raVal + cVal + rightVal;
    });

    // Handle Left Combinators: െ, േ, ൈ
    // Same logic: they go before the consonant (or before raVatthu + cons)
    t = t.replace(/(.)(്ര)?(െ|േ|ൈ)/g, (match, cons, raVatthu, leftComb) => {
        const leftVal = mapping[leftComb];
        let cVal = mapping[cons] || cons;
        let raVal = raVatthu ? mapping['്ര'] : '';
        return leftVal + raVal + cVal;
    });
    
    // Handle Vatthus: ്യ, ്വ, ്ര
    // Wait, ്ര is already handled if it had a vowel. What if it doesn't? e.g. ക്ര (ക + ്ര)
    // ്ര -> { + ക -> {I
    t = t.replace(/(.)(്യ|്വ|്ര)/g, (match, cons, vatthu) => {
        let vVal = mapping[vatthu];
        let cVal = mapping[cons] || cons;
        return vVal + cVal;
    });

    // Remaining mappings
    const keys = Object.keys(mapping).sort((a, b) => b.length - a.length);
    for (const key of keys) {
        t = t.split(key).join(mapping[key]);
    }
    
    return t;
}

console.log("മലയാളം:", convertToMltt("മലയാളം"));
console.log("ക്കൊ:", convertToMltt("ക്കൊ"));
console.log("ക്രൊ:", convertToMltt("ക്രൊ"));
console.log("ക്രേ:", convertToMltt("ക്രേ"));
console.log("ക്രാ:", convertToMltt("ക്രാ"));
