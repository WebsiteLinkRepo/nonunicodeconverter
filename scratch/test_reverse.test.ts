import { expect, test } from 'vitest';
import { convertUnicodeToShreeLipiTelugu0908, convertShreeLipiTelugu0908ToUnicode } from '../src/utils/shreeLipiTelugu0908Converter';

test('reverse converter', () => {
  const inputUnicode = 'క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ ళ క్ష ఱ';
  const legacy = convertUnicodeToShreeLipiTelugu0908(inputUnicode).text;
  const result = convertShreeLipiTelugu0908ToUnicode(legacy);
  console.log('Result:', JSON.stringify(result.text));
});
