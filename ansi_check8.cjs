const fs = require('fs');

const comp = fs.readFileSync('competitor_output2.txt');
const website1Line = comp.toString('utf8').split('\n')[1]; // website 1
const website1LineLength = website1Line.length;

let str1 = "";
for (let i = 0; i < website1LineLength; i++) {
   const compCode = website1Line.charCodeAt(i);
   str1 += website1Line[i] + "(" + compCode.toString(16) + ") ";
}

console.log(str1);
