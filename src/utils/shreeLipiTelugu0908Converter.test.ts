import { describe, expect, it } from 'vitest';
import {
  convertShreeLipiTelugu0908ToUnicode,
  convertUnicodeToShreeLipiTelugu0908,
} from './shreeLipiTelugu0908Converter';

const F = (s: string) => convertUnicodeToShreeLipiTelugu0908(s).text;
const R = (s: string) => convertShreeLipiTelugu0908ToUnicode(s).text;

// The tables are generated from measurements (see scratch/telugu0908/INVENTORY.md), so these
// tests deliberately do NOT restate them value by value - that would only assert that the
// generator ran. They pin the things a regression would break: the anchors the project owner
// verified against a real rendering, the cluster grammar, and round-tripping.

describe('Shree-Tel-0908: anchors confirmed against a real rendering', () => {
  // Reference output supplied by the project owner for the vowel row plus అం / అః.
  it('spells the independent vowels A-L', () => {
    expect(F('అఆఇఈఉఊ')).toBe('ABCDEF');
    expect(F('ఎఏఐఒఓఔ')).toBe('GHIJKL');
  });

  it('builds ఋ / ౠ from బ plus kommus, which the font has no glyph for', () => {
    expect(F('ఋ')).toBe('º$$');
    expect(F('ౠ')).toBe('º$*');
  });

  it('places the sunna and the visarga after the letter', () => {
    expect(F('అం')).toBe('A…');
    expect(F('అః')).toBe('A@');
  });
});

describe('Shree-Tel-0908: cluster grammar', () => {
  it('emits a talakattu only for letters that take one', () => {
    expect(F('క')).toBe('Mæ');   // క takes the centred hook
    expect(F('ఖ')).toBe('Q');         // ఖ carries its own top
    expect(F('బ')).toBe('º');
    expect(F('న')).toBe('¯è'); // న takes the left-shifted hook
  });

  it('drops the talakattu when a vowel sign above the letter replaces it', () => {
    const ka = F('క');
    expect(F('కా').startsWith('M')).toBe(true);
    expect(F('కా')).not.toContain(ka);   // the hook is gone
  });

  it('keeps the whole letter when the vowel sign hangs below it', () => {
    // ు does not touch the top, so the talakattu stays. Which signs behave this way is
    // recorded per consonant by the search, not assumed here.
    expect(F('కు').length).toBeGreaterThan(F('క').length - 1);
  });

  it('writes a subscript for each consonant after a virama', () => {
    // క keeps its talakattu, then an advance-only glyph (ü, 179 units) so the subscript
    // lands under the letter instead of beside it.
    expect(F('క్క')).toBe('MæüO');
    expect(F('క్ష')).toBe('„æ');
    expect(F('శ్రీ')).toBe('}');
  });

  it('stacks two subscripts in source order', () => {
    const out = F('క్ష్మ');
    expect(out.startsWith('„')).toBe(true);
    expect(out).toContain('Ã');   // ్మ
  });

  it('uses the dedicated pollu glyphs for ర్ and న్', () => {
    expect(F('ర్')).toBe('”');
    expect(F('న్')).toBe('“');
    // క takes the width-matched pollu variant Š rather than the default Œ.
    expect(F('క్')).toBe('MæŠ');
  });

  it('passes ASCII and spacing through untouched', () => {
    expect(F('abc 123.')).toBe('abc 123.');
    expect(F('తెలుగు 2026')).toContain(' 2026');
  });

  it('maps Telugu digits onto the font digit slots', () => {
    expect(F('౦౧౨౩౪౫౬౭౮౯')).toBe('0123456789');
  });

  it('drops zero-width joiners, which this font has no shaper to obey', () => {
    expect(F('క‌క')).toBe(F('కక'));
  });
});

describe('Shree-Tel-0908: reverse direction', () => {
  it('round-trips vowels, syllables, conjuncts and marks', () => {
    for (const s of ['అ', 'ఆ', 'ఔ', 'క', 'కా', 'కి', 'కీ', 'కు', 'కె', 'కే', 'కొ', 'కో',
                     'కౌ', 'క్క', 'త్త', 'క్ష', 'శ్రీ', 'కం', 'కః', 'ర్', 'న్', 'ద', 'ధ']) {
      expect(R(F(s))).toBe(s);
    }
  });

  it('round-trips running text', () => {
    const text = 'తెలుగు భాష ప్రాచీన ద్రావిడ భాష';
    expect(R(F(text))).toBe(text);
  });

  it('reports legacy bytes it cannot decode instead of swallowing them', () => {
    const res = convertShreeLipiTelugu0908ToUnicode('ðÿþ');
    expect(res.unmapped.length).toBeGreaterThan(0);
  });
});

describe('Shree-Tel-0908: unmapped reporting', () => {
  it('does not warn about the four vowels it substitutes on purpose', () => {
    expect(convertUnicodeToShreeLipiTelugu0908('ఋౠఌౡ').unmapped).toEqual([]);
  });

  it('does warn about a character the font genuinely cannot draw', () => {
    expect(convertUnicodeToShreeLipiTelugu0908('కఁ').unmapped).toContain('ఁ');
  });

  it('returns empty for empty input', () => {
    expect(convertUnicodeToShreeLipiTelugu0908('')).toEqual({ text: '', unmapped: [] });
    expect(convertShreeLipiTelugu0908ToUnicode('')).toEqual({ text: '', unmapped: [] });
  });
});
