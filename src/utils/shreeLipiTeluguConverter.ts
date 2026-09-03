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

// 2. Base Consonants (without top tick/talakattu)
const BASE_CONSONANTS: Record<string, string> = {
  'క': 'M',
  'ఖ': 'Q',
  'గ': 'V',
  'ఘ': 'P',
  'ఙ': '\\',
  'చ': '^',
  'ఛ': 'b',
  'జ': 'f',
  'ఝ': 'm',
  'ఞ': 'p',
  'ట': 'r',
  'ఠ': 'u',
  'డ': 'y',
  'ఢ': 'É',
  'ణ': String.fromCharCode(0xD7),
  'త': '™',
  'థ': '£',
  'ద': '§',
  'ధ': '®',
  'న': '¯',
  'ప': '²',
  'ఫ': '¸',
  'బ': 'º',
  'భ': '¿',
  'మ': 'G',
  'య': 'Å',
  'ర': 'Æ',
  'ల': String.fromCharCode(0xCC),
  'వ': 'Ð',
  'శ': 'Ô',
  'ష': String.fromCharCode(0x201E),
  'స': '¨',
  'హ': String.fromCharCode(0xE0),
  'ళ': 'â',
  'క్ష': '„',
  '„': '„',
  'ఱ': '‚',
};

// Pre-composed Consonant + Vowel combinations for irregulars
const HAS_TALAKATTU: Record<string, boolean> = {
  'క': true,
  'ఖ': false,
  'గ': true,
  'ఘ': true,
  'ఙ': false,
  'చ': true,
  'ఛ': false,
  'జ': true,
  'ఝ': false,
  'ఞ': false,
  'ట': false,
  'ఠ': true,
  'డ': true,
  'ఢ': true,
  'ణ': false,
  'త': true,
  'థ': true,
  'ద': true,
  'ధ': true,
  'న': true,
  'ప': true,
  'ఫ': false,
  'బ': false,
  'భ': true,
  'మ': true,
  'య': true,
  'ర': true,
  'ల': false,
  'వ': true,
  'శ': true,
  'ష': true,
  'స': true,
  'హ': false,
  'ళ': true,
  'క్ష': true,
  '„': true,
  'ఱ': false,
};

// Pre-composed Consonant + Vowel combinations for irregulars
const SPECIAL_COMBOS: Record<string, string> = {
  // తి, తీ
  'తి': '†',
  'తీ': '¡',
  // గి, గీ
  'గి': 'X',
  'గీ': 'Y',
  // చి, చీ
  'చి': '_',
  'చీ': '`',
  // జి, జీ, జు, జూ
  'జి': 'h',
  'జీ': 'i',
  'జు': 'k',
  'జూ': 'l',
  // ఠి, ఠీ
  'ఠి': 'v',
  'ఠీ': 'w',
  // ది, దీ
  'ది': '¨',
  'దీ': '©',
  // ధి, ధీ
  'ధి': '¤',
  'ధీ': '¥',
  // ని, నీ
  'ని': '°',
  'నీ': '±',
  // పి, పీ
  'పి': '³',
  'పీ': '´',
  // ఫి, ఫీ
  'ఫి': '¹',
  // బి, బీ
  'బి': '¼',
  'బీ': '½',
  // భి, భీ
  'భి': 'À',
  'భీ': 'Á',
  // రి, రీ
  'రి': 'Ç',
  'రీ': 'È',
  // లి, లీ
  'లి': 'Í',
  'లీ': 'Î',
  // వి, వీ
  'వి': 'Ñ',
  // శి, శీ
  'శి': 'Õ',
  'శీ': 'Ö',
  // షి, షీ
  'షి': 'Ú',
  // హి, హీ
  'హి': 'à',
};

// 3. Matras (Vowel Signs)
const MATRA_MAP: Record<string, string> = {
  'ా': 'é', // aa (Dirgham) - 0xE9
  'ి': 'ì', // i (Gudi) - 0xEC
  'ీ': 'í', // ii (Gudi deergham) - 0xED
  'ు': 'î', // u (Kommu) - 0xEE
  'ూ': 'ï', // uu (Kommu deergham) - 0xEF
  'ె': 'ð', // e (Ettvam) - 0xF0
  'ే': 'ñ', // ee (Ettvam deergham) - 0xF1
  'ై': 'ò', // ai (Aittvam) - 0xF2
  'ొ': 'ö', // o (Ottvam) - 0xF6
  'ో': 'ø', // oo (Ottvam deergham) - 0xF8
  'ౌ': 'ú', // au (Auttvam) - 0xFA
  'ృ': '#',      // ru (Vattisuli) - 0x23
  'ౄ': '#',      // ruu - 0x23
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
