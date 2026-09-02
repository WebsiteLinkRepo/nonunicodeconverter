# Shree-Lipi Telugu Conversion Extraction Instructions

Please convert the contents of `scratch/TELUGU_ALL_IN_ONE_INPUT.txt` using the competitor's converter tool with **Shree-Lipi (Telugu / Shree-Tel)** selected.

1. Open the competitor tool.
2. Select Source as **Unicode** and Target as **Shree-Lipi (Telugu / Shree-Tel)**.
3. Paste all contents from `scratch/TELUGU_ALL_IN_ONE_INPUT.txt` and convert.
4. Copy the entire output and paste it into `scratch/TELUGU_ALL_IN_ONE_OUTPUT.txt`.

Once you have saved `scratch/TELUGU_ALL_IN_ONE_OUTPUT.txt`, I will:
- Map every vowel, consonant, gunintham, conjunct (vatthu), and complex cluster directly to the glyphs of `Shree-Tel-0908 Regular.ttf`.
- Verify every glyph using visual rendering and automated diff testing.
- Integrate the converter into the codebase (`shreeLipiTeluguConverter.ts`, UI dropdowns, font previews, and font family linking).
