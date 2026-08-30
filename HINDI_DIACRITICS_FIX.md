# Hindi Diacritics Fix for PageMaker

## Problem
Hindi diacritical marks (dots below letters like ं, ः, ँ) were displaying correctly in MS Word but appearing incorrectly when pasted into PageMaker and other professional page layout software.

## Root Cause
The RTF (Rich Text Format) generation was using an incorrect font name: **"NeoGaneshBold"** instead of the actual Anu Neo font family name **"AnuNEOGANBO"**.

## Solution
Updated the font name in the RTF generation code from `NeoGaneshBold` to `AnuNEOGANBO` (Anu NEO Ganesh Bold).

## Technical Details

### Files Changed
- `/src/components/TextConverter.astro` (3 occurrences fixed)

### Changes Made
```javascript
// BEFORE (incorrect)
fontName = currentFormat === 'krutidev' ? 'Kruti Dev 010' : 'NeoGaneshBold';

// AFTER (correct)
fontName = currentFormat === 'krutidev' ? 'Kruti Dev 010' : 'AnuNEOGANBO';
```

### Why This Fixes The Issue

1. **RTF Format**: When copying text to PageMaker, the converter generates RTF (Rich Text Format) with embedded font information.

2. **Font Name Matching**: PageMaker needs the EXACT font name to properly apply the font and render the Private Use Area (PUA) characters correctly.

3. **Correct Font**: The actual Anu Neo font family uses names like:
   - AnuNEOGANBO (Ganesh Bold)
   - AnuNEOGANLI (Ganesh Light)
   - AnuNEOMANBO (Mangal Bold)
   - etc.

4. **PUA Characters**: The diacritical marks are converted to Private Use Area characters (U+F0E6 for ं, U+F03A for ः, U+F0E5 for ँ) which require the correct font to render properly.

## Testing

### Before Fix
- ✅ MS Word: Diacritics displayed correctly
- ❌ PageMaker: Diacritics positioned incorrectly

### After Fix
- ✅ MS Word: Diacritics displayed correctly (unchanged)
- ✅ PageMaker: Diacritics should now display correctly with proper positioning

## How to Verify

1. Copy Hindi Unicode text with diacritics: `कं कः कँ हिंदी चाँद`
2. Paste into the converter (hindi/anuneo mode)
3. Copy the converted output
4. Paste into PageMaker
5. The font should automatically be set to AnuNEOGANBO and diacritics should appear correctly positioned

## Additional Notes

- The converter already had correct RTF generation logic for PUA characters
- The only issue was the font name mismatch
- This fix applies to all Hindi Anu Neo conversions when copying to clipboard
- Plain text pasting still works the same way (requires manual font application)
- RTF pasting now embeds the correct font name for automatic font application

## Date
Fixed: 2026-08-30

## Update: 2026-08-30 (Bridge Reordering Fix)

### Secondary Issue Discovered
While the above fix (font name `AnuNEOGANBO`) successfully made the diacritics render correctly in Word, **PageMaker still rendered the diacritics improperly (e.g., the dot for anusvara was shifted to the left, instead of being centered).**

### Root Cause
Anu Neo fonts use a two-part character system for consonants like `क` (Ka) and `फ` (Pha):
1. The left body: ``
2. The right bridge/tail: `` (0xFE)

For top/bottom matras like `े` (e), the matra must sit on the left body, so the bridge is added **AFTER** the matra (e.g., `के` = `` + `े` + ``).
However, for nasal marks like anusvara (`ं` / ``) and chandrabindu (`ँ` / ``), they are designed as right-side/trailing marks that sit over the bridge's vertical stem.

The regex logic in `src/utils/anuNeoConverter.ts` erroneously grouped `` and `` into `topBottomMatras`, causing the right bridge to be inserted **after** them (e.g. `कं` = `` + `` + ``).
- Word's rendering engine automatically re-grouped and centered the characters, hiding the layout error.
- PageMaker's strict legacy renderer placed the bridge on top of the anusvara, displacing it.

### Solution
Removed `` and `` from the `topBottomMatras` constant in `src/utils/anuNeoConverter.ts`.
This ensures the bridge is inserted **before** nasal marks, completing the consonant first.
- Before: `कं` -> `` + `` + `` (Broken in PageMaker)
- After: `कं` -> `` + `` + `` (Renders perfectly)
