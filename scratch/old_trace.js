function escapeRegExp(string) {
  return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function unicodeToKrutidevOld(text) {
  if (!text) return "";

  let modified_substring = text;

  // Add spaces at the end to avoid undefined chars
  modified_substring += '  ';

  // Handle ि (choti i ki matra) - move it before the consonant
  let position_of_f = modified_substring.indexOf("ि");
  while (position_of_f !== -1) {
    const character_left_to_f = modified_substring.charAt(position_of_f - 1);
    modified_substring = modified_substring.replace(character_left_to_f + "ि", "f" + character_left_to_f);
    
    position_of_f = position_of_f - 1;
    
    // Handle conjuncts (move ि before entire conjunct)
    while (modified_substring.charAt(position_of_f - 1) === "्" && position_of_f !== 0) {
      const string_to_be_replaced = modified_substring.charAt(position_of_f - 2) + "्";
      modified_substring = modified_substring.replace(string_to_be_replaced + "f", "f" + string_to_be_replaced);
      position_of_f = position_of_f - 2;
    }
    
    position_of_f = modified_substring.indexOf("ि", position_of_f + 1);
  }

  // Handle र् (reph) - move it to after the consonant+matras
  const set_of_matras = "ािीुूृेैोौं:ँॅ";
  let position_of_half_R = modified_substring.indexOf("र्");
  
  while (position_of_half_R > 0) {
    let probable_position_of_Z = position_of_half_R + 2;
    let character_right_to_probable_position_of_Z = modified_substring.charAt(probable_position_of_Z + 1);
    
    // Find non-matra position right to probable_position_of_Z
    while (set_of_matras.indexOf(character_right_to_probable_position_of_Z) !== -1) {
      probable_position_of_Z = probable_position_of_Z + 1;
      character_right_to_probable_position_of_Z = modified_substring.charAt(probable_position_of_Z + 1);
    }
    
    const string_to_be_replaced = modified_substring.substring(
      position_of_half_R + 2,
      probable_position_of_Z + 1
    );
    modified_substring = modified_substring.replace(
      "र्" + string_to_be_replaced,
      string_to_be_replaced + "Z"
    );
    position_of_half_R = modified_substring.indexOf("र्");
  }

  // Remove the added spaces
  modified_substring = modified_substring.substring(0, modified_substring.length - 2);

  // Reverse mapping arrays
  const array_one = [
    "'", "'", '"', '"', "(", ")", "{", "}", "=", "।", "?", "-", "µ", "॰", ",", ".", "् ",
    "०", "१", "२", "३", "४", "५", "६", "७", "८", "९", "x",
    "फ़्", "क़", "ख़", "ग़", "ज़्", "ज़", "ड़", "ढ़", "फ़", "य़", "ऱ", "ऩ",
    "त्त्", "त्त", "क्त", "दृ", "कृ",
    "ह्न", "ह्य", "हृ", "ह्म", "ह्र", "ह्", "द्द", "क्ष्", "क्ष", "त्र्", "त्र", "ज्ञ",
    "छ्य", "ट्य", "ठ्य", "ड्य", "ढ्य", "द्य", "द्व",
    "श्र", "ट्र", "ड्र", "ढ्र", "छ्र", "क्र", "फ्र", "द्र", "प्र", "ग्र", "रु", "रू",
    "Z",
    "ओ", "औ", "आ", "अ", "ई", "इ", "उ", "ऊ", "ऐ", "ए", "ऋ",
    "क्", "क", "क्क", "ख्", "ख", "ग्", "ग", "घ्", "घ", "ङ",
    "चै", "च्", "च", "छ", "ज्", "ज", "झ्", "झ", "ञ",
    "ट्ट", "ट्ठ", "ट", "ठ", "ड्ड", "ड्ढ", "ड", "ढ", "ण्", "ण",
    "त्", "त", "थ्", "थ", "द्ध", "द", "ध्", "ध", "न्", "न",
    "प्", "प", "फ्", "फ", "ब्", "ब", "भ्", "भ", "म्", "म",
    "य्", "य", "र", "ल्", "ल", "ळ", "व्", "व",
    "श्", "श", "ष्", "ष", "स्", "स", "ह",
    "ऑ", "ॉ", "ो", "ौ", "ा", "ी", "ु", "ू", "ृ", "े", "ै",
    "ं", "ँ", "ः", "ॅ", "ऽ", "् ", "्"
  ];

  const array_two = [
    "^", "*", 'Þ', 'ß', "¼", "½", "¿", "À", "¾", "A", "\\", "&", "&", "Œ", "]", "-", "~ ",
    "å", "ƒ", "„", "…", "†", "‡", "ˆ", "‰", "Š", "‹", "Û",
    "¶", "d", "[k", "x", "T", "t", "M+", "<+", "Q", ";", "j", "u",
    "Ù", "Ùk", "ä", "–", "—",
    "à", "á", "â", "ã", "ºz", "º", "í", "{", "{k", "«", "=", "K",
    "Nî", "Vî", "Bî", "Mî", "<î", "|", "}",
    "J", "Vª", "Mª", "<ªª", "Nª", "Ø", "Ý", "æ", "ç", "xz", "#", ":",
    "Z",
    "vks", "vkS", "vk", "v", "bZ", "b", "m", "Å", ",s", ",", "_",
    "D", "d", "ô", "[", "[k", "X", "x", "?", "?k", "³",
    "pkS", "P", "p", "N", "T", "t", "÷", ">", "¥",
    "ê", "ë", "V", "B", "ì", "ï", "M", "<", ".", ".k",
    "R", "r", "F", "Fk", ")", "n", "/", "/k", "U", "u",
    "I", "i", "¶", "Q", "C", "c", "H", "Hk", "E", "e",
    "¸", ";", "j", "Y", "y", "G", "O", "o",
    "'", "'k", "\"", "\"k", "L", "l", "g",
    "v‚", "‚", "ks", "kS", "k", "h", "q", "w", "`", "s", "S",
    "a", "¡", "%", "W", "·", "~ ", "~"
  ];

  // Modified old logic strictly up to Z to avoid infinite loop
  for (let i = 0; i < 76; i++) {
    if (array_one[i]) {
      let idx = 0;
      while (idx !== -1) {
        modified_substring = modified_substring.replace(array_one[i], array_two[i]);
        idx = modified_substring.indexOf(array_one[i]);
      }
    }
  }

  return modified_substring;
}
console.log(unicodeToKrutidevOld("क्ख च्छ त्त द्ध द्य द्व"));
