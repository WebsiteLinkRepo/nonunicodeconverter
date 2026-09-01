
import { convertText } from './src/utils/converter';
import * as fs from 'fs';

const tamilText = fs.readFileSync('all_tamil_combinations.txt', 'utf8').split('\n');
const results = tamilText.map(t => {
    if (!t) return '';
    const res = convertText(t, 'bamini', false, false, 'tamil');
    return t + " -> " + res.convertedText;
});
fs.writeFileSync('bamini_test_results.txt', results.join('\n'), 'utf8');
