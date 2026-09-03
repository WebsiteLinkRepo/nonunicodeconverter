import { convertUnicodeToShreeLipiTelugu } from '../src/utils/shreeLipiTeluguConverter.ts';

// Test the complete consonant row from the input screenshot
const testInput = 'క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల ళ వ శ ష స హ క్ష';

console.log('Input (Unicode Telugu):');
console.log(testInput);
console.log('\nOutput (Shree-Lipi codes):');
const output = convertUnicodeToShreeLipiTelugu(testInput);
console.log(output);

// Show hex codes for debugging
console.log('\nHex breakdown:');
for (let i = 0; i < output.length; i++) {
  const char = output[i];
  const code = char.charCodeAt(0);
  if (char !== ' ') {
    console.log(`Position ${i}: '${char}' = 0x${code.toString(16).toUpperCase().padStart(2, '0')}`);
  }
}
