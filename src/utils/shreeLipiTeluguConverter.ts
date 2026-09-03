/**
 * Complete Unicode to Shree-Lipi Telugu (Shree-Tel-0908 Regular) Converter
 */

// 1. Independent Vowels
const INDEPENDENT_VOWELS: Record<string, string> = {
  'అ': 'A',
  'ఆ': 'B',
  'ఇ': 'C',
  'ఈ': 'D',
  'ఉ': 'E',
  'ఊ': 'F',
  'ఎ': 'G',
  'ఏ': 'H',
  'ఐ': 'I',
  'ఒ': 'J',
  'ఓ': 'K',
  'ఔ': 'L',
  // Shree-Tel-0908 has no single glyph for the vocalic vowels ఋ / ౠ (verified: nothing
  // in the font's 217-code cmap matches them). They are built as బ + two kommus, which
  // renders identically to the Unicode reference.
  'ఋ': String.fromCharCode(0xba, 0x24, 0x24),
  'ౠ': String.fromCharCode(0xba, 0x24, 0x2a),
};

// 2. Base Consonants (without top tick/talakattu, or pre-composed full consonants)
const BASE_CONSONANTS: Record<string, string> = {
  'క': String.fromCharCode(0x4D),
  'ఖ': String.fromCharCode(0x51),
  'గ': String.fromCharCode(0x56),
  'ఘ': String.fromCharCode(0x5B),
  'ఙ': String.fromCharCode(0x5A),
  'చ': String.fromCharCode(0x5E),
  'ఛ': String.fromCharCode(0x62),
  'జ': String.fromCharCode(0x67),
  'ఝ': String.fromCharCode(0x6D),
  'ఞ': String.fromCharCode(0x70),
  'ట': String.fromCharCode(0x72),
  'ఠ': String.fromCharCode(0x75),
  'డ': String.fromCharCode(0x79),
  'ఢ': String.fromCharCode(0xC9),
  'ణ': String.fromCharCode(0xD7),
  'త': String.fromCharCode(0xA2),
  'థ': String.fromCharCode(0xA3),
  'ద': String.fromCharCode(0xA7),
  'ధ': String.fromCharCode(0xA4),
  'న': String.fromCharCode(0xAF),
  'ప': String.fromCharCode(0xB3),
  'ఫ': String.fromCharCode(0xB8),
  'బ': String.fromCharCode(0xBA),
  'భ': String.fromCharCode(0xBE),
  'మ': String.fromCharCode(0x192),
  'య': String.fromCharCode(0xC4),
  'ర': String.fromCharCode(0xC6),
  'ళ': String.fromCharCode(0xE2),
  'వ': String.fromCharCode(0xD0),
  'శ': String.fromCharCode(0xD4),
  'ష': String.fromCharCode(0xD9),
  'స': String.fromCharCode(0xDC),
  'హ': String.fromCharCode(0xDF),
  'క్ష': String.fromCharCode(0x84),
  '„': String.fromCharCode(0x84),  // For the replaced క్ష
  'ఱ': String.fromCharCode(0x82),
};

// Whether the base consonant needs combining talakattu, and which variant
// Based on verified glyph chart - only consonants marked "raw 0x__ + 0xE6/0xE7/0xE8" need talakattu
const TALAKATTU_MAP: Record<string, string> = {
  'క': String.fromCharCode(0xE6),   // 0x4D + 0xE6
  'గ': String.fromCharCode(0xE6),   // 0x56 + 0xE6
  'ఘ': String.fromCharCode(0xE6),   // 0x5B + 0xE6
  'చ': String.fromCharCode(0xE6),   // 0x5E + 0xE6
  'ఠ': String.fromCharCode(0xE6),   // 0x75 + 0xE6
  'డ': String.fromCharCode(0xE6),   // 0x79 + 0xE6
  'ఢ': String.fromCharCode(0xE6),   // 0xC9 + 0xE6
  'త': String.fromCharCode(0xE6),   // 0xA2 + 0xE6
  'థ': String.fromCharCode(0xE6),   // 0xA3 + 0xE6
  'ద': String.fromCharCode(0xE6),   // 0xA7 + 0xE6
  'ధ': String.fromCharCode(0xE6),   // 0xA4 + 0xE6
  'న': String.fromCharCode(0xE6),   // 0xAF + 0xE6
  'ప': String.fromCharCode(0xE7),   // 0xB3 + 0xE7 (shifted)
  'ఫ': String.fromCharCode(0xE7),   // 0xB8 + 0xE7 (shifted)
  'భ': String.fromCharCode(0xE7),   // 0xBE + 0xE7 (shifted)
  'మ': String.fromCharCode(0xE6),   // 0x192 + 0xE6
  'య': String.fromCharCode(0xE8),   // 0xC4 + 0xE8 (right-offset)
  'ర': String.fromCharCode(0xE6),   // 0xC6 + 0xE6
  'ళ': String.fromCharCode(0xE6),   // 0xE2 + 0xE6
  'వ': String.fromCharCode(0xE6),   // 0xD0 + 0xE6
  'శ': String.fromCharCode(0xE6),   // 0xD4 + 0xE6
  'ష': String.fromCharCode(0xE7),   // 0xD9 + 0xE7 (shifted)
  'స': String.fromCharCode(0xE7),   // 0xDC + 0xE7 (shifted)
  '„': String.fromCharCode(0xE6),   // For క్ష
  // Explicitly NO talakattu for these pre-composed/complete glyphs:
  // ఖ (0x51), ఛ (0x62), జ (0x67), ఝ (0x6D), ఞ (0x70), ట (0x72), ణ (0xD7), బ (0xBA), హ (0xDF)
};

