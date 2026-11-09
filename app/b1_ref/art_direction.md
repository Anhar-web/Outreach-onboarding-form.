# Art Direction: Batch 1

Values: `art_tokens.json`.

## 1. Through-line

Real paper on flat colour, lit from the top-right. Composition, viewpoint, scale and ground change per post; the material never does.

- **Grain:** one SVG filter on every shape. Mottle is fractalNoise 0.035, 3 octaves, 5%. Fibre is fractalNoise 0.9, 4 octaves, 7%, multiply. The ground gets 4%. Seeds are fixed.
- **Edges:** torn edges are jagged polygons (6–12px amplitude, every 10–18px) over a pearl core offset 3px at 70%. Cut edges use feDisplacementMap at scale 3.
- **Shadows:** every layer gets a contact shadow (−1 2 2px, ink 28%) and a cast shadow (−6 10 18px, ink 18%). On dark grounds both use #00141A at 45% and 35%. Each higher layer adds 4px of cast offset, plus a 1px white highlight at the top-right.
- **Safe area:** margins are 96px at the sides, 120px at the top and 150px at the bottom, giving an 888×1080 text box. Keep key content 60px or more from the sides, because the profile grid crops to 3:4.
- **Type** (px at 1080 wide, with line-height):

| Role | Font | Size | LH |
|---|---|---|---|
| Hook | El Messiri 700 | 96 (88–110) | 1.35 |
| Hook second clause | Tajawal 500 | 54 | 1.5 |
| Type-first hook (p8) | El Messiri 700 | 120 | 1.3 |
| Step label | El Messiri 600 | 44 | 1.2 |
| Body lead | Tajawal 700 | 60 | 1.45 |
| Body support (after "\n") | Tajawal 500 | 50 | 1.5 |
| Quiet end line | El Messiri 600 | 72 | 1.4 |
| Tag | Tajawal 700 | 46 | 1.3 |
| Floor | – | 44 | – |

- **Step tab:** a torn gold strip at the top-right, 72px tall and rotated −2°, with ink text. It holds the slide's own label up to the colon («الخطوة الأولى:»). The rest follows as body, so nothing is duplicated.
- **Dots:** 14px paper discs with 12px gaps, at bottom-centre 72px up. The current slide's dot is a 20px gold disc; the rest are the text colour at 40%. They run right to left, slide 1 has none, and there are no slide numbers.
- **Conversion end:** a full gold ground with ink text. The motif returns at 25% size in the bottom-left. The existing last sentence sits on a pearl torn tag (−3°, punched hole, deep string): «الرابط في البايو.» on p6/p7/p8/p10, and «التقييم المجاني في البايو يمر عليها كلها.» on p9.
- **Attention end:** own ground, quiet line centred at 72px, one motif accent.

## 2. Colour

- **Brand:** deep #005A70 · teal #00A9A5 · pearl #F6F3EB · gold #C9935A.
- **Derived:** night #003F4F (deep −30%) · ink #0E2F38 · tealMist #DCEEEC · sandLight #EBD6BC · goldDeep #8A5A2B · tealDeep #007A77.
- **Grounds:**
  - Light: pearl, tealMist, sandLight.
  - Dark: deep, night.
  - Gold is a ground on end slides only. Teal is never a ground.
- **Contrast** (WCAG 2.x): all text is 44px or larger, so the large-text threshold is 3:1, but I target 4.5:1.
  - **Pass:** ink on pearl 12.8, ink on tealMist 11.8, ink on sandLight 10.0, ink on gold 5.3, deep on pearl 7.0, pearl on deep 7.0, pearl on night 10.4.
  - **Accent only (≥60px):** gold on night 4.3.
  - **Banned:** gold on deep 2.9, deep on gold 2.9, pearl or white on teal 2.6–2.9, teal on pearl 2.6.

## 3. Per-post spec (posting order; grid D L D L D L D L D L)

**1. p5 vacuum.** Night ground, D. One Big Object (macro).
- Motif: a canister vacuum about 70% of the frame, bleeding off the bottom-left: pearl body ellipse, deep hose arc, gold wheels.
- Five torn teal and gold "noise" strips fan from the nozzle. Two small pearl mitten-hands cover an ear at the top-left.
- Slide 1: hook top-right in pearl, 96px, 3 lines.
- Inner slides: the vacuum shrinks (70→45→25%) and drifts left. On s6 a pearl doorway stays open. Accent: gold.

**2. p7 iPad.** Pearl ground with a tealMist right panel, L. Split frame with a torn seam.
- Right: a deep iPad (28px radius) with a two-layer teal glow.
- Left: a gold concentric plate holding four sandLight biscuits.
- Slide 1: the question sits over the iPad in ink at 96px; «جهزي اللي بعده قبل ما تسحبيه» sits over the plate at 54px.
- Inner slides: the plate side grows. On s4 a deep shower-head is crossed by a gold strip.

**3. p2 عزيمة.** Deep ground, D. Top-down blueprint.
- Motif: a majlis plan in pearl outline. A U of 8 sandLight cushions, a night TV bar, two speakers, and a door gap at the bottom-right. A torn gold ring marks the seat by the door.
- Slide 1: hook top-right in pearl, 92px, over the empty centre.
- Inner slides: each «الحساب» lifts one zone in gold: the arrival path, then the seat ring, then a gold bag holding a cup, a dish and a toy.

