import { ANU7_UNICODE_TO_NONUNICODE } from './anu7';

export type FontEncoding = 'anu7';

export type ScriptLanguage = 'telugu';

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
    name: 'Anu 7 (Anu Script)',
    family: 'AnuScript7',
    script: 'telugu',
    description: 'Updated Anu Script 7 font layout for Telugu',
    fallbackFontFamily: "'AnuScript7', sans-serif"
  }
];

export function getMapping(encoding: FontEncoding, reverse: boolean = false) {
  const mappingList = ANU7_UNICODE_TO_NONUNICODE;

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

