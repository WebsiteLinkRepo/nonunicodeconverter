
import { unicodeToShreeLipi } from "./src/utils/shreeLipiConverter";
const words = ["भस्म", "मंत्र", "मुक्त", "कमल", "नमस्ते", "माता", "मित्र", "त्र्यंबकेश्वर"];
for (const w of words) {
    const r = unicodeToShreeLipi(w);
    const hex = [...r].map(c => c.charCodeAt(0).toString(16).padStart(2, '0')).join(' ');
    console.log(w + " -> " + r + " | hex: " + hex);
}
