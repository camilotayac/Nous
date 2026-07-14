#!/usr/bin/env node
/**
 * Master Orchestrator: Presentation Pipeline
 * Runs all 3 experts in sequence, repeats until 3 consecutive successes.
 * Usage: node run_pipeline.js <subcarpeta_name> [obsidian_source]
 * Exit code: 0 = 3 consecutive successes, 1 = failed after max retries
 */

const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const subcarpeta = process.argv[2];
const source = process.argv[3]; // optional: path to obsidian note

if (!subcarpeta) {
  console.error('Usage: node run_pipeline.js <subcarpeta_name> [obsidian_source]');
  process.exit(1);
}

const baseDir = __dirname;
const MAX_SUCCESSES = 3;
const MAX_RETRIES = 10;
let consecutiveSuccesses = 0;
let attempt = 0;

console.log('╔═══════════════════════════════════════════════╗');
console.log('║    PRESENTATION PIPELINE ORCHESTRATOR        ║');
console.log('║    Target: 3 consecutive zero-error runs     ║');
console.log('╚═══════════════════════════════════════════════╝\n');
console.log(`Subcarpeta: ${subcarpeta}`);
if (source) console.log(`Source: ${source}`);
console.log('');

while (consecutiveSuccesses < MAX_SUCCESSES && attempt < MAX_RETRIES) {
  attempt++;
  console.log(`\n${'═'.repeat(50)}`);
  console.log(`  ATTEMPT ${attempt} of ${MAX_RETRIES} (consecutive successes: ${consecutiveSuccesses}/${MAX_SUCCESSES})`);
  console.log(`${'═'.repeat(50)}`);

  let hasErrors = false;

  // ── Expert 1: Validate tema.md ──
  console.log('\n── Expert 1: tema.md Validation ──');
  const temaPath = path.join(baseDir, subcarpeta, 'tema.md');
  try {
    const result1 = execSync(`node "${path.join(baseDir, 'validate_tema.js')}" "${temaPath}"`, {
      encoding: 'utf8',
      stdio: 'pipe'
    });
    console.log(result1);
  } catch (err) {
    console.log(err.stdout || '');
    console.error(err.stderr || err.message);
    hasErrors = true;
  }

  // ── Expert 2: Validate HTML ──
  console.log('\n── Expert 2: HTML Presentation Validation ──');
  try {
    const result2 = execSync(`node "${path.join(baseDir, 'validate_html.js')}" "${subcarpeta}"`, {
      encoding: 'utf8',
      stdio: 'pipe'
    });
    console.log(result2);
  } catch (err) {
    console.log(err.stdout || '');
    console.error(err.stderr || err.message);
    hasErrors = true;
  }

  // ── Expert 3: Generate & Validate PDF ──
  console.log('\n── Expert 3: PDF Generation & Validation ──');
  try {
    const result3 = execSync(`node "${path.join(baseDir, 'validate_pdf.js')}" "${subcarpeta}"`, {
      encoding: 'utf8',
      stdio: 'pipe',
      timeout: 30000
    });
    console.log(result3);
  } catch (err) {
    console.log(err.stdout || '');
    console.error(err.stderr || err.message);
    hasErrors = true;
  }

  // ── Evaluate result ──
  if (hasErrors) {
    consecutiveSuccesses = 0;
    console.log(`\n❌ Attempt ${attempt} FAILED — resetting consecutive count`);
  } else {
    consecutiveSuccesses++;
    console.log(`\n✅ Attempt ${attempt} PASSED — consecutive successes: ${consecutiveSuccesses}/${MAX_SUCCESSES}`);
  }
}

console.log('\n' + '═'.repeat(50));
if (consecutiveSuccesses >= MAX_SUCCESSES) {
  console.log(`🎉 PIPELINE COMPLETE — ${MAX_SUCCESSES} consecutive successes!`);
  console.log(`   tema.md: ${path.join(baseDir, subcarpeta, 'tema.md')}`);
  console.log(`   PDF: ${path.join(baseDir, subcarpeta, 'presentacion.pdf')}`);
  process.exit(0);
} else {
  console.log(`⚠️  PIPELINE INCOMPLETE — reached max retries (${MAX_RETRIES})`);
  console.log(`   Last consecutive successes: ${consecutiveSuccesses}`);
  process.exit(1);
}
