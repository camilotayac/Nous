#!/usr/bin/env node
/**
 * Expert 2: HTML Presentation Validator
 * Validates that presentacion.html exists, has correct structure, and tema.md is loadable.
 * Usage: node validate_html.js <subcarpeta_name>
 * Exit code: 0 = pass, 1 = errors found
 */

const fs = require('fs');
const path = require('path');

const subcarpeta = process.argv[2];
if (!subcarpeta) {
  console.error('Usage: node validate_html.js <subcarpeta_name>');
  process.exit(1);
}

const baseDir = path.resolve(__dirname);
const htmlPath = path.join(baseDir, 'presentacion.html');
const temaPath = path.join(baseDir, subcarpeta, 'tema.md');
const configPath = path.join(baseDir, subcarpeta, 'config.json');
const errors = [];
const warnings = [];

// ── 1. presentacion.html exists ──
if (!fs.existsSync(htmlPath)) {
  errors.push('File: presentacion.html not found');
  console.error('\n❌ FATAL: presentacion.html missing');
  process.exit(1);
}

// ── 2. tema.md exists in subcarpeta ──
if (!fs.existsSync(temaPath)) {
  errors.push(`File: ${subcarpeta}/tema.md not found`);
}

// ── 3. config.json exists ──
if (!fs.existsSync(configPath)) {
  warnings.push(`File: ${subcarpeta}/config.json not found`);
}

// ── 4. HTML has loadTemaMarkdown function ──
const htmlContent = fs.readFileSync(htmlPath, 'utf8');
if (!htmlContent.includes('loadTemaMarkdown')) {
  errors.push('HTML: Missing loadTemaMarkdown function');
}

// ── 5. HTML has XHR fallback for file:// protocol ──
if (!htmlContent.includes('XMLHttpRequest') && !htmlContent.includes('xhr')) {
  warnings.push('HTML: No XMLHttpRequest fallback - may not work with file:// protocol');
}

// ── 6. HTML has parseTemaMarkdown function ──
if (!htmlContent.includes('parseTemaMarkdown')) {
  errors.push('HTML: Missing parseTemaMarkdown function');
}

// ── 7. HTML has color classes ──
const requiredClasses = ['c-red', 'c-green', 'c-blue', 'c-yellow', 'hl-red', 'hl-green', 'hl-blue', 'hl-yellow'];
for (const cls of requiredClasses) {
  if (!htmlContent.includes(cls)) {
    warnings.push(`HTML: Missing color class "${cls}"`);
  }
}

// ── 8. Theme file is not empty ──
if (fs.existsSync(temaPath)) {
  const temaContent = fs.readFileSync(temaPath, 'utf8').trim();
  if (temaContent.length === 0) {
    errors.push('Content: tema.md is empty');
  }
  if (!temaContent.includes('@title')) {
    errors.push('Content: tema.md missing @title tag');
  }
  if (!temaContent.includes('@last')) {
    errors.push('Content: tema.md missing @last tag');
  }
}

// ── 9. Config.json is valid JSON ──
if (fs.existsSync(configPath)) {
  try {
    const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
    if (!config.title) warnings.push('Config: Missing "title" field');
    if (!config.source) warnings.push('Config: Missing "source" field');
    if (!config.slide_count) warnings.push('Config: Missing "slide_count" field');
  } catch (e) {
    errors.push(`Config: Invalid JSON - ${e.message}`);
  }
}

// ── Output results ──
console.log('\n═══════════════════════════════════════');
console.log('  EXPERT 2: HTML Presentation Validator');
console.log('═══════════════════════════════════════\n');

if (errors.length === 0 && warnings.length === 0) {
  console.log('✅ PASSED — HTML presentation is ready');
  console.log(`   Subcarpeta: ${subcarpeta}`);
  console.log(`   HTML: ${htmlPath}`);
  console.log(`   tema.md: ${temaPath}`);
  process.exit(0);
}

if (errors.length > 0) {
  console.log(`❌ ERRORS (${errors.length}):`);
  for (const e of errors) console.log(`   • ${e}`);
}

if (warnings.length > 0) {
  console.log(`\n⚠️  WARNINGS (${warnings.length}):`);
  for (const w of warnings) console.log(`   • ${w}`);
}

console.log('');
process.exit(errors.length > 0 ? 1 : 0);
