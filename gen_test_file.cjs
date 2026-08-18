const fs = require('fs');

const vowels = "అ ఆ ఇ ఈ ఉ ఊ ఋ ౠ ఎ ఏ ఐ ఒ ఓ ఔ అం అః".split(" ");
const consonants = "క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ ళ క్ష ఱ".split(" ");

// Generate ka with all matras
const matras = ["ా", "ి", "ీ", "ు", "ూ", "ృ", "ౄ", "ె", "ే", "ై", "ొ", "ో", "ౌ", "ం", "ః"];
const ka_matras = ["క"];
for (let m of matras) {
  ka_matras.push("క" + m);
}

// Generate all consonants with their own vatthu
// ్ (virama) is \u0C4D
const vatthus = [];
for (let c of consonants) {
  vatthus.push(c + "్" + c);
}

const allWords = [...vowels, ...consonants, ...ka_matras, ...vatthus];

// Join with newlines
const content = allWords.join("\n");
fs.writeFileSync('telugu_test_full.md', content);
console.log("Created telugu_test_full.md with", allWords.length, "lines.");