// Pre-composed Consonant + Vowel combinations for irregulars
const SPECIAL_COMBOS: Record<string, string> = {
  // తి, తీ
  'తి': String.fromCharCode(0x2020),
  'తీ': String.fromCharCode(0xA1),
  // గి, గీ
  'గి': String.fromCharCode(0x57),
  'గీ': String.fromCharCode(0x58),
  // చి, చీ
  'చి': String.fromCharCode(0x5F),
  'చీ': String.fromCharCode(0x60),
  // ఛి, ఛీ
  'ఛి': String.fromCharCode(0x63),
  'ఛీ': String.fromCharCode(0x64),
  // జి, జీ, జు, జూ
  'జి': String.fromCharCode(0x68),
  'జీ': String.fromCharCode(0x68),
  'జు': String.fromCharCode(0x6B),
  'జూ': String.fromCharCode(0x6C),
  // ఝి, ఝీ
  'ఝి': String.fromCharCode(0x6D),
  'ఝీ': String.fromCharCode(0x6E),
  // ఠి, ఠీ
  'ఠి': String.fromCharCode(0x76),
  'ఠీ': String.fromCharCode(0x77),
  // ది, దీ
  'ది': String.fromCharCode(0xA8),
  'దీ': String.fromCharCode(0xA9),
  // ధి, ధీ
  'ధి': String.fromCharCode(0xA4),
  'ధీ': String.fromCharCode(0xA5),
  // ని, నీ
  'ని': String.fromCharCode(0xB0),
  'నీ': String.fromCharCode(0xB1),
  // పి, పీ
  'పి': String.fromCharCode(0xB4),
  'పీ': String.fromCharCode(0xB4),
  // ఫి
  'ఫి': String.fromCharCode(0xB8),
  // బి, బీ
  'బి': String.fromCharCode(0xBC),
  'బీ': String.fromCharCode(0xBD),
  // భి, భీ
  'భి': String.fromCharCode(0xBF),
  'భీ': String.fromCharCode(0xC1),
  // రి, రీ
  'రి': String.fromCharCode(0xC7),
  'రీ': String.fromCharCode(0xC8),
  // లి, లీ
  'లి': String.fromCharCode(0xCD),
  'లీ': String.fromCharCode(0xCD),
  // వి, వీ
  'వి': String.fromCharCode(0xD1),
  'వీ': String.fromCharCode(0xD2),
  // శి, శీ
  'శి': String.fromCharCode(0xD5),
  'శీ': String.fromCharCode(0xD6),
  // షి
  'షి': String.fromCharCode(0xDA),
  // హి
  'హి': String.fromCharCode(0xE0),
  // ళి, ళీ
  'ళి': String.fromCharCode(0xE3),
  'ళీ': String.fromCharCode(0xE4),
};

// 3. Matras (Vowel Signs)
const MATRA_MAP: Record<string, string> = {
  'ా': 'é',
  'ి': 'ì',
  'ీ': 'í',
  'ు': String.fromCharCode(0xEE),
  'ూ': String.fromCharCode(0xEF),
  'ృ': String.fromCharCode(0x23),
  'ౄ': String.fromCharCode(0x23, 0x2A),
  'ె': 'ð',
  'ే': 'ñ',
  'ై': 'ò',
  'ొ': 'ö',
  'ో': 'ø',
  'ౌ': 'ú',
};

