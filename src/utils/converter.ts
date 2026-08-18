import { getMapping, type FontEncoding } from './mappings/index';

export interface UnmappedError {
  index: number;
  char: string;
  codePoint: string;
  reason: string;
}

export interface ConversionStats {
  inputCharCount: number;
  outputCharCount: number;
  wordCount: number;
  lineCount: number;
  unmappedCount: number;
  processingTimeMs: number;
}

export interface ConversionResult {
  convertedText: string;
  errors: UnmappedError[];
  stats: ConversionStats;
}

export interface ConversionOptions {
  encoding?: FontEncoding;
  reverse?: boolean;
  useAltRaaVatthu?: boolean;
}

const ANU7_VATTUS: Record<string, string> = {
  "్క": "\u00D8", // Ø
  "్ఖ": "\u2030", // ‰
  "్గ": "Z",      // Z
  "్ఘ": "\u00E9", // é
  "్ఙ": "_",
  "్చ": "\u00CC", // Ì
  "్ఛ": "\u00CC\u00DB", // ÌÛ
  "్జ": "\u00A8", // ¨
  "్ఝ": "_",
  "్ఞ": "\u00E3", // ã
  "్ట": "\u00BC", // ¼
  "్ఠ": "\u00F7", // ÷
  "్డ": "\u00A6", // ¦
  "్ఢ": "_",
  "్ణ": "\u2019", // ’
  "్త": "\u00EF", // ï
  "్థ": "\u0153", // œ
  "్ద": "\u00DD", // Ý
  "్ధ": "\u00C6", // Æ
  "్న": "\u2022", // •
  "్ప": "\u00CE", // Î
  "్ఫ": "\u00CE\u00DB", // ÎÛ
  "్బ": "\u00D2", // Ò
  "్భ": "\u00D2\u00DB", // ÒÛ
  "్మ": "\u02C6", // ˆ
  "్య": "\u00AB", // «
  "్ర": "\u00E7", // ç (pre-base ra-vattu)
  "్ల": "\u00A2", // ¢
  "్వ": "\u00C7", // Ç
  "్శ": "\u00F4", // ô
  "్ష": "\u00FC", // ü
  "్స": "\u00E0", // à
  "్హ": "\u00BD", // ½
  "్ళ": "\u00DF", // ß
  "్ఱ": "_"
};

/**
 * Synchronously converts input text based on target encoding and direction.
 */
