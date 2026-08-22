import { BAMINI_TAMIL_UNICODE_TO_NONUNICODE } from './src/utils/mappings/baminiTamil';
const lu = BAMINI_TAMIL_UNICODE_TO_NONUNICODE.find(x => x.to === 'Y');
const la = BAMINI_TAMIL_UNICODE_TO_NONUNICODE.find(x => x.to === 'y');
console.log("lu from:", lu?.from.split('').map(c => c.charCodeAt(0).toString(16)));
console.log("la from:", la?.from.split('').map(c => c.charCodeAt(0).toString(16)));
