import { convertUnicodeToShreeLipiTelugu0908 } from './src/utils/shreeLipiTelugu0908Converter';
const input = 'క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ ళ క్ష ఱ';
const legacy = convertUnicodeToShreeLipiTelugu0908(input).text;
for (let i=0; i<legacy.length; i++) {
  console.log(legacy[i], legacy.charCodeAt(i).toString(16));
}
