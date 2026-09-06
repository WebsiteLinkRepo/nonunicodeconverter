import { chromium } from 'playwright';
import { readFileSync, writeFileSync } from 'node:fs';

const inputStr = 'క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ ళ క్ష ఱ';
import { convertUnicodeToShreeLipiTelugu0908 } from '../../src/utils/shreeLipiTelugu0908Converter.js';

// we need to compile the TS converter first!
