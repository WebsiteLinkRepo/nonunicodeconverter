import { SHREE_LIPI_MAPPINGS } from './mappings/shreeLipi';

const reverseMap: Record<string, string> = {};
const sortedMap = [...SHREE_LIPI_MAPPINGS].sort((a, b) => b.from.length - a.from.length);

for (const entry of sortedMap) {
  if (entry.to && entry.from) {
    if (!reverseMap[entry.to] || entry.from.length > reverseMap[entry.to].length) {
       reverseMap[entry.to] = entry.from;
    }
  }
}

// Ensure the explicit fallbacks from forward conversion are in the reverse map
const fallbacks: Record<string, string> = {
    '।': '&', '॥': '&&', 'ा': 'm', 'ी': 'r', 'ु': 'w', 'ू': 'y',
    'ृ': '¥', 'ॄ': '¦', 'े': 'o', 'ै': '¡', 'ं': '§', 'ः': '…',
    'ँ': '±', 'ॅ': '°', '्': '²', '़': 'µ', '|': '&',
    '१': '1', '२': '2', '३': '3', '४': '4', '५': '5',
    '६': '6', '७': '7', '८': '8', '९': '9', '०': '0',
};
for (const [k, v] of Object.entries(fallbacks)) {
    if (!reverseMap[v] || k.length > reverseMap[v].length) {
        reverseMap[v] = k; // Need to inverse k/v
    }
}

// These overrides are composite vowels and other structural mapping from the first block
const specificFallbacks: Record<string, string> = {
    'ो': 'mo', 'ौ': 'm¡', 'ॉ': 'm°', 'ों': 'mo§', 'ें': 'o§', 'ैं': '¢',
    'ड़': '‹S>', 'ढ़': '‹T>',
    'उच्छ्वास' : 'CÀN²>dmg',
    'वैशिष्ट्य' : 'd¡{eï²`',
    'स्फूर्ति' : 'ñ\\y${V©',
    "स्फू" : "ñ\\y$",
    "आर्द्र" : "AmÐ©",
    "र्द्र" : "Ð©",
    "च्छ्र" : "ÀN>«",
    "ज्ञ्य" : "k²`",
    "क्त्य" : "º²$`",
    "ञ्च" : "ÄM",
    "ञ्छ" : "ÄN>",
    "ञ्ज" : "ÄO",
    "ञ्झ" : "ÄP",
    "त्त्त्य" : "ÎË`",
    "त्म्य" : "Ëå`",
    "त्स्न" : "ËñZ",
    "त्स्य" : "Ëñ`",
    "द्र्य" : "Ú©",
    "ष्ट्य" : "ï²`",
    "ऱ्हा" : "èhm",
    "ऱ्ह" : "èh",
    "ऱ्" : "è",
    "कुऱ्हाड": "Hw\$èhmS>"

};
for (const [k, v] of Object.entries(specificFallbacks)) {
    if (!reverseMap[v] || k.length > reverseMap[v].length) {
        reverseMap[v] = k; 
    }
}

const reverseKeys = Object.keys(reverseMap).sort((a, b) => b.length - a.length);

/**
 * Converts Shree-Lipi (Shree-Dev7) legacy encoding back to Unicode Devanagari Hindi/Marathi text.
 */
export function shreeLipiToUnicode(text: string, language: "hindi" | "marathi" = "hindi"): string {
  if (!text) return "";

  let processText = text;

  // Re-assemble short-i special formatting
  processText = processText.replace(/qH\$/g, "{H\$§");
  processText = processText.replace(/qR>/g, "{R>§");
  processText = processText.replace(/qS>/g, "{S>§");
  processText = processText.replace(/qT>/g, "{T>§");
  processText = processText.replace(/qa/g, "{a§");
  processText = processText.replace(/qi/g, "{i§");

  processText = processText.replace(/p([ñŠßÝËã½¿ÀÁÊÜäåîùƒ])/g, "{$1");

  // Undo right-bracket glyphs fix
  processText = processText.replace(/([QTRNSL])([o¡¢])>/g, '$1>$2');
  processText = processText.replace(/‹([QTRNSL])([o¡¢])>/g, '‹$1>$2');

  let result = '';
  // Apply longest-match reverse mapping
  let i = 0;
  while (i < processText.length) {
    let matched = false;
    for (const key of reverseKeys) {
      if (processText.startsWith(key, i)) {
        result += reverseMap[key];
        i += key.length;
        matched = true;
        break;
      }
    }
    if (!matched) {
      result += processText[i];
      i++;
    }
  }
  
  // Reorder short 'i' and short 'i' + anusvara
  // Backward from: { + consonant -> consonant + ि
  const reverseIAnusvaraRegex = /\{((?:[क-हक़-य़]्)*[क-हक़-य़])§/g;
  result = result.replace(reverseIAnusvaraRegex, '$1िं');

  const reverseIRegex = /\{((?:[क-हक़-य़]्)*[क-हक़-य़])/g;
  result = result.replace(reverseIRegex, '$1ि');

  if (language === "marathi") {
    // Halant Lla before consonants -> ù
    result = result.replace(/ù([क-हक़-य़])/g, "ळ्$1");
  }
  result = result.split("i~").join("ळ्");

  // Fix Specific complex conjuncts that were overridden
  result = result.split("उछ्वास").join("उच्छ्वास"); 
  
  // Fix Decomposed Nuktas when reversed to their components
  // Sometimes { + consonant + nukta => consonant + nukta + ि -> needs to be consonant+नुकता+ि
  // This reverse nukta swap fixes cases where nukta and matra overlap 
  result = result.replace(/([क-ह])ि़/g, '$1़ि');
  
  // Undo specific normalizations (make sure we default to the standard ones to match forward's first phase)
  result = result.replace(/हृ्ह/g, "ऱ्ह"); // Clean up any weird combinations from eyelash Ra
  
  return result;
}
