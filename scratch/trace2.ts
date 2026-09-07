import { convertText } from '../src/utils/converter.js';

console.log("convertText ఋ:", convertText("ఋ", 'anu7', false, false, "telugu").convertedText.split('').map(c => c.charCodeAt(0).toString(16)).join(' '));
