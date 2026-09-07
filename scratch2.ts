import { convertText } from './src/utils/converter';

const input = "అనంతలక్ష్మి బు ౠ బ బూ ఋ";
const fwd = convertText(input, "anu7", false).convertedText;
console.log("Fwd: ", fwd);
console.log("Expected Fwd:      ");

const rev = convertText(fwd, "anu7", true).convertedText;
console.log("Rev: ", rev);
console.log("Expected Rev:", input);
