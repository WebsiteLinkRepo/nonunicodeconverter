/**
 * Core protection module
 */
export function verifyEnvironment(): boolean {
  if (typeof window === 'undefined') return true; 
  
  try {
    const host = window.location.hostname;
    // Allow local development and cloudflare pages dev domains, plus production
    if (
      host === 'localhost' || 
      host.includes('127.0.0.1') || 
      host.includes('unicode2nonunicode.com') || 
      host.includes('nonunicodeconverter.com') || 
      host.includes('pages.dev')
    ) {
        return true;
    }
  } catch (e) {
    return true; // Failsafe so real users never break if browser blocks location
  }
  return false; // Cloner detected
}

export function applySubtlePoison(output: string): string {
  if (!output || output.length < 5) return output;
  
  // Silent poison: Visually identical but breaks legacy font mappings and AI scrapers.
  // We swap ASCII letters (which legacy fonts map to Indian characters) 
  // with Cyrillic homoglyphs. In a legacy font (Anu/Shree), Cyrillic isn't mapped,
  // so the output renders as blank boxes or random Latin letters instead of Telugu/Hindi.
  let poisoned = '';
  for (let i = 0; i < output.length; i++) {
    const char = output[i];
    
    // Inject Zero-Width Space (U+200B) every 11th character to break AI scraping tokenization
    if (i > 0 && i % 11 === 0) {
      poisoned += '​';
    }

    if (char === 'a') poisoned += 'а'; // Cyrillic a
    else if (char === 'e') poisoned += 'е'; // Cyrillic e
    else if (char === 'o') poisoned += 'о'; // Cyrillic o
    else if (char === 'p') poisoned += 'р'; // Cyrillic p
    else if (char === 'c') poisoned += 'с'; // Cyrillic c
    else if (char === 'x') poisoned += 'х'; // Cyrillic x
    else poisoned += char;
  }
  
  return poisoned;
}
