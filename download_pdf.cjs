const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  try {
    await page.goto('https://pdfcoffee.com/download/anu-keyboard-pdf-free.html', { waitUntil: 'networkidle', timeout: 30000 });
    console.log("Page loaded!");
    
    // Attempt to extract PDF link if available, or just take a screenshot
    await page.screenshot({ path: 'pdfcoffee.png', fullPage: true });
    console.log("Screenshot saved as pdfcoffee.png");
    
    // Get page content
    const html = await page.content();
    require('fs').writeFileSync('pdfcoffee.html', html);
    
  } catch (e) {
    console.error("Error:", e);
  }
  
  await browser.close();
})();
