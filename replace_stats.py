with open("src/components/TextConverter.astro", "r") as f:
    lines = f.readlines()

new_content = """  <!-- Bottom Stats Bar -->
  <div class="flex flex-wrap items-center justify-between gap-3 px-3 py-2 bg-[var(--canvas-soft)] border border-[var(--hairline)] rounded-lg text-[11px] font-mono text-[var(--ink-secondary)]">
    <div class="flex items-center gap-3 flex-shrink-0">
      <span>Lines: <strong id="lines-stat" class="text-[var(--ink)]">0</strong></span>
      <span>•</span>
      <span>Words: <strong id="words-stat" class="text-[var(--ink)]">0</strong></span>
    </div>
    <div class="flex items-center">
      <a href="/contact" class="flex items-center gap-1.5 text-[11px] font-sans font-medium text-[var(--ink-secondary)] hover:text-[var(--ink)] transition-colors bg-[var(--canvas)] hover:bg-[var(--canvas-soft-2)] border border-[var(--hairline)] px-2.5 py-1 rounded-md shadow-2xs">
        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
        Wrong output? Need a new font? Contact us
      </a>
    </div>
  </div>"""

for i in range(len(lines)):
    if '<!-- Bottom Stats Bar -->' in lines[i]:
        lines[i:i+8] = [new_content + "\n"]
        break

with open("src/components/TextConverter.astro", "w") as f:
    f.writelines(lines)
