# Production library

A reusable kit for Home Orbit carousels. **It's a kit, not a cage**: reuse it for speed, and vary the composition every time.

- `kit/`: base.css (brand tokens, fonts, RTL), paper.svg (grain, torn and cut edges, shadows), kit.py (torn shapes, step tab, progress dots, CTA tag, quiet end), build.py (injects the approved Arabic verbatim and splits long slides), render.js (Playwright → PNG with font and verbatim checks), verify.py.
- `kit/posts/*.py`: the Batch 1 post modules. Reusable motifs: vacuum, iPad, tray of biscuits, majlis plan (with the `host` option), clue board + teardrop, bedroom panorama + chair, clock + quarter wedge, overhead plate, fridge (with the `magnets` option) + speech bubble, park route map + car, type-first with gold offset, storybook, chair, door.
- Compositions already used in Batch 1 (avoid repeating them back to back next batch): one big object, torn diagonal split, top-down plan, clue board, side panorama, radial clock, overhead flat-lay, scale contrast, route map, type-first.
- Batch 1 grounds: night, deep, deep + tealMist, sandLight, gold, tealMist, pearl (type-first only).
