import { BAMINI_TAMIL_UNICODE_TO_NONUNICODE } from '../src/utils/mappings/baminiTamil';

export function unicodeToBamini(text: string): string {
    let result = text;
    
    // In Bamini, pre-base vowels e, E, ai (ெ, ே, ை) go BEFORE the consonant.
    // O (ொ) becomes e (ெ) + consonant + h (ா)
    // O (ோ) becomes E (ே) + consonant + h (ா)
    // au (ௌ) becomes e (ெ) + consonant + s (ள)

    // First decompose the split matras
    result = result.replace(/([\u0B80-\u0B9F\u0BA3-\u0BB9])ொ/g, "ெ$1ா");
    result = result.replace(/([\u0B80-\u0B9F\u0BA3-\u0BB9])ோ/g, "ே$1ா");
    result = result.replace(/([\u0B80-\u0B9F\u0BA3-\u0BB9])ௌ/g, "ெ$1ள");

    // Then move pre-base matras to the left
    result = result.replace(/([\u0B80-\u0B9F\u0BA3-\u0BB9])([ெேை])/g, "$2$1");

    // Now run through Bamini mapping table
    for (const entry of BAMINI_TAMIL_UNICODE_TO_NONUNICODE) {
        if (entry.from) {
            result = result.split(entry.from).join(entry.to);
        }
    }

    return result;
}

console.log("Tamil test:", unicodeToBamini("தமிழ்")); // Thamizh
