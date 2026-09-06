import { convertUnicodeToShreeLipiTelugu0908 } from '../src/utils/shreeLipiTelugu0908Converter';

const input = 'క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట';
const result = convertUnicodeToShreeLipiTelugu0908(input);
console.log('Result:', JSON.stringify(result.text));
console.log('Hex dump:', result.text.split('').map(c => c.charCodeAt(0).toString(16).padStart(4, '0')).join(' '));
