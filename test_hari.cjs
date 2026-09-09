const fs = require('fs');
const content = fs.readFileSync('src/utils/mappings/hariGujarati.ts', 'utf-8');
const mappings = [];
const regex = /{ from: '(.*?)', to: '(.*?)' }/g;
let match;
while ((match = regex.exec(content)) !== null) {
  mappings.push({ from: match[1], to: match[2] });
}
mappings.sort((a,b) => b.from.length - a.from.length);

let text = "નમસ્કાર! ગુજરાતી ભાષા ખૂબ જ સુંદર છે.";
// 1. Re-ordering pre-base matra (Short-i / િ)
const gujaratiConsonant = '[ક-હળક્ષજ્ઞ]';
const halant = '્';
const consonantCluster = `(?:${gujaratiConsonant}${halant})*${gujaratiConsonant}`;
const matras = '[ાીુૂૃેૈોૌંઃ]?';
const shortIRegex = new RegExp(`(${consonantCluster})િ`, 'g');
text = text.replace(shortIRegex, '($1');

for (const mapping of mappings) {
  const mapRegex = new RegExp(mapping.from.replace(/([.*+?^=!:${}()|\[\]\/\\])/g, "\\$1"), 'g');
  text = text.replace(mapRegex, mapping.to);
}
console.log(text);
