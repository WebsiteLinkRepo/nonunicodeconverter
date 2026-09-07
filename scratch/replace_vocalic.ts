let input = "ఋా ఋూ ఌా";
input = input
  .replace(/ఋ[ాూ]/g, "ౠ")
  .replace(/ఌ[ాూ]/g, "ౡ");
console.log(input);
