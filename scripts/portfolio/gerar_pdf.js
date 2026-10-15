// Gera assets/portfolio/portfolio-gestecno.pdf a partir de portfolio.html.
// Requer Node e Playwright (npm i -D playwright && npx playwright install chromium).
// Uso, na raiz do projeto:  node scripts/portfolio/gerar_pdf.js
const path = require("path");
const { chromium } = require("playwright");

(async () => {
  const src = path.join(__dirname, "portfolio.html");
  const out = path.join(__dirname, "..", "..", "assets", "portfolio", "portfolio-gestecno.pdf");
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto("file://" + src, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: out, format: "A4", landscape: true, printBackground: true, preferCSSPageSize: true });
  await browser.close();
  console.log("PDF gerado em", out);
})();
