import { unicodeToAnuNeo } from './src/utils/anuNeoConverter';
console.log("पा -> " + unicodeToAnuNeo("पा").split('').map(c => (c.charCodeAt(0) - 0xF000).toString(16)).join(' '));
console.log("प्रा -> " + unicodeToAnuNeo("प्रा").split('').map(c => (c.charCodeAt(0) - 0xF000).toString(16)).join(' '));
