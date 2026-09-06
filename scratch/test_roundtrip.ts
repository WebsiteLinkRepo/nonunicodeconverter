import { convertUnicodeToShreeLipiTelugu0908, convertShreeLipiTelugu0908ToUnicode } from '../src/utils/shreeLipiTelugu0908Converter';
const expected = "క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ ళ క్ష ఱ";
const legacy = convertUnicodeToShreeLipiTelugu0908(expected).text;
const decoded = convertShreeLipiTelugu0908ToUnicode(legacy).text;
console.log("Expected:", expected);
console.log("Legacy:", legacy);
console.log("Decoded :", decoded);
