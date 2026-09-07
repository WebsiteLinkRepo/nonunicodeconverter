import fs from 'fs';
import { unicodeToAnu6 } from './src/utils/anu6Converter';

const input = fs.readFileSync('input_telugu.txt', 'utf8');
const output = unicodeToAnu6(input);
fs.writeFileSync('my_output.txt', output);
