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

ts_code = """// ML-TT Karthika (Malayalam) Converter
// Auto-generated from karthika.map

const mapping: Record<string, string> = {
"""
# Sort by length descending to match longest sequences first
for k, v in sorted(map_data.items(), key=lambda x: -len(x[0])):
    k = k.replace('\\', '\\\\').replace('"', '\\"')
    v = v.replace('\\', '\\\\').replace('"', '\\"')
    ts_code += f'  "{k}": "{v}",\n'

ts_code += """};

const leftCombinators = ["െ", "േ", "ൈ", "്ര"];
const splitCombinators = ["ൊ", "ോ"];

export function unicodeToIsmMalayalam(mlUnicode: string): string {
    if (!mlUnicode) return "";
    
    let text = mlUnicode;
    
    // First pass: Pre-process chillu and special cases
    // (If needed, handled by longest match in mapping later, 
    //  but we need to handle split combinators first)
    
    // Process Split Combinators (ൊ, ോ)
    for (const key of splitCombinators) {
        if (mapping[key]) {
            const value = mapping[key]; // e.g. "sm"
            const leftPart = value.charAt(0);
            const rightPart = value.charAt(1);
            
            // We need to find `consonant + ൊ`
            // But wait, the consonant could be a conjunct like `ക്ക` (ka + virama + ka)
            // So we can't just use a simple replace without knowing the consonant boundaries.
            // Actually, we can just find the index of `key` and move the left part before the consonant cluster!
        }
    }
    
    return text;
}
"""

with open('src/utils/ismMalayalamConverter.ts', 'w') as f:
    f.write(ts_code)
