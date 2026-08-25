import { convertText } from './src/utils/converter';
import fs from 'fs';

const text = fs.readFileSync('telugu_all_combinations.txt', 'utf8');
const result = convertText(text, 'anu7');
if (result.errors.length > 0) {
    console.log(`Found ${result.errors.length} errors.`);
    // print unique error characters
    const uniqueChars = new Set(result.errors.map(e => e.char));
    console.log("Unmapped chars:", Array.from(uniqueChars).join(", "));
} else {
    console.log("No errors found!");
}
