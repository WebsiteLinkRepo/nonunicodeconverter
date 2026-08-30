import { unicodeToAnuNeo } from './src/utils/anuNeoConverter.ts';

const testCases = [
  'क',
  'के',
  'खे',
  'गे',
];

console.log('Debugging ke conversion:\n');

for (const input of testCases) {
  const result = unicodeToAnuNeo(input);

  console.log(`Input: "${input}"`);
  console.log(`Output: ${Array.from(result).map(c => '0x' + c.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0')).join(' ')}`);
  console.log(`Chars: ${Array.from(result).map(c => `U+${c.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0')}`).join(' ')}`);

  // Also show ASCII representation
  const ascii = Array.from(result).map(c => {
    const code = c.charCodeAt(0);
    if (code >= 0xF000 && code <= 0xF0FF) {
      // Convert PUA to Latin approximate
      const latin = String.fromCharCode(code - 0xF000 + 0x40);
      return `'${latin}' (0x${latin.charCodeAt(0).toString(16).toUpperCase()})`;
    }
    return c;
  }).join(' ');

  console.log(`ASCII: ${ascii}`);
  console.log('');
}
