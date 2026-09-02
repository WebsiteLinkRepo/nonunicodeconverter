import { unicodeToShreeLipi } from '../src/utils/shreeLipiConverter';
import fs from 'fs';

const raw = fs.readFileSync('scratch/ULTIMATE_TEST.md', 'utf-8');
const lines = raw.split('\n').filter(l => l.trim() && !l.startsWith('#'));
const converted = lines.map(l => unicodeToShreeLipi(l));
fs.writeFileSync('scratch/converted_ultimate.json', JSON.stringify(converted, null, 2), 'utf-8');
console.log('Done converting');
