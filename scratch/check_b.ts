import { convertText } from '../src/utils/converter.js';

function toHex(str) {
  return str.split('').map(c => c.charCodeAt(0).toString(16).padEnd(4)).join(' ');
}
console.log("Output బుూ:", toHex(convertText("బుూ", 'anu7', false, false, 'telugu').convertedText));
