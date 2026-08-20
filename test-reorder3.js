let resultText = "\u0C4D\u0C30\u0C38\u0C40\u0C4D\u0C24"; // ్రసీ్త
console.log("Input:", resultText);

// Move Raa Vatthu just after the base consonant
resultText = resultText.replace(/(\u0C4D\u0C30)([\u0C15-\u0C39\u0C58-\u0C5A])/g, '$2$1');
console.log("After move:", resultText);

// Post-reordering 2
resultText = resultText.replace(
  /([\u0C15-\u0C39\u0C58-\u0C5A])([\u0C3E-\u0C4C])((?:\u0C4D[\u0C15-\u0C39\u0C58-\u0C5A])+)/g,
  '$1$3$2'
);
console.log("After vowel reorder:", resultText);
