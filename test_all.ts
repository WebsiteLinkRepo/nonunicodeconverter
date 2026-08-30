import { unicodeToKrutidev } from './src/utils/krutiDevConverter.js';
import { unicodeToAnuNeo } from './src/utils/anuNeoConverter.js';
import { unicodeToAnu6 } from './src/utils/anu6Converter.js';
console.log("Krutidev:", unicodeToKrutidev("अर्धवर्णों"));
console.log("AnuNeo:", unicodeToAnuNeo("अर्धवर्णों"));
console.log("Anu6:", unicodeToAnu6("अर्धवर्णों"));
