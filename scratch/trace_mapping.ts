import { getMapping } from '../src/utils/mappings/index.js';
const mapping = getMapping('anu7', false);
const entry = mapping.find(e => e.from === 'ఋ');
console.log("Entry for ఋ:", entry);
