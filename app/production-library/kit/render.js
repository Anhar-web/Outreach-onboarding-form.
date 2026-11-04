#!/usr/bin/env node
/* Render built slides to PNG and check them.

     node render.js p5 p7 p2      # these posts
     node render.js               # every app/output/<id>/ that has a manifest.json

   For each app/output/<id>/slide-N.html -> slide-N.png (1080x1350, DPR 1), plus
   contact.png (all slides tiled) and check.json. Exits non-zero on any FAIL:
     - fonts: El Messiri 600/700 and Tajawal 500/700 must be loaded (Arabic glyphs)
     - verbatim: text pulled from the rendered DOM, re-joined across split slides,
       must equal posts_draft.json slides_ar exactly (character for character)
     - size floor: no text under 44px
     - bounds: text boxes inside the canvas with >= 60px side margin
   WARNs (printed, written to check.json): text line boxes crossing an element
   marked data-avoid, more than 5 lines on a slide, text into the bottom dots zone.
*/
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const APP = path.resolve(__dirname, '..', '..');
const OUT = path.join(APP, 'output');
const POSTS = JSON.parse(fs.readFileSync(path.join(APP, 'posts_draft.json'), 'utf8'));
const SEP = { none: '', sp: ' ', nl: '\n' };
const FACES = ['700 96px "El Messiri"', '600 72px "El Messiri"', '700 60px "Tajawal"', '500 50px "Tajawal"'];

async function main() {
  let ids = process.argv.slice(2);
  if (!ids.length) ids = fs.readdirSync(OUT).filter(d => fs.existsSync(path.join(OUT, d, 'manifest.json')));
  const launch = {};
  if (process.env.HTTPS_PROXY) launch.proxy = { server: process.env.HTTPS_PROXY };
  const browser = await chromium.launch(launch);
  const ctx = await browser.newContext({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1, ignoreHTTPSErrors: true });
  let failed = false;
  for (const id of ids) failed = (await renderPost(ctx, id)) || failed;
  await browser.close();
  if (failed) { console.error('\nRENDER FAILED: see FAIL lines above'); process.exit(1); }
}

