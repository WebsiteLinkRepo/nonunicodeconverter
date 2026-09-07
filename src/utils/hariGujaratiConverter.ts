import { HARI_GUJARATI_MAPPINGS } from './mappings/hariGujarati';

const gujaratiConsonant = '[ક-હળક્ષજ્ઞ]';
const halant = '્';
const consonantCluster = `(?:${gujaratiConsonant}${halant})*${gujaratiConsonant}`;
const matras = '[ાીુૂૃેૈોૌંઃ]?';

export function unicodeToHari(text: string): string {
  let converted = text;

  // 1. Re-ordering pre-base matra (Short-i / િ)
  // Move િ before the cluster and replace with '('
  const shortIRegex = new RegExp(`(${consonantCluster})િ`, 'g');
  converted = converted.replace(shortIRegex, '($1');

  // Handle repha: ર્ (r + halant). Need to move it AFTER consonant + matra.
  const rephaRegex = new RegExp(`ર${halant}(${consonantCluster})(${matras})`, 'g');
  converted = converted.replace(rephaRegex, '$1$2<');
  
  // Create sorted mapping (longest match first)
  const sortedMap = [...HARI_GUJARATI_MAPPINGS].sort((a,b) => b.from.length - a.from.length);
  
  // Standard string replacement via mappings
  for (const mapping of sortedMap) {
    if (!mapping.to) continue;
    const regex = new RegExp(mapping.from.replace(/([.*+?^=!:${}()|\[\]\/\\])/g, "\\$1"), 'g');
    converted = converted.replace(regex, mapping.to);
  }

  // specific combination cleanup
  converted = converted.replace(/\)</g, '„');

  return converted;
}

const reverseMap: Record<string, string> = {};
const reverseSortedMap = [...HARI_GUJARATI_MAPPINGS].sort((a,b) => a.from.length - b.from.length);
for (const entry of reverseSortedMap) {
    if (entry.to && entry.from) {
        if (!reverseMap[entry.to] || entry.from.length > reverseMap[entry.to].length) {
            reverseMap[entry.to] = entry.from;
        }
    }
}
const reverseKeys = Object.keys(reverseMap).sort((a,b) => b.length - a.length);

export function hariToUnicode(text: string): string {
    if (!text) return "";

    let processedText = text;

    // clean up specific combination mapping first - „ is ) + <
    processedText = processedText.replace(/„/g, ')<');

    let result = '';
    let i = 0;
    while(i < processedText.length) {
        let matched = false;
        for (const key of reverseKeys) {
            if (processedText.startsWith(key, i)) {
                result += reverseMap[key];
                i += key.length;
                matched = true;
                break;
            }
        }
        if (!matched) {
            result += processedText[i];
            i++;
        }
    }

    // Now undo the positional swaps
    
    // 1. Repha: `ConsonantCluster + Matra + <` -> `ર્ + ConsonantCluster + Matra`
    const rephaReverseRegex = new RegExp(`(${consonantCluster})(${matras})<`, 'g');
    result = result.replace(rephaReverseRegex, `ર${halant}$1$2`); 

    // 2. Short I: `( + ConsonantCluster` -> `ConsonantCluster + િ`
    const shortIReverseRegex = new RegExp(`\\((${consonantCluster})`, 'g');
    result = result.replace(shortIReverseRegex, '$1િ');

    return result;
}
