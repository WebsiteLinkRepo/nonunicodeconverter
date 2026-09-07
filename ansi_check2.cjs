const fs = require('fs');

// Read windows-1252 mapped versions (often how Latin-1 extended characters are parsed)
const comp = fs.readFileSync('competitor_output.txt');
const compLine = comp.toString('utf8').split('\n')[1]; // website 1 (Anu 6.0 ANSI)
const website3Line = comp.toString('utf8').split('\n')[7]; // website 3 (Anu 7.0 ANSI)

const my = fs.readFileSync('my_output.txt', 'utf8');

console.log("Analyzing char mapping logic for Anu 6.0...\n");

for (let i = 0; i < 25; i++) {
   const compCode = compLine.charCodeAt(i);
   let myCode = my.charCodeAt(i); 
   let isOffset = myCode >= 0xF000;
   
   console.log(`Char ${i}: My: ${myCode.toString(16).padStart(4, '0')} (${my.charAt(i)}) -> Comp: ${compCode.toString(16).padStart(4, '0')} (${compLine.charAt(i)}) | Mapped: ${isOffset ? (myCode - 0xF000).toString(16).padStart(4, '0') : myCode.toString(16).padStart(4, '0')}`);
}
