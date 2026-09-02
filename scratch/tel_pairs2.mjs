import { convertUnicodeToShreeLipiTelugu as conv } from '../src/utils/shreeLipiTeluguConverter.ts';
import { writeFileSync } from 'node:fs';
const items = 'క ఠ ఢ ర ళ క్ష క్ష్మ కి కా'.split(' ');
writeFileSync('scratch/tel_pairs.txt', items.map(s => `${s}\t${conv(s)}`).join('\n') + '\n');
console.log(items.map(s => `${s} -> ${[...conv(s)].map(c=>c.charCodeAt(0).toString(16)).join(' ')}`).join('\n'));
