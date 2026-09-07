import { BAMINI_TAMIL_UNICODE_TO_NONUNICODE } from './mappings/baminiTamil';

export function unicodeToBamini(text: string): string {
    if (!text) return "";
    let result = text;
    
    for (const entry of BAMINI_TAMIL_UNICODE_TO_NONUNICODE) {
        if (entry.from) {
            result = result.split(entry.from).join(entry.to);
        }
    }

    return result;
}

const reverseMap: Record<string, string> = {};
const sortedMap = [...BAMINI_TAMIL_UNICODE_TO_NONUNICODE].sort((a, b) => a.from.length - b.from.length);
for (const entry of sortedMap) {
  if (entry.to && entry.from && !reverseMap[entry.to]) {
     reverseMap[entry.to] = entry.from;
  }
}
const reverseKeys = Object.keys(reverseMap).sort((a, b) => b.length - a.length);

export function baminiToUnicode(text: string): string {
  if (!text) return "";

  let result = '';
  let i = 0;
  while (i < text.length) {
    let matched = false;
    for (const key of reverseKeys) {
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

  return result;
}
