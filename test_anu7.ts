import { convertText } from "./src/utils/converter";

const txt = "అనంతలక్ష్మి ఋ ౠ";
const result = convertText(txt, "anu7", false, "telugu");
const reversed = convertText(result.convertedText, "anu7", true, "telugu");

console.log("Input:", txt);
console.log("Output:", result.convertedText);
console.log("Reversed:", reversed.convertedText);
console.log("Matches:", txt === reversed.convertedText);
