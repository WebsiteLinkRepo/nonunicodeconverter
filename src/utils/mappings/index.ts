import { ANU7_UNICODE_TO_NONUNICODE } from './anu7';
import { ANU6_UNICODE_TO_NONUNICODE } from './anu6';
import { KRUTI_DEV_UNICODE_TO_NONUNICODE } from './krutiDev';
import { BAMINI_TAMIL_UNICODE_TO_NONUNICODE } from './baminiTamil';
import { ANU_TAMIL_UNICODE_TO_NONUNICODE } from './anuTamil';
import { ISM_MALAYALAM_UNICODE_TO_NONUNICODE } from './ismMalayalam';
import { NUDI_KANNADA_UNICODE_TO_NONUNICODE } from './nudiKannada';

import { SHREE_LIPI_UNICODE_TO_NONUNICODE } from './shreeLipi';

export type FontEncoding = 'anu7' | 'anu6' | 'krutidev' | 'bamini' | 'anutamil' | 'ism' | 'nudi' | 'shreelipi';

export type ScriptLanguage = 'telugu' | 'hindi' | 'kannada' | 'tamil' | 'malayalam';

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
    name: 'Anu 7.0 (Telugu)',
    family: 'AnuScript7',
    script: 'telugu',
    description: 'Updated Anu Script 7 font layout for Telugu',
    fallbackFontFamily: "'AnuScript7', sans-serif"
  },
  {
    id: 'anu6',
    name: 'Anu 6.0 (Telugu - Experimental)',
    family: 'AnuScript6',
    script: 'telugu',
    description: 'Anu Script 6 font layout for Telugu (Experimental)',
    fallbackFontFamily: "'AnuScript6', sans-serif"
  },
  {
    id: 'krutidev',
    name: 'Anu 7.0 / Kruti Dev (Hindi)',
    family: 'Mangal',
    script: 'hindi',
    description: 'Legacy font layout for Hindi',
    fallbackFontFamily: "'Mangal', sans-serif"
  },
  {
    id: 'bamini',
    name: 'Anu 7.0 / Bamini (Tamil)',
    family: 'Bamini',
    script: 'tamil',
    description: 'Legacy font layout for Tamil',
    fallbackFontFamily: "'Bamini', sans-serif"
  },
  {
    id: 'anutamil',
    name: 'Anu Script (Tamil)',
    family: 'AnuScript7',
    script: 'tamil',
    description: 'Anu Script font layout for Tamil',
    fallbackFontFamily: "'AnuScript7', sans-serif"
  },
  {
    id: 'ism',
    name: 'Anu 7.0 / ISM (Malayalam)',
    family: 'ML-TTKarthika',
    script: 'malayalam',
    description: 'Legacy font layout for Malayalam',
    fallbackFontFamily: "'ML-TTKarthika', sans-serif"
  },
  {
    id: 'nudi',
    name: 'Anu 7.0 / Nudi (Kannada)',
    family: 'Hemavathi',
    script: 'kannada',
    description: 'Legacy font layout for Kannada',
    fallbackFontFamily: "'Hemavathi', sans-serif"
  },
  {
    id: 'shreelipi',
    name: 'Shree-Lipi (Telugu)',
    family: 'SHREE-TEL',
    script: 'telugu',
    description: 'Legacy font layout for Shree-Lipi Telugu',
    fallbackFontFamily: "'SHREE-TEL', sans-serif"
  }
];

export function getMapping(encoding: FontEncoding, reverse: boolean = false) {
  let mappingList = ANU7_UNICODE_TO_NONUNICODE;
  let script = 'telugu';

  if (encoding === 'anu6') {
    mappingList = ANU6_UNICODE_TO_NONUNICODE;
  } else if (encoding === 'krutidev') {
    mappingList = KRUTI_DEV_UNICODE_TO_NONUNICODE;
    script = 'hindi';
  } else if (encoding === 'bamini') {
    mappingList = BAMINI_TAMIL_UNICODE_TO_NONUNICODE;
    script = 'tamil';
  } else if (encoding === 'anutamil') {
    mappingList = ANU_TAMIL_UNICODE_TO_NONUNICODE;
    script = 'tamil';
  } else if (encoding === 'ism') {
    mappingList = ISM_MALAYALAM_UNICODE_TO_NONUNICODE;
    script = 'malayalam';
  } else if (encoding === 'nudi') {
    mappingList = NUDI_KANNADA_UNICODE_TO_NONUNICODE;
    script = 'kannada';
  } else if (encoding === 'shreelipi') {
    mappingList = SHREE_LIPI_UNICODE_TO_NONUNICODE;
    script = 'telugu';
  }

  const blockOffsets: Record<string, number> = {
    hindi: 0x0300,       // Devanagari (0x0900) -> Telugu (0x0C00)
    tamil: 0x0080,       // Tamil (0x0B80) -> Telugu (0x0C00)
    kannada: -0x0080,    // Kannada (0x0C80) -> Telugu (0x0C00)
    malayalam: -0x0100   // Malayalam (0x0D00) -> Telugu (0x0C00)
  };

  const offset = blockOffsets[script] || 0;
  let processedMapping = mappingList;

  if (offset !== 0) {
    processedMapping = mappingList.map(entry => {
      if (!entry.from) return entry;
      let shiftedFrom = '';
      for (let i = 0; i < entry.from.length; i++) {
        const code = entry.from.charCodeAt(i);
        if (script === 'hindi' && code >= 0x0900 && code <= 0x097F) shiftedFrom += String.fromCharCode(code + offset);
        else if (script === 'tamil' && code >= 0x0B80 && code <= 0x0BFF) shiftedFrom += String.fromCharCode(code + offset);
        else if (script === 'kannada' && code >= 0x0C80 && code <= 0x0CFF) shiftedFrom += String.fromCharCode(code + offset);
        else if (script === 'malayalam' && code >= 0x0D00 && code <= 0x0D7F) shiftedFrom += String.fromCharCode(code + offset);
        else shiftedFrom += entry.from[i];
      }
      return { from: shiftedFrom, to: entry.to };
    });
  }

  if (reverse) {
    const archaic = /[\u0C29\u0C34\u0C0C\u0C61\u0C58\u0C59\u0C5A]/;
    return processedMapping
      .filter(entry => {
        if (!entry.from || !entry.to || entry.to.trim() === '') return false;
        if (script === 'telugu' && archaic.test(entry.from)) return false;
        return true;
      })
      .map(entry => ({ from: entry.to, to: entry.from }))
      .sort((a, b) => b.from.length - a.from.length);
  }

  return [...processedMapping].sort((a, b) => b.from.length - a.from.length);
}
