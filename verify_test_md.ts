import { unicodeToAnuNeo } from './src/utils/anuNeoConverter.ts';
import fs from 'fs';

const content = fs.readFileSync('HINDI_CONVERSION_TEST.md', 'utf8');
const sections = content.split(/^## /m).slice(1);

let total = 0;
let passed = 0;

for (const sec of sections) {
  const lines = sec.split('\n');
  const title = lines[0].trim();
  const rawSec = lines.slice(1).join('\n');
  const inputParts = rawSec.split('**Unicode Input:**\n```\n');
  if (inputParts.length < 2) continue;
  const input = inputParts[1].split('```')[0].trim();

  const outputParts = rawSec.split('**Non-Unicode (Anu Neo) Output:**\n```\n');
  if (outputParts.length < 2) continue;
  const expected = outputParts[1].split('```')[0].trim();

  total++;
  const actual = unicodeToAnuNeo(input).trim();
  if (actual === expected) {
    console.log('PASS:', title);
    passed++;
  } else {
    console.log('FAIL:', title);
    console.log('  Expected:', expected);
    console.log('  Actual:  ', actual);
  }
}
console.log(`Summary: ${passed}/${total} passed`);
