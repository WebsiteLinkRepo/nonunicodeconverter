import { convertText } from '../src/utils/converter.js';

const forward = convertText("ఋా", 'anu7', false, false, 'telugu').convertedText;
console.log("Forward ఋా -> anu7:", [...forward].map(c => c.charCodeAt(0).toString(16)).join(' '));
const reverse = convertText(forward, 'anu7', true, false, 'telugu').convertedText;
console.log("Reverse anu7 -> telugu:", reverse, "Expected: ౠ");
