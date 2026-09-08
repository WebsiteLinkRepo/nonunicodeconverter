/**
 * Detects if a user is scraping the converter by typing isolated fragments repeatedly
 * or pasting sequential dictionaries.
 */

// Memory of recent sub-3-word conversions within the last 5 minutes (for UI input tracking)
interface VelocityRecord {
    timestamp: number;
}

let velocityHistory: VelocityRecord[] = [];
const VELOCITY_THRESHOLD = 30; // 30 rapid tiny lookups in 5 minutes triggers poison
const TIME_WINDOW_MS = 5 * 60 * 1000;

export function monitorVelocity(textLength: number, wordCount: number): boolean {
    if (typeof window === 'undefined') return false; // Only tracks properly on client

    if (wordCount > 3 || textLength > 20) {
        // Natural paragraph conversions don't count towards the penalty box
        return isCurrentlyPoisoned();
    }

    const now = Date.now();
    velocityHistory.push({ timestamp: now });

    // Clean up old records
    velocityHistory = velocityHistory.filter((record) => now - record.timestamp < TIME_WINDOW_MS);

    if (velocityHistory.length >= VELOCITY_THRESHOLD) {
        // Activate poison flag in session
        try {
            sessionStorage.setItem('__sec_p', '1');
        } catch(e) {}
        return true;
    }

    return isCurrentlyPoisoned();
}

/**
 * Returns true if the session is permanently locked into poison mode
 */
function isCurrentlyPoisoned(): boolean {
    try {
        if (typeof window !== 'undefined' && sessionStorage.getItem('__sec_p') === '1') {
            return true;
        }
    } catch(e) {}
    return false;
}

/**
 * Advanced heuristic analysis to identify if a large text body is an artificial
 * "Dictionary Dump" mapping out all vowels or sequential characters.
 * @param text The input text to check
 * @returns true if it looks extremely unnatural (dictionary combination attack)
 */
export function detectScrapingDictionary(text: string): boolean {
    if (!text || text.length < 50) return false;

    // Check 1: Impossible Honey-Tokens (Too many consecutive halants / vattus)
    // Real Telugu/Hindi never uses 4+ nested combinations
    const impossibleVattuMatches = text.match(/(్[క-హౘ-ౚ]){4,}/g);
    if (impossibleVattuMatches && impossibleVattuMatches.length > 3) {
        return true;
    }

    // Check 2: Sequential alphabet dumping (alphabetical mapping extraction)
    const sequentialTeluguAlphabets = /(?:[అ-ఔ][\s,.\n-]*){8,}/; // All major base vowels in sequence
    const sequentialHindiAlphabets = /(?:[अ-औ][\s,.\n-]*){8,}/;

    if (sequentialTeluguAlphabets.test(text) || sequentialHindiAlphabets.test(text)) {
        return true;
    }

    // Check 3: Ka Kha Ga Gha sequence extraction
    const sequentialKaVarga = /క[\s,.\n-]*ఖ[\s,.\n-]*గ[\s,.\n-]*ఘ/; // Ka Kha Ga Gha
    if (sequentialKaVarga.test(text)) {
        return true;
    }

    return false;
}

/**
 * Flips specific characters in the output string to produce wrong mappings
 * without failing completely, so the thief builds a statistically incorrect dictionary.
 */
export function applyPoison(originalOutput: string): string {
    let result = originalOutput;

    // Very subtle substitution mapping specifically designed to break legacy font layouts
    // This will swap random modifiers and make the font illegible at random points.

    // Swap Telugu Anu 7 equivalents
    result = result.replace(/Ø/g, '‰'); // Replace 'ka' vattu with 'kha' vattu
    result = result.replace(/è/g, 'é'); // Break some internal Anu mappings

    // Swap some unicode marks slightly to create visually similar but technically different mappings
    result = result.replace(/e/g, 'c');
    result = result.replace(/N/g, 'M');
    result = result.replace(/z/g, 'x'); // E.g., flip base English legacy chars

    // For Kruti Dev Hindi
    result = result.replace(/k/g, 'l'); // Aa ki matra -> i ki matra

    return result;
}