<script>
  import { convertText } from '../utils/converter';
  import type { FontEncoding } from '../utils/mappings';
  import { TRANSLATIONS, type Language } from '../utils/i18n';

  interface HistoryItem {
    id: string;
    input: string;
    output: string;
    font: string;
    timestamp: number;
  }

  const rootEl = document.getElementById('converter-root') as HTMLDivElement;
  let currentLang: Language = (rootEl?.dataset.lang as Language) || 'en';
  let selectedFontStyle = 'priyanka';
  let currentFontSize = 16;
  let historyItems: HistoryItem[] = [];
  let isManualReverse: boolean | null = null;

  const fontStyles: Record<string, string> = {
    priyanka: 'AnuPriyanka',
    anupama: 'AnuAnupama',
    subhalekha: 'AnuSubhalekha',
    bapu: 'AnuBapu',
    ramana: 'AnuRamana',
    gowthami: 'AnuGowthami'
  };

  const langSelect = document.getElementById('lang-select') as HTMLSelectElement;
  const logoTitleText = document.getElementById('logo-title-text') as HTMLSpanElement;
  const pageTitle = document.getElementById('page-title') as HTMLHeadingElement;
  const pageSubtitle = document.getElementById('page-subtitle') as HTMLParagraphElement;
  const labelSelectFont = document.getElementById('label-select-font') as HTMLSpanElement;
  const autoStatus = document.getElementById('auto-status') as HTMLSpanElement;

  const labelCleanSpaces = document.getElementById('label-clean-spaces') as HTMLSpanElement;

  const labelAltRaaVatthu = document.getElementById('label-alt-raa-vatthu') as HTMLSpanElement;
  const altRaaVatthuWrapper = document.getElementById('alt-raa-vatthu-wrapper') as HTMLLabelElement;

  const fontTabs = document.querySelectorAll<HTMLButtonElement>('.font-tab');
  const activeFontLabel = document.getElementById('active-font-label') as HTMLSpanElement;
  const inputBoxTitle = document.getElementById('input-box-title') as HTMLSpanElement;
  const outputBoxTitle = document.getElementById('output-box-title') as HTMLSpanElement;
  
  const inputText = document.getElementById('input-text') as HTMLTextAreaElement;
  const outputText = document.getElementById('output-text') as HTMLTextAreaElement;
  const charCount = document.getElementById('char-count') as HTMLSpanElement;

  const cleanSpacesChk = document.getElementById('clean-spaces-chk') as HTMLInputElement;

  const altRaaVatthuChk = document.getElementById('alt-raa-vatthu-chk') as HTMLInputElement;
  
  const zoomInBtn = document.getElementById('zoom-in-btn') as HTMLButtonElement;
  const zoomOutBtn = document.getElementById('zoom-out-btn') as HTMLButtonElement;

  const copyBtn = document.getElementById('copy-btn') as HTMLButtonElement;
  const copyBtnText = document.getElementById('copy-btn-text') as HTMLSpanElement;
  const downloadBtn = document.getElementById('download-btn') as HTMLButtonElement;
  const downloadBtnText = document.getElementById('download-btn-text') as HTMLSpanElement;
  const pasteBtn = document.getElementById('paste-btn') as HTMLButtonElement;
  const clearBtn = document.getElementById('clear-btn') as HTMLButtonElement;
  const swapBtn = document.getElementById('swap-btn') as HTMLButtonElement;

  const sampleTeluguBtn = document.getElementById('sample-telugu-btn') as HTMLButtonElement;
  const sampleHindiBtn = document.getElementById('sample-hindi-btn') as HTMLButtonElement;


  const linesStat = document.getElementById('lines-stat') as HTMLElement;
  const wordsStat = document.getElementById('words-stat') as HTMLElement;
  
  const warningBar = document.getElementById('unmapped-warning-bar') as HTMLDivElement;
  const warningMsg = document.getElementById('warning-msg') as HTMLSpanElement;
  const warningCharsList = document.getElementById('warning-chars-list') as HTMLSpanElement;
  const footerText = document.getElementById('footer-text') as HTMLSpanElement;

  const historyContainer = document.getElementById('history-container') as HTMLDivElement;
  const historyTitle = document.getElementById('history-title') as HTMLSpanElement;
  const historyList = document.getElementById('history-list') as HTMLDivElement;
  const clearHistoryBtn = document.getElementById('clear-history-btn') as HTMLButtonElement;

  // Saved Preferences
  const savedFontSize = localStorage.getItem('fontSize');
  if (savedFontSize) {
    currentFontSize = parseInt(savedFontSize);
    applyFontSize(currentFontSize);
  }

  const savedAltRaa = localStorage.getItem('altRaaVatthu');
  if (altRaaVatthuChk && savedAltRaa === 'true') {
    altRaaVatthuChk.checked = true;
  }

  loadHistory();

  function applyFontSize(size: number) {
    currentFontSize = Math.min(28, Math.max(12, size));
    if (inputText) inputText.style.fontSize = `${currentFontSize}px`;
    if (outputText) outputText.style.fontSize = `${currentFontSize}px`;
    localStorage.setItem('fontSize', currentFontSize.toString());
  }

  zoomInBtn?.addEventListener('click', () => applyFontSize(currentFontSize + 2));
  zoomOutBtn?.addEventListener('click', () => applyFontSize(currentFontSize - 2));

  function updateLanguage(lang: Language) {
    currentLang = lang;
    const t = TRANSLATIONS[lang] || TRANSLATIONS.en;

    if (logoTitleText) logoTitleText.textContent = t.siteTitle;
    if (pageTitle) pageTitle.textContent = t.title;
    if (pageSubtitle) pageSubtitle.textContent = t.subtitle;
    if (labelSelectFont) labelSelectFont.textContent = t.selectFontLabel;
    if (labelCleanSpaces) labelCleanSpaces.textContent = t.cleanSpacesLabel;

    if (labelAltRaaVatthu) labelAltRaaVatthu.textContent = t.altRaaVatthuLabel;
    if (inputBoxTitle) inputBoxTitle.textContent = t.inputBoxHeader;
    if (outputBoxTitle) outputBoxTitle.textContent = t.outputBoxHeader;
    if (pasteBtn) pasteBtn.textContent = t.pasteBtn;
    if (clearBtn) clearBtn.textContent = t.clearBtn;
    if (downloadBtnText) downloadBtnText.textContent = t.downloadBtn;
    if (inputText) inputText.placeholder = t.inputPlaceholder;
    if (outputText) outputText.placeholder = "Converted " + activeFontNameLabel() + " text will appear here automatically...";
    if (copyBtnText) copyBtnText.textContent = t.copyBtn;
    if (footerText) footerText.textContent = t.footerText;
    if (historyTitle) historyTitle.textContent = t.historyTitle;
    if (clearHistoryBtn) clearHistoryBtn.textContent = t.clearHistoryBtn;

    processConversion();
  }

  updateLanguage(currentLang);

  // AUTOMATIC SANITIZATION: Built-in default behavior for 100% clean Photoshop, InDesign & Word pasting!
  function sanitizeForAdobeAndWord(text: string): string {
    if (!text) return text;
    // 1. Convert smart quotes / curly quotes to straight quotes to prevent MS Word & Photoshop auto-correct glyph corruption
    let sanitized = text.replace(/[\u2018\u2019]/g, "'").replace(/[\u201C\u201D]/g, '"');
    // 2. Strip Zero-Width Joiner (ZWJ), Zero-Width Non-Joiner (ZWNJ), Zero-Width Space & BOM markers that produce square boxes □ in Photoshop
    sanitized = sanitized.replace(/[\uFEFF\u200B\u200C\u200D]/g, '');
    // 3. Normalize non-breaking spaces
    sanitized = sanitized.replace(/\u00A0/g, ' ');
    return sanitized;
  }

  function processConversion(autoDetectScript: boolean | Event = true) {
    if (autoDetectScript instanceof Event) {
      autoDetectScript = true;
    }
    
    let val = inputText.value;
    const t = TRANSLATIONS[currentLang] || TRANSLATIONS.en;

    const scriptSelect = document.getElementById('script-select') as HTMLSelectElement;
    
    if (val && autoDetectScript) {
      const hasTelugu = /[\u0C00-\u0C7F]/.test(val);
      const hasHindi = /[\u0900-\u097F]/.test(val);
      if (hasHindi && !hasTelugu && scriptSelect) {
        scriptSelect.value = 'hindi';
      } else if (hasTelugu && !hasHindi && scriptSelect) {
        scriptSelect.value = 'telugu';
      }
    }

    const script = scriptSelect ? (scriptSelect.value as any) : 'telugu';

    
    const PLACEHOLDERS: Record<string, string> = {
      telugu: "Paste Telugu Unicode text here... (e.g. అందరికీ నమస్కారం)",
      hindi: "Paste Hindi Unicode text here... (e.g. हिंदी भारत की राजभाषा है)",
      tamil: "Paste Tamil Unicode text here... (e.g. அனைவருக்கும் வணக்கம்)",
      kannada: "Paste Kannada Unicode text here... (e.g. ಎಲ್ಲರಿಗೂ ನಮಸ್ಕಾರ)",
      malayalam: "Paste Malayalam Unicode text here... (e.g. എല്ലാവർക്കും നമസ്കാരം)"
    };
    
    const scriptNames: Record<string, string> = { 
      hindi: 'Hindi', tamil: 'Tamil', kannada: 'Kannada', malayalam: 'Malayalam', telugu: 'Telugu' 
    };
    
    if (script === 'telugu') {
      sampleTeluguBtn?.classList.remove('hidden');
      sampleHindiBtn?.classList.add('hidden');
      if (altRaaVatthuWrapper) altRaaVatthuWrapper.style.display = 'flex';
    } else if (script === 'hindi') {
      sampleTeluguBtn?.classList.add('hidden');
      sampleHindiBtn?.classList.remove('hidden');
      if (altRaaVatthuWrapper) altRaaVatthuWrapper.style.display = 'none';
    } else {
      sampleTeluguBtn?.classList.add('hidden');
      sampleHindiBtn?.classList.add('hidden');
      if (altRaaVatthuWrapper) altRaaVatthuWrapper.style.display = 'none';
    }
    
    if (inputText) inputText.placeholder = PLACEHOLDERS[script] || PLACEHOLDERS['telugu'];

    if (!val) {

      outputText.value = '';
      inputText.style.fontFamily = 'sans-serif';
      outputText.style.fontFamily = 'sans-serif';
      charCount.textContent = `0 ${t.charsLabel}`;
      if (linesStat) linesStat.textContent = '0';
      if (wordsStat) wordsStat.textContent = '0';
      autoStatus.textContent = t.autoDetectNotice;
      warningBar.classList.add('hidden');
      return;
    }

    // Always sanitize input automatically for Adobe Photoshop, InDesign & Word safety
    val = sanitizeForAdobeAndWord(val);

    if (cleanSpacesChk?.checked) {
      val = val.replace(/[ \t]+/g, ' ').replace(/\n{3,}/g, '\n\n').trim();
    }



    const hasTeluguChar = /[\u0C00-\u0C7F]/.test(val);
    const hasHindiChar = /[\u0900-\u097F]/.test(val);
    const isUnicodeInput = hasTeluguChar || hasHindiChar;
    const reverse = isManualReverse !== null ? isManualReverse : !isUnicodeInput;
    
    const isTelugu = script === 'telugu';

    const altRaaVatthuChk = document.getElementById('alt-raa-vatthu-chk') as HTMLInputElement;
    const useAltRaaVatthu = (altRaaVatthuChk && isTelugu) ? altRaaVatthuChk.checked : false;
    const effectiveFontStyle = useAltRaaVatthu ? 'bapu' : selectedFontStyle;

    const scriptNameUpper = scriptNames[script].toUpperCase();

    if (reverse) {
      autoStatus.textContent = `Non-Unicode ➔ ${scriptNames[script]} Unicode`;
      if (inputBoxTitle) inputBoxTitle.textContent = 'NON-UNICODE TEXT INPUT';
      if (outputBoxTitle) outputBoxTitle.textContent = `${scriptNameUpper} UNICODE OUTPUT`;
    } else {
      autoStatus.textContent = `${scriptNames[script]} Unicode ➔ ${activeFontNameLabel()}`;
      if (inputBoxTitle) inputBoxTitle.textContent = `${scriptNameUpper} UNICODE INPUT`;
      if (outputBoxTitle) outputBoxTitle.textContent = 'NON-UNICODE OUTPUT';
    }


    const fontVersionSelect = document.getElementById('font-version-select') as HTMLSelectElement;
    const encoding = fontVersionSelect ? (fontVersionSelect.value as any) : 'anu7';

    import('../utils/converter').then(({ convertText }) => {
      const altRaaVatthuChk = document.getElementById('alt-raa-vatthu-chk') as HTMLInputElement;
      const useAltRaaVatthu = (altRaaVatthuChk && !isHindi) ? altRaaVatthuChk.checked : false;

      const res = convertText(val, encoding, reverse, useAltRaaVatthu, script);
      
      // Do NOT sanitize output. Anu fonts intentionally use smart quotes (‘, “, etc.) for Telugu glyphs.
      // Replacing them with straight quotes breaks characters like 'దీర్ఘం', 'కు', 'క్కని' etc.
      const finalOutput = res.convertedText;

      outputText.value = finalOutput;
      
      // When Alt Raa Vatthu is checked, it moves the Raa Vatthu character to the end of the syllable.
      // AnuPriyanka draws this character as a left-wrapper, so it looks broken when placed at the end.
      // AnuBapu explicitly draws this character as a right-sided curve.
      // To ensure the preview is visually correct, we automatically switch the preview font to AnuBapu if Alt Raa Vatthu is used.

      
      // Apply correct font style preview
      // Only apply legacy fonts if there is actual text, otherwise let it fall back to sans-serif so the placeholder is legible
      let legacyFontToApply = 'sans-serif';
      if (encoding === 'krutidev') legacyFontToApply = "'Kruti Dev 010', 'Kruti Dev', 'DevLys 010', sans-serif";
      else if (encoding === 'bamini') legacyFontToApply = "'Bamini', sans-serif";
      else if (encoding === 'nudi') legacyFontToApply = "'Nudi', sans-serif";
      else if (encoding === 'ism') legacyFontToApply = "'ML-TTKarthika', sans-serif";
      else if (encoding === 'shreelipi') legacyFontToApply = "'SHREE-TEL', sans-serif";
      else legacyFontToApply = fontStyles[effectiveFontStyle] || 'AnuPriyanka';

      if (reverse) {
        inputText.style.fontFamily = (inputText.value) ? legacyFontToApply : 'sans-serif';
        outputText.style.fontFamily = 'sans-serif';
      } else {
        inputText.style.fontFamily = 'sans-serif';
        outputText.style.fontFamily = (outputText.value) ? legacyFontToApply : 'sans-serif';
      }


      charCount.textContent = `${val.length.toLocaleString()} ${t.charsLabel}`;

      if (linesStat) linesStat.textContent = res.stats.lineCount.toLocaleString();
      if (wordsStat) wordsStat.textContent = res.stats.wordCount.toLocaleString();

      if (res.stats.unmappedCount > 0) {
        warningBar.classList.remove('hidden');
        warningMsg.textContent = t.unmappedNotice;
        const uniqueUnmapped = Array.from(new Set(res.errors.map(e => e.char))).slice(0, 8).join(', ');
        warningCharsList.textContent = `Chars: ${uniqueUnmapped}`;
      } else {
        warningBar.classList.add('hidden');
      }

      saveToHistoryDebounced(val, finalOutput, selectedFontStyle);

      // Auto-copy functionality
      const autoCopyChk = document.getElementById('auto-copy-chk') as HTMLInputElement;
      if (autoCopyChk && autoCopyChk.checked && finalOutput) {
        try {
          navigator.clipboard.writeText(finalOutput).then(() => {
            if (copyBtnText) {
              const oldText = copyBtnText.textContent;
              copyBtnText.textContent = "COPIED AUTO!";
              setTimeout(() => copyBtnText.textContent = oldText, 1500);
            }
          });
        } catch (e) {
          // ignore auto-copy errors
        }
      }
    });
  }

  let historyTimeout: any;
  function saveToHistoryDebounced(input: string, output: string, fontStyle: string) {
    clearTimeout(historyTimeout);
    if (!input || input.trim().length < 3) return;
    historyTimeout = setTimeout(() => {
      addToHistory(input, output, fontStyle);
    }, 1500);
  }

  function addToHistory(input: string, output: string, fontStyle: string) {
    const existingIndex = historyItems.findIndex(item => item.input === input);
    if (existingIndex !== -1) {
      historyItems.splice(existingIndex, 1);
    }
    historyItems.unshift({
      id: Date.now().toString(),
      input,
      output,
      font: fontStyle,
      timestamp: Date.now()
    });
    if (historyItems.length > 8) historyItems.pop();
    localStorage.setItem('conversion_history', JSON.stringify(historyItems));
    renderHistory();
  }

  function loadHistory() {
    try {
      const data = localStorage.getItem('conversion_history');
      if (data) {
        historyItems = JSON.parse(data);
        renderHistory();
      }
    } catch {
      historyItems = [];
    }
  }

  function renderHistory() {
    if (!historyContainer || !historyList) return;
    if (historyItems.length === 0) {
      historyContainer.classList.add('hidden');
      return;
    }
    historyContainer.classList.remove('hidden');
    historyList.innerHTML = historyItems.map(item => `
      <div data-id="${item.id}" class="history-item flex items-center justify-between p-2 rounded-lg bg-[var(--canvas)] border border-[var(--hairline)] hover:border-[var(--hairline-strong)] transition-all cursor-pointer text-xs">
        <div class="truncate max-w-[80%] flex items-center gap-2">
          <span class="font-mono text-[10px] px-1.5 py-0.5 rounded bg-[var(--canvas-soft-2)] text-[var(--ink-secondary)]">${item.font}</span>
          <span class="truncate text-[var(--ink)] font-medium">${escapeHtml(item.input.substring(0, 50))}</span>
        </div>
        <span class="text-[10px] font-mono text-[var(--ink-tertiary)]">${formatTime(item.timestamp)}</span>
      </div>
    `).join('');

    document.querySelectorAll('.history-item').forEach(el => {
      el.addEventListener('click', () => {
        const id = el.getAttribute('data-id');
        const item = historyItems.find(i => i.id === id);
        if (item) {
          inputText.value = item.input;
          selectedFontStyle = item.font;
          processConversion();
        }
      });
    });
  }

  clearHistoryBtn?.addEventListener('click', () => {
    historyItems = [];
    localStorage.removeItem('conversion_history');
    renderHistory();
  });

  function escapeHtml(str: string): string {
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function formatTime(ts: number): string {
    const d = new Date(ts);
    return `${d.getHours().toString().padStart(2, '0')}:${d.getMinutes().toString().padStart(2, '0')}`;
  }

  inputText.addEventListener('input', processConversion);
  cleanSpacesChk?.addEventListener('change', processConversion);

  
  const fontVersionSelectEl = document.getElementById('font-version-select') as HTMLSelectElement;
  if (fontVersionSelectEl) {
    fontVersionSelectEl.addEventListener('change', () => {
      if (activeFontLabel) {
        activeFontLabel.textContent = activeFontNameLabel();
      }
      processConversion();
    });
  }

  
  const scriptSelectEl = document.getElementById('script-select') as HTMLSelectElement;
  
  const FONT_OPTIONS: Record<string, {value: string, label: string}[]> = {
    telugu: [
      { value: 'anu7', label: 'Anu Script Manager 7.0' },
      { value: 'anu6', label: 'Anu Script Manager 6.0' },
      { value: 'shreelipi', label: 'Shree-Lipi' }
    ],
    hindi: [
      { value: 'krutidev', label: 'Kruti Dev (Popular)' },
      { value: 'anu7', label: 'Anu Script Manager (Hindi)' }
    ],
    tamil: [
      { value: 'bamini', label: 'Bamini (Popular)' },
      { value: 'anu7', label: 'Anu Script Manager (Tamil)' }
    ],
    kannada: [
      { value: 'nudi', label: 'Nudi' },
      { value: 'anu7', label: 'Anu Script Manager (Kannada)' }
    ],
    malayalam: [
      { value: 'ism', label: 'ISM / ML-TTKarthika' },
      { value: 'anu7', label: 'Anu Script Manager (Malayalam)' }
    ]
  };

  function updateFontDropdown() {
    if (!fontVersionSelectEl || !scriptSelectEl) return;
    const currentScript = scriptSelectEl.value;
    const options = FONT_OPTIONS[currentScript] || FONT_OPTIONS['telugu'];
    
    fontVersionSelectEl.innerHTML = options.map(opt => 
      `<option value="${opt.value}">${opt.label}</option>`
    ).join('');
  }

  if (scriptSelectEl) {
    scriptSelectEl.addEventListener('change', () => {
      updateFontDropdown();
      const anuFontSelectEl = document.getElementById('anu-font-select') as HTMLSelectElement;
      if (anuFontSelectEl) {
        if (scriptSelectEl.value === 'hindi') anuFontSelectEl.value = 'AnuNEOGANBO';
        else if (scriptSelectEl.value === 'telugu') anuFontSelectEl.value = 'AnuANUPB';
        else if (scriptSelectEl.value === 'kannada') anuFontSelectEl.value = 'AnuDINEIGHT';
        else if (scriptSelectEl.value === 'tamil') anuFontSelectEl.value = 'AnuPADMINI_';
      }
      processConversion(false);
    });
  }
  
  // Call once on init
  updateFontDropdown();


  altRaaVatthuChk?.addEventListener('change', () => {
    localStorage.setItem('altRaaVatthu', altRaaVatthuChk.checked.toString());
    processConversion();
  });

  // Preset Sample Click Handlers
  sampleTeluguBtn?.addEventListener('click', () => {
    selectedFontStyle = 'priyanka';
    isManualReverse = false;
    inputText.value = "అందరికీ నమస్కారం. తెలుగు భాష చాలా అద్భుతమైనది.";
    processConversion();
  });



  sampleHindiBtn?.addEventListener('click', () => {
    selectedFontStyle = 'priyanka';
    isManualReverse = false;
    inputText.value = "नमस्ते! हिंदी बहुत ही सुंदर और प्राचीन भाषा है।";
    processConversion();
  });

  swapBtn?.addEventListener('click', () => {
    const currentInput = inputText.value;
    const currentOutput = outputText.value;

    if (currentOutput && currentOutput.trim().length > 0) {
      const isOutputUnicode = /[\u0C00-\u0C7F\u0900-\u097F]/.test(currentOutput);
      inputText.value = currentOutput;
      isManualReverse = !isOutputUnicode;
    } else if (currentInput && currentInput.trim().length > 0) {
      const isInputUnicode = /[\u0C00-\u0C7F\u0900-\u097F]/.test(currentInput);
      const currentReverse = isManualReverse !== null ? isManualReverse : !isInputUnicode;
      isManualReverse = !currentReverse;
    } else {
      isManualReverse = isManualReverse === null ? true : !isManualReverse;
    }

    swapBtn.classList.add('scale-105');
    setTimeout(() => swapBtn.classList.remove('scale-105'), 150);

    processConversion();
  });

  
  function activeFontNameLabel(): string {
    const fontVersionSelectEl = document.getElementById('font-version-select') as HTMLSelectElement;
    if (fontVersionSelectEl) {
      if (fontVersionSelectEl.options.length > 0 && fontVersionSelectEl.selectedIndex >= 0) {
        return fontVersionSelectEl.options[fontVersionSelectEl.selectedIndex].text;
      }
    }
    return 'Target Font';
  }


  // Initial call to set UI states
  const initScriptIsHindi = typeof scriptSelectEl !== 'undefined' && scriptSelectEl ? scriptSelectEl.value === 'hindi' : false;
  const useAltRaaVatthuInit = (altRaaVatthuChk && !initScriptIsHindi) ? altRaaVatthuChk.checked : false;
  const effectiveFontStyleInit = useAltRaaVatthuInit ? 'bapu' : selectedFontStyle;
  
  let initLegacyFontToApply = 'sans-serif';
  const initEncoding = fontVersionSelectEl ? fontVersionSelectEl.value : 'anu7';
  if (initEncoding === 'krutidev') initLegacyFontToApply = "'Kruti Dev 010', 'Kruti Dev', 'DevLys 010', sans-serif";
  else if (initEncoding === 'bamini') initLegacyFontToApply = "'Bamini', sans-serif";
  else if (initEncoding === 'nudi') initLegacyFontToApply = "'Nudi', sans-serif";
  else if (initEncoding === 'ism') initLegacyFontToApply = "'ML-TTKarthika', sans-serif";
  else if (initEncoding === 'shreelipi') initLegacyFontToApply = "'SHREE-TEL', sans-serif";
  else initLegacyFontToApply = fontStyles[effectiveFontStyleInit] || 'AnuPriyanka';

  inputText.style.fontFamily = (inputText.value) ? initLegacyFontToApply : 'sans-serif';
  outputText.style.fontFamily = (outputText.value) ? initLegacyFontToApply : 'sans-serif';

  if (activeFontLabel) {
    activeFontLabel.textContent = activeFontNameLabel();
  }

  const cp1252: Record<number, number> = {
    0x20AC: 0x80, 0x201A: 0x82, 0x0192: 0x83, 0x201E: 0x84, 0x2026: 0x85, 0x2020: 0x86, 0x2021: 0x87,
    0x02C6: 0x88, 0x2030: 0x89, 0x0160: 0x8A, 0x2039: 0x8B, 0x0152: 0x8C, 0x017D: 0x8E, 0x2018: 0x91,
    0x2019: 0x92, 0x201C: 0x93, 0x201D: 0x94, 0x2022: 0x95, 0x2013: 0x96, 0x2014: 0x97, 0x02DC: 0x98,
    0x2122: 0x99, 0x0161: 0x9A, 0x203A: 0x9B, 0x0153: 0x9C, 0x017E: 0x9E, 0x0178: 0x9F
  };

  function charToWin1252(char: string): number {
    const code = char.charCodeAt(0);
    if (cp1252[code]) return cp1252[code];
    if (code <= 255) return code;
    return 63; // '?' fallback
  }

  function generateRTF(text: string, fontName: string): string {
    let rtf = `{\\rtf1\\ansi\\ansicpg1252\\deff0{\\fonttbl{\\f0\\fnil\\fcharset0 ${fontName};}}\n\\viewkind4\\uc1\\pard\\lang1033\\f0\\fs24 `;
    for (let i = 0; i < text.length; i++) {
      const char = text[i];
      if (char === '\n') {
        rtf += '\\par\n';
      } else if (char === '\r') {
        // ignore
      } else if (char === '\\') {
        rtf += '\\\\';
      } else if (char === '{') {
        rtf += '\\{';
      } else if (char === '}') {
        rtf += '\\}';
      } else {
        const code = charToWin1252(char);
        if (code > 127 || code < 32) {
          rtf += `\\` + `'` + code.toString(16).padStart(2, '0');
        } else {
          rtf += char;
        }
      }
    }
    rtf += '}';
    return rtf;
  }

  // Copy Output Handler
  copyBtn.addEventListener('click', async () => {
    let val = outputText.value;
    const t = TRANSLATIONS[currentLang] || TRANSLATIONS.en;
    if (!val) {
      inputText.focus();
      return;
    }

    const isOutputUnicode = /[\u0C00-\u0C7F\u0900-\u097F]/.test(val);
    const rtfText = generateRTF(val, fontStyles[selectedFontStyle] || 'AnuPriyanka');

    let success = false;
    
    // Try modern ClipboardItem API first (supports RTF)
    try {
      if (typeof ClipboardItem !== 'undefined' && navigator.clipboard && navigator.clipboard.write) {
        const textBlob = new Blob([val], { type: 'text/plain' });
        const items: Record<string, Blob> = { 'text/plain': textBlob };
        if (!isOutputUnicode) {
          items['text/rtf'] = new Blob([rtfText], { type: 'text/rtf' });
        }
        await navigator.clipboard.write([new ClipboardItem(items)]);
        success = true;
      }
    } catch (e) {
      // Fall back to old method
    }

    if (!success) {
      const listener = (e: ClipboardEvent) => {
        e.preventDefault();
        if (e.clipboardData) {
          e.clipboardData.setData('text/plain', val);
          if (!isOutputUnicode) {
            e.clipboardData.setData('text/rtf', rtfText);
          }
        }
      };

      outputText.select();
      document.addEventListener('copy', listener);
      try {
        const result = document.execCommand('copy');
        success = result;
      } catch (err) {
        success = false;
      }
      document.removeEventListener('copy', listener);
    }

    if (!success) {
      // Ultimate fallback: Just copy plain text
      try {
        await navigator.clipboard.writeText(val);
        success = true;
      } catch (err) {
        console.error('Failed to copy', err);
      }
    }

    if (success) {
      copyBtnText.textContent = t.copiedBtn;
      copyBtn.classList.remove('bg-[var(--ink)]');
      copyBtn.classList.add('bg-emerald-600', 'text-white');
      
      setTimeout(() => {
        copyBtnText.textContent = t.copyBtn;
        copyBtn.classList.remove('bg-emerald-600', 'text-white');
        copyBtn.classList.add('bg-[var(--ink)]');
      }, 2000);
    }
  });

  // Download Output Handler (.txt)
  downloadBtn?.addEventListener('click', () => {
    let text = outputText.value;
    if (!text) {
      inputText.focus();
      return;
    }
    const blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `converted-${selectedFontStyle}-${Date.now()}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  });

  // Paste Handler
  pasteBtn.addEventListener('click', async () => {
    try {
      const text = await navigator.clipboard.readText();
      if (text) {
        const start = inputText.selectionStart;
        const end = inputText.selectionEnd;
        inputText.value = inputText.value.substring(0, start) + text + inputText.value.substring(end);
        inputText.selectionStart = inputText.selectionEnd = start + text.length;
        inputText.focus();
        processConversion();
      }
    } catch {
      inputText.focus();
    }
  });

  // Clear Handler
  clearBtn.addEventListener('click', () => {
    isManualReverse = null;
    inputText.value = '';
    processConversion();
    inputText.focus();
  });

  // Remove English Handler
  const removeEnglishBtn = document.getElementById('remove-english-btn');
  if (removeEnglishBtn) {
    removeEnglishBtn.addEventListener('click', () => {
      // Remove A-Z, a-z
      inputText.value = inputText.value.replace(/[A-Za-z]/g, '');
      processConversion();
    });
  }
</script>
