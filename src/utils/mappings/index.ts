import { ANU7_UNICODE_TO_NONUNICODE } from './anu7';
import { ANU6_UNICODE_TO_NONUNICODE } from './anu6';

export type FontEncoding = 'anu7' | 'anu6';

export type ScriptLanguage = 'telugu' | 'hindi';

export interface FontOption {
  id: FontEncoding;
  name: string;
  family: string;
  script: ScriptLanguage;
  description: string;
  fallbackFontFamily: string;
}

export const AVAILABLE_FONTS: FontOption[] = [
  {
    id: 'anu7',
    name: 'Anu 7.0',
    family: 'AnuScript7',
    script: 'telugu',
    description: 'Updated Anu Script 7 font layout for Telugu',
    fallbackFontFamily: "'AnuScript7', sans-serif"
  },
  {
    id: 'anu6',
    name: 'Anu 6.0 (Experimental)',
    family: 'AnuScript6',
    script: 'telugu',
    description: 'Anu Script 6 font layout for Telugu (Experimental)',
    fallbackFontFamily: "'AnuScript6', sans-serif"
  }
];

export function getMapping(encoding: FontEncoding, reverse: boolean = false) {
  let mappingList = ANU7_UNICODE_TO_NONUNICODE;
  if (encoding === 'anu6') {
    mappingList = ANU6_UNICODE_TO_NONUNICODE;
  }

  if (reverse) {
    // Filter out archaic characters to prevent legacy strings mapping back to rare/incorrect letters (like ఴ, ఩)
    const archaic = /[\u0C29\u0C34\u0C0C\u0C61\u0C58\u0C59\u0C5A]/;
    return mappingList
      .filter(entry => entry.from && entry.to && entry.to.trim() !== '' && !archaic.test(entry.from))
      .map(entry => ({ from: entry.to, to: entry.from }))
      .sort((a, b) => b.from.length - a.from.length);
  }

  return [...mappingList].sort((a, b) => b.from.length - a.from.length);
}
