import { convertText } from './src/utils/converter.ts';
const te = "అందరికీ నమస్కారం. తెలుగు భాష చాలా అద్భుతమైనది.";
const forward = convertText(te, "anu7", false, false, "telugu");
console.log("Forward output (ASCII):", forward.convertedText);
const back = convertText(forward.convertedText, "anu7", true, false, "telugu");
console.log("Reverse output (Unicode):", back.convertedText);
