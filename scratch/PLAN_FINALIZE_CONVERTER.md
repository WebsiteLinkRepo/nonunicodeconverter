# Shree-Lipi Telugu Verification & Fix Plan

## Goal
Systematically verify and perfect the **Unicode to Shree-Lipi Telugu (Shree-Tel)** conversion step-by-step.

## Steps

### Step 1: Base Characters Check
- Verify all Independent Vowels (అ, ఆ, ఇ...).
- Verify all Base Consonants (క, ఖ, గ...) and ensure the Talakattu (top tick) logic applies correctly.
- *Test:* Generate image/verification for vowels and base consonants. Fix any mapping bugs.

### Step 2: Guninthalu (Matras / Vowel Signs)
- Verify combinations of all Consonants + all Vowels (e.g. కా, కి, కీ, కు, కూ, కే, కై, కో, కౌ...).
- Check irregular Vowel marks (e.g. `కు`, `గూ`, `చు`, `ము`, `యు`, `రు` usually change form in Telugu).
- *Test:* Run `render_gunintham_comparison.py` or similar to check specific tricky rows. Diff against competitor output. Fix mappings.

### Step 3: Modifiers (Anusvara, Visarga, Pollu)
- Verify `ం` (Anusvara), `ః` (Visarga) mappings and positioning.
- Verify Halant/Virama/Pollu `్` behavior at the end of words (e.g. క్).

### Step 4: Vattulu (Consonant Conjuncts / Subscripts)
- Verify `్క`, `్గ`, `్చ`, etc.
- Verify `ya-vattu` (`్య`) and `ra-vattu` (`్ర` pre-base and post-base).
- Verify `da-ta` variations (whether some vattulu attach differently).
- *Test:* Run vattulu scripts to diff with competitor output. Fix `VATTULU` mapping dictionary.

### Step 5: Complex Consonant Clusters & Special Ligatures
- Ligatures like `క్ష`, `జ్ఞ`.
- Multi-vattu cases like `త్ర్య`, `క్ష్మ`, `స్త్ర`.
- Fix ordering (e.g. which vattu goes first).

### Step 6: Complex Paragraph Verification
- Use `TELUGU_COMPLEX_PARAS_INPUT.txt` vs competitor's `TELUGU_COMPLEX_PARAS_OUTPUT.txt`.
- Compare side-by-side renders or text diffs.
- Isolate any remaining broken words, fix them in `shreeLipiTeluguConverter.ts`.
- Achieve 100% visual and code parity.

## Execution
We will proceed through these steps one by one, checking diffs, updating the code, and moving to the next.
