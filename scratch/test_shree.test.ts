import { expect, test } from 'vitest';
import { convertUnicodeToShreeLipiTelugu0908, convertShreeLipiTelugu0908ToUnicode } from '../src/utils/shreeLipiTelugu0908Converter';

test('converter', () => {
  const input = 'క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట';
  const result = convertUnicodeToShreeLipiTelugu0908(input);
  console.log('Result:', JSON.stringify(result.text));
  console.log('Hex dump:', result.text.split('').map(c => c.charCodeAt(0).toString(16).padStart(4, '0')).join(' '));
  expect(result.text).toBeDefined();
});
