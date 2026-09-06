import { expect, test } from 'vitest';
import { convertUnicodeToShreeLipiTelugu0908, convertShreeLipiTelugu0908ToUnicode } from '../src/utils/shreeLipiTelugu0908Converter';

// I need to print the REVERSE_INDEX to see if it contains spaces
import * as fs from 'fs';
const fileContent = fs.readFileSync('src/utils/shreeLipiTelugu0908Converter.ts', 'utf-8');
console.log('REVERSE has space?', fileContent.includes("' '") || fileContent.includes('" "'));

