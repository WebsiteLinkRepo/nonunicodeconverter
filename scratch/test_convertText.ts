import { convertText } from '../src/utils/converter';
const unicodeText = "క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట";
const res = convertText(unicodeText, 'shreelipi', false, false, 'telugu');
console.log(JSON.stringify(res.convertedText));
