import { convertText } from './src/utils/converter';

const hindiStr = 'हिंदी';
console.log('Input:', hindiStr);

const res1 = convertText(hindiStr, 'anu7', false, false, 'hindi');
console.log('Forward Anu7 Output:', res1.convertedText);

const res2 = convertText(res1.convertedText, 'anu7', true, false, 'hindi');
console.log('Reverse to Hindi Output:', res2.convertedText);
console.log('Match?', res2.convertedText === hindiStr);
