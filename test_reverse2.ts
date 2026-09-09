import { convertText } from './src/utils/converter';
const text = "అందరికీ నమస్కారం. తెలుగు భాష చాలా అద్భుతమైనది.";
const res1 = convertText(text, 'anu7', false, false, 'telugu');
const res2 = convertText(res1.convertedText, 'anu7', true, false, 'telugu');

const out = res2.convertedText;
for (let i=0; i<out.length; i++) {
  console.log(out[i], out.charCodeAt(i).toString(16));
}
