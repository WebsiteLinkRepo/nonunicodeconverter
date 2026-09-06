import { convertShreeLipiTelugu0908ToUnicode } from '../src/utils/shreeLipiTelugu0908Converter';
const legacyText = "M\u00E6 Q V\u00E6 \u0153\u00E8 \\ ^\u00E6 b\u00E6 f m p r";
const result = convertShreeLipiTelugu0908ToUnicode(legacyText);
console.log("Input:", legacyText);
console.log("Output text:", result.text);
console.log("Expected: క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట");
