import { convertUnicodeToShreeLipiTelugu0908 } from '../src/utils/shreeLipiTelugu0908Converter';
const input = "క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట";
const out = convertUnicodeToShreeLipiTelugu0908(input).text;
console.log(JSON.stringify(out));
