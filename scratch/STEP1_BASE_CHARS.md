# Step 1: Base Characters Verification (Vowels & Consonants)

This document tracks verification for **Independent Vowels**, **Base Consonants**, and **Base Consonants with Virama/Pollu**.

## 1. Independent Vowels (స్వతంత్ర అచ్చులు)

| Unicode | Name | Shree-Lipi Glyph Code | Glyph / Char | Verified | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| అ | A | `0x0041` | `A` | ⏳ Pending | |
| ఆ | AA | `0x0042` | `B` | ⏳ Pending | |
| ఇ | I | `0x0043` | `C` | ⏳ Pending | |
| ఈ | II | `0x0044` | `D` | ⏳ Pending | |
| ఉ | U | `0x0045` | `E` | ⏳ Pending | |
| ఊ | UU | `0x0046` | `F` | ⏳ Pending | |
| ఋ | R | `0x0192` | `ƒ` | ⏳ Pending | |
| ౠ | RR | `0x0192` + `...` | `ƒ` + matra | ⏳ Pending | Check if Shree-Lipi has distinct glyph |
| ఎ | E | `0x0047` | `G` | ⏳ Pending | |
| ఏ | EE | `0x0048` | `H` | ⏳ Pending | |
| ఐ | AI | `0x0049` | `I` | ⏳ Pending | |
| ఒ | O | `0x004A` | `J` | ⏳ Pending | |
| ఓ | OO | `0x004B` | `K` | ⏳ Pending | |
| ఔ | AU | `0x004C` | `L` | ⏳ Pending | |
| అం | Am | `A` + `0x00FD` | `Aý` | ⏳ Pending | Anusvara check |
| అః | Aha | `A` + `0x00A6` | `A¦` | ⏳ Pending | Visarga check |

---

## 2. Base Consonants (హల్లులు - సహజ రూపం / Talakattu)

In Shree-Lipi Telugu, some consonants have a built-in top tick (Talakattu), while others require an explicit Talakattu mark (`0x0060` or similar), and some never take a Talakattu (e.g. ఖ, ఙ, ఛ, ఝ, ఞ, ట, ఠ, ఢ, ఫ, ఱ).

| Unicode | Consonant | Shree-Lipi Base Code | Talakattu Needed? | Shree-Lipi Full Form | Verified | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| క | Ka | `a` (`0x0061`) | Yes | `a` + tick or standalone? | ⏳ Pending | |
| ఖ | Kha | `Q` (`0x0051`) | No | `Q` | ⏳ Pending | No tick |
| గ | Ga | `V` (`0x0056`) | Yes | `V` | ⏳ Pending | |
| ఘ | Gha | `R` (`0x0052`) | Yes | `R` | ⏳ Pending | |
| ఙ | Nga | `Z` (`0x005A`) | No | `Z` | ⏳ Pending | |
| చ | Cha | `^` (`0x005E`) | Yes | `^` | ⏳ Pending | |
| ఛ | Chha | `b` (`0x0062`) | No | `b` | ⏳ Pending | |
| జ | Ja | `\` (`0x005C`) | Yes | `\` | ⏳ Pending | |
| ఝ | Jha | `m` (`0x006D`) | No | `m` | ⏳ Pending | |
| ఞ | Nya | `p` (`0x0070`) | No | `p` | ⏳ Pending | |
| ట | Tta | `r` (`0x0072`) | No | `r` | ⏳ Pending | |
| ఠ | Ttha | `u` (`0x0075`) | No | `u` | ⏳ Pending | |
| డ | Dda | `y` (`0x0079`) | Yes | `y` | ⏳ Pending | |
| ఢ | Ddha | `\|` (`0x007C`) | No | `\|` | ⏳ Pending | |
| ణ | Nna | `~` (`0x007E`) | Yes | `~` | ⏳ Pending | |
| త | Ta | `™` (`0x2122`) | Yes | `™` | ⏳ Pending | |
| థ | Tha | `£` (`0x00A3`) | Yes | `£` | ⏳ Pending | |
| ద | Da | `§` (`0x00A7`) | Yes | `§` | ⏳ Pending | |
| ధ | Dha | `®` (`0x00AE`) | Yes | `®` | ⏳ Pending | |
| న | Na | `¯` (`0x00AF`) | Yes | `¯` | ⏳ Pending | |
| ప | Pa | `²` (`0x00B2`) | Yes | `²` | ⏳ Pending | |
| ఫ | Pha | `¸` (`0x00B8`) | No | `¸` | ⏳ Pending | |
| బ | Ba | `º` (`0x00BA`) | Yes | `º` | ⏳ Pending | |
| భ | Bha | `¿` (`0x00BF`) | Yes | `¿` | ⏳ Pending | |
| మ | Ma | `Ä` (`0x00C4`) | Yes | `Ä` | ⏳ Pending | |
| య | Ya | `Å` (`0x00C5`) | Yes | `Å` | ⏳ Pending | |
| ర | Ra | `ˆ` (`0x02C6`) | Yes | `ˆ` | ⏳ Pending | |
| ఱ | Rra | `‚` (`0x201A`) | No | `‚` | ⏳ Pending | |
| ల | La | `Ë` (`0x00CB`) | Yes | `Ë` | ⏳ Pending | |
| ళ | Lla | `Ã` (`0x00C3`) | Yes | `Ã` | ⏳ Pending | |
| వ | Va | `Ð` (`0x00D0`) | Yes | `Ð` | ⏳ Pending | |
| శ | Sha | `Ô` (`0x00D4`) | Yes | `Ô` | ⏳ Pending | |
| ష | Ssa | `Ù` (`0x00D9`) | Yes | `Ù` | ⏳ Pending | |
| స | Sa | `Ü` (`0x00DC`) | Yes | `Ü` | ⏳ Pending | |
| హ | Ha | `˜` (`0x02DC`) | Yes | `˜` | ⏳ Pending | |
| క్ష | Ksha | `„` (`0x201E`) | Yes | `„` | ⏳ Pending | Special Conjunct |

---

## 3. Consonants with Virama / Pollu (పొల్లు హల్లులు)
Example: `క్`, `ఖ్`, `గ్`, `ఘ్`... (Halant `0x0C4D`)

| Unicode | Pollu Glyph | Verified | Notes |
| :--- | :--- | :--- | :--- |
| క్ ... హ్ | Consonant + Pollu mark (`0x0078` / `x` or special) | ⏳ Pending | |

---

## Test & Verification Runner
We will generate a visual test card using `PIL` with font `public/SHREE-TEL.ttf` comparing:
1. Expected visual appearance.
2. Converter output.
