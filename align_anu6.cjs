const fs = require('fs');

const inputStr = `అ ఆ ఇ ఈ ఉ ఊ ఋ ౠ ఎ ఏ ఐ ఒ ఓ ఔ అం అః
క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ ళ క్ష ఱ
క కా కి కీ కు కూ కృ కౄ కె కే కై కొ కో కౌ కం కః
క్క ఖ్ఖ గ్గ ఘ్ఘ ఙ్ఙ చ్చ ఛ్ఛ జ్జ ఝ్ఝ ఞ్ఞ ట్ట ఠ్ఠ డడ్డ ఢ్ఢ ణ్ణ త్త థ్థ ద్ద ధ్ధ న్న ప్ప ఫ్ఫ బ్బ భ్భ మ్మ య్య ర్ర ల్ల వ్వ శ్శ ష్ష స్స హ్హ ళ్ళ క్క్ష ఱ్ఱ`;

const outputStr = `J P W D L T |°° |°¶ Z U S X F B JO J—
H› Y Q® „¦¬° V KÇ KÇ [ ~¡ & @ ~”¡ _È _È } \`Ç ^ŠÎ ^Î ^Î # „¬ „¦¬ | ƒ’ =° †Ç° ~¡  = ‰× +¬ ‹¬ ‚¬ì ˆ× H›Æ Ž
H› Hê H÷ H© ä›½ ä›€ H›$ H›$ì ïH öH ïHá Hù HË HÒ H›O H›:
H›ø Yš Q®¾ „¦¬°É VV KÇó KÇó [û ~¡~¡ &ý @“ ~”¡» _È_ÈÛ _È_ }â \`Çë ^ŠÎÖ ^Îí ^Îœ #ß „¬æ „¦¬æ |Ä ƒ’Ä =°à †Ç°¼ ã~¡ Á =Þ ‰×Å +¬Â ‹¬ž ‚¬ì ˆ×¤ H›øÂ Ž]`;

const inputLines = inputStr.split('\n');
const outputLines = outputStr.split('\n');

for (let i=0; i<inputLines.length; i++) {
  const inTokens = inputLines[i].trim().split(/\s+/);
  const outTokens = outputLines[i].trim().split(/\s+/);
  
  if (inTokens.length !== outTokens.length) {
    console.log(`Line ${i} mismatch length: In ${inTokens.length}, Out ${outTokens.length}`);
    console.log("In:", inTokens);
    console.log("Out:", outTokens);
  } else {
    for (let j=0; j<inTokens.length; j++) {
      console.log(`{ from: "${outTokens[j]}", to: "${inTokens[j]}" },`);
    }
  }
}
