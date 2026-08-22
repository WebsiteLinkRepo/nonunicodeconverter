const fs = require('fs');

function generate(lang, vowels, consonants, matras, virama) {
  const allWords = [...vowels, ...consonants];
  const ka = consonants[0];
  for (let m of matras) allWords.push(ka + m);
  for (let c of consonants) allWords.push(c + virama + c);
  fs.writeFileSync(`${lang}_test_full.md`, allWords.join('\n'));
  console.log(`Created ${lang}_test_full.md`);
}

// Hindi
generate('hindi', 
  "अ आ इ ई उ ऊ ऋ ॠ ए ऐ ओ औ अं अः".split(" "),
  "क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स ह क्ष त्र ज्ञ".split(" "),
  ["ा", "ि", "ी", "ु", "ू", "ृ", "ॄ", "े", "ै", "ो", "ौ", "ं", "ः"],
  "्"
);

// Kannada
generate('kannada',
  "ಅ ಆ ಇ ಈ ಉ ಊ ಋ ೠ ಎ ಏ ಐ ಒ ಓ ಔ ಅಂ ಅಃ".split(" "),
  "ಕ ಖ ಗ ಘ ಙ ಚ ಛ ಜ ಝ ಞ ಟ ಠ ಡ ಢ ಣ ತ ಥ ದ ಧ ನ ಪ ಫ ಬ ಭ ಮ ಯ ರ ಲ ವ ಶ ಷ ಸ ಹ ಳ ಕ್ಷ ಱ".split(" "),
  ["ಾ", "ಿ", "ೀ", "ು", "ೂ", "ೃ", "ೄ", "ೆ", "ೇ", "ೈ", "ೊ", "ೋ", "ೌ", "ಂ", "ಃ"],
  "್"
);

// Malayalam
generate('malayalam',
  "അ ആ ഇ ഈ ഉ ഊ ഋ ൠ എ ഏ ഐ ഒ ഓ ഔ അം അഃ".split(" "),
  "ക ഖ ഗ ഘ ങ ച ഛ ജ ഝ ഞ ട ഠ ഡ ഢ ണ ത ഥ ദ ധ ന പ ഫ ബ ഭ മ യ ര ല വ ശ ഷ സ ഹ ള ഴ റ".split(" "),
  ["ാ", "ി", "ീ", "ു", "ൂ", "ൃ", "ൄ", "െ", "േ", "ൈ", "ൊ", "ോ", "ൌ", "ം", "ഃ"],
  "്"
);

// Tamil
generate('tamil',
  "அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ".split(" "),
  "க ங ச ஞ ட ண த ந ப ம ய ர ல வ ழ ள ற ன".split(" "),
  ["ா", "ி", "ீ", "ு", "ூ", "ெ", "ே", "ை", "ொ", "ோ", "ௌ"],
  "்"
);
