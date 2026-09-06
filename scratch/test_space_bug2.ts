import { convertUnicodeToShreeLipiTelugu0908 } from '../src/utils/shreeLipiTelugu0908Converter';

const unicodeText1 = "కఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరలవశషసహళక్షఱ";
const shreeOut1 = convertUnicodeToShreeLipiTelugu0908(unicodeText1);
console.log("No spaces Shree Out:", shreeOut1.text);
