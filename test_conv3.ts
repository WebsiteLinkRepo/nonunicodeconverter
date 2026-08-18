import { convertText } from './src/utils/converter';
const text = "ఉంది";
const res = convertText(text, 'anu7', false);
console.log(res.convertedText);
for(let i=0; i<res.convertedText.length; i++) {
    console.log(res.convertedText[i], res.convertedText.charCodeAt(i).toString(16));
}
