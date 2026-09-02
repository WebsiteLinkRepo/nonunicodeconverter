import { describe, it, expect } from 'vitest';
import { convertUnicodeToShreeLipiTelugu } from './shreeLipiTeluguConverter';

// Expected values below were verified against public/SHREE-TEL.ttf (Shree-Tel-0908)
// by rendering the converter output next to the Unicode reference glyph and by
// checking glyph metrics (combining marks have advance 40 with negative bounds;
// base forms overhang their advance so the talakattu can overlay them).

describe('Shree-Lipi Telugu Converter', () => {
  it('converts independent vowels correctly', () => {
    expect(convertUnicodeToShreeLipiTelugu('అ')).toBe('A');
    expect(convertUnicodeToShreeLipiTelugu('ఆ')).toBe('B');
    expect(convertUnicodeToShreeLipiTelugu('ఇ')).toBe('C');
    expect(convertUnicodeToShreeLipiTelugu('ఈ')).toBe('D');
    expect(convertUnicodeToShreeLipiTelugu('ఉ')).toBe('E');
    expect(convertUnicodeToShreeLipiTelugu('ఊ')).toBe('F');
    expect(convertUnicodeToShreeLipiTelugu('ఎ')).toBe('G');
    expect(convertUnicodeToShreeLipiTelugu('ఏ')).toBe('H');
    expect(convertUnicodeToShreeLipiTelugu('ఐ')).toBe('I');
    expect(convertUnicodeToShreeLipiTelugu('ఒ')).toBe('J');
    expect(convertUnicodeToShreeLipiTelugu('ఓ')).toBe('K');
    expect(convertUnicodeToShreeLipiTelugu('ఔ')).toBe('L');
  });

  it('builds ఋ / ౠ, which have no single glyph in Shree-Tel-0908', () => {
    // 0x76 / 0x77 are ఠి / ఠీ, NOT ఋ / ౠ — mapping them there rendered ఠి ఠీ.
    // Correct form is బ + two kommus.
    expect(convertUnicodeToShreeLipiTelugu('ఋ')).toBe('º$$');
    expect(convertUnicodeToShreeLipiTelugu('ౠ')).toBe('º$*');
  });

  it('converts base consonants with talakattu correctly', () => {
    expect(convertUnicodeToShreeLipiTelugu('క')).toBe('Mæ');   // 0x4D, not 0x61 (చ)
    expect(convertUnicodeToShreeLipiTelugu('ఖ')).toBe('Q');
    expect(convertUnicodeToShreeLipiTelugu('గ')).toBe('Væ');
    expect(convertUnicodeToShreeLipiTelugu('చ')).toBe('^æ');
    expect(convertUnicodeToShreeLipiTelugu('ఠ')).toBe('uæ');   // ఠ does take a talakattu
    expect(convertUnicodeToShreeLipiTelugu('ఢ')).toBe('Éæ');   // 0xC9, not 0x7C (a combining mark)
    expect(convertUnicodeToShreeLipiTelugu('ర')).toBe('Ææ');   // 0xC6, not 0x2C6
    expect(convertUnicodeToShreeLipiTelugu('ళ')).toBe('âæ');   // 0xE2, not 0xC3
  });

  it('converts guninthalu (vowel combinations) correctly', () => {
    expect(convertUnicodeToShreeLipiTelugu('కా')).toBe('Mé');
    expect(convertUnicodeToShreeLipiTelugu('కి')).toBe('Mì');
    expect(convertUnicodeToShreeLipiTelugu('కీ')).toBe('Mí');
    expect(convertUnicodeToShreeLipiTelugu('కు')).toBe('Mî');
    expect(convertUnicodeToShreeLipiTelugu('కూ')).toBe('Mï');
    expect(convertUnicodeToShreeLipiTelugu('కె')).toBe('Mð');
    expect(convertUnicodeToShreeLipiTelugu('కే')).toBe('Mñ');
    expect(convertUnicodeToShreeLipiTelugu('కై')).toBe('Mò');
    expect(convertUnicodeToShreeLipiTelugu('కొ')).toBe('Mö');
    expect(convertUnicodeToShreeLipiTelugu('కో')).toBe('Mø');
    expect(convertUnicodeToShreeLipiTelugu('కౌ')).toBe('Mú');
  });

  it('handles special combinations like తి and తీ', () => {
    expect(convertUnicodeToShreeLipiTelugu('తి')).toBe('†');
    expect(convertUnicodeToShreeLipiTelugu('తీ')).toBe('¡');
    expect(convertUnicodeToShreeLipiTelugu('ది')).toBe('¨');
    expect(convertUnicodeToShreeLipiTelugu('దీ')).toBe('©');
  });

  it('converts conjuncts (vatthulu) correctly', () => {
    expect(convertUnicodeToShreeLipiTelugu('క్క')).toBe('MŒæ');
    expect(convertUnicodeToShreeLipiTelugu('క్ర')).toBe('M–æ');
    expect(convertUnicodeToShreeLipiTelugu('క్ల')).toBe('MÏæ');
    // క్ష is pre-substituted to 0x201E, so HAS_TALAKATTU must be keyed by that glyph too
    expect(convertUnicodeToShreeLipiTelugu('క్ష')).toBe('„æ');
    expect(convertUnicodeToShreeLipiTelugu('క్ష్మ')).toBe('„šæ');
  });

  it('converts numbers, anusvara and visarga', () => {
    expect(convertUnicodeToShreeLipiTelugu('౦౧౨౩౪')).toBe('01234');
    // 0x2026 is the free-standing sunna; 0x30 is the digit zero and 0xC6 is the ర base
    expect(convertUnicodeToShreeLipiTelugu('కం')).toBe('Mæ…');
    expect(convertUnicodeToShreeLipiTelugu('అం')).toBe('A…');
    // 0x40 is the visarga; 0x3A is the Latin colon
    expect(convertUnicodeToShreeLipiTelugu('కః')).toBe('Mæ@');
    expect(convertUnicodeToShreeLipiTelugu('అః')).toBe('A@');
  });

  it('converts virama (pollu)', () => {
    expect(convertUnicodeToShreeLipiTelugu('క్')).toBe('M¢');
  });

  it('converts the special ligature శ్రీ', () => {
    expect(convertUnicodeToShreeLipiTelugu('శ్రీ')).toBe('}');
  });
});
