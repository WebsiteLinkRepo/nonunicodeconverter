import { describe, it, expect } from 'vitest';
import { convertUnicodeToShreeLipiTelugu } from './shreeLipiTeluguConverter';

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

  it('converts base consonants with talakattu correctly', () => {
    expect(convertUnicodeToShreeLipiTelugu('క')).toBe('aæ');
    expect(convertUnicodeToShreeLipiTelugu('ఖ')).toBe('Qæ');
    expect(convertUnicodeToShreeLipiTelugu('గ')).toBe('Væ');
    expect(convertUnicodeToShreeLipiTelugu('చ')).toBe('^æ');
  });

  it('converts guninthalu (vowel combinations) correctly', () => {
    expect(convertUnicodeToShreeLipiTelugu('కా')).toBe('aé');
    expect(convertUnicodeToShreeLipiTelugu('కి')).toBe('aì');
    expect(convertUnicodeToShreeLipiTelugu('కీ')).toBe('aí');
    expect(convertUnicodeToShreeLipiTelugu('కు')).toBe('aî');
    expect(convertUnicodeToShreeLipiTelugu('కూ')).toBe('aï');
    expect(convertUnicodeToShreeLipiTelugu('కె')).toBe('að');
    expect(convertUnicodeToShreeLipiTelugu('కే')).toBe('añ');
    expect(convertUnicodeToShreeLipiTelugu('కై')).toBe('aò');
    expect(convertUnicodeToShreeLipiTelugu('కొ')).toBe('aö');
    expect(convertUnicodeToShreeLipiTelugu('కో')).toBe('aø');
    expect(convertUnicodeToShreeLipiTelugu('కౌ')).toBe('aú');
  });

  it('handles special combinations like తి and తీ', () => {
    expect(convertUnicodeToShreeLipiTelugu('తి')).toBe('†');
    expect(convertUnicodeToShreeLipiTelugu('తీ')).toBe('¡');
    expect(convertUnicodeToShreeLipiTelugu('ది')).toBe('¨');
    expect(convertUnicodeToShreeLipiTelugu('దీ')).toBe('©');
  });

  it('converts conjuncts (vatthulu) correctly', () => {
    expect(convertUnicodeToShreeLipiTelugu('క్క')).toBe('aŒæ');
    expect(convertUnicodeToShreeLipiTelugu('క్ర')).toBe('a–æ');
    expect(convertUnicodeToShreeLipiTelugu('క్ల')).toBe('aÏæ');
    expect(convertUnicodeToShreeLipiTelugu('క్ష్మ')).toBe('„šæ');
  });

  it('converts numbers, anusvara and visarga', () => {
    expect(convertUnicodeToShreeLipiTelugu('౦౧౨౩౪')).toBe('01234');
    expect(convertUnicodeToShreeLipiTelugu('కం')).toBe('aæÆ');
    expect(convertUnicodeToShreeLipiTelugu('కః')).toBe('aæ:');
  });

  it('converts the special ligature శ్రీ', () => {
    expect(convertUnicodeToShreeLipiTelugu('శ్రీ')).toBe('}');
  });
});
