/* Home Orbit kit runtime. Included by every slide.
   Draws torn-paper backgrounds behind HTML elements marked .torn (step tabs, CTA
   tags) once fonts have loaded, so the paper fits the real text width.
     data-fill   paper colour        data-seed  fixed seed (same output every run)
     data-sides  torn edges (t b l r) data-hole  1 = punched hole + deep string (tags)
   Sets <html data-kit-ready="1"> when done; render.js waits for it. */
(function () {
  const PEARL = '#F6F3EB', DEEP = '#005A70';
  function rng(seed) { // mulberry32
    let a = seed >>> 0;
    return function () { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a);
      t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
  }
  const U = (r, a, b) => a + (b - a) * r();
  function edge(r, ax, ay, bx, by, nx, ny, torn, out) {
    const L = Math.hypot(bx - ax, by - ay), ux = (bx - ax) / L, uy = (by - ay) / L;
    out.push([ax, ay]); let t = 0, flip = r() < .5;
    for (;;) {
      t += torn ? U(r, 10, 18) : U(r, 40, 80); if (t >= L - 4) break;
      let d; if (torn) { if (r() < .7) flip = !flip; d = flip ? U(r, 6, 12) : U(r, 0, 3); } else d = U(r, -.8, .8);
      out.push([ax + ux * t + nx * d, ay + uy * t + ny * d]);
    }
  }
  function tornRect(w, h, sides, seed, grow) {
    const r = rng(seed), x = -grow, y = -grow; w += 2 * grow; h += 2 * grow; const p = [];
    edge(r, x, y, x + w, y, 0, 1, sides.includes('t'), p);
    edge(r, x + w, y, x + w, y + h, -1, 0, sides.includes('r'), p);
    edge(r, x + w, y + h, x, y + h, 0, -1, sides.includes('b'), p);
    edge(r, x, y + h, x, y, 1, 0, sides.includes('l'), p);
    return p.map(q => q[0].toFixed(1) + ',' + q[1].toFixed(1)).join(' ');
  }
  function tone(el) { const s = el.closest('.slide'); return (s && s.dataset.tone) || 'l'; }
  function build() {
    document.querySelectorAll('.torn').forEach(el => {
      const w = el.offsetWidth, h = el.offsetHeight, seed = +(el.dataset.seed || 1);
      const sides = el.dataset.sides || 'lr', fill = el.dataset.fill || PEARL, t = tone(el);
      let extra = '';
      if (el.dataset.hole) { // punched hole near the left end + string leaving to the top-left
        const ground = getComputedStyle(el.closest('.slide')).backgroundColor;
        const hx = 48, hy = h / 2;
        extra = `<circle cx="${hx}" cy="${hy}" r="11" fill="${ground}"/>` +
                `<circle cx="${hx}" cy="${hy}" r="11" fill="none" stroke="rgba(14,47,56,.35)" stroke-width="2"/>`;
        // slack string: out of the hole, loops down-left and trails off
        el._string = `<path d="M${hx} ${hy} C ${hx - 70} ${hy - 50}, ${hx - 150} ${hy + 10}, ${hx - 120} ${hy + 90} S ${hx - 60} ${hy + 190}, ${hx - 170} ${hy + 230}" ` +
                     `fill="none" stroke="${DEEP}" stroke-width="5" stroke-linecap="round"/>` +
                     `<circle cx="${hx}" cy="${hy}" r="6" fill="${DEEP}"/>`;
      }
      const svg = `<svg class="torn-bg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">` +
        `<g filter="url(#pt-${t}1)"><polygon points="${tornRect(w, h, sides, seed + 101, 3)}" fill="${PEARL}" fill-opacity=".7"/>` +
        `<polygon points="${tornRect(w, h, sides, seed, 0)}" fill="${fill}"/>${extra}</g>` +
        (el._string ? `<g filter="url(#pc-${t}2)">${el._string}</g>` : '') + `</svg>`;
      el.insertAdjacentHTML('afterbegin', svg);
    });
    document.documentElement.dataset.kitReady = '1';
  }
  const AR = 'أبجد هوز حطي كلمن';
  const faces = ['700 96px "El Messiri"', '600 72px "El Messiri"', '700 60px "Tajawal"', '500 50px "Tajawal"'];
  Promise.all(faces.map(f => document.fonts.load(f, AR)))
    .then(() => document.fonts.ready)
    .then(build, build);
})();
