import { convertText } from '../src/utils/converter.js';

function toHex(str) {
  return str.split('').map(c => c.charCodeAt(0).toString(16).padEnd(4)).join(' ');
}

console.log("Output ఋ:", toHex(convertText("ఋ", 'anu7', false, false, 'telugu').convertedText));
console.log("Output ౠ:", toHex(convertText("ౠ", 'anu7', false, false, 'telugu').convertedText));
console.log("Output ఋా:", toHex(convertText("ఋా", 'anu7', false, false, 'telugu').convertedText));
console.log("Output ఋూ:", toHex(convertText("ఋూ", 'anu7', false, false, 'telugu').convertedText));
console.log("Output బు:", toHex(convertText("బు", 'anu7', false, false, 'telugu').convertedText));
console.log("Output బూ:", toHex(convertText("బూ", 'anu7', false, false, 'telugu').convertedText));

