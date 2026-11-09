# Carousel Designer + Illustrator brief: Batch 2

You build finished 1080×1350 cut-paper carousel PNGs for Home Orbit (مدار البيت) with the Batch 2 kit in this folder.

## Read first (in full)
1. `/home/user/Outreach-onboarding-form./app/art_direction_b2.md`: the art direction. Your posts' rows in the table are your brief.
2. `README.md` in this folder: the kit (the Batch 1 doc applies, with Batch 2 paths): `python3 build.py <ids>`, then `node render.js <ids>`.
3. `common.py`: `hook_box`, `body_box`, `soft_cta`, `cta_end`. Use them so the whole batch shares one type system.
4. `posts/p10.py`: the Batch 2 reference module (vertical cascade). Copy its structure.
5. Batch 1 motif modules for reuse and inspiration: `../kit/posts/*.py` (vacuum p5, bedroom + chair p3, clock p6, plate p4, fridge + bubble p9, park map p1, majlis plan p2, iPad + tray p7, clue board p10, type-first p8). Import their helper functions by copying the code into your module. Don't import across folders.
6. The look to match (Anhar's Batch 1 finals): `/tmp/claude-0/-home-user-Outreach-onboarding-form-/2f60d0e2-13b6-57dc-aaa0-40f500a6367d/images/1.webp`…`4.webp`. Look at them with the Read tool. They show bold, simple, BIG cut-paper objects with lots of breathing room, big pearl El Messiri hooks top-right, and grained flat grounds.

## Hard rules
- **Never type Arabic in a module.** The text comes from `app/posts_b2.json` through the kit. Place segments only. `render.js` must print `verbatim PASS` and no FAIL lines.
- **No visible line may end with a comma** (Anhar's rule). The kit handles commas automatically: it hides the comma where a line breaks and glues short list commas. If `render.js` FAILs "a line ends with a comma", fix it with `keep_in(...)` / `brk(seg, 'phrase')` or `seg.comma = 'break' | 'glue'`. Never edit the words.
- Every module function `slide(ctx)` must handle all of its post's slides. The **last slide** is `cta_end(ctx, mini_art=...)`: gold ground, the post's motif small in a corner, tag position varied. Place the **soft CTA** (`ctx.t.soft()` is not None) with `soft_cta(ctx, y=...)` on a free area, never over art or other text.
- Hooks: El Messiri 88–100px, top-right, broken at phrase boundaries (use `keep=` / `breaks=` in `hook_box`). Use at most 5 lines.
- **Never draw a child's face, and never anything that reads as a face** (no two dots plus a curve on a round shape). People appear as hands, sleeves, the back of a head, feet, or a shape under a duvet.
- No added words or numbers on the art. Counts are shown as dots or shapes.
- Text pairs: pearl text on deep/night, ink text on tealMist/sandLight/pearl/gold. `ink_or_pearl(ground)` handles it.
- Light from the top-right. Everything is paper: `paper()`, `torn_rect`, `torn_circle`, `torn_strip`, `torn_poly`. No gradients and no realism.

## Quality bar (look at every slide)
- After each render, **Read `app/output_b2/<id>/contact.png`** and at least slides 1, 2 and the last slide at full size. Iterate until:
  - no FAIL;
  - no text crosses art (the "crosses motif" warnings are real problems; fix them);
  - objects are **big, simple and recognisable at a glance**: a shower head must read as a shower head, a blender as a blender. If something reads as a mushroom or a muffin, redraw it;
  - the art **evolves** across slides (state, scale, position change), so swiping feels like a story;
  - the composition matches your row in the art direction and doesn't look like the other posts;
  - long slides keep the art smaller and lower; text never shrinks under 50px (44px soft CTA only).
- Over 6 lines on a text-heavy slide is acceptable (the copy is approved and long). Keep generous line spacing and put art where the text isn't.

## Deliver
When all of your posts render with no FAIL and you are happy with the contact sheets, reply with (under 200 words): per post, the composition, what evolves across the slides, any remaining warnings, and anything you'd flag for QA. Don't touch other designers' posts or the shared kit files (kit.py, common.py, build.py, render.js). If you believe the kit needs a change, describe it in your reply instead.
