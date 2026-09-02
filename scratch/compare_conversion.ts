import { readFileSync, writeFileSync } from 'fs';
import { unicodeToShreeLipiTamil } from '../src/utils/shreeLipiTamilConverter.js';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Read the input text
const inputText = readFileSync(join(__dirname, 'TAMIL_COMPLEX_PARAS_INPUT.txt'), 'utf-8');

// Convert it with our tool
const ourOutput = unicodeToShreeLipiTamil(inputText);

// Read the competitor text
const competitorOutput = readFileSync(join(__dirname, 'TAMIL_COMPLEX_PARAS_OUTPUT.txt'), 'utf-8');

// Write out ours for direct comparison
writeFileSync(join(__dirname, 'OUR_OUTPUT.txt'), ourOutput);

console.log(`Input Length: ${inputText.length}`);
console.log(`Our Output Length: ${ourOutput.length}`);
console.log(`Competitor Output Length: ${competitorOutput.length}`);
console.log(`Are they identical? ${ourOutput === competitorOutput}`);

if (ourOutput !== competitorOutput) {
  for (let i = 0; i < Math.max(ourOutput.length, competitorOutput.length); i++) {
    if (ourOutput[i] !== competitorOutput[i]) {
      console.log(`Mismatch at index ${i}: Ours='${ourOutput[i]}', Theirs='${competitorOutput[i]}'`);
      console.log(`Context Ours:   ...${ourOutput.substring(Math.max(0, i - 10), i + 10)}...`);
      console.log(`Context Theirs: ...${competitorOutput.substring(Math.max(0, i - 10), i + 10)}...`);
      break;
    }
  }
}
