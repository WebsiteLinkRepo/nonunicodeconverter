import puppeteer from 'puppeteer';
import * as fs from 'fs';
import * as path from 'path';

async function main() {
    let out = "Missing or Unknown Candidates for Gha, Nga, Ma, Ha\n";
    const candidates = [0x5f, 0x153, 0x152, 0x2dc, 0x0ac, 0x0a1, 0x0a2, 0x0ab, 0x0b6, 0x0c9, 0x0cb, 0x0cd, 0x0ce, 0x0cf, 0x0160];
    
    // Gha, Nga, Ma, Ha in Shreelipi Telugu:
    // Let's print out what the Unicode text "ఘ ఙ మ హ" looks like normally, to compare
    // But since this is a custom font we can only search its slots
    // Instead we will render a few blocks
}