**4. p10 crying.** SandLight ground, L. Clue board.
- Motif: a cut deep teardrop (300px) at centre-low. Three blank pearl torn notes with gold pins sit around it.
- Slide 1: hook top-right in ink, 96px.
- Inner slides: each «شي» enlarges one note, which gains a flat deep icon: an iPad with an off-dot, then a puzzle piece, then a blender.

**5. p3 bedtime.** Night ground, D. Panorama: one 8640px strip, sliced.
- Motif: a side-view bed (deep frame, pearl blanket lump, no head), a gold slipper, a pearl moon and a gold lamp glow. Mum's gold chair moves bed → mid-room → door across s4–s8.
- Slide 1: hook centred in the upper third, pearl, 92px.
- Inner slides: a continuous floor line, with text in the upper 45%. On s8 the door is ajar with a light wedge.

**6. p6 shoes.** Pearl ground, L. One Big Object (centred radial).
- Motif: a 760px sandLight clock with a deep rim and ink hands. The quarter-hour before 12 is a torn gold wedge, and small deep shoes sit at 12.
- Slide 1: hook top-right in ink, 88px, with the clock filling the lower 60%.
- Inner slides: s4 an iPad with a gold cross; s5 a cup and a biscuit in the wedge; s6 the shoes move into the wedge.

**7. p4 plate.** Deep ground, D. Top-down flat-lay, geometric only.
- Motif: a 640px pearl plate. On it, four gold nugget blobs with sandLight dots, 7 gold fry bars, and a gold toast square with a goldDeep crust. An empty 200px dish sits beside it.
- Slide 1: hook top-right in pearl, 92px; the plate is cropped low.
- Inner slides: s3 a torn teal ring around the gold food; s4 the food turns pearl/deep; s5–7 a goldDeep falafel disc sits in the small dish.

**8. p9 name.** TealMist ground, L. Scale contrast.
- Motif: a giant deep fridge door ajar on the left, 70% of the frame height, with a pearl glow wedge. A tiny empty pearl speech bubble sits at the right.
- Slide 1: the clause up to «يلتفت؟» is set at 92px in ink; «جربي هذي…» follows at 50px.
- Inner slides: the bubble grows from 120 to 420px while the fridge recedes. On s4 a gold biscuit appears in the bubble.

**9. p1 park.** Deep ground with a teal lawn, D. Top-down route map. This replaces the photo hybrid.
- Motif: a torn teal lawn island over the lower 60%. A gold blanket with pearl stripes sits at the bottom-right, and a dashed pearl path runs from it to a small night car at the top-left.
- Slide 1: hook on a torn pearl strip (−1.5°) across the top third, ink, 88px.
- Inner slides: items travel the path. s3 a gold pin on the car; s4 the bag, then the ball, then the blanket lift off; s6 a juice box in the car.

**10. p8 aunt.** Pearl ground, L. Type-first.
- Motif: deep cut-paper letters over a gold duplicate offset −8px 8px, with one small closed storybook (gold cover).
- Slide 1: «مو كل مرة… يعاندك.» at 120px, and the rest at 54px.
- Inner slides: low vignettes. The book stays by a gold chair; striped pyjamas pass to a sandLight hand.

**Adjacency:** macro → split → map → board → panorama → radial → flat-lay → scale → route → type; neighbouring grounds always differ in value.

## 4. Brand check

All ten carry grain, double shadows, El Messiri hooks, gold tab and dots (plus the gold tag on conversion posts). Freshness against the side-view rooms:
- **p5:** one cropped object, with no room and no puppets.
- **p7:** a split object pair with no figures.
- **p2:** a plan view, not an elevation.
- **p10:** a symbolic board with no scene.
- **p3:** the closest to a room, but a sliced panorama with no figures.
- **p6:** a clock dial; time stands in for place.
- **p4:** an overhead flat-lay of geometric food.
- **p9:** extreme scale on a single object.
- **p1:** a map with a path and markers, not a landscape.
- **p8:** pure type and one prop.

## 5. Arabic setting

- `dir=rtl`, right-aligned. Centre only where specified, and never justify.
- Letter-spacing is 0. No synthetic bold, and El Messiri no heavier than 700.
- **Line breaks:**
  - Every "\n" is a hard break.
  - Otherwise, break only at a comma, a full stop or a phrase boundary.
  - Never split a construct pair, a preposition from its noun («بـ لا»), a quote, or a label from its colon.
  - Use `text-wrap: balance` on hooks and `pretty` on body to avoid widows.
- **Limits:** about 20 characters per line at 96px and 30–34 at 60px. A hook gets at most 4 lines, a slide at most 5. Add no numerals.
- **Legibility gate** (checked on the PNG):
  1. The hook reads at 270px wide.
  2. No text is under 44px.
  3. Contrast is 4.5:1 or better.
  4. No text crosses a motif.
  5. The safe area is respected.
  6. A diff against `slides_ar` is empty.
  7. The dots run right to left.

## 6. Fit flags (not rewritten)

**Red** (over 5 lines at 50px, or hook below 88px):
- p7 s6 (151 characters)
- p9 s1 hook (124)
- p3 s7 (123)
- p2 s7 (120)
- p7 s4 (111)

**Amber** (fits only at 50px, tight):
- p6 s5 (107)
- p8 s8 (107, no "\n")
- p2 s3 (103)
- p6 s7 (103)
- p8 s1 hook (101, needs the big/small split)
- p5 s5 (101)
- p2 s2 (99)
- p9 s8 (98)
- p1 s4 (95)
- p4 s6 (95)

**Split hooks:** p1 s1, p6 s1 (80 characters): question big, clause small.

**No "\n":** p8 s2–s7 break at full stops.
