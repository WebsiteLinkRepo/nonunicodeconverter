import { convertText } from '../src/utils/converter';

console.log("Kruti Dev:", convertText("नमस्ते", "krutidev", false, false, "hindi").convertedText);
console.log("Bamini Tamil:", convertText("தமிழ்", "bamini", false, false, "tamil").convertedText);
console.log("Anu Telugu:", convertText("నమస్తే", "anu7", false, false, "telugu").convertedText);

