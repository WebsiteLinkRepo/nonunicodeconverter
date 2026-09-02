import { readFileSync, writeFileSync } from 'fs';
import { convertUnicodeToShreeLipiTelugu } from '../src/utils/shreeLipiTeluguConverter';

const unicodeText = readFileSync('scratch/TELUGU_COMPLEX_PARAS_INPUT.txt', 'utf-8');
const converted = convertUnicodeToShreeLipiTelugu(unicodeText);
writeFileSync('scratch/TELUGU_COMPLEX_PARAS_OUTPUT.txt', converted);
console.log('Converted Telugu complex paras saved to scratch/TELUGU_COMPLEX_PARAS_OUTPUT.txt');
