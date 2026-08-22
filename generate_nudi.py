import json

with open('/tmp/KannadaAsciiUnicodeSDK/Kannada.AsciiUnicode/Resources/NudiBarahaMapping.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Reverse the mappings
mapping = {v: k for k, v in data['mapping'].items()}
vattaksharagalu = {v: k for k, v in data['vattaksharagalu'].items()}

# MANUALLY ADD RA VATTHU
vattaksharagalu["ರ"] = "æ"

# Write to TS file
ts_code = """
// Nudi Kannada Converter (Forward Conversion)
// Auto-generated from KannadaAsciiUnicodeSDK rules

const mapping: Record<string, string> = {
"""

for k, v in sorted(mapping.items(), key=lambda x: -len(x[0])):
    ts_code += f'  "{k}": "{v}",\n'

ts_code += """};

const vattaksharagalu: Record<string, string> = {
"""
for k, v in vattaksharagalu.items():
    ts_code += f'  "{k}": "{v}",\n'

ts_code += """};

const dependentVowels = new Set([
  "್", "ಾ", "ಿ", "ೀ", "ು", "ೂ", "ೃ", "ೆ", "ೇ", "ೈ", "ೊ", "ೋ", "ೌ"
]);

export function unicodeToNudi(knUnicode: string): string {
    if (!knUnicode) return "";
    const words = knUnicode.split(" ");
    const outWords = [];
    for (const word of words) {
        outWords.push(processWord(word));
    }
    return outWords.join(" ");
}

function processWord(word: string): string {
    let chars = Array.from(word);
    
    // First pass: reorder Vatthu and Dependent Vowels
    for (let zz = 1; zz < chars.length; zz++) {
        if (chars[zz] === '್') {
            const remaining = chars.length - zz;
            if (remaining <= 1) {
                // Word ending with ್, do nothing
            } else if (remaining === 2) {
                // No dependent vowel after consonant
                const nextChar = chars[zz + 1];
                if (vattaksharagalu[nextChar]) {
                    chars[zz] = vattaksharagalu[nextChar];
                    chars.splice(zz + 1, 1);
                }
            } else {
                const nextChar = chars[zz + 1];
                const dv = chars[zz + 2];
                if (dependentVowels.has(dv) && vattaksharagalu[nextChar]) {
                    chars[zz] = dv;
                    chars[zz + 1] = vattaksharagalu[nextChar];
                    chars.splice(zz + 2, 1);
                } else if (vattaksharagalu[nextChar]) {
                    chars[zz] = vattaksharagalu[nextChar];
                    chars.splice(zz + 1, 1);
                }
            }
        }
    }
    
    // Second pass: Map to ASCII
    let resultText = chars.join("");
    let op = "";
    let i = 0;
    
    while (i < resultText.length) {
        let maxLen = Math.min(4, resultText.length - i);
        let matchFound = false;
        
        for (let j = maxLen; j > 0; j--) {
            const t = resultText.substring(i, i + j);
            if (mapping[t]) {
                op += mapping[t];
                i += j;
                matchFound = true;
                break;
            }
        }
        
        if (!matchFound) {
            op += resultText[i];
            i++;
        }
    }
    
    return op;
}
"""

with open('src/utils/nudiConverter.ts', 'w', encoding='utf-8') as f:
    f.write(ts_code)
