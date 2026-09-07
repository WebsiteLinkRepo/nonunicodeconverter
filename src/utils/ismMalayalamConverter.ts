// ML-TT (ISM Malayalam) Converter
// Auto-generated from karthika.map rules

const mapping: Record<string, string> = {
  "സ്റ്റ": "Ì",
  "ക്ക": "¡",
  "ക്ല": "¢",
  "ക്ഷ": "£",
  "ഗ്ഗ": "¤",
  "ഗ്ല": "¥",
  "ങ്ക": "¦",
  "ങ്ങ": "§",
  "ച്ച": "¨",
  "ഞ്ച": "©",
  "ഞ്ഞ": "ª",
  "ട്ട": "«",
  "ണ്‍": "¬",
  "ണ്ട": "­",
  "ണ്ണ": "®",
  "ത്ത": "¯",
  "ത്ഥ": "°",
  "ദ്ദ": "±",
  "ദ്ധ": "²",
  "ന്‍": "³",
  "ന്ദ": "µ",
  "ന്ന": "¶",
  "ന്മ": "·",
  "പ്ല": "¹",
  "ബ്ബ": "º",
  "ബ്ല": "»",
  "മ്പ": "¼",
  "മ്മ": "½",
  "മ്ല": "Ÿ",
  "യ്യ": "¿",
  "ര്‍": "À",
  "റ്റ": "ä",
  "ല്‍": "Â",
  "ല്ല": "Ã",
  "ള്‍": "Ä",
  "ള്ള": "Å",
  "വ്വ": "Æ",
  "ശ്ല": "Ç",
  "ശ്ശ": "È",
  "സ്ല": "É",
  "സ്സ": "Ê",
  "ഹ്ല": "Ë",
  "ഡ്ഡ": "Í",
  "ക്ട": "Î",
  "ബ്ധ": "Ï",
  "ബ്ദ": "Ð",
  "ച്ഛ": "Ñ",
  "ഹ്മ": "Ò",
  "ഹ്ന": "Ó",
  "ന്ധ": "Ô",
  "ത്സ": "Õ",
  "ജ്ജ": "Ö",
  "ണ്മ": "×",
  "സ്ഥ": "Ø",
  "ന്ഥ": "Ù",
  "ജ്ഞ": "Ú",
  "ത്ഭ": "Û",
  "ഗ്മ": "Ü",
  "ശ്ച": "Ý",
  "ണ്ഡ": "Þ",
  "ത്മ": "ß",
  "ക്ത": "à",
  "ഗ്ന": "á",
  "ന്റ": "â",
  "ഷ്ട": "ã",
  "ന്ത": "´",
  "പ്പ": "¸",
  "്‌": "v",
  "്യ": "y",
  "്വ": "z",
  "്ര": "{",
  "ം": "w",
  "ഃ": "x",
  "അ": "A",
  "ആ": "B",
  "ഇ": "C",
  "ഈ": "Cu",
  "ഉ": "D",
  "ഊ": "Du",
  "ഋ": "E",
  "ഌ": "\\p",
  "എ": "F",
  "ഏ": "G",
  "ഐ": "sF",
  "ഒ": "H",
  "ഓ": "Hm",
  "ഔ": "Hu",
  "ക": "I",
  "ഖ": "J",
  "ഗ": "K",
  "ഘ": "L",
  "ങ": "M",
  "ച": "N",
  "ഛ": "O",
  "ജ": "P",
  "ഝ": "Q",
  "ഞ": "R",
  "ട": "S",
  "ഠ": "T",
  "ഡ": "U",
  "ഢ": "V",
  "ണ": "W",
  "ത": "X",
  "ഥ": "Y",
  "ദ": "Z",
  "ധ": "[",
  "ന": "\\",
  "പ": "]",
  "ഫ": "^",
  "ബ": "_",
  "ഭ": "`",
  "മ": "a",
  "യ": "b",
  "ര": "c",
  "റ": "d",
  "ല": "e",
  "ള": "f",
  "ഴ": "g",
  "വ": "h",
  "ശ": "i",
  "ഷ": "j",
  "സ": "k",
  "ഹ": "l",
  "ാ": "m",
  "ി": "n",
  "ീ": "o",
  "ു": "p",
  "ൂ": "q",
  "ൃ": "r",
  "െ": "s",
  "േ": "t",
  "ൈ": "ss",
  "ൊ": "sm",
  "ോ": "tm",
  "ൌ": "su",
  "ൗ": "u",
  "-": "þ",
  "്": "v",
  "ൺ": "¬",
  "ൻ": "³",
  "ർ": "À",
  "ൽ": "Â",
  "ൾ": "Ä",
};

export function unicodeToIsmMalayalam(mlUnicode: string): string {
    if (!mlUnicode) return "";
    
    // Normalize ZWJ Chillu sequences to atomic Chillus
    let t = mlUnicode
        .replace(/ണ്\u200D/g, "ൺ")
        .replace(/ന്\u200D/g, "ൻ")
        .replace(/ര്\u200D/g, "ർ")
        .replace(/ല്\u200D/g, "ൽ")
        .replace(/ള്\u200D/g, "ൾ")
        .replace(/ക്\u200D/g, "ൿ")
        .replace(/\u200C/g, "")
        .replace(/\u200D/g, "");

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

const ismReverseMap: Record<string, string> = {};
for (const [key, value] of Object.entries(mapping)) {
    if (!value || !key) continue;
    
    // If multiple keys map to the same value (like atomic chillu vs ZWJ chillu),
    // we want the atomic chillu to win.
    if (!ismReverseMap[value]) {
        ismReverseMap[value] = key;
    } else {
        // Atomic chillus are single characters (length 1), ZWJ chillus are length 3
        if (key.length === 1 && ismReverseMap[value].length > 1) {
            ismReverseMap[value] = key;
        }
    }
}
ismReverseMap['v'] = '്'; // override ‌ addition
const ismReverseKeys = Object.keys(ismReverseMap).sort((a, b) => b.length - a.length);

export function ismMalayalamToUnicode(mlText: string): string {
    if (!mlText) return "";

    let t = mlText;

    

    let result = '';
    let i = 0;
    while(i < t.length) {
        let matched = false;
        for (const key of ismReverseKeys) {
            if (t.startsWith(key, i)) {
                result += ismReverseMap[key];
                i += key.length;
                matched = true;
                break;
            }
        }
        if (!matched) {
            result += t[i];
            i++;
        }
    }

    // Post reordering for Malayalam
    // 1. Ra-vatthu comes BEFORE consonant in non-unicode. Swap it back to AFTER consonant
    result = result.replace(/്ര([ക-ഹളഴറ])/g, '$1്ര');
    
    // 2. Pre-base e-matras (െ, േ, ൈ) come before consonant in non-unicode. Swap to AFTER consonant block
    result = result.replace(/([െേൈ])((?:[ക-ഹളഴറ]|ന്റ)(?:്(?:[ക-ഹളഴറ]|ന്റ))*)/g, '$2$1');
    
    // 3. െ + ാ = ൊ, േ + ാ = ോ, െ + ൗ = ൌ
    result = result.replace(/ൊ/g, 'ൊ');
    result = result.replace(/ോ/g, 'ോ');
    result = result.replace(/ൌ/g, 'ൌ');

    return result;
}
