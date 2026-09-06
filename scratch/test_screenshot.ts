import { convertUnicodeToShreeLipiTelugu0908 } from '../src/utils/shreeLipiTelugu0908Converter.ts';
const input = "క ఖ గ ఘ జ చ ఛ జ ఝ ఇ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ ళ క్ష అ";
const legacy = convertUnicodeToShreeLipiTelugu0908(input).text;
console.log("Legacy:", legacy);
