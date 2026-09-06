import { convertUnicodeToShreeLipiTelugu0908, convertShreeLipiTelugu0908ToUnicode } from './src/utils/shreeLipiTelugu0908Converter';

const input = 'క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ ళ క్ష ఱ';
console.log('forward:', convertUnicodeToShreeLipiTelugu0908(input).text);
console.log('reverse:', convertShreeLipiTelugu0908ToUnicode(input).text);
