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
  'క': String.fromCharCode(0x4D),      // 0x4D + talakattu (0xE6)
  'ఖ': String.fromCharCode(0x51),      // 0x51 is full glyph
  'గ': String.fromCharCode(0x56),      // 0x56 + talakattu (0xE6)
  'ఘ': String.fromCharCode(0x55),      // 0x55 + talakattu (0xE6)
  'ఙ': String.fromCharCode(0x5C),      // 0x5C is full glyph
  'చ': String.fromCharCode(0x5E),      // 0x5E + talakattu (0xE6)
  'ఛ': String.fromCharCode(0x62),      // 0x62 is full glyph
  'జ': String.fromCharCode(0x67),      // 0x67 is full glyph
  'ఝ': String.fromCharCode(0x6D),      // 0x6D is full glyph
  'ఞ': String.fromCharCode(0x70),      // 0x70 is full glyph
  'ట': String.fromCharCode(0x72),      // 0x72 is full glyph
  'ఠ': String.fromCharCode(0x75),      // 0x75 + talakattu (0xE6)
  'డ': String.fromCharCode(0x79),      // 0x79 + talakattu (0xE6)
  'ఢ': String.fromCharCode(0xC9),      // 0xC9 + talakattu (0xE6)
  'ణ': String.fromCharCode(0xD7),      // 0xD7 is full glyph
  'త': String.fromCharCode(0x2122),    // 0x2122 (0x99 in Shree-Lipi) + talakattu (0xE6)
  'థ': String.fromCharCode(0xA3),      // 0xA3 + talakattu (0xE6)
  'ద': String.fromCharCode(0xA7),      // 0xA7 + talakattu (0xE6)
  'ధ': String.fromCharCode(0xA4),      // 0xA4 + talakattu (0xE6)
  'న': String.fromCharCode(0xAF),      // 0xAF + talakattu (0xE6)
  'ప': String.fromCharCode(0xB3),      // 0xB3 + talakattu (0xE6)
  'ఫ': String.fromCharCode(0xB8),      // 0xB8 + talakattu (0xE6)
  'బ': String.fromCharCode(0xBA),      // 0xBA is full glyph
  'భ': String.fromCharCode(0xBE),      // 0xBE + talakattu (0xE6)
  'మ': String.fromCharCode(0xC3),      // 0xC3 + talakattu (0xE6)
  'య': String.fromCharCode(0xC4),      // 0xC4 + talakattu (0xE6)
  'ర': String.fromCharCode(0xC6),      // 0xC6 + talakattu (0xE6)
  'ఱ': String.fromCharCode(0x201A),    // 0x201A (0x82) is full glyph
  'ల': String.fromCharCode(0xCC),      // 0xCC is full glyph
  'ళ': String.fromCharCode(0xE2),      // 0xE2 + talakattu (0xE6)
  'వ': String.fromCharCode(0xD0),      // 0xD0 + talakattu (0xE6)
  'శ': String.fromCharCode(0xD4),      // 0xD4 + talakattu (0xE6)
  'ష': String.fromCharCode(0xD9),      // 0xD9 + talakattu (0xE6)
  'స': String.fromCharCode(0xDC),      // 0xDC + talakattu (0xE6)
  'హ': String.fromCharCode(0xDF),      // 0xDF is full glyph
  'క్ష': String.fromCharCode(0x201E),   // 0x201E (0x84) is full glyph
};

// Whether the base consonant needs combining talakattu (0xE6) appended
const HAS_TALAKATTU: Record<string, boolean> = {
  'క': true,    // 0x4D needs talakattu
  'ఖ': false,   // 0x51 is FULL, no talakattu
  'గ': true,    // 0x56 needs talakattu
  'ఘ': true,    // 0x55 needs talakattu
  'ఙ': false,   // 0x5C is FULL, no talakattu
  'చ': true,    // 0x5E needs talakattu
  'ఛ': false,   // 0x62 is FULL, no talakattu
  'జ': false,   // 0x67 is FULL, no talakattu
  'ఝ': false,   // 0x6D is FULL, no talakattu
  'ఞ': false,   // 0x70 is FULL, no talakattu
  'ట': false,   // 0x72 is FULL, no talakattu
  'ఠ': true,    // 0x75 needs talakattu
  'డ': true,    // 0x79 needs talakattu
  'ఢ': true,    // 0xC9 needs talakattu
  'ణ': false,   // 0xD7 is FULL, no talakattu
  'త': true,    // 0x2122 needs talakattu
  'థ': true,    // 0xA3 needs talakattu
  'ద': true,    // 0xA7 needs talakattu
  'ధ': true,    // 0xA4 needs talakattu
  'న': true,    // 0xAF needs talakattu
  'ప': true,    // 0xB3 needs talakattu
  'ఫ': true,    // 0xB8 needs talakattu
  'బ': false,   // 0xBA is FULL, no talakattu
  'భ': true,    // 0xBE needs talakattu
  'మ': true,    // 0xC3 needs talakattu
  'య': true,    // 0xC4 needs talakattu
  'ర': true,    // 0xC6 needs talakattu
  'ఱ': false,   // 0x201A is FULL, no talakattu
  'ల': false,   // 0xCC is FULL, no talakattu
  'ళ': true,    // 0xE2 needs talakattu
  'వ': true,    // 0xD0 needs talakattu
  'శ': true,    // 0xD4 needs talakattu
  'ష': true,    // 0xD9 needs talakattu
  'స': true,    // 0xDC needs talakattu
  'హ': false,   // 0xDF is FULL, no talakattu
  'క్ష': false,  // 0x201E is FULL, no talakattu
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
  'భి': String.fromCharCode(0xC0),
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
  'ు': String.fromCharCode(0x24),
  'ూ': String.fromCharCode(0x2A),
  'ృ': String.fromCharCode(0x23),
  'ౄ': String.fromCharCode(0x23, 0x2A),
  'ె': 'ð',
  'ే': 'ñ',
  'ై': 'ò',
  'ొ': 'ö',
  'ో': 'ø',
  'ౌ': 'ú',
};

// 4. Subscript Consonants (Vatthulu / Ottulu)
const VATTHULU: Record<string, string> = {
  '„': '<',
  'క': 'Œ', // Œ
  'ఖ': 'U',
  'గ': 'W',
  'ఘ': 'œ', // œ
  'ఙ': 'Z',
  'చ': 'e',
  'ఛ': 'd',
  'జ': 'j',
  'ఝ': 'n',
  'ఞ': 'q',
  'ట': 's',
  'ఠ': 'x',
  'డ': 'z',
  'ఢ': '{',
  'ణ': 'Š', // Š
  'త': 'ª', // ª (or t-vattu)
  'థ': '¦', // ¦
  'ద': 'ª', // ª
  'ధ': 'É', // É
  'న': 'Ý', // Ý (or Þ)
  'ప': 'µ', // µ
  'ఫ': '¹',
  'బ': '¾', // ¾
  'భ': 'Â', // Â
  'మ': 'š', // š
  'య': 'Ÿ', // Ÿ
  'ర': '–', // –
  'ల': 'Ï', // Ï
  'వ': 'Ó', // Ó
  'శ': 'Ø', // Ø
  'ష': 'Û', // Û
  'స': 'Þ', // Þ
  'హ': 'å', // å
  'ళ': 'å',
  'క్ష': '<',
  'ఱ': '‚',
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
        } else if (HAS_TALAKATTU[consonantUni]) {
          result += TALAKATTU;
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
