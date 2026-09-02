import { convertUnicodeToShreeLipiTelugu as conv } from '../src/utils/shreeLipiTeluguConverter.ts';
import { readFileSync, writeFileSync } from 'node:fs';
const inp = readFileSync(process.argv[2], 'utf8');
writeFileSync(process.argv[3], inp.split('\n').map(l => conv(l)).join('\n'));
