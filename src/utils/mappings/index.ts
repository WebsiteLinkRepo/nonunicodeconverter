import { ANU6_UNICODE_TO_NONUNICODE } from './anu6';
import { ANU7_UNICODE_TO_NONUNICODE } from './anu7';
import { SHREE_LIPI_UNICODE_TO_NONUNICODE } from './shreeLipi';
import { APPLE_TELUGU_UNICODE_TO_NONUNICODE } from './appleTelugu';
import { KRUTI_DEV_UNICODE_TO_NONUNICODE } from './krutiDev';
import { BAMINI_TAMIL_UNICODE_TO_NONUNICODE } from './baminiTamil';
import { ISM_MALAYALAM_UNICODE_TO_NONUNICODE } from './ismMalayalam';

export type FontEncoding = 
  | 'anu6' 
  | 'anu7' 
  | 'shree-lipi' 
  | 'apple-telugu' 
  | 'kruti-dev' 
  | 'bamini-tamil' 
  | 'ism-malayalam';

export type ScriptLanguage = 'telugu' | 'hindi' | 'tamil' | 'malayalam';

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
    id: 'anu6',
    name: 'Anu 6 (Anu Graphic)',
    family: 'AnuScript6',
    script: 'telugu',
    description: 'Standard Anu Graphic 6 font layout for Telugu',
    fallbackFontFamily: "'AnuScript6', 'Anu Graphic', sans-serif"
  },
  {
    id: 'anu7',
    name: 'Anu 7 (Anu Script)',
    family: 'AnuScript7',
    script: 'telugu',
    description: 'Updated Anu Script 7 font layout for Telugu',
    fallbackFontFamily: "'AnuScript7', sans-serif"
  },
  {
    id: 'shree-lipi',
    name: 'Shree-Lipi Telugu',
    family: 'ShreeTel',
    script: 'telugu',
    description: 'Shree-Lipi modular font layout for Telugu',
    fallbackFontFamily: "'ShreeTel', sans-serif"
  },
  {
    id: 'apple-telugu',
    name: 'Apple / Modular Telugu',
    family: 'AppleTelugu',
    script: 'telugu',
    description: 'Apple & Modular Telugu font mapping',
    fallbackFontFamily: "'Apple Telugu', sans-serif"
  },
  {
    id: 'kruti-dev',
    name: 'Kruti Dev 010 (Hindi)',
    family: 'KrutiDev010',
    script: 'hindi',
    description: 'Standard Kruti Dev & Devlys 010 font layout for Hindi / Devnagari',
    fallbackFontFamily: "'Kruti Dev 010', 'Devlys 010', sans-serif"
  },
  {
    id: 'bamini-tamil',
    name: 'Bamini (Tamil)',
    family: 'Bamini',
    script: 'tamil',
    description: 'Standard Bamini legacy font layout for Tamil',
    fallbackFontFamily: "'Bamini', sans-serif"
  },
  {
    id: 'ism-malayalam',
    name: 'ISM Revathi (Malayalam)',
    family: 'Revathi',
    script: 'malayalam',
    description: 'ISM / Revathi font layout for Malayalam',
    fallbackFontFamily: "'Revathi', sans-serif"
  }
];

export function getMapping(encoding: FontEncoding, reverse: boolean = false) {
  let mappingList;
  switch (encoding) {
    case 'anu7':
      mappingList = ANU7_UNICODE_TO_NONUNICODE;
      break;
    case 'shree-lipi':
      mappingList = SHREE_LIPI_UNICODE_TO_NONUNICODE;
      break;
    case 'apple-telugu':
      mappingList = APPLE_TELUGU_UNICODE_TO_NONUNICODE;
      break;
    case 'kruti-dev':
      mappingList = KRUTI_DEV_UNICODE_TO_NONUNICODE;
      break;
    case 'bamini-tamil':
      mappingList = BAMINI_TAMIL_UNICODE_TO_NONUNICODE;
      break;
    case 'ism-malayalam':
      mappingList = ISM_MALAYALAM_UNICODE_TO_NONUNICODE;
      break;
    case 'anu6':
    default:
      mappingList = ANU6_UNICODE_TO_NONUNICODE;
      break;
  }

  if (reverse) {
    return mappingList
      .filter(entry => entry.from && entry.to && entry.to.trim() !== '')
      .map(entry => ({ from: entry.to, to: entry.from }))
      .sort((a, b) => b.from.length - a.from.length);
  }

  return [...mappingList].sort((a, b) => b.from.length - a.from.length);
}
