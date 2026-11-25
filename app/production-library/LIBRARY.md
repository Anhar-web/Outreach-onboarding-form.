# Production library

A reusable kit for Home Orbit carousels. **It's a kit, not a cage**: reuse it for speed, and vary the composition every time.

- `kit/`: base.css (brand tokens, fonts, RTL), paper.svg (grain, torn and cut edges, shadows), kit.py (torn shapes, step tab, progress dots, CTA tag, quiet end), build.py (injects the approved Arabic verbatim and splits long slides), render.js (Playwright → PNG with font and verbatim checks), verify.py.
- `kit/posts/*.py`: the Batch 1 post modules. Reusable motifs: vacuum, iPad, tray of biscuits, majlis plan (with the `host` option), clue board + teardrop, bedroom panorama + chair, clock + quarter wedge, overhead plate, fridge (with the `magnets` option) + speech bubble, park route map + car, type-first with gold offset, storybook, chair, door.
- Compositions already used in Batch 1 (avoid repeating them back to back next batch): one big object, torn diagonal split, top-down plan, clue board, side panorama, radial clock, overhead flat-lay, scale contrast, route map, type-first.
- Batch 1 grounds: night, deep, deep + tealMist, sandLight, gold, tealMist, pearl (type-first only).

## Batch 4 kit: `kit_b4/` ("Paper & Light", Nov 2026)
- `looks.py`: the five looks (1 Layered Paper Night, 2 Cream Page, 3 Paper Vignette, 4 Doorway Light, 5 Night Bubble) built by `make(ctx, CONF)`; post modules are one-line CONFs.
- Components: paper waves, moon, lantern, glow, stars, gold line arcs, deckled pearl paper cards (HTML, auto-sized), QR card, gold «الافتراض…» / «الخطوة…» tags, tool tags.
- People (flat paper silhouettes, no faces): mother in hijab and abaya, child, seated woman, standing man.
- `scenes.py`: majlis + sweets tray, majlis + gift bag, toy room, doorway + shoes, toy aisle, door; objects: car, lift panel, rice plate, tray, dallah, gift bag, toy car, blocks, shoes.
- New: `kit.js` measures and shrinks each text block to its `data-maxh` (hook ≥72px, body ≥50px); a label is detected on any line starting «الخطوة».
- Retire or refresh one look next batch (spec rule 7).
