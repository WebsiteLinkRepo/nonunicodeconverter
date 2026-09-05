/**
 * Unicode Telugu <-> Shree-Lipi "Shree-Tel-0908" legacy encoding.
 *
 * The font carries no GSUB/GPOS, so rendering is literally "look each character up in the
 * (3,1) cmap, draw it, advance by hmtx". Shree-Lipi therefore encodes the *layout*: every
 * vowel sign is a post-base mark whose ink extends into negative x so it draws back over the
 * letter, and the font ships several width variants of each sign so that one of them lands
 * correctly on any given letter. Picking the right variant per letter is the whole job -
 * modelling one variant per sign is what made the previous attempt render ై ొ ో ౌ wrongly.
 *
 * Cluster grammar:  C (virama C)* (matra | virama)?  |  V   , then ం / ః / ఁ.
 * Emission order:   head, subscripts, vowel sign, sunna or visarga.
 *
 * Nothing needs reordering: unlike the Devanagari and Malayalam converters in this
 * directory, no Telugu sign in this font is pre-base.
 *
 * Tables come from scratch/telugu0908/build_tables.py; provenance for each value is in
 * scratch/telugu0908/INVENTORY.md.
 */
import {
  ANUSVARA,
  CONSONANTS,
  DIGITS,
  INDEPENDENT_VOWELS,
  LIGATURES,
  MATRAS,
  NAKAARA_POLLU,
  POLLU,
  REPH,
  VISARGA,
  type ConsonantForms,
} from './mappings/shreeLipiTelugu0908';

const VIRAMA = '్';
const ANUSVARA_U = 'ం';
const VISARGA_U = 'ః';
const CANDRABINDU = 'ఁ';
const ARASUNNA = 'ఀ';
const NUKTA = '\u0C3C';
const KSHA = 'క్ష';
/** Private-use stand-in so the scanner can treat the 3-character క్ష as one consonant. */
const KSHA_SENTINEL = '\uE000';

/** Consonants the font spells with a dedicated "letter + pollu" glyph. */
const POLLU_FORMS: Record<string, string> = { 'ర': REPH, 'న': NAKAARA_POLLU };

/** Longest-first so multi-character keys win in the pre-pass. */
const LIGATURE_KEYS = Object.keys(LIGATURES).sort((a, b) => b.length - a.length);

/** Vowel-sign spelling for one consonant: its own measured variant, else the generic one. */
function markFor(f: ConsonantForms, matra: string): string {
  return f.mark[matra] ?? MATRAS[matra] ?? '';
}

/**
 * Which form of the letter the sign attaches to. A sign drawn above the letter takes the
 * talakattu's place, so it follows the narrow `base`; ు ూ ృ ౄ hang below and leave the top
 * alone, so those follow the complete form. Which signs behave which way is measured per
 * consonant, not assumed.
 */
function headFor(f: ConsonantForms, matra: string): string {
  return f.onFull?.includes(matra) ? f.full : f.base;
}

export interface Telugu0908Result {
  text: string;
  /** Telugu characters with no representation in this font, in input order, de-duplicated. */
  unmapped: string[];
}

export function convertUnicodeToShreeLipiTelugu0908(input: string): Telugu0908Result {
  if (!input) return { text: '', unmapped: [] };

  let text = input;
  // Zero-width joiners only exist to steer a Unicode shaper; this font has no shaper.
  text = text.replace(/[\u200C\u200D]/g, '');
  for (const lig of LIGATURE_KEYS) text = text.split(lig).join(LIGATURES[lig]);
  text = text.split(KSHA).join(KSHA_SENTINEL);
  for (const [uni, legacy] of Object.entries(DIGITS)) text = text.split(uni).join(legacy);

  const unmapped: string[] = [];
  const note = (ch: string) => {
    if (!unmapped.includes(ch)) unmapped.push(ch);
  };

  let out = '';
  let i = 0;
  while (i < text.length) {
    const ch = text[i];

    if (INDEPENDENT_VOWELS[ch]) {
      out += INDEPENDENT_VOWELS[ch];
      i += 1;
      continue;
    }

    const key = ch === KSHA_SENTINEL ? KSHA : ch;
    const forms = CONSONANTS[key];
    if (forms) {
      i += 1;
      const vattus: string[] = [];
      const subKeys: string[] = [];
      let matra = '';
      let pollu = false;

      // C (virama C)* (matra | virama)?
      while (i < text.length) {
        if (text[i] === VIRAMA) {
          const raw = text[i + 1];
          const nextKey = raw === KSHA_SENTINEL ? KSHA : raw;
          const sub = nextKey ? CONSONANTS[nextKey] : undefined;
          if (sub) {
            vattus.push(sub.vattu);
            subKeys.push(nextKey);
            i += 2;
            continue;
          }
          pollu = true;
          i += 1;
          break;
        }
        if (MATRAS[text[i]] !== undefined) {
          // A second vowel sign cannot attach to the same letter; leave it for the next pass.
          if (matra) break;
          matra = text[i];
          i += 1;
          continue;
        }
        break;
      }

      // A subscript is a mark that draws back over whatever precedes it, so a narrow letter
      // needs an advance-only glyph in front of the subscript or the mark lands beside the
      // letter rather than under it. See scratch/telugu0908/geomcheck.py.
      const pad = vattus.length
        ? (forms.padFor?.[subKeys[0]] ?? forms.pad ?? '')
        : '';

      if (matra) {
        // A precomposed C+sign glyph is one unit, so it cannot carry an intervening subscript.
        const pre = vattus.length === 0 ? forms.pre?.[matra] : undefined;
        out += pre ?? headFor(forms, matra) + pad + vattus.join('') + markFor(forms, matra);
      } else if (pollu) {
        out += (vattus.length === 0 && POLLU_FORMS[key])
          ? POLLU_FORMS[key]
          : forms.full + pad + vattus.join('') + forms.pollu;
      } else {
        out += forms.full + pad + vattus.join('');
      }
      continue;
    }

    if (ch === ANUSVARA_U) { out += ANUSVARA; i += 1; continue; }
    if (ch === VISARGA_U) { out += VISARGA; i += 1; continue; }
    if (ch === VIRAMA) { out += POLLU; i += 1; continue; }
    // The font has no arasunna, candrabindu or nukta glyph. Arasunna and candrabindu are
    // nasalisation marks, so the sunna is the closest thing it can draw; a bare nukta has
    // nothing to attach to and is dropped.
    if (ch === CANDRABINDU || ch === ARASUNNA) { out += ANUSVARA; note(ch); i += 1; continue; }
    if (ch === NUKTA) { note(ch); i += 1; continue; }

    if (/[ఀ-౿]/.test(ch)) note(ch);
    out += ch;
    i += 1;
  }

  return { text: out, unmapped };
}

