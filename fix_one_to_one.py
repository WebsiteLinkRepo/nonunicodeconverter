import re

with open('src/layouts/Layout.astro', 'r') as f:
    layout = f.read()

# 1. We replace the body with a bounded hero container:
body_start = layout.find('<body')
body_end = layout.find('>', body_start) + 1

# Find the end of the body tag
header_start = layout.find('<!-- Main Header Bar -->')
if header_start == -1: header_start = layout.find('<header')

# Let's replace everything from body start to header start
new_body_intro = """<body class="min-h-screen bg-black dark:bg-[#030303] text-[var(--text-main)] font-sans antialiased flex flex-col items-center justify-center p-2 sm:p-4 lg:p-6 selection:bg-[var(--text-main)] selection:text-[var(--bg-color)]">
	<div class="hero relative w-full max-w-[1400px] min-h-[92vh] rounded-xl border border-[var(--border-color)] flex flex-col bg-[var(--bg-color)] shadow-2xl overflow-hidden isolation-isolate transition-colors duration-300">
		<canvas id="fx" class="absolute inset-0 w-full h-full z-0 pointer-events-none"></canvas>
		<div class="grain absolute inset-[-50%] z-[1] pointer-events-none opacity-[0.075] bg-[url('data:image/svg+xml,%3Csvg viewBox=\\'0 0 180 180\\' xmlns=\\'http://www.w3.org/2000/svg\\'%3E%3Cfilter id=\\'n\\'%3E%3CfeTurbulence type=\\'fractalNoise\\' baseFrequency=\\'.85\\' numOctaves=\\'4\\' stitchTiles=\\'stitch\\'/%3E%3C/filter%3E%3Crect width=\\'100%25\\' height=\\'100%25\\' filter=\\'url(%23n)\\' opacity=\\'.7\\'/%3E%3C/svg%3E')] bg-[length:150px] bg-repeat"></div>
"""

# Let's change the header itself to match the image
new_header = """
		<!-- EXTREME 1-to-1 Header -->
		<header class="relative z-10 w-full px-4 sm:px-8 h-16 flex items-center justify-between border-b border-[var(--divider)]">
			<!-- Brand / Logo -->
			<a href="/" class="flex items-center gap-2.5 group cursor-pointer flex-shrink-0">
				<div class="w-6 h-6 rounded flex items-center justify-center bg-[var(--text-main)] text-[var(--bg-color)] font-bold text-sm">
					↑
				</div>
				<span id="logo-title-text" class="font-bold text-sm tracking-tight text-[var(--text-main)]">Unicode2NonUnicode</span>
			</a>

			<!-- Navigation & Tools -->
			<div class="flex items-center gap-4 sm:gap-6 flex-shrink-0">
				<!-- Nav Links -->
				<nav class="hidden md:flex items-center gap-6 text-[13px] font-medium text-[var(--text-muted)]">
					<a href="/" class="hover:text-[var(--text-main)] transition-colors">Converter</a>
					<a href="/about" class="hover:text-[var(--text-main)] transition-colors">About</a>
					<a href="/contact" class="hover:text-[var(--text-main)] transition-colors">Contact</a>
					<a href="/privacy" class="hover:text-[var(--text-main)] transition-colors">Privacy</a>
					<a href="/terms" class="hover:text-[var(--text-main)] transition-colors">Terms</a>
				</nav>

                <!-- Language Selector -->
                <div class="relative flex items-center">
                    <select 
                        id="lang-select" 
                        class="appearance-none bg-transparent text-[var(--text-muted)] hover:text-[var(--text-main)] font-medium border border-[var(--divider)] rounded-md cursor-pointer focus:outline-none text-[13px] px-3 pr-8 py-1.5 transition-colors"
                        aria-label="Select Language"
                    >
                        <option value="en" selected={lang === 'en'} class="bg-[var(--bg-color)] text-[var(--text-main)] py-1">EN</option>
                        <option value="te" selected={lang === 'te'} class="bg-[var(--bg-color)] text-[var(--text-main)] py-1">TE</option>
                    </select>
                    <svg class="w-3.5 h-3.5 text-[var(--text-muted)] absolute right-2.5 pointer-events-none" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7" />
                    </svg>
                </div>

				<!-- Theme Toggle -->
				<button 
					id="theme-toggle-btn" 
					type="button" 
					class="px-3.5 py-1.5 rounded-md border border-[var(--btn-sec-border)] bg-[var(--btn-sec-bg)] text-[13px] font-medium text-[var(--text-main)] hover:bg-[var(--divider)] transition-colors flex items-center justify-center cursor-pointer"
				>
					Toggle Theme
				</button>
			</div>
		</header>
"""

