# Fix SEO & Routing Problems — Plan

## What's NOT being touched
- `src/utils/seoRoutes.ts` — converter logic is perfect, don't touch
- `src/pages/[converter].astro` — perfect
- `src/pages/[lang]/[converter].astro` — perfect
- `src/components/TextConverter.astro` — perfect
- No page files in `src/pages/` or `src/pages/[lang]/` (structure is correct)
- No changes to the multi-page SEO font routing strategy

## What IS being fixed (all in `src/layouts/Layout.astro`)

### Fix 1: Canonical URL (line 22) — CRITICAL SEO
**Current (broken):**
```js
const canonicalUrl = Astro.url.pathname === '/' 
  ? 'https://nonunicodeconverter.com/' 
  : `https://nonunicodeconverter.com/${lang}`;
```
Every page except `/` has its canonical pointing to the language homepage. Google thinks `/about`, `/unicode-to-priyanka-converter`, `/te/unicode-to-anu-converter` are all duplicates of the homepage.

**Fix:** Build the canonical from the actual pathname:
```js
const pathname = Astro.url.pathname.replace(/\/$/, '') || '/';
const canonicalUrl = `https://nonunicodeconverter.com${pathname}`;
```
This gives every page its own correct canonical URL.

### Fix 2: Logo link (line 169) — UX
**Current (broken):**
```html
<a href="/">
```
Telugu user on `/te/about` clicks logo → goes to `/` (English) instead of `/te`.

**Fix:**
```html
<a href={lang === 'en' ? '/' : `/${lang}`}>
```
Same pattern as every other nav link already uses.

### Fix 3: Language switcher (lines 311-316) — UX
**Current (broken):**
```js
const targetPath = `/${selectedLang}`;
window.location.href = targetPath;
```
Switching language from `/te/about` goes to `/hi` instead of `/hi/about`. User loses their current page.

**Fix:** Strip the current lang prefix from pathname, then prepend the new one:
```js
langSelect?.addEventListener('change', (e) => {
  const selectedLang = (e.target as HTMLSelectElement).value;
  const currentLang = document.documentElement.lang;
  let path = window.location.pathname.replace(/\/$/, '');
  
  // Strip current lang prefix if present
  if (currentLang !== 'en' && (path === `/${currentLang}` || path.startsWith(`/${currentLang}/`))) {
    path = path.substring(currentLang.length + 1);
  }
  
  // Build new path
  const targetPath = selectedLang === 'en' ? (path || '/') : `/${selectedLang}${path}`;
  window.location.href = targetPath;
});
```

### Fix 4: `/en` duplicate of `/` (line 7-9 of `[lang].astro`) — SEO
**Current:** `[lang].astro` generates an `/en/` page because TRANSLATIONS includes `'en'`. This duplicates `index.astro` which is the canonical English homepage.

**Fix in `src/pages/[lang].astro`:** Filter out `'en'` from getStaticPaths:
```js
export function getStaticPaths() {
  return Object.keys(TRANSLATIONS)
    .filter(l => l !== 'en')
    .map((lang) => ({ params: { lang } }));
}
```

### Fix 5: Hreflang pointing to non-existent pages (lines 96-109) — SEO
**Current:** Every page emits hreflang for all 8 languages. But font-specific converters like `/unicode-to-priyanka-converter` only exist for `en` + `te`. So hreflang points to `/hi/unicode-to-priyanka-converter` which is a 404.

**Fix:** Pass the available languages as a prop from converter pages, and default to all 8 for static pages. Only emit hreflang for languages where the page actually exists.

Approach: Add an optional `availableLangs` prop to Layout. Converter pages pass it from seoRoutes data. Static pages don't pass it (defaults to all 8). The hreflang loop filters to only those languages.

Implementation:
- Add `availableLangs?: Language[]` to Layout's Props interface
- In `seoRoutes.ts`, export a helper to look up which langs have a given converter slug
- In `[converter].astro` and `[lang]/[converter].astro`, pass `availableLangs` to Layout
- In Layout's hreflang loop, filter to `availableLangs` when provided

### Fix 6: og:url uses broken canonical (line 121) — SEO
**Current:** `og:url` uses the same broken `canonicalUrl`. Fix 1 automatically fixes this since both use the same variable.

## Files modified
1. `src/layouts/Layout.astro` — fixes 1, 2, 3, 5, 6
2. `src/pages/[lang].astro` — fix 4
3. `src/utils/seoRoutes.ts` — add helper for available langs (read-only to existing route logic)
4. `src/pages/[converter].astro` — pass availableLangs prop to Layout
5. `src/pages/[lang]/[converter].astro` — pass availableLangs prop to Layout

## Verification
- `astro build` must succeed with no errors
- Spot-check built HTML to confirm canonical URLs are correct
- Confirm `/en/index.html` is no longer generated