// ---------------------------------------------------------------- reverse

/**
 * Legacy -> Unicode. Built by inverting the same tables the forward direction uses, so the
 * two cannot drift: every string the encoder can emit appears here as a key. Longest match
 * wins, which is what lets `base + subscript + vowel sign` decode as three separate pieces
 * while a precomposed C+sign glyph decodes as one.
 */
function buildReverseMap(): Array<[string, string]> {
  const pairs: Array<[string, string]> = [];

  for (const [uni, legacy] of Object.entries(LIGATURES)) pairs.push([legacy, uni]);

  for (const [ch, f] of Object.entries(CONSONANTS)) {
    for (const [m, glyphs] of Object.entries(f.pre ?? {})) pairs.push([glyphs, ch + m]);
    for (const [m, glyphs] of Object.entries(f.mark)) {
      pairs.push([(f.onFull?.includes(m) ? f.full : f.base) + glyphs, ch + m]);
      // Also register the sign on its own, so a cluster that carried a subscript between the
      // letter and the sign still decodes.
      pairs.push([glyphs, m]);
    }
    if (POLLU_FORMS[ch]) pairs.push([POLLU_FORMS[ch], ch + VIRAMA]);
    pairs.push([f.full + f.pollu, ch + VIRAMA], [f.full + POLLU, ch + VIRAMA]);
    pairs.push([f.full, ch]);
    // `base` only ever appears in encoder output with a subscript or a sign after it, so
    // decoding it as the plain letter is unambiguous.
    pairs.push([f.base, ch]);
    pairs.push([f.vattu, VIRAMA + ch]);
    // The pad carries no meaning of its own; drop it so a padded conjunct decodes.
    for (const p of new Set([f.pad, ...Object.values(f.padFor ?? {})])) {
      if (p) pairs.push([f.full + p, ch], [f.base + p, ch]);
    }
  }

  for (const [uni, legacy] of Object.entries(INDEPENDENT_VOWELS)) pairs.push([legacy, uni]);
  for (const [uni, legacy] of Object.entries(DIGITS)) pairs.push([legacy, uni]);
  for (const [m, glyphs] of Object.entries(MATRAS)) pairs.push([glyphs, m]);
  pairs.push([ANUSVARA, ANUSVARA_U], [VISARGA, VISARGA_U], [POLLU, VIRAMA]);

  // Longest key first so the greedy scan cannot take a prefix of a longer form. Ties broken
  // deterministically, and the first binding for a key wins so per-consonant spellings beat
  // the generic sign-only fallbacks registered alongside them.
  const seen = new Set<string>();
  return pairs
    .filter(([k]) => k.length > 0)
    .sort((a, b) => (b[0].length - a[0].length) || (a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0))
    .filter(([k]) => (seen.has(k) ? false : (seen.add(k), true)));
}

const REVERSE = buildReverseMap();
const REVERSE_MAX = REVERSE.length ? REVERSE[0][0].length : 0;
const REVERSE_INDEX = new Map<string, string>(REVERSE.map(([k, v]) => [k, v]));

export function convertShreeLipiTelugu0908ToUnicode(input: string): Telugu0908Result {
  if (!input) return { text: '', unmapped: [] };
  const unmapped: string[] = [];
  let out = '';
  let i = 0;
  while (i < input.length) {
    let hit = '';
    let len = 0;
    for (let n = Math.min(REVERSE_MAX, input.length - i); n > 0; n -= 1) {
      const found = REVERSE_INDEX.get(input.slice(i, i + n));
      if (found !== undefined) { hit = found; len = n; break; }
    }
    if (len === 0) {
      const ch = input[i];
      // Anything in the legacy high range that will not decode is worth reporting; plain
      // ASCII and whitespace pass through silently, as they do in the forward direction.
      if (ch.charCodeAt(0) > 0x7F && !unmapped.includes(ch)) unmapped.push(ch);
      out += ch;
      i += 1;
      continue;
    }
    out += hit;
    i += len;
  }
  // A vowel sign decoded on its own lands after the subscripts it followed in the legacy
  // stream; Unicode wants it there too, so no reordering is needed. What does need fixing is
  // a sign that ended up before a subscript because the letter used a precomposed form.
  out = out.replace(/([ా-ౌ])((?:్[క-హౘ-ౚ])+)/g, '$2$1');
  return { text: out, unmapped };
}
