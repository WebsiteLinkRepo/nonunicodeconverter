const fs = require('fs');
const content = fs.readFileSync('src/utils/mappings/anu7.ts', 'utf-8');
const lines = content.split('\n');

const mappedTo = [
  '‹', 'T', 'Ö', '<', 'య', 'ా', 'ూ', 'బ'
];

for (const line of lines) {
  if (line.includes('‹TÖ')) {
    console.log("Found ‹TÖ:", line);
  }
}
