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

/**
 * Synchronously converts input text based on target encoding and direction.
 */
export function convertText(
  inputText: string,
  encoding: FontEncoding = 'anu6',
  reverse: boolean = false,
  useAltRaaVatthu: boolean = false
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

  // Fast string replacement using replacement pass
  let resultText = inputText;
  for (const entry of mapping) {
    if (entry.from && resultText.includes(entry.from)) {
      resultText = resultText.split(entry.from).join(entry.to);
    }
  }

  // Handle Alternative Raa Vatthu (ర వత్తు) variant glyph code (µ) for Anu fonts
  if (useAltRaaVatthu && (encoding === 'anu6' || encoding === 'anu7')) {
    if (!reverse) {
      // In Unicode -> Non-Unicode, replace standard Raa Vatthu glyph ³ with alternate glyph µ
      resultText = resultText.split('³').join('µ');
    } else {
      // In Non-Unicode -> Unicode, ensure alternate Raa Vatthu glyph µ is also converted to ్ర
      resultText = resultText.split('µ').join('్ర');
    }
  }

  // Detect unmapped Indic characters if forward converting
  const errors: UnmappedError[] = [];
  if (!reverse) {
    // Check for leftover Telugu (U+0C00-U+0C7F) or Devnagari (U+0900-U+097F) Unicode characters
    const indicRegex = /[\u0C00-\u0C7F\u0900-\u097F]/g;
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
  encoding: FontEncoding = 'anu6',
  reverse: boolean = false,
  useAltRaaVatthu: boolean = false,
  onProgress?: (progressPercent: number) => void
): Promise<ConversionResult> {
  const CHUNK_SIZE = 10000;
  if (inputText.length <= CHUNK_SIZE) {
    return convertText(inputText, encoding, reverse, useAltRaaVatthu);
  }

  const startTime = performance.now();
  const lines = inputText.split('\n');
  const convertedChunks: string[] = [];
  let totalErrors: UnmappedError[] = [];
  let processedChars = 0;

  for (let i = 0; i < lines.length; i += 200) {
    const chunkLines = lines.slice(i, i + 200).join('\n');
    const chunkResult = convertText(chunkLines, encoding, reverse, useAltRaaVatthu);
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
