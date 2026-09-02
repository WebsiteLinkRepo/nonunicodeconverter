import { SHREELIPI_TAMIL_UNICODE_TO_NONUNICODE } from './mappings/shreeLipiTamil';

// Pre-build forward lookup
const lookupMap: Record<string, string> = {};
for (const entry of SHREELIPI_TAMIL_UNICODE_TO_NONUNICODE) {
  if (entry.from && entry.to) {
    lookupMap[entry.from] = entry.to;
  }
}
const forwardKeys = Object.keys(lookupMap).sort((a, b) => b.length - a.length);

// Pre-build reverse lookup
const reverseMap: Record<string, string> = {};
for (const entry of SHREELIPI_TAMIL_UNICODE_TO_NONUNICODE) {
  if (entry.to && entry.from) {
    reverseMap[entry.to] = entry.from;
  }
}
const reverseKeys = Object.keys(reverseMap).sort((a, b) => b.length - a.length);

/**
 * Converts Unicode Tamil to Shree-Lipi Tamil (SHREE-TAM7-0803)
 * Uses longest-match greedy substitution based on competitor mapping behavior.
 */
export function unicodeToShreeLipiTamil(text: string): string {
  if (!text) return "";

  let result = '';
  let i = 0;
  while (i < text.length) {
    let matched = false;
    for (const key of forwardKeys) {
      if (text.startsWith(key, i)) {
        result += lookupMap[key];
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

/**
 * Converts Shree-Lipi Tamil (SHREE-TAM7-0803) to Unicode Tamil
 * Uses longest-match greedy substitution to prevent token collisions.
 */
export function shreeLipiTamilToUnicode(text: string): string {
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
