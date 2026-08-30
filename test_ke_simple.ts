import { unicodeToAnuNeo } from './src/utils/anuNeoConverter.ts';

const result = unicodeToAnuNeo('के');
console.log('Input: के');
console.log('Output:', result);
console.log('Length:', result.length);
console.log('Hex:', Array.from(result).map(c => '0x' + c.charCodeAt(0).toString(16).toUpperCase()).join(' '));

// Show each character
for (let i = 0; i < result.length; i++) {
  const char = result[i];
  const code = char.charCodeAt(0);
  console.log(`[${i}] U+${code.toString(16).toUpperCase().padStart(4, '0')} = '${char}'`);
}
