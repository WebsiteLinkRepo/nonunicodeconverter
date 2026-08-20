let resultText = "\u0C38\u0C3E\u0C4D\u0C35\u0C24\u0C02\u0C4D\u0C30\u0C24\u0C4D\u0C2F\u0C02"; 
console.log("Input:", resultText);

// Move Raa Vatthu
resultText = resultText.replace(/(\u0C4D\u0C30)([\u0C15-\u0C39\u0C58-\u0C5A][\u0C3E-\u0C4C]*(?:\u0C4D[\u0C15-\u0C39\u0C58-\u0C5A])*)/g, '$2$1');
console.log("After move:", resultText);

// Post-reordering 2
resultText = resultText.replace(
  /([\u0C15-\u0C39\u0C58-\u0C5A])([\u0C3E-\u0C4C])((?:\u0C4D[\u0C15-\u0C39\u0C58-\u0C5A])+)/g,
  '$1$3$2'
);
console.log("After vowel reorder:", resultText);
