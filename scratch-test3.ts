import { getMapping } from './src/utils/mappings/index';
const anu7 = getMapping("anu7", false);

console.log( anu7.find(e => e.from === "డగ్గ") );
console.log( anu7.find(e => e.from === "గ్ని") );
console.log( anu7.find(e => e.from === "క్ష్మి") );
console.log( anu7.find(e => e.from === "క్మి") );
console.log( anu7.find(e => e.to === String.fromCharCode(0xF0BF, 0xF0A3, 0xF0D8)) );
