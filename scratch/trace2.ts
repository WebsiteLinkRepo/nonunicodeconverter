import { unicodeToKrutidev } from '../src/utils/krutiDevConverter.ts';
console.log(unicodeToKrutidev("क्ष त्र ज्ञ श्र").split("").map(c => c.charCodeAt(0)));
console.log(unicodeToKrutidev("क्ख च्छ त्त द्ध द्य द्व").split("").map(c => c.charCodeAt(0)));
