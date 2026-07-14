const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

(async () => {
  try {
    const subcarpeta = process.argv[2] || '01_cinetica_quimica';
    const temaPath = path.resolve(__dirname, subcarpeta, 'tema.md');
    
    // Verificar que tema.md existe (para validación)
    if (!fs.existsSync(temaPath)) {
      console.error(`Error: No se encontró ${temaPath}`);
      process.exit(1);
    }
    
    console.log("Iniciando Puppeteer...");
    const browser = await puppeteer.launch({
      headless: true,
      args: [
        '--allow-file-access-from-files',
        '--font-render-hinting=none',
        '--force-color-profile=srgb'
      ]
    });
    const page = await browser.newPage();
    
    // Emular medio de pantalla para preservar colores en PDF
    await page.emulateMediaType('screen');
    
    // Usar HTML de la subcarpeta si existe, si no usar el principal
    const subcarpetaHtml = path.resolve(__dirname, subcarpeta, 'presentacion.html');
    const rootHtml = path.resolve(__dirname, 'presentacion.html');
    const htmlPath = fs.existsSync(subcarpetaHtml) ? subcarpetaHtml : rootHtml;
    
    console.log(`Cargando presentación: ${htmlPath}...`);
    await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0' });
    
    // Esperar a que se cargue la estructura de diapositivas
    await page.waitForSelector('.paragraph-block');
    
    console.log("Preparando presentación para impresión (revelando todos los pasos)...");
    await page.evaluate(() => {
      if (typeof window.prepareForPrint === 'function') {
        window.prepareForPrint();
      } else {
        console.warn("window.prepareForPrint no está definido");
      }
    });
    
    // Configurar viewport horizontal (Landscape)
    await page.setViewport({ width: 1920, height: 1080 });
    
    const pdfPath = path.resolve(__dirname, subcarpeta, 'presentacion.pdf');
    console.log(`Exportando diapositivas a PDF (formato horizontal)...`);
    
    await page.pdf({
      path: pdfPath,
      format: 'A4',
      landscape: true,
      printBackground: true,
      margin: {
        top: '0px',
        right: '0px',
        bottom: '0px',
        left: '0px'
      }
    });
    
    console.log(`\n¡Éxito! PDF generado correctamente en: ${pdfPath}`);
    await browser.close();
  } catch (err) {
    console.error("\nError durante la exportación:", err.message);
    process.exit(1);
  }
})();
