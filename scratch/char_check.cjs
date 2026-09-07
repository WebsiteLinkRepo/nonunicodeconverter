const fs = require('fs');
const content = fs.readFileSync('src/utils/mappings/anu7.ts', 'utf-8');
const lines = content.split('\n');

for (const line of lines) {
  if (line.includes('‹')) console.log(line);
  if (line.includes('TÖ')) console.log(line);
}