# Replace in layout
# Find header end
header_end = layout.find('</header>') + len('</header>')

# Find spotlight effects and remove it, because we merge it into body
spotlight_start = layout.find('<!-- Spotlight Background Effects -->')
if spotlight_start != -1:
    spotlight_end = layout.find('<!-- Main Header Bar -->')
    layout = layout[:spotlight_start] + layout[spotlight_end:]

# Do the replacement for body start and header
body_start = layout.find('<body')
body_end = layout.find('>', body_start) + 1
header_end = layout.find('</header>') + len('</header>')

layout = layout[:body_start] + new_body_intro + new_header + layout[header_end:]

# Replace the closing body tag to include closing div
closing_body = layout.find('</body>')
if closing_body != -1:
    layout = layout[:closing_body] + "\t</div>\n\t</body>" + layout[closing_body+7:]

# Now let's fix the exact script
script_start = layout.find('// --- Spotlight Canvas Logic ---')
if script_start != -1:
    script_block_start = layout.rfind('<script>', 0, script_start)
    script_block_end = layout.find('</script>', script_start) + len('</script>')
    
    exact_script = """<script> 
const canvas = document.getElementById("fx");
const ctx = canvas.getContext("2d"); 
let W, H, dpr; 

function resize(){ 
 if(!canvas) return;
 const r = canvas.getBoundingClientRect(); 
 W = r.width; H = r.height; 
 dpr = window.devicePixelRatio || 1; 
 canvas.width = Math.round(W * dpr); 
 canvas.height = Math.round(H * dpr); 
 renderStaticCanvas();
} 
window.addEventListener("resize", resize); 

function renderStaticCanvas(){ 
 if(!ctx) return;
 let isLightMode = !document.documentElement.classList.contains('dark');
 ctx.resetTransform();
 ctx.clearRect(0, 0, canvas.width, canvas.height); 
 ctx.scale(dpr, dpr);
 
 const cx = W * 0.5; const cy = -H * 0.12; 
 const bgColor = isLightMode ? "#f8fafc" : "#08090b";
 const cWhite = (alpha) => `rgba(255, 255, 255, ${alpha})`;
 const r = isLightMode ? 15 : 255; const g = isLightMode ? 23 : 255; const b = isLightMode ? 42 : 255;
 const cRay = (alpha) => `rgba(${r}, ${g}, ${b}, ${alpha})`;

 const coreAlpha1 = isLightMode ? 0.35 : 0.12;
 const coreAlpha2 = isLightMode ? 0.15 : 0.05;
 const sourceAlpha = isLightMode ? 0.65 : 0.85;
 const broadAlphaBase = isLightMode ? 0.055 : 0.09;
 const thinAlphaBase = isLightMode ? 0.035 : 0.035;
 
 ctx.fillStyle = bgColor; ctx.fillRect(0, 0, W, H); 
 
 let bg = ctx.createRadialGradient(cx, cy, 0, cx, H * 0.45, H); 
 bg.addColorStop(0, cWhite(coreAlpha1)); bg.addColorStop(0.3, cWhite(coreAlpha2)); bg.addColorStop(1, cWhite(0)); 
 ctx.fillStyle = bg; ctx.fillRect(0, 0, W, H); 
 
 let source = ctx.createRadialGradient(cx, cy, 0, cx, cy, W * 0.2); 
 source.addColorStop(0, cWhite(sourceAlpha)); source.addColorStop(0.1, cWhite(sourceAlpha * 0.5)); source.addColorStop(0.5, cWhite(sourceAlpha * 0.1)); source.addColorStop(1, cWhite(0)); 
 ctx.fillStyle = source; ctx.fillRect(0, 0, W, H); 
 
 ctx.save();
 ctx.globalCompositeOperation = isLightMode ? "multiply" : "screen"; 
 
 const broadRays = [];
 for(let i=0; i<=12; i++) broadRays.push({ i: i, q: (i / 12) - 0.5 });
 broadRays.push({ i: 1, q: -0.17, forceSway: 0 }, { i: 2, q: 0, forceSway: 0 });

 broadRays.forEach(ray => {
     const dist = Math.abs(ray.q) * 2;   
     const staticSway = ray.forceSway !== undefined ? ray.forceSway : Math.sin(ray.i * 2.3) * W * 0.035 * (ray.q < 0 ? -1 : 1);
     const bottomX = cx + (ray.q * W * 1.5) + staticSway;
     const topW = W * 0.025; const botW = W * (0.04 + dist * 0.02);
     const alpha = Math.max(0, broadAlphaBase - dist * (broadAlphaBase * 0.5));
     
     ctx.save(); ctx.filter = `blur(${10 + dist * 8}px)`;
     ctx.beginPath(); ctx.moveTo(cx - topW, cy); ctx.lineTo(cx + topW, cy);
     ctx.lineTo(bottomX + botW, H * 1.2); ctx.lineTo(bottomX - botW, H * 1.2); ctx.closePath();
     
     const grad = ctx.createLinearGradient(cx, cy, bottomX, H * 1.2);
     grad.addColorStop(0, cRay(alpha)); grad.addColorStop(0.3, cRay(alpha * 0.6)); grad.addColorStop(1, cRay(0));
     ctx.fillStyle = grad; ctx.fill(); ctx.restore();
 });
 
 const thinRays = [];
 for(let i=0; i<=20; i++) thinRays.push({ i: i, q: (i / 20) - 0.5 });
 thinRays.push({ i: 1, q: -0.17, forceSway: 0 }, { i: 2, q: 0, forceSway: 0 });

 thinRays.forEach(ray => {
     const dist = Math.abs(ray.q) * 2;
     const staticSway = ray.forceSway !== undefined ? ray.forceSway : Math.cos(ray.i * 3.7) * W * 0.045 * (ray.q < 0 ? -1 : 1);
     const bottomX = cx + (ray.q * W * 1.25) + staticSway;
     const topW = W * 0.008; const botW = W * (0.006 + (ray.i%3===0 ? 0.008 : 0)); 
     const alpha = Math.max(0, thinAlphaBase - dist * (thinAlphaBase * 0.5));
     
     ctx.save(); ctx.filter = "blur(2px)";
     ctx.beginPath(); ctx.moveTo(cx - topW, cy); ctx.lineTo(cx + topW, cy);
     ctx.lineTo(bottomX + botW, H * 1.2); ctx.lineTo(bottomX - botW, H * 1.2); ctx.closePath();
     
     const grad = ctx.createLinearGradient(cx, cy, bottomX, H * 1.2);
     grad.addColorStop(0, cRay(alpha * 2.5)); grad.addColorStop(0.2, cRay(alpha)); grad.addColorStop(1, cRay(0));
     ctx.fillStyle = grad; ctx.fill(); ctx.restore();
 });
 ctx.restore(); 
 
 for(let i=0; i<65; i++){ 
   const px = (Math.sin(i * 17.173)*0.5+0.5) * W; const py = (Math.cos(i * 23.345)*0.5+0.5) * H * 0.95; 
   if(Math.abs(px - cx) < W * 0.45){ 
     const baseA = isLightMode ? 0.15 : 0.015;
     ctx.fillStyle = cWhite(baseA + (baseA * 1.5)*(1 - Math.abs(px - cx)/(W*0.45))); 
     ctx.fillRect(px, py, isLightMode ? 1.5 : 1.2, isLightMode ? 1.5 : 1.2); 
   } 
 } 
 
 let v = ctx.createRadialGradient(cx, H*0.4, W*0.1, cx, H*0.5, W*0.9);
 v.addColorStop(0, "rgba(0,0,0,0)");
 if (isLightMode) { v.addColorStop(0.65, "rgba(15, 23, 42, 0.02)"); v.addColorStop(1, "rgba(15, 23, 42, 0.12)"); }
 else { v.addColorStop(0.65, "rgba(0,0,0,0.06)"); v.addColorStop(1, "rgba(0,0,0,0.45)"); }
 ctx.fillStyle = v; ctx.fillRect(0,0,W,H);
} 
if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(() => resize());
} else {
    setTimeout(resize, 100);
}
const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
        if (mutation.attributeName === 'class') {
            renderStaticCanvas();
        }
    });
});
observer.observe(document.documentElement, { attributes: true });
</script>"""
    layout = layout[:script_block_start] + exact_script + layout[script_block_end:]


with open('src/layouts/Layout.astro', 'w') as f:
    f.write(layout)
