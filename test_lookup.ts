import { getMapping } from './src/utils/mappings/index';

const map = getMapping('krutidev', false);
const lookupMap: Record<string, string> = {};
for (const entry of map) {
  if (entry.from) {
    lookupMap[entry.from] = entry.to;
  }
}

const key = '\u0C15\u0C4D\u0C37';
console.log('Lookup Map keys containing U+0C15:', Object.keys(lookupMap).filter(k => k.includes('\u0C15')));
console.log('Value for Ksha:', lookupMap[key]);
