#!/usr/bin/env node
/**
 * Expert 3: PDF Generator & Validator
 * Generates PDF from presentacion.html and validates the output.
 * Usage: node validate_pdf.js <subcarpeta_name>
 * Exit code: 0 = pass, 1 = errors found
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const subcarpeta = process.argv[2];
if (!subcarpeta) {
  console.error('Usage: node validate_pdf.js <subcarpeta_name>');
  process.exit(1);
}

(async () => {
  const baseDir = __dirname;
  const temaPath = path.resolve(baseDir, subcarpeta, 'tema.md');
  const rootTemaPath = path.resolve(baseDir, 'tema.md');
  const pdfPath = path.resolve(baseDir, subcarpeta, 'presentacion.pdf');
  const htmlPath = path.resolve(baseDir, 'presentacion.html');

  console.log('\n═══════════════════════════════════════');
  console.log('  EXPERT 3: PDF Generator & Validator');
  console.log('═══════════════════════════════════════\n');

  // ── 1. Pre-flight checks ──
  if (!fs.existsSync(temaPath)) {
    console.error(`❌ tema.md not found: ${temaPath}`);
    process.exit(1);
  }

  if (!fs.existsSync(htmlPath)) {
    console.error(`❌ presentacion.html not found: ${htmlPath}`);
    process.exit(1);
  }

  const temaContent = fs.readFileSync(temaPath, 'utf8').trim();
  if (temaContent.length === 0) {
    console.error('❌ tema.md is empty');
    process.exit(1);
  }

  // ── 2. Copy tema.md to root for HTML loading ──
  fs.copyFileSync(temaPath, rootTemaPath);
  console.log(`📋 Copied tema.md to root for loading`);

  let browser;
  try {
    // ── 3. Launch Puppeteer ──
    console.log('🚀 Launching Puppeteer...');
    browser = await puppeteer.launch({
      headless: true,
      args: ['--allow-file-access-from-files', '--no-sandbox']
    });
    const page = await browser.newPage();

    // ── 4. Load presentation ──
    console.log(`📄 Loading presentation...`);
    await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0', timeout: 15000 });

    // ── 5. Wait for content to load ──
    const hasContent = await page.evaluate(() => {
      const track = document.getElementById('track');
      return track && track.children.length > 0;
    });

    if (!hasContent) {
      console.error('❌ Presentation loaded but no content rendered');
      console.error('   The fetch/XHR may have failed. Check file:// permissions.');
      process.exit(1);
    }

    // ── 6. Check slide count ──
    const slideCount = await page.evaluate(() => {
      return document.querySelectorAll('.paragraph-block').length;
    });

    if (slideCount === 0) {
      console.error('❌ No slides found in presentation');
      process.exit(1);
    }

    console.log(`📊 Found ${slideCount} slides`);

    // ── 7. Prepare for print (reveal all steps) ──
    console.log('🖨️  Preparing for print...');
    await page.evaluate(() => {
      if (typeof window.prepareForPrint === 'function') {
        window.prepareForPrint();
      }
    });

    // ── 8. Wait for animations ──
    await new Promise(r => setTimeout(r, 1500));

    // ── 9. Set viewport and generate PDF ──
    await page.setViewport({ width: 1920, height: 1080 });

    console.log(`📥 Generating PDF...`);
    await page.pdf({
      path: pdfPath,
      format: 'A4',
      landscape: true,
      printBackground: true,
      margin: { top: '0px', right: '0px', bottom: '0px', left: '0px' }
    });

    // ── 10. Validate PDF output ──
    if (!fs.existsSync(pdfPath)) {
      console.error('❌ PDF file was not created');
      process.exit(1);
    }

    const stats = fs.statSync(pdfPath);
    const sizeMB = (stats.size / 1024 / 1024).toFixed(2);

    if (stats.size === 0) {
      console.error('❌ PDF file is empty');
      process.exit(1);
    }

    if (stats.size > 5 * 1024 * 1024) {
      console.log(`⚠️  PDF is large: ${sizeMB} MB (recommended < 5 MB)`);
    }

    console.log(`\n✅ PASSED — PDF generated successfully`);
    console.log(`   Path: ${pdfPath}`);
    console.log(`   Size: ${sizeMB} MB`);
    console.log(`   Slides: ${slideCount}`);

  } catch (err) {
    console.error(`\n❌ ERROR during PDF generation: ${err.message}`);
    process.exit(1);
  } finally {
    // ── Cleanup: remove root tema.md ──
    if (fs.existsSync(rootTemaPath)) {
      fs.unlinkSync(rootTemaPath);
      console.log('🧹 Cleaned up root tema.md');
    }
    if (browser) await browser.close();
  }
})();
