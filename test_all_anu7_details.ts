import { convertText } from './src/utils/converter';
import fs from 'fs';

const text = fs.readFileSync('telugu_all_combinations.txt', 'utf8').split('\n');
for (const line of text) {
    if (line.trim().length === 0) continue;
    const result = convertText(line, 'anu7');
    if (result.errors.length > 0) {
        console.log(`Failed on input: '${line}'`);
    }
}
