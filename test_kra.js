const { neoMap } = require('./src/utils/mappings/neo.ts');
const text = 'क्र';
console.log('Text characters:', [...text].map(c => c.charCodeAt(0).toString(16)));
console.log('Map has key:', neoMap.hasOwnProperty(text));
