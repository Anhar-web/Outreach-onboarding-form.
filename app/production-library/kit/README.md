# Home Orbit carousel kit (Batch 1)

This kit turns `app/posts_draft.json` into finished 1080×1350 cut-paper carousel PNGs.
Read `app/art_direction.md` and `app/art_tokens.json` first. Where they differ, `art_tokens.json` wins, including its `anharOverrides` and the updated grounds for p6 and p7.

```
python3 build.py p5 p7 p2        # posts_draft.json + posts/<id>.py  ->  app/output/<id>/slide-N.html
node render.js p5 p7 p2          # -> slide-N.png, contact.png, check.json  (exits 1 on any FAIL)
python3 verify.py p5 p7 p2       # browser-free verbatim check (optional, fast)
```
Run the commands from this folder. With no arguments, each script handles every post. `render.js` uses `require('playwright')`. The fonts come from Google Fonts, so the renderer needs network access. It uses `$HTTPS_PROXY` when that is set.

## Files

| file | what it is |
|---|---|
| `base.css` | Google Fonts `@import` (El Messiri 600/700, Tajawal 500/700, `display=block`), CSS variables for every colour, type size and margin in the tokens, the `.slide` canvas (RTL, letter-spacing 0, no synthetic bold), text roles (`.hook .clause .typefirst .lead .support .quiet .tag`, all with `text-wrap: balance`), `.amber`, step tab, CTA tag, progress dots, `.sh-l` / `.sh-d` shadow classes for HTML pieces |
| `paper.svg` | **Generated** by `make_paper_svg.py` from the tokens. Holds the SVG `<defs>` that `build.py` inlines into every slide (filters only work inline). Filters: `pg` (ground grain), `pc-{l,d}{1,2,3}` (cut paper: displaced edge, mottle and fibre grain, contact and cast shadow, top-right rim highlight), `pt-{l,d}{1,2,3}` (torn paper: same filter without displacement), `pn` (grain only), `glow-s` and `glow-l` (soft light). `l`/`d` picks the light-ground or dark-ground shadow set. `1/2/3` is the layer height: each layer up adds 4px of cast offset. |
| `make_paper_svg.py` | Regenerates `paper.svg`. Grain strength is tuned at the top of the file. |
| `kit.py` | Python helpers for post modules: geometry (`torn_rect`, `torn_poly`, `torn_circle`, `torn_ring`, `torn_strip`, `arc_pts`), `paper()` (wraps shapes as one sheet), `glow()`, `avoid()`, the **text model** (`SlideText`, `Seg`, `keep`, `keep_in`, `text_box`), and components (`step_tab`, `dots`, `conversion_tag`) |
| `kit.js` | Runs in each slide. Once the fonts load, it draws the torn paper behind `.torn` HTML elements (step tab, CTA tag with punched hole and deep string), sized to the real text. When it finishes it sets `<html data-kit-ready="1">`. |
| `build.py` | Builds the slide HTML and `manifest.json` (see below) |
| `render.js` | Renders the PNGs, makes the contact sheet, runs the checks |
| `verify.py` | Runs the same verbatim check as `render.js`, straight from the HTML |
| `posts/p5.py`, `p7.py`, `p2.py` | The finished post modules. Copy one to start a new post. |

## How the text stays verbatim

**You never type Arabic in a module.** `build.py` cuts each `slides_ar[i]` into segments:
- **label**: an auto-detected prefix up to and including the colon, such as «الخطوة الأولى:», «الحساب الأول:» or «أول شي:». It goes in the gold tab.
- **hook**: slide 1.
- **lead**: the first line.
- **support**: each line after a `"\n"`.

Every segment records the exact characters that sat before it in the source (a space, a `"\n"` or nothing). The module only *places* segments. After the module returns, `build.py` asserts that every segment was placed exactly once. `render.js` then reads the text back from the **rendered DOM**, re-joins it (across split slides too) and compares it to `slides_ar` character for character.

