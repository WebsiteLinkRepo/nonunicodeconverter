let resultText = "\u0C4D\u0C30\u0C38\u0C40\u0C4D\u0C24"; // ్రసీ్త (çdÓï)
let resultText2 = "\u0C4D\u0C30\u0C24\u0C4D\u0C2F\u0C02"; // ్రత్యం (çÔá«+)

function fixVattus(text) {
  // Move Raa Vattu to the end of the consonant cluster, but BEFORE Ya Vattu
  // First, move Raa Vattu to the very end of the cluster
  text = text.replace(/(\u0C4D\u0C30)([\u0C15-\u0C39\u0C58-\u0C5A][\u0C3E-\u0C4C]*(?:\u0C4D[\u0C15-\u0C39\u0C58-\u0C5A])*)/g, '$2$1');
  
  // Then, if Raa Vattu is followed by Ya Vattu, swap them!
  // Wait, if Raa Vattu was moved to the end, it is AFTER Ya Vattu now.
  // We need to swap them back so Ya Vattu is last.
  text = text.replace(/(\u0C4D\u0C2F)(\u0C4D\u0C30)/g, '$2$1');
  
  // Post-reordering 2
  text = text.replace(
    /([\u0C15-\u0C39\u0C58-\u0C5A])([\u0C3E-\u0C4C])((?:\u0C4D[\u0C15-\u0C39\u0C58-\u0C5A])+)/g,
    '$1$3$2'
  );
  return text;
}

console.log("Stree:", fixVattus(resultText));
console.log("Tryam:", fixVattus(resultText2));
