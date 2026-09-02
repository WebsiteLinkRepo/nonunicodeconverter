import { convertUnicodeToShreeLipiTelugu as conv } from '../src/utils/shreeLipiTeluguConverter.ts';
import { writeFileSync } from 'node:fs';
const set = process.argv[2];
const SETS = {
  cons: 'క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ ళ క్ష ఱ'.split(' '),
  matra: 'క కా కి కీ కు కూ కృ కె కే కై కొ కో కౌ కం కః క్'.split(' '),
  vow: 'అ ఆ ఇ ఈ ఉ ఊ ఋ ౠ ఎ ఏ ఐ ఒ ఓ ఔ'.split(' '),
};
const items = SETS[set];
writeFileSync('scratch/tel_pairs.txt', items.map(s => `${s}\t${conv(s)}`).join('\n') + '\n');
console.log(items.map(s => `${s} -> ${[...conv(s)].map(c => c.charCodeAt(0).toString(16)).join(' ')}`).join('\n'));
