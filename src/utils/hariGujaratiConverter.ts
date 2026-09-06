import { HARI_GUJARATI_MAPPINGS } from './mappings/hariGujarati';

export function unicodeToHari(text: string): string {
  let converted = text;

  // 1. Re-ordering pre-base matra (Short-i / િ)
  // In Gujarati, if we have a consonant (or a consonant cluster) followed by િ,
  // we must move િ to before the cluster, and it maps to '('
  const gujaratiConsonant = '[ક-હળક્ષજ્ઞ]';
  const halant = '્';
  const consonantCluster = `(?:${gujaratiConsonant}${halant})*${gujaratiConsonant}`;
  
  // Move િ before the cluster and replace with '('
  const shortIRegex = new RegExp(`(${consonantCluster})િ`, 'g');
  converted = converted.replace(shortIRegex, '($1');

  // Handle repha: ર્ (r + halant). Need to move it AFTER consonant + matra.
  // E.g. ર્યા -> y + ા + <.
  // The structure is: ર્ + ConsonantCluster + Matra(optional) -> ConsonantCluster + Matra + <
  const matras = '[ાીુૂૃેૈોૌંઃ]?'; 
  const rephaRegex = new RegExp(`ર${halant}(${consonantCluster})(${matras})`, 'g');
  converted = converted.replace(rephaRegex, '$1$2<');
  
  // Standard string replacement via mappings
  for (const mapping of HARI_GUJARATI_MAPPINGS) {
    // Escape regex characters in mapping.from if necessary
    const regex = new RegExp(mapping.from.replace(/([.*+?^=!:${}()|\[\]\/\\])/g, "\\$1"), 'g');
    converted = converted.replace(regex, mapping.to);
  }

  // Cleanup potential artifact from repha/matra combinations
  // In Hari: `<` + `)` (wait, matra is BEFORE `<` now. So `)` + `<` ? No, `<` is repha. 
  // Let's see: earlier we saw 'વિદ્યાર્થી' -> (vwiY„ . 
  // ર્ + થ + ી -> થ + ી + ર્ -> Y + ) + < = Y)<
  // If the font treats `Y„` as "arthi", it means `)<` -> `„`.
  converted = converted.replace(/\)</g, '„');
  
  return converted;
}
