// Emits "unicode<TAB>converted" lines for the verification renderer.
import { convertUnicodeToShreeLipiTelugu as conv } from '../src/utils/shreeLipiTeluguConverter.ts';
import { writeFileSync } from 'node:fs';

const items = [
  'అ', 'ఆ', 'ఇ', 'ఈ', 'ఉ', 'ఊ', 'ఋ', 'ౠ', 'ఎ', 'ఏ',
  'ఐ', 'ఒ', 'ఓ', 'ఔ', 'అం', 'అః',
];

writeFileSync('scratch/tel_pairs.txt',
  items.map(s => `${s}\t${conv(s)}`).join('\n') + '\n');
console.log(items.map(s => `${s} -> ${[...conv(s)].map(c => c.charCodeAt(0).toString(16)).join(' ')}`).join('\n'));
