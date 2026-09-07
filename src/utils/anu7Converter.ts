import { ANU7_UNICODE_TO_NONUNICODE } from './mappings/anu7';

const reverseMap: Record<string, string> = {};
const sortedMap = [...ANU7_UNICODE_TO_NONUNICODE].sort((a, b) => b.from.length - a.from.length);

for (const entry of sortedMap) {
  if (entry.to && entry.from && !/[ఴ఩]/.test(entry.from)) {
    if (!reverseMap[entry.to] || entry.from.length > reverseMap[entry.to].length) {
       reverseMap[entry.to] = entry.from;
    }
  }
}

// Manually add the generic vattu mappings from converter.ts
const ANU7_VATTUS: Record<string, string> = {
  "్క": "Ø", // Ø
  "్ఖ": "‰", // ‰
  "్గ": "Z",      // Z
  "్ఘ": "é", // é
  "్ఙ": "_",
  "్చ": "Ì", // Ì
  "్ఛ": "ÌÛ", // ÌÛ
  "్జ": "¨", // ¨
  "్ఝ": "_",
  "్ఞ": "ã", // ã
  "్ట": "¼", // ¼
  "్ఠ": "÷", // ÷
  "్డ": "¦", // ¦
  "్ఢ": "_",
  "్ణ": "’", // ’
  "్త": "ï", // ï
  "్థ": "œ", // œ
  "్द": "Ý", // Wait, mapping indicates this is da
  "్ద": "Ý", // Ý
  "్ధ": "Æ", // Æ
  "్న": "•", // •
  "్ప": "Î", // Î
  "్ఫ": "ÎÛ", // ÎÛ
  "్బ": "Ò", // Ò
  "్భ": "ÒÛ", // ÒÛ
  "్మ": "ˆ", // ˆ
  "్య": "«", // «
  "్ర": "ç", // ç (pre-base ra-vattu)
  "్ల": "¢", // ¢
  "్వ": "Ç", // Ç
  "్శ": "ô", // ô
  "్ష": "ü", // ü
  "్స": "à", // à
  "్హ": "½", // ½
  "్ళ": "ß", // ß
  "్ఱ": "_"
};

for (const [vattu, legacy] of Object.entries(ANU7_VATTUS)) {
    if (!reverseMap[legacy] || vattu.length > reverseMap[legacy].length) {
        reverseMap[legacy] = vattu;
    }
}

const reverseAnu7Keys = Object.keys(reverseMap).sort((a, b) => b.length - a.length);

export function anu7ToUnicode(text: string): string {
  if (!text) return "";

  let result = '';
  // Apply longest-match reverse mapping
  let i = 0;
  while (i < text.length) {
    let matched = false;
    for (const key of reverseAnu7Keys) {
      if (text.startsWith(key, i)) {
        result += reverseMap[key];
        i += key.length;
        matched = true;
        break;
      }
    }
    if (!matched) {
      result += text[i];
      i++;
    }
  }

  // Post-reordering 0: Move Raa Vatthu (్ర) AFTER the consonant it precedes
  // (In forward conversion it is prepended. E.g. ç + T -> T + ç)
  result = result.replace(/(్ర)([క-హౘ-ౚ][ా-ౌ]*(?:్[క-హౘ-ౚ])*)/g, '$2$1');
  
  // Post-reordering 0.5: In Telugu phonetics, Ya Vatthu (్య) is always the final consonant in a cluster. 
  // So if Raa Vatthu was moved after Ya Vatthu, swap them back
  result = result.replace(/(్య)(్ర)/g, '$2$1');

  // Post-reordering 1: Reorder pre-base e-matras (ె, ే, ై, ొ, ో, ౌ) after the consonant
  result = result.replace(
    /([ెేైొోౌ])((?:[క-హౘ-ౚ](?:్[క-హౘ-ౚ])*))/g,
    '$2$1'
  );

  // Post-reordering 2: Reorder vowel signs (ా, ి, ీ, ు, ూ, etc.) after the post-base vattus
  result = result.replace(
    /([క-హౘ-ౚ])([ా-ౌ])((?:్[క-హౘ-ౚ])+)/g,
    '$1$3$2'
  );

  return result;
}
