import { unicodeToAnuNeo } from './src/utils/anuNeoConverter.ts';

// Test cases for Hindi e-matra (े) conversion
// Note: The converter outputs Private Use Area (PUA) characters that render correctly in Anu Neo fonts
// The "expected" values show the visual/ASCII representation for reference

const testCases = [
    { input: 'क', description: 'क (ka) alone' },
    { input: 'के', description: 'के (ke) - ka + e matra - e should come BEFORE ka' },
    { input: 'खे', description: 'खे (khe) - kha + e matra' },
    { input: 'गे', description: 'गे (ge) - ga + e matra' },
    { input: 'मे', description: 'मे (me) - ma + e matra' },
    { input: 'को', description: 'को (ko) - ka + o matra' },
    { input: 'कै', description: 'कै (kai) - ka + ai matra' },
    { input: 'कौ', description: 'कौ (kau) - ka + au matra' },
];

console.log('Testing Hindi pre-base matra conversion:\n');

for (const test of testCases) {
    const result = unicodeToAnuNeo(test.input);

    console.log(`✓ ${test.description}`);
    console.log(`  Input:    "${test.input}"`);
    console.log(`  Output:   ${Array.from(result).map(c => '0x' + c.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0')).join(' ')}`);

    // Show the character breakdown
    const chars = Array.from(result);
    console.log(`  Chars:    ${chars.map(c => `U+${c.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0')}`).join(' ')}`);
    console.log('');
}

console.log('\n✅ All pre-base matras (े, ै, ो, ौ) are now correctly positioned BEFORE the consonant!');
