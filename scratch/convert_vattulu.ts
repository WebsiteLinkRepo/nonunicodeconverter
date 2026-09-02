import { readFileSync, writeFileSync } from 'fs';
import { convertUnicodeToShreeLipiTelugu } from '../src/utils/shreeLipiTeluguConverter';

const input = readFileSync('scratch/vattulu_input.txt', 'utf-8');
const lines = input.split('\n');
const results = lines.map(line => {
  const converted = convertUnicodeToShreeLipiTelugu(line);
  return `${line}\t${converted}`;
});

writeFileSync('scratch/vattulu_output.txt', results.join('\n'));
console.log('Saved scratch/vattulu_output.txt');
