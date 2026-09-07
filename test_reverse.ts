import { getMapping } from './src/utils/mappings/index';

const reverseAnu7 = getMapping("anu7", true);
const matches = reverseAnu7.filter(e => e.from === '' || e.from.includes('') || e.to === 'బు' || e.to === 'ఋ');
console.log(matches);
