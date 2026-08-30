import { readFileSync } from 'fs';

const content = readFileSync('/home/samuelvictor/unicode2nonunicode.com/src/utils/krutiDevConverter.ts', 'utf-8');

const u2k = content.split('function unicodeToKrutidev')[1];
const arr1Str = u2k.split('const array_one = [')[1].split('];')[0];
const arr2Str = u2k.split('const array_two = [')[1].split('];')[0];

const arr1 = eval(`[${arr1Str}]`);
const arr2 = eval(`[${arr2Str}]`);

if (arr1.length !== arr2.length) {
    console.log(`Length mismatch: ${arr1.length} vs ${arr2.length}`);
} else {
    for (let i=0; i<arr1.length; i++) {
        console.log(`${i}: ${arr1[i]} -> ${arr2[i]}`);
    }
}
