const fs = require('fs');

const comp = fs.readFileSync('competitor_output2.txt');
const website1Line = comp.toString('utf8').split('\n')[1]; // website 1
const website3Line = comp.toString('utf8').split('\n')[8]; // website 3

console.log("Analyzing char mapping logic for Anu 6.0...\n");

for (let i = 0; i < website1Line.length; i++) {
   const compCode = website1Line.charCodeAt(i);
   console.log(`Char ${i}: ASCII: ${compCode.toString(16).padStart(4, '0')} (${website1Line.charAt(i)})`);
}
