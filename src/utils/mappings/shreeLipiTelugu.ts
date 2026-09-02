export const SHREE_LIPI_TELUGU_MAPPINGS = [
  // Independent Vowels
  { from: 'అ', to: 'A' },
  { from: 'ఆ', to: 'B' },
  { from: 'ఇ', to: 'C' },
  { from: 'ఈ', to: 'D' },
  { from: 'ఉ', to: 'E' },
  { from: 'ఊ', to: 'F' },
  { from: 'ఎ', to: 'G' },
  { from: 'ఏ', to: 'H' },
  { from: 'ఐ', to: 'I' },
  { from: 'ఒ', to: 'J' },
  { from: 'ఓ', to: 'K' },
  { from: 'ఔ', to: 'L' },
  { from: 'ఋ', to: '?' }, // Need to map

  // Consonants (Base forms) - mapping to their primary base glyph
  // Based on visual inspection of the catalog
  { from: 'క', to: 'a' },
  { from: 'ఖ', to: 'Q' },
  { from: 'గ', to: 'V' },     // or Y
  { from: 'ఘ', to: '\\u0192' }, // 0x192 (402) is ఘ
  { from: 'ఙ', to: 'Z' },     // 'Z' (0x5A)

  { from: 'చ', to: '^' },     // '^' (0x5E)
  { from: 'ఛ', to: 'b' },     // 'b' (0x62)
  { from: 'జ', to: '\\\\' }, // '\' (0x5C) -> '\\' in string
  { from: 'ఝ', to: 'm' },     // 'm' (0x6D)
  { from: 'ఞ', to: 'n' },     // 'n' (0x6E)

  { from: 'ట', to: 'r' },     // 'r' (0x72)
  { from: 'ఠ', to: 't' },     // 't' (0x74)
  { from: 'డ', to: 'y' },     // 'y' (0x79)
  { from: 'ఢ', to: '|' },     // '|' (0x7C)
  { from: 'ణ', to: '~' },     // '~' (0x7E)

  { from: 'త', to: '\\u2122' }, // 0x2122 (8482) is త
  { from: 'థ', to: '\\u00A3' }, // 0xA3 (163) is థ
  { from: 'ద', to: '\\u00A7' }, // 0xA7 (167) is ద
  { from: 'ధ', to: '\\u00AA' }, // 0xAA (170) is ధ
  { from: 'న', to: '\\u00AF' }, // 0xAF (175) is న

  { from: 'ప', to: '\\u00B2' }, // 0xB2 (178) is ప
  { from: 'ఫ', to: '\\u00B8' }, // 0xB8 (184) is ఫ
  { from: 'బ', to: '\\u00BA' }, // 0xBA (186) is బ
  { from: 'భ', to: '\\u00BF' }, // 0xBF (191) is భ
  { from: 'మ', to: '\\u00C4' }, // 0xC4 is య? Wait. 0xC4 = య.

  // Need to fix మ and య

  { from: 'య', to: '\\u00C4' }, // 0xC4 is య base
  { from: 'ర', to: '?' }, // Need to map. Let's find ర.
  { from: 'ల', to: '\\u00CB' }, // 0xCB is ల base
  { from: 'వ', to: '\\u00D3' }, // 0xD3 is వ base
  { from: 'శ', to: '\\u00D4' }, // 0xD4 is శ base
  { from: 'ష', to: '\\u0153' }, // 0x153 (339) is ష base
  { from: 'స', to: '\\u00DC' }, // 0xDC is స base
  { from: 'హ', to: '\\u02DC' }, // 0x2DC (732) is హ base
  { from: 'ళ', to: '\\u00CA' }, // 0xCA is ళ base
  { from: 'క్ష', to: '<' },    // '<' (0x3C)
  { from: 'ఱ', to: '\\u0160' }, // 0x160 (352) is ఱ

  // Talakattu default (will be added after consonants unless cancelled)
  // Matras
  // દીర్ఘం (aa) = ా -> 'N' or '*' or '0xFA'
  // గుడి (i) = ి -> '0xEC' (ì)
  // గుడి దీర్ఘం (ii) = ీ -> '0xEE' (î)
  // కొమ్ము (u) = ు -> '0xF0' (ð) or '0x2013'
  // కొమ్ము దీర్ఘం (uu) = ూ -> '0xF3' (ó) or '0x2014'
  // ృ (ru) -> 'P' (P)
  // ె (e) -> '0xE7' ?
  // ే (ee) -> '0xE8' ?
  // ై (ai) -> '0xFB' (û)
  // ొ (o) -> ?
  // ో (oo) -> ?
  // ౌ (au) -> '0x178' (376)
  // ం (sunna) -> '0x2026'
  // ః (visarga) -> '@' (0x40)

];