You can change the presentation freely:
- `seg.role = 'quiet' | 'clause' | 'lead'` restyles a segment.
- `ctx.t.split_seg(seg, '؟ ')` cuts a hook into question plus clause.
- `keep_in(ctx.t.segs, 'phrase one', 'phrase two', ...)` makes lines break **only between** the phrases you list. Use it so breaks fall at commas and phrase boundaries, never inside «بدل ما», «قولي له» or «شوي شوي». It only adds no-wrap spans; the words are untouched.
- `text_box(..., size={'hook': 88})` sets a size within the token range.

## Long slides (anharOverrides.longSlides)

Red-flag slides (`fitFlags.red`: p7 s6, p9 s1, p3 s7, p2 s7, p7 s4) are split automatically into two output slides. The split falls at the `"\n"` nearest the middle, or at the full stop nearest the middle if the slide has no `"\n"`. The words are the same and in the same order. In the module, `ctx.s` is the **source** slide number (s1…sN, as in the spec), and `ctx.part` is 0 for an unsplit slide or 1/2 for the two halves. Amber slides stay single. `ctx.amber` is True for them, and the slide gets the `.amber` class, so the lead is set at bodySupport (50px).

## Adding a post (e.g. p10)

1. Copy `posts/p7.py` (conversion) or `posts/p5.py` (attention) to `posts/p10.py`.
2. Write `slide(ctx)` and return a dict:
   ```python
   {'ground': 'sandLight',          # token colour name; picks the shadow set (deep/night = dark)
    'art': '<svg shapes>',           # drawn on the 1080x1350 canvas, over the grained ground
    'html': text_box(...) + step_tab(ctx.t.label()),
    'dots_theme': 'light'}           # optional: light | dark | gold (default comes from the ground)
   ```
   Useful values on `ctx`: `ctx.s`, `ctx.part`, `ctx.i`/`ctx.n` (output index and total), `ctx.first`, `ctx.last`, `ctx.amber`, `ctx.t.label()`, `ctx.t.body()`, `ctx.cta_text()`, `ctx.spec` (that post's tokens).
3. Build every motif from paper:
   - `paper(shapes, tone, layer)` for cut objects.
   - `torn_rect/poly/circle/ring/strip` for torn notes, strips, tabs, seams and islands.
   - Pass `T='translate(..) scale(..)'` to reuse one motif at several sizes. The filter stays outside the transform, so shadows and grain stay full size.

   Wrap the main masses in `avoid(svg, 'name')`. `render.js` warns if a line of text crosses one. If you clip a crop, add `data-clip-y` (see `p2.py`).
4. **Conversion end**: gold ground, ink text. `cta = ctx.t.body()[-1]` must equal `ctx.cta_text()`; assert it. Place it with `conversion_tag(cta, x, y)`, and add the motif at 25% in the bottom-left.
   **Attention end**: keep the post's own ground, set `role='quiet'`, centre the line (`align='center'`) and add one accent.
5. Run `python3 build.py p10 && node render.js p10`. Then **look at** `app/output/p10/contact.png` and at single PNGs. Iterate until `render.js` prints no FAIL and the slides look finished.

## What render.js checks

**FAIL** (exit code 1):
- A font is not loaded. All four faces are checked against Arabic glyphs.
- The verbatim diff is not empty.
- Text is under 44px.
- A text box or line goes past the 60px crop-safe edge.
- A line overflows its box.

**warn**:
- A line crosses an `avoid` motif.
- A line sits inside the 96px side margin.
- Text reaches the dots zone.
- A slide has more than 5 lines.

## Rules to keep (handbook Part C plus tokens)

- Use stylised cut paper only: no photos, no realism, and never a child's face. Heads may appear from behind or with the face off-frame.
- Use only the text-on-ground pairs in `colors.textOn`:
  - pearl on deep or night;
  - ink on pearl, tealMist, sandLight or gold.
  - **Never** put gold text on deep, pearl on teal or teal on pearl.
  - Teal is never a ground.
- Blue dominates the batch, and pearl must not dominate. Vary the composition, viewpoint and scale from post to post; the paper material is the through-line.
- At 96px El Messiri runs about 50px per character, so 888px holds about 18 characters. If a hook phrase cannot fit, drop toward 88px (the bottom of the range) and/or widen the box to a 80px margin, which is still 60px crop-safe. Never break inside a phrase.
