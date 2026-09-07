import { ANU6_UNICODE_TO_NONUNICODE } from './mappings/anu6';

// Add specific overrides for Anu 6 that are missing from the 15k list
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ష్ట్ర", to: "R" });
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ష్ట్రా", to: "ã‘ “" }); // based on competitor output
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ౠ", to: "|°¶" });
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ృ", to: "$" });
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ౄ", to: "$ì" }); 
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ఙ్ఙ", to: "VV" }); 
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ఞ్ఞ", to: "&ý" }); 
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ఱ్ఱ", to: "Ž]" }); 
ANU6_UNICODE_TO_NONUNICODE.push({ from: ";", to: "\u00A0" }); // strictly match competitor punctuation handling

// Sort descending by length
const sortedMap = [...ANU6_UNICODE_TO_NONUNICODE].sort((a, b) => b.from.length - a.from.length);

const reverseMap: Record<string, string> = {};
for (const entry of sortedMap) {
  if (entry.to && entry.from && !/[ఴ఩]/.test(entry.from)) {
    if (!reverseMap[entry.to]) {
       reverseMap[entry.to] = entry.from;
    }
  }
}
const reverseAnu6Keys = Object.keys(reverseMap).sort((a, b) => b.length - a.length);

export function unicodeToAnu6(text: string, useAltRaaVatthu: boolean = false): string {
  let result = text;

  // Handle straight single quotes (open vs closed)
  result = result.replace(/(\S)'/g, "$1Ñ");

  // Iterate the 15,000 mappings
  for (const entry of sortedMap) {
      if (result.includes(entry.from)) {
          let target = entry.to;
          if (useAltRaaVatthu && entry.from.includes("్ర") && target.startsWith("")) {
              target = target.substring(1) + "";
          }
          result = result.split(entry.from).join(target);
      }
  }

  return result;
}

export function anu6ToUnicode(text: string): string {
  if (!text) return "";

  // Support alternate Raa Vatthu by moving post-base  (\uF0E3) to pre-base before reverse conversion
  let processText = text.replace(/([\uF000-\uF0FF]+)(\uF0E3)/g, '$2$1');

  // Reverse specific character quirks added during forward conversion map modifications
  processText = processText.replace(/Ñ/g, "'");

  let result = '';
  // Apply longest-match reverse mapping
  let i = 0;
  while (i < processText.length) {
    let matched = false;
    for (const key of reverseAnu6Keys) {
      if (processText.startsWith(key, i)) {
        result += reverseMap[key];
        i += key.length;
        matched = true;
        break;
      }
    }
    if (!matched) {
      result += processText[i];
      i++;
    }
  }

  return result;
}
