function convert(text) {
    let processedText = text;
    const narrowMatras = '\uF0EC\uF0EE\uF077\uF0E6\uF0E5\uF07D\uF024\uF03A';
    const bridgeRegex = new RegExp(`([\uF04E\uF0A2][${narrowMatras}]*)(?![\uF07E\uF0FE])`, 'g');
    processedText = processedText.replace(bridgeRegex, '$1\uF0FE');
    return processedText;
}

// Test N (F04E) -> Nþ (F04E F0FE)
let t1 = '\uF04E';
// Test Ny (F04E F079) -> Nþy (F04E F0FE F079)
let t2 = '\uF04E\uF079';
// Test Nç (F04E F0E7) -> Nþç (F04E F0FE F0E7)
let t3 = '\uF04E\uF0E7';
// Test with existing bridge Nþy -> Nþy (no change)
let t4 = '\uF04E\uF0FE\uF079';
// Test with halant N~ (F04E F07E) -> N~ (no change)
let t5 = '\uF04E\uF07E';
// Test with narrow matra N+narrow -> N+narrow+þ
let t6 = '\uF04E\uF0EE';

console.log("t1:", [...convert(t1)].map(c=>c.charCodeAt(0).toString(16)).join(' '));
console.log("t2:", [...convert(t2)].map(c=>c.charCodeAt(0).toString(16)).join(' '));
console.log("t3:", [...convert(t3)].map(c=>c.charCodeAt(0).toString(16)).join(' '));
console.log("t4:", [...convert(t4)].map(c=>c.charCodeAt(0).toString(16)).join(' '));
console.log("t5:", [...convert(t5)].map(c=>c.charCodeAt(0).toString(16)).join(' '));
console.log("t6:", [...convert(t6)].map(c=>c.charCodeAt(0).toString(16)).join(' '));
