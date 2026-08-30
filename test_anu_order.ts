import { unicodeToAnuNeo } from './src/utils/anuNeoConverter.ts';

console.log('कं:', Array.from(unicodeToAnuNeo('कं')).map(c => '0x' + c.charCodeAt(0).toString(16).toUpperCase()).join(' '));
console.log('कः:', Array.from(unicodeToAnuNeo('कः')).map(c => '0x' + c.charCodeAt(0).toString(16).toUpperCase()).join(' '));
console.log('कँ:', Array.from(unicodeToAnuNeo('कँ')).map(c => '0x' + c.charCodeAt(0).toString(16).toUpperCase()).join(' '));
