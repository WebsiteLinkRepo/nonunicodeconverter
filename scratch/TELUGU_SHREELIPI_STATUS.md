# Shree-Lipi Telugu (Shree-Tel-0908) mapping status

Font: `public/SHREE-TEL.ttf` — full name `Shree-Tel-0908`, 217 cmap codes, 219 glyphs.
Byte-identical to `~/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf` (md5 e1c117bb…).

## Method that works (reuse this)

1. **Glyph metrics classify the inventory** (`fontTools` + `BoundsPen`, upem 1000):
   - `advance <= 60` with negative x-bounds → **combining mark** (matra / talakattu / vattu)
   - `advance < ink right edge` → **base form**, designed to be overlaid by a mark
   - otherwise → **standalone / complete form**
   Counts: 34 combining, 42 base, 140 standalone.
   Talakattu = `0xE6` (adv 40, bounds -104..196 → draws left over the preceding base).
2. **Chamfer shape match** (`scratch/tel_match.py`) ranks candidates against a Noto Sans
   Telugu reference. True matches score ~0.6–1.5; anything above ~2.5 is not a match.
   Two-glyph search: `scratch/tel_pair2.py`.
3. **Confirm visually** with `scratch/tel_rows.py out.png 'REF:cand,cand,…'`
   (candidates are `+`-joined hex codes, e.g. `ba+24`). Never trust the matcher alone.

## Verified and fixed

| Item | Was | Now | Evidence |
| --- | --- | --- | --- |
| ఋ | `0x76` | `0xBA 0x24` (approx) | `0x76`/`0x77` are **ఠి/ఠీ**. No single glyph or glyph pair in the font matches ఋ (best 2.9 vs 0.8 for real matches) — the font has no ఋ/ౠ. Emitting బ+kommu as the closest renderable shape. |
| ౠ | `0x77` | `0xBA 0x2A` (approx) | same |
| anusvara ం | `0x30` | `0x2026` | `0x30` = digit zero (adv 543); `0xC6` = ర base (adv 206, overhangs); `0x2026` = free-standing sunna (adv 411) |
| visarga ః | `0x3A` | `0x40` | `0x3A` is the Latin colon (adv 217); `0x40` is the visarga (adv 232) |
| క | `0x61` | `0x4D` | `4d+e6` matches exactly (0.8). `0x61` is a చ-family glyph. |
| ఠ | no talakattu | talakattu | `75+e6` (0.6) |
| ఢ | `0x7C` | `0xC9` + talakattu | `0x7C` is a *combining* mark. `c9+e6` (1.6) |
| ర | `0x2C6` | `0xC6` + talakattu | `c6+e6` (0.7) |
| ళ | `0xC3` | `0xE2` + talakattu | `e2+e6` (1.4). Removed the `ళి`/`ళీ` combos that pointed at `0xE2` (the base). |
| క్ష talakattu | dropped | fixed | `HAS_TALAKATTU` was keyed `'క్ష'`, but క్ష is pre-substituted to `0x201E` before the loop — added `'„': true` |

Also confirmed already-correct: vowels `0x41`–`0x4C`, virama `0xA2`, talakattu `0xE6`,
i-matra `0xEC` (`కి` = `4d+ec`, 0.8), aa-matra `0xE9` (`కా` renders correctly),
and ఖ గ చ ఛ జ ఝ ఞ ట డ త థ ద న ఫ భ వ శ ఱ.

## Still wrong — not yet fixed

**Outright wrong glyph** (renders a different letter):
- **ఘ** → currently `0x52+e6`, which is **ఖ**. Correct code not found; not in the top-6 shortlist, so probably a two-glyph form.
- **ఙ** → currently `0x5a`, a small unrelated mark. Candidates `0x66`/`0x67`/`0x5c` all render జ-like; needs a careful ఙ-vs-జ comparison.
- **మ** → currently `0xC4+e6`, which renders **య**.
- **హ** → currently `0x2DC+e6`, renders a హా-like shape.

**Detached talakattu** — the code uses a *standalone* (already-complete) glyph and then
appends `0xE6`, which floats off to the upper right instead of overlaying. Fix is either
to switch to the adjacent BASE(overhang) code or to set `HAS_TALAKATTU` false:
- ణ (`0x7E` — a *combining* code, so certainly wrong), ధ (`0xAE` — also combining),
  ప (`0xB2`), బ (`0xBA`), య (`0xC5`), ల (`0xCB`), ష (`0xD9`), స (`0xDC`)

**Matras beyond ా / ి**: `కు కూ కృ కె కై` do not match any `base + mark` pair
(best costs 2.2–4.4). Telugu u/uu/vattisuli reshape the base, so this font almost
certainly carries **precomposed** forms per consonant (cf. `0x53`=ఖి, `0x54`=ఖీ).
`ీ` may be `0xEE` rather than `0xED` (`కీ` = `4d+ee`, 1.3) — but `ు` currently occupies
`0xEE`, so both must move together. Left untouched to avoid a collision.

**All 36 vattulu are unverified.** At least `VATTHULU['ధ'] = 0xC9` is wrong — `0xC9` is a
base form (now assigned to ఢ), not a combining mark. `క్ష్మ` renders with a detached
talakattu, so the మ-vattu is wrong too.

## Note on the old fixtures

`scratch/TELUGU_COMPLEX_PARAS_OUTPUT.txt`, `gunintham_output.txt` and `vattulu_output.txt`
are **our own** earlier output, not external ground truth — the paragraph file is
byte-identical to the current converter apart from the anusvara. Do not treat them as
expected values.
