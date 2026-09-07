const fs = require('fs');
const comp = fs.readFileSync('competitor_output.txt', 'utf8').split('\n')[1]; // Line 2 has website 1's output
const my = fs.readFileSync('my_output.txt', 'utf8');

console.log("Competitor char codes (first 25):");
console.log(Array.from(comp).slice(0, 25).map(c => ({ char: c, hex: c.charCodeAt(0).toString(16) })));

console.log("My char codes (first 25):");
console.log(Array.from(my).slice(0, 25).map(c => ({ char: c, hex: c.charCodeAt(0).toString(16) })));

let isOffsetExactlyF000 = true;
// Check the private use area offset issue
for (let i = 0; i < Math.min(comp.length, my.length); i++) {
   const compCode = comp.charCodeAt(i);
   let myCode = my.charCodeAt(i);
   if (myCode >= 0xF000) myCode -= 0xF000;
   
   if (compCode !== myCode && compCode !== my.charCodeAt(i)) { // Sometimes ASCII space is same
       console.log(`Mismatch at index ${i}: comp=${comp.charAt(i)}(${compCode.toString(16)}) my=${my.charAt(i)}(${my.charCodeAt(i).toString(16)}) -> mapped=${myCode.toString(16)}`);
       isOffsetExactlyF000 = false;
       break;
   }
}
console.log("Is it exactly an F000 offset difference overall?", isOffsetExactlyF000);