async function renderPost(ctx, id) {
  const dir = path.join(OUT, id);
  const man = JSON.parse(fs.readFileSync(path.join(dir, 'manifest.json'), 'utf8'));
  const post = POSTS.find(p => p.id === id);
  const page = await ctx.newPage();
  const bySrc = {};
  const report = { post: id, slides: [], fail: [], warn: [] };
  const fail = m => { report.fail.push(m); console.log('  FAIL ' + m); };
  const warn = m => { report.warn.push(m); console.log('  warn ' + m); };
  console.log(`${id}: ${man.slides.length} slides`);

  for (const s of man.slides) {
    const file = path.join(dir, s.file);
    await page.goto('file://' + file);
    await page.waitForFunction(() => document.documentElement.dataset.kitReady === '1', null, { timeout: 30000 });
    const fonts = await page.evaluate(async faces => {
      const AR = 'أبجد هوز حطي كلمن';
      await Promise.all(faces.map(f => document.fonts.load(f, AR)));
      await document.fonts.ready;
      return faces.map(f => [f, document.fonts.check(f, AR)]);
    }, FACES);
    for (const [f, ok] of fonts) if (!ok) fail(`${s.file}: font not loaded: ${f}`);

    const info = await page.evaluate(() => {
      const slide = document.querySelector('.slide');
      const segs = [...document.querySelectorAll('[data-seg]')].map(e => ({
        ord: parseFloat(e.dataset.ord), sep: e.dataset.sep, text: e.textContent,
        size: parseFloat(getComputedStyle(e).fontSize),
      })).sort((a, b) => a.ord - b.ord);
      // line boxes of every text element
      const lines = [];
      document.querySelectorAll('[data-seg]').forEach(e => {
        const r = document.createRange(); r.selectNodeContents(e);
        const seen = new Set();
        for (const q of r.getClientRects()) {
          if (q.width < 2) continue;
          const key = Math.round(q.top / 8);
          if (seen.has(key)) continue; seen.add(key);
          const box = e.closest('.tx'); const bq = box ? box.getBoundingClientRect() : null;
          lines.push({ x: q.left, y: q.top, w: q.width, h: q.height, ord: e.dataset.ord, text: e.textContent.slice(0, 24),
                       bx: bq ? bq.left : undefined, bw: bq ? bq.width : undefined });
        }
      });
      const boxes = [...document.querySelectorAll('.tx, .step-tab, .cta-tag')].map(e => {
        const q = e.getBoundingClientRect(); return { cls: e.className, x: q.left, y: q.top, w: q.width, h: q.height,
          over: e.scrollHeight > e.clientHeight + 2 && e.style.height !== '' };
      });
      const avoid = [...document.querySelectorAll('[data-avoid]')].map(e => {
        const q = e.getBoundingClientRect(); const c = e.closest('[data-clip-y]');
        const top = c ? Math.max(q.top, +c.dataset.clipY) : q.top;   // bbox ignores clip-path: clamp to the crop
        return { name: e.dataset.avoid, x: q.left, y: top, w: q.width, h: Math.max(0, q.bottom - top) };
      });
      return { segs, lines, boxes, avoid };
    });

    for (const g of info.segs) if (g.size < 44) fail(`${s.file}: text at ${g.size}px < 44px floor: ${g.text.slice(0, 30)}`);
    for (const b of info.boxes) {
      if (b.x < 60 - 0.5 || b.x + b.w > 1080 - 60 + 0.5 || b.y < 40 || b.y + b.h > 1350 - 40)
        fail(`${s.file}: ${b.cls} box out of bounds (${b.x | 0},${b.y | 0},${b.w | 0}x${b.h | 0})`);
      if (b.over) fail(`${s.file}: ${b.cls} overflows its height`);
    }
    for (const l of info.lines) {
      if (l.x < 60 - 0.5 || l.x + l.w > 1080 - 60 + 0.5) fail(`${s.file}: text line "${l.text}" outside the 60px crop-safe edge (${l.x | 0}..${(l.x + l.w) | 0})`);
      else if (l.x < 96 - 0.5 || l.x + l.w > 1080 - 96 + 0.5) warn(`${s.file}: text line "${l.text}" inside the 96px side margin (${l.x | 0}..${(l.x + l.w) | 0})`);
      if (l.bx !== undefined && (l.x < l.bx - 1 || l.x + l.w > l.bx + l.bw + 1)) fail(`${s.file}: text line "${l.text}" overflows its text box`);
      for (const a of info.avoid) {
        const ix = Math.min(l.x + l.w, a.x + a.w) - Math.max(l.x, a.x);
        const iy = Math.min(l.y + l.h, a.y + a.h) - Math.max(l.y, a.y);
        if (ix > 4 && iy > 4) warn(`${s.file}: text line "${l.text}" crosses motif "${a.name}"`);
      }
      if (l.y + l.h > 1350 - 100) warn(`${s.file}: text line "${l.text}" reaches the dots zone`);
    }
    const nLines = info.lines.filter(l => !String(l.ord).includes('label')).length;
    if (nLines > 6) warn(`${s.file}: ${nLines} text lines (max 5 + tab)`);
    (bySrc[s.src] = bySrc[s.src] || []).push({ part: s.part, segs: info.segs });

    await page.screenshot({ path: path.join(dir, s.file.replace('.html', '.png')), clip: { x: 0, y: 0, width: 1080, height: 1350 } });
    report.slides.push({ file: s.file, src: s.src, part: s.part, lines: nLines });
  }

  // verbatim
  post.slides_ar.forEach((want, i) => {
    const parts = (bySrc[i] || []).sort((a, b) => a.part - b.part);
    if (!parts.length) return fail(`source slide ${i + 1} missing from output`);
    const got = parts.flatMap(p => p.segs).map(g => SEP[g.sep] + g.text).join('');
    if (got !== want) fail(`verbatim mismatch on source slide ${i + 1}:\n    want ${JSON.stringify(want)}\n    got  ${JSON.stringify(got)}`);
  });
  report.verbatim = report.fail.some(f => f.startsWith('verbatim') || f.startsWith('source')) ? 'FAIL' : 'PASS';
  console.log(`  verbatim ${report.verbatim} (${post.slides_ar.length} source slides -> ${man.slides.length} output slides)`);

  // contact sheet
  const n = man.slides.length, cols = Math.min(n, 4), tw = 360, th = 450, gap = 16;
  const rows = Math.ceil(n / cols);
  const W = cols * tw + (cols + 1) * gap, H = rows * th + (rows + 1) * gap + 40;
  const imgs = man.slides.map(s => `<img src="data:image/png;base64,${fs.readFileSync(path.join(dir, s.file.replace('.html', '.png'))).toString('base64')}">`).join('');
  await page.setViewportSize({ width: W, height: H });
  await page.setContent(`<html><body style="margin:0;background:#222;width:${W}px;height:${H}px;font:14px sans-serif;color:#ccc">
    <div style="padding:12px 16px">${id}: ${n} slides, slide 1 at top-right, read right to left</div>
    <div style="display:grid;grid-template-columns:repeat(${cols},${tw}px);gap:${gap}px;padding:0 ${gap}px;direction:rtl">
    ${imgs.replace(/<img/g, `<img style="width:${tw}px;height:${th}px;display:block"`)}</div></body></html>`);
  await page.waitForFunction(() => [...document.images].every(i => i.complete));
  await page.screenshot({ path: path.join(dir, 'contact.png') });
  await page.setViewportSize({ width: 1080, height: 1350 });
  await page.close();
  fs.writeFileSync(path.join(dir, 'check.json'), JSON.stringify(report, null, 1));
  return report.fail.length > 0;
}

main().catch(e => { console.error(e); process.exit(1); });
