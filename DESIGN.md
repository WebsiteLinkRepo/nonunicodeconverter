---
version: 8.0.0-final
name: Volumetric-Spotlight-Soft-Icy-Mist
description: A zero-dependency HTML5 `<canvas>` effect rendering a frozen, mathematically dispersed volumetric light cone. Features multi-theme support (Dark Void / Soft Icy Mist), bulletproof high-res scaling, targeted gap-fill rays, and universal blending for realistic shadows.

colors:
  # Dark Mode Tokens (Cinematic Void)
  canvas-dark: "#08090b"
  text-dark-main: "#f5f5f5"
  text-dark-muted: "#aaa"
  border-dark: "#292c30"
  badge-bg-dark: "rgba(0,0,0,0.18)"
  badge-border-dark: "#3a3c40"
  btn-primary-bg-dark: "#eee"
  btn-primary-text-dark: "#111"
  btn-sec-bg-dark: "rgba(255,255,255,0.025)"
  btn-sec-border-dark: "#67686b"
  nav-bg-dark: "rgba(9,10,12,0.48)"
  divider-dark: "rgba(255,255,255,0.04)"
  ray-dark-core: "255, 255, 255" # Pure White (Screen Blend)
  vignette-dark-edge: "rgba(0,0,0,0.45)"
  
  # Light Mode Tokens (Soft Icy Mist)
  canvas-light: "#e6f0fa" # Soft, premium icy mist
  text-light-main: "#0b172a" # Deep frosty navy
  text-light-muted: "#576d8b" # Cool steel blue
  border-light: "#c2d6eb"
  badge-bg-light: "rgba(45, 85, 150, 0.08)"
  badge-border-light: "#a3c0df"
  btn-primary-bg-light: "#112240"
  btn-primary-text-light: "#fff"
  btn-sec-bg-light: "rgba(45, 85, 150, 0.04)"
  btn-sec-border-light: "#a3c0df"
  nav-bg-light: "rgba(230, 240, 250, 0.75)"
  divider-light: "rgba(45, 85, 150, 0.12)"
  ray-light-shadows: "45, 85, 150" # Frosty Slate-Blue (Multiply Blend)
  light-core-origin: "255, 255, 255" # Subtle White Glow
  vignette-light-edge: "rgba(45, 85, 150, 0.18)"
  
  # Shared Tokens
  grain-opacity: "0.075"

typography:
  hero-emphasis-dark:
    background: "linear-gradient(180deg, #ffffff 0%, #9ca3af 100%)"
  hero-emphasis-light:
    background: "linear-gradient(180deg, #0b172a 0%, #4a6280 100%)"

spacing:
  origin-y: "-12%"
  light-bleed-y: "120%"
---

## Architectural Rules

The Volumetric Spotlight is a mathematically static, zero-loop canvas render to ensure zero idle CPU usage. 

**Key Visual Characteristics:**
- **Inverted Volumetrics:** Pure white light cuts through Dark Mode using a `screen` composite. Frosty slate-blue shadow rays cut through Light Mode using a `multiply` composite against a subtle white core.
- **Universal Blending:** The `globalCompositeOperation` wraps **ALL** rays (both broad and thin) to ensure Light Mode shadows physically cut through the core glow without being washed out.
- **Subtle Dust:** Particle dust is locked to pure white in both modes to avoid looking like dark dirt smudges against bright backgrounds.
- **Bulletproof Crispness:** `window.devicePixelRatio` is fully unlocked, utilizing `Math.round()` for exact physical pixel mapping. The SVG grain uses a strict `background-size: 150px; background-repeat: repeat;` to prevent stretching and blockiness at maximum browser zoom.

## Mandatory Ray Anchors

To prevent unnatural gaps and ensure a bold central focal point, the procedural trigonometric loop relies on two explicitly injected, hardcoded rays for both the broad and thin passes:
1. **Left Gap Fill:** `q: -0.17` (Plugs a natural mathematical void on the left side).
2. **Dead Center Pillar:** `q: 0` (Forces a perfectly vertical, dominant light beam down the center of the screen).

## AI Implementation Guardrails

**DO NOT REWRITE THE CANVAS MATH.** The `<canvas id="fx">` engine, its targeted ray injections, and its composite wrapping have been meticulously manually calibrated. AI agents must integrate the exact provided JavaScript logic character-for-character and limit their modifications strictly to the surrounding DOM, CSS UI components, and global state management.