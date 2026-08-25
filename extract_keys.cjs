const fs = require('fs');
const anu7Content = fs.readFileSync('src/utils/mappings/anu7.ts', 'utf8');

const regex = /{ from: "(.*?)", to: "(.*?)" }/g;
let match;
const words = [];

while ((match = regex.exec(anu7Content)) !== null) {
  words.push(match[1]);
}

fs.writeFileSync('telugu_all_combinations.txt', words.join('\n'));
console.log(`Extracted ${words.length} combinations.`);