const VATTHULU: Record<string, string> = {
  'క': String.fromCharCode(0x152),
  'ఖ': String.fromCharCode(0x50),
  'గ': String.fromCharCode(0x57),
  'ఘ': String.fromCharCode(0x153),
  'ఙ': String.fromCharCode(0x5A),
  'చ': String.fromCharCode(0x61),
  'ఛ': String.fromCharCode(0x65),
  'జ': String.fromCharCode(0x6E),
  'ఝ': String.fromCharCode(0x71),
  'ఞ': String.fromCharCode(0x71),
  'ట': String.fromCharCode(0x73),
  'ఠ': String.fromCharCode(0x78),
  'డ': String.fromCharCode(0x7A),
  'ఢ': String.fromCharCode(0x7C),
  'ణ': String.fromCharCode(0x178),
  'త': String.fromCharCode(0xAC),
  'థ': String.fromCharCode(0xAE),
  'ద': String.fromCharCode(0xAA),
  'ధ': String.fromCharCode(0xC9),
  'న': String.fromCharCode(0xB2),
  'ప': String.fromCharCode(0xB5),
  'ఫ': String.fromCharCode(0xB9),
  'బ': String.fromCharCode(0xBE),
  'భ': String.fromCharCode(0xC2),
  'మ': String.fromCharCode(0x161),
  'య': String.fromCharCode(0xC5),
  'ర': String.fromCharCode(0x2013),
  'ల': String.fromCharCode(0xCF),
  'వ': String.fromCharCode(0xD3),
  'శ': String.fromCharCode(0xD8),
  'ష': String.fromCharCode(0xDA),
  'స': String.fromCharCode(0xDE),
  'హ': String.fromCharCode(0xE5),
  'ళ': String.fromCharCode(0x201A),
  'క్ష': String.fromCharCode(0x3C),
  'ఱ': String.fromCharCode(0x201C),
};

const TALAKATTU = 'æ';                        // 0xE6 - combining talakattu (adv 40, draws left)
const ANUSVARA = String.fromCharCode(0x2026); // Sunna. 0x30 is the DIGIT zero (adv 543) and
                                              // 0xC6 is the ర base (adv 206, overhangs so the
                                              // talakattu can overlay it); 0x2026 is the
                                              // free-standing sunna circle (adv 411).
const VISARGA = String.fromCharCode(0x40);    // 0x3A is the Latin colon; 0x40 is the visarga
const VIRAMA = String.fromCharCode(0xA2);     // ¢ - combining pollu below-left

export function convertUnicodeToShreeLipiTelugu(input: string): string {
  if (!input) return '';

  // 1. Direct whole-word and special multi-character replacements
  let text = input
    .replace(/శ్రీ/g, '}')
    .replace(/క్ష/g, '„')
    .replace(/౦/g, '0')
    .replace(/౧/g, '1')
    .replace(/౨/g, '2')
    .replace(/౩/g, '3')
    .replace(/౪/g, '4')
    .replace(/౫/g, '5')
    .replace(/౬/g, '6')
    .replace(/౭/g, '7')
    .replace(/౮/g, '8')
    .replace(/౯/g, '9');

  let result = '';
  let i = 0;

  while (i < text.length) {
    const ch = text[i];

    // Check Independent Vowels
    if (INDEPENDENT_VOWELS[ch]) {
      result += INDEPENDENT_VOWELS[ch];
      i++;
      continue;
    }

    // Check Consonants
    if (BASE_CONSONANTS[ch]) {
      const baseChar = BASE_CONSONANTS[ch];
      const consonantUni = ch;
      i++;

      let hasVirama = false;
      let vattuList: string[] = [];
      let matraUni = '';

      while (i < text.length) {
        if (text[i] === '్') { // Halant / Virama
          i++;
          if (i < text.length && BASE_CONSONANTS[text[i]]) {
            // Subscript consonant (vattu)
            const sub = text[i];
            vattuList.push(VATTHULU[sub] || BASE_CONSONANTS[sub]);
            i++;
          } else {
            hasVirama = true;
            break;
          }
        } else if (MATRA_MAP[text[i]]) {
          matraUni = text[i];
          i++;
        } else if (text[i] === 'ం' || text[i] === 'ః') {
          break;
        } else {
          break;
        }
      }

      // Check for pre-composed irregular combo (only when no vattulu precede the matra)
      const comboKey = consonantUni + matraUni;
      if (vattuList.length === 0 && SPECIAL_COMBOS[comboKey]) {
        result += SPECIAL_COMBOS[comboKey];
      } else {
        result += baseChar;
        // Vattulu go between base consonant and vowel sign (before matra/talakattu)
        for (const v of vattuList) {
          result += v;
        }
        if (hasVirama) {
          result += VIRAMA;
        } else if (matraUni && MATRA_MAP[matraUni]) {
          result += MATRA_MAP[matraUni];
        } else if (TALAKATTU_MAP[consonantUni]) {
          result += TALAKATTU_MAP[consonantUni];
        }
      }

      continue;
    }

    // Anusvara
    if (ch === 'ం') {
      result += ANUSVARA;
      i++;
      continue;
    }

    // Visarga
    if (ch === 'ః') {
      result += VISARGA;
      i++;
      continue;
    }

    // Pass-through
    result += ch;
    i++;
  }

  return result;
}
