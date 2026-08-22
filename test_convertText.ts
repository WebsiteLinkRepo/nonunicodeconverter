import { convertText } from './src/utils/converter';
const input = "மேலும் உலகெங்கிலும்";
const res = convertText(input, "bamini", false, false, "tamil");
console.log(res.convertedText);
