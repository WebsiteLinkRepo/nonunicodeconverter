const fs = require('fs');
const comp = fs.readFileSync('competitor_output.txt', 'utf8').split('\n')[1]; // Line 2 has website 1's output
const my = fs.readFileSync('my_output.txt', 'utf8');

console.log("Competitor char codes (first 10):", Array.from(comp).slice(0, 10).map(c => c.charCodeAt(0).toString(16)));
console.log("My char codes (first 10):", Array.from(my).slice(0, 10).map(c => c.charCodeAt(0).toString(16)));

// Let's see if My output maps exactly to competitor output by subtracting 
const diff = Array.from(my).slice(0, 10).map(c => {
  const code = c.charCodeAt(0);
  return code >= 0xF000 ? code - 0xF000 : code;
});
console.log("My diff:", diff.map(x => x.toString(16)));
