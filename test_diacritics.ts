import { unicodeToAnuNeo } from './src/utils/anuNeoConverter';

// Test diacritical marks
const tests = [
  { label: 'कं (ka + anusvara)', input: 'कं' },
  { label: 'कः (ka + visarga)', input: 'कः' },
  { label: 'कँ (ka + chandrabindu)', input: 'कँ' },
  { label: 'नमस्ते', input: 'नमस्ते' },
  { label: 'चाँद', input: 'चाँद' },
  { label: 'हिंदी', input: 'हिंदी' },
];

console.log('Testing diacritical marks conversion:\n');

tests.forEach(({ label, input }) => {
  const output = unicodeToAnuNeo(input);

  // Show hex codes
  const inputHex = Array.from(input).map(c =>
    `U+${c.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0')}`
  ).join(' ');

  const outputHex = Array.from(output).map(c =>
    `U+${c.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0')}`
  ).join(' ');

  console.log(`${label}:`);
  console.log(`  Input:  ${input}`);
  console.log(`  Input hex:  ${inputHex}`);
  console.log(`  Output: ${output}`);
  console.log(`  Output hex: ${outputHex}`);
  console.log();
});
