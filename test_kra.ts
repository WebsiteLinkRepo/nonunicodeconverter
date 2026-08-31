import { neoMap } from './src/utils/mappings/neo';
const text = 'क्र';
console.log('Text characters:', [...text].map(c => c.charCodeAt(0).toString(16)));
console.log('Map key exist:', neoMap.hasOwnProperty(text));
console.log('Map value for 크:', neoMap['क्र']);