export function convertText(
  inputText: string,
  encoding: FontEncoding = 'anu7',
  reverse: boolean = false,
  useAltRaaVatthu: boolean = false,
  script: 'telugu' | 'hindi' = 'telugu'
): ConversionResult {
  const startTime = performance.now();

  if (!inputText || inputText.trim() === '') {
    return {
      convertedText: '',
      errors: [],
      stats: {
        inputCharCount: 0,
        outputCharCount: 0,
        wordCount: 0,
        lineCount: 0,
        unmappedCount: 0,
        processingTimeMs: 0
      }
    };
  }

  const mapping = getMapping(encoding, reverse);
  let resultText = inputText;

  // Auto-transliterate Devanagari (Hindi) to Telugu for Anu fonts before processing
  // This allows Hindi users to just paste Mangal font and get it converted to Anu
  if (!reverse || (reverse && script === 'hindi')) {
      // In forward conversion, we ALWAYS map Devanagari to Telugu before checking the mapping array.
      // In reverse conversion, this block won't be hit unless we add post-processing later.
  }
  
  if (!reverse) {
    resultText = resultText.replace(/[\u0900-\u097F]/g, (char) => {
      return String.fromCharCode(char.charCodeAt(0) + 0x0300);
    });

    // -------------------------------------------------------------
    // FORWARD CONVERSION (Unicode -> Legacy Anu 7.0)
    // -------------------------------------------------------------
    // Create a fast lookup map from the mapping array
    const lookupMap: Record<string, string> = {};
    for (const entry of mapping) {
      if (entry.from) {
        lookupMap[entry.from] = entry.to;
      }
    }

    // Split text into Telugu syllables and non-Telugu characters
    const syllableRegex = /(?:(?:[\u0C05-\u0C14]|(?:[\u0C15-\u0C39\u0C58-\u0C5A](?:\u0C4D[\u0C15-\u0C39\u0C58-\u0C5A])*[\u0C3E-\u0C4C\u0C4D]?))[\u0C02\u0C03]?)/g;

    resultText = resultText.replace(syllableRegex, (syllable) => {
      // 1. Direct match in lookup table
      if (lookupMap[syllable] !== undefined) {
        return lookupMap[syllable];
      }

      // 2. Complex Syllable Decomposer & Layout Compiler (Fallback)
      const baseConsonant = syllable[0];

      // Find all vattus (e.g. ్క, ్త)
      const vattuMatches = syllable.match(/\u0C4D[\u0C15-\u0C39\u0C58-\u0C5A]/g) || [];

      // Strip base consonant and vattus to find remaining vowel signs
      let remaining = syllable.substring(1);
      for (const vattu of vattuMatches) {
        remaining = remaining.replace(vattu, "");
      }

      // Separate modifiers (ం -> +, ః -> \u00A6)
      let modifier = "";
      if (remaining.endsWith("\u0C02")) { // ం
        modifier = "+";
        remaining = remaining.slice(0, -1);
      } else if (remaining.endsWith("\u0C03")) { // ః
        modifier = "\u00A6";
        remaining = remaining.slice(0, -1);
      }

      const baseSyllable = baseConsonant + remaining;
      let baseConv = lookupMap[baseSyllable];
      if (baseConv === undefined) {
        // Fallback
        baseConv = (lookupMap[baseConsonant] || "") + (lookupMap[remaining] || "");
      }

      let hasRaVattu = false;
      const vattuConvs: string[] = [];
      for (const vattu of vattuMatches) {
        if (vattu === "\u0C4D\u0C30") { // ్ర (ra-vattu)
          hasRaVattu = true;
        } else {
          vattuConvs.push(ANU7_VATTUS[vattu] || "");
        }
      }

      let res = baseConv;
      if (hasRaVattu) {
        res = "\u00E7" + res; // Prepend pre-base ra-vattu
      }
      for (const vc of vattuConvs) {
        res = res + vc; // Append other post-base vattus
      }
      res = res + modifier; // Append modifier at the very end

      return res;
    });
  } else {
    // -------------------------------------------------------------
    // REVERSE CONVERSION (Legacy Anu 7.0 -> Unicode)
    // -------------------------------------------------------------
    // Pre-processing: Move ç (pre-base ra-vattu) to the end of the syllable cluster
    resultText = resultText.replace(/\u00E7([^\s\u00E7]+)/g, '$1\u00E7');

    // Run standard replacement (it contains standalone vattu mappings now)
    for (const entry of mapping) {
      if (entry.from && resultText.includes(entry.from)) {
        resultText = resultText.split(entry.from).join(entry.to);
      }
    }

    // Post-reordering 1: Reorder pre-base e-matras (ె, ే, ై, ొ, ో, ౌ) after the consonant
    resultText = resultText.replace(
      /([\u0C46\u0C47\u0C48\u0C4A\u0C4B\u0C4C])((?:[\u0C15-\u0C39\u0C58-\u0C5A](?:\u0C4D[\u0C15-\u0C39\u0C58-\u0C5A])*))/g,
      '$2$1'
    );

    // Post-reordering 2: Reorder vowel signs (ా, ి, ీ, ు, ూ, etc.) after the post-base vattus
    resultText = resultText.replace(
      /([\u0C15-\u0C39\u0C58-\u0C5A])([\u0C3E-\u0C4C])((?:\u0C4D[\u0C15-\u0C39\u0C58-\u0C5A])+)/g,
      '$1$3$2'
    );
    
    // Post-processing: Map back to Hindi (Devanagari) if script is hindi
    if (script === 'hindi') {
      resultText = resultText.replace(/[\u0C00-\u0C7F]/g, (char) => {
        return String.fromCharCode(char.charCodeAt(0) - 0x0300);
      });
    }
  }

  // Detect unmapped Indic characters if forward converting (excluding digits/punctuation)
  const errors: UnmappedError[] = [];
  if (!reverse) {
    // Check for leftover Telugu (U+0C00-U+0C7F) Unicode characters
    const indicRegex = /[\u0C00-\u0C7F]/g;
    let match: RegExpExecArray | null;
    while ((match = indicRegex.exec(resultText)) !== null) {
      const char = match[0];
      const codePoint = `U+${char.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0')}`;
      errors.push({
        index: match.index,
        char,
        codePoint,
        reason: `No mapping found in target font (${encoding.toUpperCase()})`
      });
    }
  }

  const endTime = performance.now();
  const processingTimeMs = Math.max(0.1, Number((endTime - startTime).toFixed(2)));

  const words = inputText.trim() ? inputText.trim().split(/\s+/).length : 0;
  const lines = inputText ? inputText.split('\n').length : 0;

  return {
    convertedText: resultText,
    errors,
    stats: {
      inputCharCount: inputText.length,
      outputCharCount: resultText.length,
      wordCount: words,
      lineCount: lines,
      unmappedCount: errors.length,
      processingTimeMs
    }
  };
}

/**
 * Asynchronously converts large text inputs in chunks without blocking the UI thread.
 */
export async function convertTextAsync(
  inputText: string,
  encoding: FontEncoding = 'anu7',
  reverse: boolean = false,
  useAltRaaVatthu: boolean = false,
  script: 'telugu' | 'hindi' = 'telugu',
  onProgress?: (progressPercent: number) => void
): Promise<ConversionResult> {
  const CHUNK_SIZE = 10000;
  if (inputText.length <= CHUNK_SIZE) {
    return convertText(inputText, encoding, reverse, useAltRaaVatthu, script);
  }

  const startTime = performance.now();
  const lines = inputText.split('\n');
  const convertedChunks: string[] = [];
  let totalErrors: UnmappedError[] = [];
  let processedChars = 0;

  for (let i = 0; i < lines.length; i += 200) {
    const chunkLines = lines.slice(i, i + 200).join('\n');
    const chunkResult = convertText(chunkLines, encoding, reverse, useAltRaaVatthu, script);
    convertedChunks.push(chunkResult.convertedText);
    totalErrors = totalErrors.concat(chunkResult.errors);

    processedChars += chunkLines.length;
    if (onProgress) {
      onProgress(Math.min(100, Math.round((processedChars / inputText.length) * 100)));
    }

    // Yield control to UI thread
    await new Promise((resolve) => setTimeout(resolve, 0));
  }

  const finalOutput = convertedChunks.join('\n');
  const endTime = performance.now();
  const processingTimeMs = Math.max(0.1, Number((endTime - startTime).toFixed(2)));

  return {
    convertedText: finalOutput,
    errors: totalErrors,
    stats: {
      inputCharCount: inputText.length,
      outputCharCount: finalOutput.length,
      wordCount: inputText.trim() ? inputText.trim().split(/\s+/).length : 0,
      lineCount: lines.length,
      unmappedCount: totalErrors.length,
      processingTimeMs
    }
  };
}
