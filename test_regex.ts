const syllableRegex = /(?:(?:[\u0C05-\u0C14]|(?:[\u0C15-\u0C39\u0C58-\u0C5A](?:\u0C4D[\u0C15-\u0C39\u0C58-\u0C5A])*[\u0C3E-\u0C4C\u0C4D]?))[\u0C02\u0C03]?)/g;
const text = '\u0C15\u0C4D\u0C37\u0C2E\u0C3E'; // Ksha + Ma
const matches = text.match(syllableRegex);
console.log('Matches:', matches);
