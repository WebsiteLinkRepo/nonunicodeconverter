import { ANU6_UNICODE_TO_NONUNICODE } from './mappings/anu6';

// Add specific overrides for Anu 6 that are missing from the 15k list
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ష్ట్ర", to: "R" });
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ష్ట్రా", to: "ã‘ “" }); // based on competitor output
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ౠ", to: "|°¶" }); 
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ఙ్ఙ", to: "VV" }); 
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ఞ్ఞ", to: "&ý" }); 
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ఱ్ఱ", to: "Ž]" }); 
ANU6_UNICODE_TO_NONUNICODE.push({ from: ";", to: "\u00A0" }); // strictly match competitor punctuation handling

// Sort descending by length
const sortedMap = [...ANU6_UNICODE_TO_NONUNICODE].sort((a, b) => b.from.length - a.from.length);

export function unicodeToAnu6(text: string): string {
  let result = text;

  // Iterate the 15,000 mappings
  for (const entry of sortedMap) {
      if (result.includes(entry.from)) {
          result = result.split(entry.from).join(entry.to);
      }
  }

  return result;
}
