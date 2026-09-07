import { unicodeToAnu6 } from './src/utils/anu6Converter';

const input = "కౄరమృగము ౠషి 'కోట్'";
const anu6 = unicodeToAnu6(input);

const comp = "H›$ì~¡=°$Q®=ò |°¶+² 'HË\˜Ñ";

console.log("My Hex:");
console.log(Array.from(anu6).map(c => c.charCodeAt(0).toString(16).padStart(4, '0')).join(' '));
console.log("Comp Hex:");
console.log(Array.from(comp).map(c => c.charCodeAt(0).toString(16).padStart(4, '0')).join(' '));

