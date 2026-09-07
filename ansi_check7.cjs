const fs = require('fs');
const lines6 = fs.readFileSync('src/utils/mappings/anu6.ts', 'utf8').split('\n');

const finds = [
 "[\\uF048]", "[\\uF024]", "0024"
];

for(let f of finds) {
   const res = lines6.filter(l => l.includes("u"+f.substring(2,6)));
   if(res.length < 5) console.log(f, res);
   else console.log(f, res.slice(0, 5), `... (${res.length} matches)`);
}
