const input = "Telugu: ౦౧౨౩౪౫౬౭౮౯ Tamil: ௦௧௨௩௪௫௬௭௮௯ Kannada: ೦೧೨೩೪೫೬೭೮೯ Malayalam: ൦൧൨൩൪൫൬൭൮൯ Hindi: ०१२३४५६७८९";
const processedInput = input
    .replace(/[\u0C66-\u0C6F]/g, match => String(match.charCodeAt(0) - 0x0C66))
    .replace(/[\u0BE6-\u0BEF]/g, match => String(match.charCodeAt(0) - 0x0BE6))
    .replace(/[\u0CE6-\u0CEF]/g, match => String(match.charCodeAt(0) - 0x0CE6))
    .replace(/[\u0D66-\u0D6F]/g, match => String(match.charCodeAt(0) - 0x0D66));
console.log(processedInput);
