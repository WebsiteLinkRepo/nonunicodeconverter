
import { convertText } from './src/utils/converter';

const testTamil = "தமிழ் மொழி உலகின் மிகப் பழமையான மற்றும் மிகவும் சிறப்பு வாய்ந்த செம்மொழிகளுள் ஒன்றாகும்.";

console.log("=== TAMIL with Anu 7.0 ===");
const resAnu = convertText(testTamil, 'anu7', false, false, 'tamil');
console.log("Converted Anu 7.0:", resAnu.convertedText);
console.log("Errors:", resAnu.errors);

console.log("\n=== TAMIL with Bamini ===");
const resBamini = convertText(testTamil, 'bamini', false, false, 'tamil');
console.log("Converted Bamini:", resBamini.convertedText);
console.log("Errors:", resBamini.errors);
