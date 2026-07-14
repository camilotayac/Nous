#!/usr/bin/env node
/**
 * Expert 1: tema.md Validator
 * Validates structure, delimiters, colors, LaTeX, and cognitive load rules.
 * Usage: node validate_tema.js <path_to_tema.md>
 * Exit code: 0 = pass, 1 = errors found
 */

const fs = require('fs');
const path = require('path');

const file = process.argv[2];
if (!file) {
  console.error('Usage: node validate_tema.js <path_to_tema.md>');
  process.exit(1);
}

if (!fs.existsSync(file)) {
  console.error(`ERROR: File not found: ${file}`);
  process.exit(1);
}

const content = fs.readFileSync(file, 'utf8');
const lines = content.split('\n');
const errors = [];
const warnings = [];

// ── 1. Structure: @title must be first ──
const firstTag = lines.find(l => l.trim().startsWith('@'));
if (!firstTag || !firstTag.trim().startsWith('@title')) {
  errors.push('Structure: First tag must be @title');
}

// ── 2. Must have @vocab after @title ──
const tagOrder = lines.filter(l => l.trim().startsWith('@')).map(l => l.trim());
const vocabIdx = tagOrder.indexOf('@vocab');
const titleIdx = tagOrder.indexOf('@title');
if (vocabIdx === -1) {
  errors.push('Structure: Missing @vocab section');
} else if (vocabIdx !== titleIdx + 1) {
  errors.push('Structure: @vocab must come immediately after @title');
}

// ── 3. Must have @last at the end ──
const lastTag = tagOrder[tagOrder.length - 1];
if (lastTag !== '@last') {
  errors.push('Structure: Last tag must be @last (resumen)');
}

// ── 4. Sequential numbering (@1, @2, @3...) ──
const slideTags = tagOrder.filter(t => /^@\d+[a-z]*$/.test(t));
const baseNumbers = [...new Set(slideTags.map(t => parseInt(t.match(/^@(\d+)/)[1])))];
for (let i = 0; i < baseNumbers.length; i++) {
  if (baseNumbers[i] !== i + 1) {
    errors.push(`Structure: Slide numbering gap - expected @${i + 1}, found @${baseNumbers[i]}`);
  }
}

// ── 5. Max 3 sub-steps per slide (e.g., @1a, @1b, @1c) ──
const subStepCounts = {};
for (const tag of slideTags) {
  const m = tag.match(/^@(\d+)([a-z]*)$/);
  if (m) {
    const base = m[1];
    if (!subStepCounts[base]) subStepCounts[base] = [];
    subStepCounts[base].push(tag);
  }
}
for (const [base, tags] of Object.entries(subStepCounts)) {
  if (tags.length > 3) {
    errors.push(`Cognitive load: Slide @${base} has ${tags.length} sub-steps (max 3)`);
  }
}

// ── 6. Total slides max 10 ──
if (baseNumbers.length > 10) {
  warnings.push(`Cognitive load: ${baseNumbers.length} slides (recommended max 10)`);
}

// ── 7. Color syntax validation ──
const colorPattern = /\{([rgby]):([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}/g;
const highlightPattern = /\[([rgby]):([^\]]*)\]/g;
let match;
const invalidColors = [];

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  // Check {color:text} syntax
  const colorRegex = /\{([rgby]):/g;
  while ((match = colorRegex.exec(line)) !== null) {
    const colorCode = match[1];
    if (!['r', 'g', 'b', 'y'].includes(colorCode)) {
      errors.push(`Color: Invalid color code "${colorCode}" on line ${i + 1}`);
    }
  }
  // Check [color:text] syntax
  const hlRegex = /\[([rgby]):/g;
  while ((match = hlRegex.exec(line)) !== null) {
    const colorCode = match[1];
    if (!['r', 'g', 'b', 'y'].includes(colorCode)) {
      errors.push(`Color: Invalid highlight code "${colorCode}" on line ${i + 1}`);
    }
  }
}

// ── 8. LaTeX formula validation ──
const formulaPattern = /\$([^$]+)\$/g;
for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  let fMatch;
  const fRegex = /\$([^$]+)\$/g;
  while ((fMatch = fRegex.exec(line)) !== null) {
    const formula = fMatch[1];
    // Check for balanced braces in formula
    let braceCount = 0;
    for (const ch of formula) {
      if (ch === '{') braceCount++;
      if (ch === '}') braceCount--;
      if (braceCount < 0) {
        errors.push(`LaTeX: Unbalanced closing brace in formula on line ${i + 1}: ${formula.substring(0, 40)}...`);
        break;
      }
    }
    if (braceCount !== 0) {
      errors.push(`LaTeX: Unbalanced opening braces in formula on line ${i + 1}: ${formula.substring(0, 40)}...`);
    }
    // Check fraction syntax: /frac{n}{d} not \frac{n}{d}
    if (formula.includes('\\frac')) {
      errors.push(`LaTeX: Use /frac (forward slash) not \\frac (backslash) on line ${i + 1}`);
    }
    // Check sout syntax
    if (formula.includes('\\sout')) {
      errors.push(`LaTeX: Use /sout (forward slash) not \\sout (backslash) on line ${i + 1}`);
    }
  }
}

// ── 9. Vocab section must have definitions ──
const vocabStart = lines.findIndex(l => l.trim() === '@vocab');
if (vocabStart !== -1) {
  const vocabLines = [];
  for (let i = vocabStart + 1; i < lines.length; i++) {
    if (lines[i].trim().startsWith('@')) break;
    vocabLines.push(lines[i]);
  }
  const vocabItems = vocabLines.filter(l => l.trim().startsWith('-'));
  if (vocabItems.length === 0) {
    warnings.push('Vocab: No vocabulary items found in @vocab section');
  }
  for (const item of vocabItems) {
    if (!item.includes('**') || !item.includes(':')) {
      warnings.push(`Vocab: Item should use **bold**:definition format: "${item.trim().substring(0, 50)}"`);
    }
  }
}

// ── 10. Check for common mistakes ──
for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  // Unicode subscripts (should use LaTeX _)
  if (/[₀₁₂₃₄₅₆₇₈₉]/.test(line) && !line.trim().startsWith('%')) {
    warnings.push(`Unicode: Found subscript characters on line ${i + 1} - use LaTeX _ instead`);
  }
  // Units without space
  if (/\d+(g|mol|M|s|L)\b/.test(line) && !line.trim().startsWith('%')) {
    warnings.push(`Formatting: Missing space between number and unit on line ${i + 1}`);
  }
  // Unresolved references
  if (/\[@[^\]]+\]/.test(line)) {
    warnings.push(`Reference: Found [@reference] on line ${i + 1} - should be removed for slides`);
  }
}

// ── Output results ──
console.log('\n═══════════════════════════════════════');
console.log('  EXPERT 1: tema.md Validator');
console.log('═══════════════════════════════════════\n');

if (errors.length === 0 && warnings.length === 0) {
  console.log('✅ PASSED — tema.md structure is valid');
  console.log(`   Slides: ${baseNumbers.length}`);
  console.log(`   Total sub-steps: ${slideTags.length}`);
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
