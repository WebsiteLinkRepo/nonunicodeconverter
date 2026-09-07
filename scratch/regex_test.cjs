const regex = /(?:(?:[అ-ఔౠౡ][ా-ౌ]?|(?:[క-హౘ-ౚ](?:్[క-హౘ-ౚ])*[ా-ౌ్]?))[ంః]?)/g;
console.log("ఋ".match(regex));
console.log("ౠ".match(regex));
console.log("ఋా".match(regex));
