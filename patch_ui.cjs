const fs = require('fs');

let content = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

// Replace the Script and Format dropdown area to be Script first, then Format, and add dynamic logic
const uiHtmlReplacement = `
      <!-- Script Selector -->
      <div class="flex items-center gap-1.5 font-medium text-[var(--ink-secondary)]">
        <label for="script-select">Language:</label>
        <select id="script-select" class="bg-[var(--canvas)] border border-[var(--hairline)] rounded px-2 py-0.5 text-xs text-[var(--ink)] focus:outline-none focus:border-[var(--ink)] cursor-pointer">
          <option value="telugu">Telugu</option>
          <option value="hindi">Hindi</option>
          <option value="tamil">Tamil</option>
          <option value="kannada">Kannada</option>
          <option value="malayalam">Malayalam</option>
        </select>
      </div>

      <!-- Font Version Selector -->
      <div class="flex items-center gap-1.5 font-medium text-[var(--ink-secondary)]">
        <label for="font-version-select">Format:</label>
        <select id="font-version-select" class="bg-[var(--canvas)] border border-[var(--hairline)] rounded px-2 py-0.5 text-xs text-[var(--ink)] focus:outline-none focus:border-[var(--ink)] cursor-pointer">
          <!-- Populated dynamically via JS -->
        </select>
      </div>
`;

content = content.replace(/<!-- Font Version Selector -->[\s\S]*?<!-- Clean Extra Lines Checkbox -->/, uiHtmlReplacement + "\n\n      <!-- Clean Extra Lines Checkbox -->");

// Now update the script to handle dynamic options
const dynamicScriptLogic = `
  const scriptSelectEl = document.getElementById('script-select') as HTMLSelectElement;
  const fontVersionSelectEl = document.getElementById('font-version-select') as HTMLSelectElement;
  
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
      \`<option value="\${opt.value}">\${opt.label}</option>\`
    ).join('');
    
    // Default fallback logic handled during switch
  }

  if (scriptSelectEl) {
    scriptSelectEl.addEventListener('change', () => {
      updateFontDropdown();
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
`;

// Replace the old scriptSelectEl event listener logic
content = content.replace(/const scriptSelectEl = document\.getElementById\('script-select'\) as HTMLSelectElement;[\s\S]*?if \(scriptSelectEl\) \{[\s\S]*?\}\n  \}/, dynamicScriptLogic);

fs.writeFileSync('src/components/TextConverter.astro', content);
console.log("Patched TextConverter.astro");
