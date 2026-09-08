import re

for filename in ['src/pages/index.astro', 'src/pages/[lang].astro']:
    with open(filename, 'r') as f:
        content = f.read()
    
    old_hero = r'<!-- Hero Section -->\s*<div class="text-center py-2 sm:py-4 space-y-2">\s*<h1 id="page-title" class="text-2xl sm:text-4xl font-bold tracking-tight text-\[var\(--ink\)\]">\s*\{t\.h1\}\s*</h1>\s*<p id="page-subtitle" class="text-xs sm:text-base text-\[var\(--ink-secondary\)\] max-w-2xl mx-auto leading-relaxed">\s*\{t\.subtitle\}\s*</p>\s*</div>'
    
    new_hero = """<!-- Hero Section -->
		<div class="text-center py-6 sm:py-10 space-y-4 z-10 relative">
			<span class="badge mb-2">100% FREE · DTP CONVERTER</span>
			<h1 id="page-title" class="text-3xl sm:text-5xl font-[750] tracking-tight text-[var(--ink)] leading-[1.1]">
				<span class="block">{t.h1.split(' ').slice(0, t.h1.split(' ').length > 3 ? -2 : -1).join(' ')}</span>
				<em class="text-em block mt-1">{t.h1.split(' ').slice(t.h1.split(' ').length > 3 ? -2 : -1).join(' ')}</em>
			</h1>
			<p id="page-subtitle" class="text-sm sm:text-base text-[var(--ink-secondary)] max-w-2xl mx-auto leading-relaxed mt-4">
				{t.subtitle}
			</p>
		</div>"""
    
    content = re.sub(old_hero, new_hero, content, flags=re.DOTALL)
    
    with open(filename, 'w') as f:
        f.write(content)

