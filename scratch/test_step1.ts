import { convertUnicodeToShreeLipiTelugu } from '../src/utils/shreeLipiTeluguConverter.js';
import * as fs from 'fs';

const input = 'అ ఆ ఇ ఈ ఉ ఊ ఋ ౠ ఎ ఏ ఐ ఒ ఓ ఔ అం అః';
const output = convertUnicodeToShreeLipiTelugu(input);

console.log('Unicode:', input);
console.log('Shree-Lipi:', output);

// Save string to text file
fs.writeFileSync('scratch/step1_out.txt', output);
