const fs = require('fs');

const telugu = fs.readFileSync('input_telugu2.txt', 'utf8').trim();
// కౄరమృగము ౠషి 'కోట్'
// క (ka) + ౄ (vocalic rr) + ర (ra) + మ (ma) + ృ (vocalic r) + గ (ga) + ము (mu)
// ౠ (vocalic RR) + షి (shi)
// 'కోట్' ('kot')

console.log("Analyzing char mapping logic for Anu 6.0...\n");
console.log("Input: ", telugu);
for(let i=0; i<telugu.length; i++) {
   console.log(telugu[i], telugu.charCodeAt(i).toString(16));
}
