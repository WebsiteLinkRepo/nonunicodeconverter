import fs from 'fs';
import { unicodeToShreeLipi } from '../src/utils/shreeLipiConverter';

// 1. Check Ultimate Test
console.log("=== RUNNING ULTIMATE TEST VERIFICATION IN TS ===");
const rawUltimateInput = fs.readFileSync('scratch/ULTIMATE_TEST.md', 'utf-8');
const ultimateLines = rawUltimateInput.split('\n').filter(l => !l.startsWith('#') && l.trim());
const ultimateInput = ultimateLines.join('\n\n');
const expectedUltimate = fs.readFileSync('scratch/ULTIMATE_OUTPUT.txt', 'utf-8').trim();

const actualUltimate = unicodeToShreeLipi(ultimateInput).trim();

const inpWords = ultimateInput.split(/\s+/).filter(Boolean);
const actWords = actualUltimate.split(/\s+/).filter(Boolean);
const expWords = expectedUltimate.split(/\s+/).filter(Boolean);

let matched = 0;
let mismatches = [];

for (let i = 0; i < expWords.length; i++) {
    if (actWords[i] === expWords[i]) {
        matched++;
    } else {
        mismatches.push({
            input: inpWords[i],
            actual: actWords[i],
            expected: expWords[i]
        });
    }
}

console.log("Ultimate Test Matched: " + matched + " / " + expWords.length + " (" + ((matched / expWords.length) * 100).toFixed(2) + "%)");

if (mismatches.length > 0) {
    console.log("Mismatches found:");
    for (const m of mismatches) {
        console.log("❌ " + m.input + " -> Actual: '" + m.actual + "' | Expected: '" + m.expected + "'");
    }
} else {
    console.log("🎉 100% PERFECT 1-TO-1 MATCH FOR ULTIMATE TEST IN PRODUCTION TYPESCRIPT ENGINE!");
}
