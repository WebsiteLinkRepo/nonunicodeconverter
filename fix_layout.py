import re

with open('src/layouts/Layout.astro', 'r') as f:
    content = f.read()

# Replace Ambient Background Glow
glow_pattern = r'<!-- Ambient Background Glow.*?</div>'
replacement = """<!-- Spotlight Background Effects -->
		<div class="fixed inset-0 w-full h-[600px] pointer-events-none -z-10 [mask-image:linear-gradient(to_bottom,black_40%,transparent_100%)]">
			<canvas id="fx" class="absolute inset-0 w-full h-full"></canvas>
			<div class="grain"></div>
		</div>"""
content = re.sub(glow_pattern, replacement, content, flags=re.DOTALL)

# Add spotlight script to the end of the file before </body>
script = """
		<script>
			// --- Spotlight Canvas Logic ---
			const canvas = document.getElementById("fx");
			const ctx = canvas?.getContext("2d");
			let W, H, dpr;

			function renderStaticCanvas() {
				if (!ctx) return;
				const isLightMode = !document.documentElement.classList.contains('dark');

				ctx.resetTransform();
				ctx.clearRect(0, 0, canvas.width, canvas.height);
				ctx.scale(dpr, dpr);

				const cx = W * 0.5;
				const cy = -H * 0.12;

				// Colors based on theme
				const bgColor = isLightMode ? "#f8fafc" : "#08090b";
				const cWhite = (alpha) => `rgba(255, 255, 255, ${alpha})`;
				const r = isLightMode ? 15 : 255;
				const g = isLightMode ? 23 : 255;
				const b = isLightMode ? 42 : 255;
				const cRay = (alpha) => `rgba(${r}, ${g}, ${b}, ${alpha})`;

				const coreAlpha1 = isLightMode ? 0.35 : 0.12;
				const coreAlpha2 = isLightMode ? 0.15 : 0.05;
				const sourceAlpha = isLightMode ? 0.65 : 0.85;

				const broadAlphaBase = isLightMode ? 0.035 : 0.09;
				const thinAlphaBase = isLightMode ? 0.02 : 0.035;

				// Background
				ctx.fillStyle = bgColor;
				ctx.fillRect(0, 0, W, H);

				let bg = ctx.createRadialGradient(cx, cy, 0, cx, H * 0.45, H);
				bg.addColorStop(0, cWhite(coreAlpha1));
				bg.addColorStop(0.3, cWhite(coreAlpha2));
				bg.addColorStop(1, cWhite(0));
				ctx.fillStyle = bg;
				ctx.fillRect(0, 0, W, H);

				let source = ctx.createRadialGradient(cx, cy, 0, cx, cy, W * 0.2);
				source.addColorStop(0, cWhite(sourceAlpha));
				source.addColorStop(0.1, cWhite(sourceAlpha * 0.5));
				source.addColorStop(0.5, cWhite(sourceAlpha * 0.1));
				source.addColorStop(1, cWhite(0));
				ctx.fillStyle = source;
				ctx.fillRect(0, 0, W, H);

				// --- 4. Broad Volumetric Soft Beams ---
				const broadRays = [];
				const numBroad = 12;
				for (let i = 0; i <= numBroad; i++) {
					broadRays.push({ i: i, q: (i / numBroad) - 0.5 });
				}
				// PERFECT FIX: Specifically injecting one custom ray to perfectly fill the empty left gap
				broadRays.push({ i: 1, q: -0.17, forceSway: 0 });
				// Dead Center Pillar
				broadRays.push({ i: 5, q: 0, forceSway: 0 });

				broadRays.forEach(ray => {
					const { i, q, forceSway } = ray;
					const dist = Math.abs(q) * 2;
					const direction = q < 0 ? -1 : 1;
					const staticSway = forceSway !== undefined ? forceSway : Math.sin(i * 2.3) * W * 0.035 * direction;

					const bottomX = cx + (q * W * 1.5) + staticSway;
					const topW = W * 0.025;
					const botW = W * (0.04 + dist * 0.02);

					const alpha = Math.max(0, broadAlphaBase - dist * (broadAlphaBase * 0.5));
					const blur = 10 + dist * 8;

					ctx.save();
					ctx.filter = `blur(${blur}px)`;
					ctx.beginPath();
					ctx.moveTo(cx - topW, cy); ctx.lineTo(cx + topW, cy);
					ctx.lineTo(bottomX + botW, H * 1.2); ctx.lineTo(bottomX - botW, H * 1.2);
					ctx.closePath();

					const grad = ctx.createLinearGradient(cx, cy, bottomX, H * 1.2);
					grad.addColorStop(0, cRay(alpha));
					grad.addColorStop(0.3, cRay(alpha * 0.6));
					grad.addColorStop(1, cRay(0));

					ctx.fillStyle = grad; ctx.fill(); ctx.restore();
				});

				// --- 5. Sharp, Disjointed Partitions ---
				ctx.save();
				ctx.globalCompositeOperation = isLightMode ? "multiply" : "screen";
				const thinRays = [];
				const numThin = 20;
				for (let i = 0; i <= numThin; i++) {
					thinRays.push({ i: i, q: (i / numThin) - 0.5 });
				}
				// PERFECT FIX: Matching sharp ray injected exactly in the left gap
				thinRays.push({ i: 1, q: -0.17, forceSway: 0 });
				// Dead Center Pillar
				thinRays.push({ i: 10, q: 0, forceSway: 0 });

				thinRays.forEach(ray => {
					const { i, q, forceSway } = ray;
					const dist = Math.abs(q) * 2;
					const direction = q < 0 ? -1 : 1;
					const staticSway = forceSway !== undefined ? forceSway : Math.cos(i * 3.7) * W * 0.045 * direction;

					const bottomX = cx + (q * W * 1.25) + staticSway;
					const topW = W * 0.008;
					const botW = W * (0.006 + (i % 3 === 0 ? 0.008 : 0));

					const alpha = Math.max(0, thinAlphaBase - dist * (thinAlphaBase * 0.5));

					ctx.save();
					ctx.filter = "blur(2px)";
					ctx.beginPath();
					ctx.moveTo(cx - topW, cy); ctx.lineTo(cx + topW, cy);
					ctx.lineTo(bottomX + botW, H * 1.2); ctx.lineTo(bottomX - botW, H * 1.2);
					ctx.closePath();

					const grad = ctx.createLinearGradient(cx, cy, bottomX, H * 1.2);
					grad.addColorStop(0, cRay(alpha * 2.5));
					grad.addColorStop(0.2, cRay(alpha));
					grad.addColorStop(1, cRay(0));

					ctx.fillStyle = grad; ctx.fill(); ctx.restore();
				});
				ctx.restore();

				// 6. Static Dust Particles
				for (let i = 0; i < 65; i++) {
					const seed1 = i * 17.173;
					const seed2 = i * 23.345;
					const px = (Math.sin(seed1) * 0.5 + 0.5) * W;
					const py = (Math.cos(seed2) * 0.5 + 0.5) * H * 0.95;

					if (Math.abs(px - cx) < W * 0.45) {
						const baseA = isLightMode ? 0.15 : 0.015;
						const alpha = baseA + (baseA * 1.5) * (1 - Math.abs(px - cx) / (W * 0.45));
						ctx.fillStyle = cWhite(alpha);
						ctx.fillRect(px, py, isLightMode ? 1.5 : 1.2, isLightMode ? 1.5 : 1.2);
					}
				}

				// 7. Vignette
				let v = ctx.createRadialGradient(cx, H * 0.4, W * 0.1, cx, H * 0.5, W * 0.9);
				v.addColorStop(0, "rgba(0,0,0,0)");
				if (isLightMode) {
					v.addColorStop(0.65, "rgba(15, 23, 42, 0.02)");
					v.addColorStop(1, "rgba(15, 23, 42, 0.12)");
				} else {
					v.addColorStop(0.65, "rgba(0,0,0,0.06)");
					v.addColorStop(1, "rgba(0,0,0,0.45)");
				}
				ctx.fillStyle = v; ctx.fillRect(0, 0, W, H);
			}

			function resizeCanvas() {
				if (!canvas) return;
				const r = canvas.getBoundingClientRect();
				W = r.width;
				H = r.height;
				dpr = window.devicePixelRatio || 1;
				canvas.width = Math.round(W * dpr);
				canvas.height = Math.round(H * dpr);
				renderStaticCanvas();
			}

			if (canvas) {
				window.addEventListener("resize", resizeCanvas);
				
				// Handle theme changes by observing class changes on document.documentElement
				const observer = new MutationObserver((mutations) => {
					mutations.forEach((mutation) => {
						if (mutation.attributeName === 'class') {
							renderStaticCanvas();
						}
					});
				});
				observer.observe(document.documentElement, { attributes: true });

				// Try to run after fonts are ready
				if (document.fonts && document.fonts.ready) {
					document.fonts.ready.then(() => resizeCanvas());
				} else {
					// Fallback
					setTimeout(resizeCanvas, 100);
				}
                // Initial resize 
                resizeCanvas();
			}
		</script>
	</body>
"""
content = re.sub(r'\s*</body>\s*', script, content)

with open('src/layouts/Layout.astro', 'w') as f:
    f.write(content)

