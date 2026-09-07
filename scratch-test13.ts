import { convertText } from './src/utils/converter';

const res = convertText("జ్క", 'anu7', false); // should trigger fallback (jka)
console.log("Raw output:", res.convertedText);
for (let i = 0; i < res.convertedText.length; i++) {
    console.log(res.convertedText[i], res.convertedText.charCodeAt(i).toString(16));
}
