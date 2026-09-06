import { convertUnicodeToShreeLipiTelugu0908, convertShreeLipiTelugu0908ToUnicode } from '../src/utils/shreeLipiTelugu0908Converter';

const unicodeText = "క ఖ గ ఘ జ చ ఛ జ ఝ ఇ ట ర డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ ళ క్ష ఱ";
const shreeOut = convertUnicodeToShreeLipiTelugu0908(unicodeText);
console.log("Shree Out:", shreeOut.text);

const roundtrip = convertShreeLipiTelugu0908ToUnicode(shreeOut.text);
console.log("Roundtrip text:", roundtrip.text);
console.log("Lossless?", roundtrip.text === unicodeText);
