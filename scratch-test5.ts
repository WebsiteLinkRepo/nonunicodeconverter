import { getMapping } from './src/utils/mappings/index';
const anu7 = getMapping("anu7", false);

console.log( anu7.find(e => e.from === "్్య") );
console.log( anu7.find(e => e.from === "్న") );
console.log( anu7.find(e => e.from === "్మ") );
console.log( anu7.find(e => e.from === "్ల") );
console.log( anu7.find(e => e.from === "్వ") );

