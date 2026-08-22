import json

map_data = {}
with open('/tmp/unicode-to-mltt-converter/www/public/karthika.map', 'r') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split('=', 1)
        if len(parts) == 2:
            map_data[parts[1]] = parts[0]

ts_code = """// ML-TT (ISM Malayalam) Converter
// Auto-generated from karthika.map rules

const mapping: Record<string, string> = {
"""
for k, v in sorted(map_data.items(), key=lambda x: -len(x[0])):
    k = k.replace('\\', '\\\\').replace('"', '\\"')
    v = v.replace('\\', '\\\\').replace('"', '\\"')
    ts_code += f'  "{k}": "{v}",\n'

ts_code += """};

export function unicodeToIsmMalayalam(mlUnicode: string): string {
    if (!mlUnicode) return "";
    
    // Normalize ZWJ Chillu sequences to atomic Chillus
    let t = mlUnicode
        .replace(/ണ്\\u200D/g, "ൺ")
        .replace(/ന്\\u200D/g, "ൻ")
        .replace(/ര്\\u200D/g, "ർ")
        .replace(/ല്\\u200D/g, "ൽ")
        .replace(/ള്\\u200D/g, "ൾ")
        .replace(/ക്\\u200D/g, "ൿ")
        .replace(/\\u200C/g, "")
        .replace(/\\u200D/g, "");

    // 1. Process conjuncts (consonant + virama + consonant)
    t = t.replace(/(.)്(.)/g, (match, left, right) => {
        const key = left + '്' + right;
        if (mapping[key]) return mapping[key];
        return match;
    });

    // 2. Handle Split Combinators: ൊ, ോ
    t = t.replace(/(.)(്യ|്വ|്ര)?(ൊ|ോ)/g, (match, cons, vatthu, splitComb) => {
        if (!mapping[splitComb]) return match;
        const leftVal = mapping[splitComb].charAt(0);
        const rightVal = mapping[splitComb].charAt(1);
        
        let cVal = mapping[cons] || cons;
        let vVal = vatthu ? mapping[vatthu] : '';
        let core = (vatthu === '്ര') ? (vVal + cVal) : (cVal + vVal);
        return leftVal + core + rightVal;
    });

    // 3. Handle Left Combinators: െ, േ, ൈ
    t = t.replace(/(.)(്യ|്വ|്ര)?(െ|േ|ൈ)/g, (match, cons, vatthu, leftComb) => {
        if (!mapping[leftComb]) return match;
        const leftVal = mapping[leftComb];
        
        let cVal = mapping[cons] || cons;
        let vVal = vatthu ? mapping[vatthu] : '';
        let core = (vatthu === '്ര') ? (vVal + cVal) : (cVal + vVal);
        return leftVal + core;
    });
    
    // 4. Handle independent Vatthus: ്യ, ്വ, ്ര
    t = t.replace(/(.)(്യ|്വ|്ര)/g, (match, cons, vatthu) => {
        if (!mapping[vatthu]) return match;
        let cVal = mapping[cons] || cons;
        let vVal = mapping[vatthu];
        let core = (vatthu === '്ര') ? (vVal + cVal) : (cVal + vVal);
        return core;
    });

    // 5. Remaining mappings
    const keys = Object.keys(mapping).sort((a, b) => b.length - a.length);
    for (const key of keys) {
        t = t.split(key).join(mapping[key]);
    }
    
    return t;
}
"""

with open('src/utils/ismMalayalamConverter.ts', 'w') as f:
    f.write(ts_code)
