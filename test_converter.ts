import { convertText } from './src/utils/converter.js';

const unicodeText = "ఇది ప్రధానంగా ఆంధ్రప్రదేశ్ మరియు తెలంగాణ రాష్ట్రాలలో మాట్లాడుతారు. ఈ భాషకు చక్కని సాహిత్యం, వ్యాకరణం మరియు గొప్ప చరిత్ర ఉంది.";
console.log("Unicode:", unicodeText);
const anuText = convertText(unicodeText, "anu7", false);
console.log("Anu:", anuText.convertedText);
const backToUnicode = convertText(anuText.convertedText, "anu7", true);
console.log("Back to Unicode:", backToUnicode.convertedText);


