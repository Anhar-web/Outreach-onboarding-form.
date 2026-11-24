# Batch 4 visual system: "Paper & Light"
Nov 2026. Built from a slide-by-slide look at Anhar's 25 legacy posts, compared with Batches 1–3. Use it with `BATCH4_HANDOFF.md`, for art direction and production.

Files in `app/b4/visual/`:
- `legacy_visuals_L01-L13.png` and `legacy_visuals_L14-L25.png`: slides 1 and 3 of every legacy post.
- `looks_sheet.png`: the 5 looks, as mockups.
- `grid_sheet.png`: a 12-post feed grid.
- `mock.py` and `render.js`: the mockup code (SVG/CSS, rendered with Playwright).

**Mockup copy is borrowed from legacy posts, for layout only.**

---

## 1. What the legacy visuals tell us

### Six visual families appeared
| Family | Posts | Look | Results |
|---|---|---|---|
| **A. Layered paper night** | L01–L06, L09 | Deep navy, teal, sand and cream 3D paper layers (waves, arches, a staircase, a moonlit door, lanterns), one warm light source, a translucent white text box in the centre | **203K, 39.5K, 38.4K**, 5.6K, 3.9K, 2.5K, 2.0K |
| **B. Warm window light** | L07, L08, L10, L11 | Real golden-hour interiors, sunbeams, wood and beige, plus a text box | 1.7K, 1.3K, 3.0K, 0.9K |
| **C. Calm outdoor** | L12, L13 | Shoreline and sea rocks, plus a text box | 1.2K, 2.0K |
| **D. Cream page** | L14–L18 | Plain cream ground, teal headline, navy body, thin line arcs and soft teal circles at the edges. Text only | **159K, 13.4K**, 6.8K, 5.6K, 3.7K |
| **E. Storybook + pastel** | L19–L23 | Watercolour slide 1 with a small label, peach and pastel inner slides with pencil leaf and flower lines | **16.8K**, 5.1K, 4.5K, 3.4K, 1.4K |
| **F. Soft single object** | L24, L25 | Soft photo or a dusty-blue ground with one 3D clay speech bubble holding the text | 1.3K each (very early posts) |

### What every family did the same way (the real constants)
1. **Copy on a light surface, always.** Dark navy text on white, cream or pastel: either a light panel over the art, or a light ground. Nothing busy ever sat behind a letter.
2. **The art lives at the edges.** In family A the rich paper scene frames the card, only peeking around it. In D and E the art is a corner motif or one thin line. The middle 70% belongs to the words.
3. **Big hook type** fills about 60% of slide 1. Inner slides are quieter than slide 1 (D and E) or reuse slide 1's background (A).
4. **One warm light accent** (a lantern, lamp glow, moon or sunbeam) gives depth and warmth without competing.
5. **One palette family per post:** navy, teal and sand; or cream and teal; or peach and lavender. Never more.

### Why the styles wore out
- **Hits came from three different families (A, D, E).** No single style is "the" winner.
- **Each family did well while it was fresh, then faded** with repetition, as Anhar saw. Batch 3 repeated one look 12 times (dark teal cut-paper) and reach fell from an 878-view average in the first six posts to 451 in the last six.
- **So variety across the feed is a requirement, not a nice-to-have.**

### What Batches 1–3 did differently, and what changes now
- **Text was pearl on a dark ground**, with the art filling the lower half and **competing** with the copy. Legacy always kept art at the edges.
- **"Slide 1 always dark"** came from a confounded Batch 2 read (the light posts also went out minutes apart). Legacy breakouts were mostly light (D, E) or light-card-on-dark (A). **Retired: the ground now rotates by look.**
- **The rules that stay:**
  - no photos or AI images (we build everything in the SVG kit)
  - no child faces
  - paper grain
  - fonts: El Messiri for hooks, Tajawal for body
  - brand colours
  - nothing under 44px
  - keep clear of the 60px grid crop

---

## 2. The system: "Paper & Light"
**One idea:** a sheet of paper carries the words, and the world is cut paper around it, lit by one warm light. Five looks share fonts, grain, the deckled pearl paper and the warm light, and differ in ground, depth and amount of art. The art always **frames** the copy and never sits behind it.

### Palette
- **Brand colours:**
  - deep `#005A70`
  - night `#003F4F`
  - ink `#0E2F38`
  - tealDeep `#007A77`
  - teal `#00A9A5`, accents only
  - tealMist `#DCEEEC`
  - pearl `#F6F3EB`
  - sand `#EBD6BC`
  - gold `#C9935A`
- **Proposed, needs Anhar's OK:** **dusk `#B7CBD6`** and duskDeep `#7F9DB0`, a dusty-blue ground taken from legacy L25. Ink on dusk passes contrast.
- **Text colours:**
  - ink on every light surface
  - highlight words in **tealDeep** on pearl and tealMist, and **deep** on sand and dusk; never teal (teal on light fails contrast)
  - never gold text

### Type (unchanged)
- **Hook:** El Messiri 700, 80–96px, with one tealDeep highlight phrase per slide at most.
- **Body:** Tajawal 500, 50–56px; Tajawal 700 for a lead line.
- **Line breaks follow the copy's beats:** short lines, plenty of air.

### The five looks
| # | Look | Ground | How the art sits | Best for | Legacy root |
|---|---|---|---|---|---|
| **1** | **Layered Paper Night** | night / deep | 4–5 stacked paper wave layers (deep → tealDeep → sand → pearl) rising from the bottom, a darker layer at the top, one warm glow (moon, lantern or doorway), a few paper stars. Copy sits on an **opaque deckled pearl paper card** with a real shadow. *Not* the translucent box. | **Logical-fallacy series** «الافتراض اللي يصعّب الموضوع», serious or tender topics, bedtime | A (203K / 39.5K / 38.4K) |
| **2** | **Cream Page** | pearl / sand / tealMist | Type-first. Thin gold line arcs in one corner, one soft tealMist circle bleeding off an edge, one small cut-paper object (star, shoe, cup) low in a corner. The headline is in tealDeep. | Funny story hooks, the problem + solution hook (Eid), punchy posts | D (159K / 13.4K) |
| **3** | **Paper Vignette** | tealMist / pearl / sand | Big hook in the top 55%. A **small cut-paper stage set** in the bottom 40% that names the place: a majlis cushion row and coffee tray, a supermarket shelf edge, a café counter, a car-seat corner, a bath tile line. **No faces**: backs, hands, objects. | Public and family scenes with people reacting (the reach driver) | E's thumbnail idea, in paper |
| **4** | **Warm Window Light** | sand / pearl | Golden-hour window light as soft pale diagonal beams across the ground. One or two paper objects at the bottom (school bag, clock, shoes). Copy directly on the ground. | Mornings, routines, home moments, time-cost hooks | B (golden interiors) |
| **5** | **Blue Hour Minimal** | dusk / tealMist | **One big 3D paper object holds the copy:** a speech bubble, a note card, a plate, a shoe-box lid. Plus one soft circle and one tiny accent (heart, star). Simplest look. | Short hooks, relatives' quotes, "what people say" posts, CTA-heavy endings | F (L25) |

### Slide rhythm inside a post
- **Slide 1:** the look at full strength: the most art, the biggest hook.
- **Slides 2 to n−1:** quieter. The **same look and ground**, but the art pulls back to one edge, scales down, or shifts position. Look 1 keeps only the lowest two paper layers; look 3 drops the stage set and keeps one prop in a corner. The art may **evolve** with the story (the moon rises, the tray empties), but stays at the edges.
- **Slide 3 (the solution):** the named tool gets a small paper tag (gold for look 1, tealMist for looks 2–5), never a big step tab over art.
- **Last slide (CTA):** the same look. The QR code sits on a pearl paper card. One small motif from slide 1 returns in a corner, so the post closes like a loop.
- **The text box rule:** opaque deckled paper only (looks 1 and 5), with a real drop shadow. **Never a translucent white box** (Anhar).

---

## 3. The feed grid (anti-sameness rules)
TikTok shows 3 columns, newest top-left. Two posts a day means each day fills 2 tiles, so plan in rows of 3.
1. **No two consecutive posts share a look.**
2. **Every row of 3 has 3 different looks**, and no column repeats a look in adjacent rows.
3. **Value rhythm:** at most 1 dark tile (look 1) per row. Never 2 dark tiles touching.
4. **Grounds rotate inside a look:** the same look returns on a different ground (look 2 on pearl, then sand, then tealMist).
5. **About 3 posts per look per 12** (look 1 = the fallacy series, ~3–4).
6. **Look 1 is the "series" look,** so the fallacy posts are recognisable as a series without the rest of the feed looking the same.
7. **Every batch, retire or refresh one look** (new composition family, or a new accent object) so no look runs more than ~2 batches unchanged.

**Sample 12-post sequence** (`grid_sheet.png`):

| Row | Slot 1 | Slot 2 | Slot 3 |
|---|---|---|---|
| 1 | Look 1, night | Look 2, pearl | Look 3, tealMist |
| 2 | Look 4, sand | Look 1, deep | Look 5, dusk |
| 3 | Look 2, sand | Look 3, pearl | Look 1, night |
| 4 | Look 4, pearl | Look 5, tealMist | Look 2, tealMist |

**The hook decides the look,** not the other way round. Use the slate to place looks; if a hook needs a scene (people reacting), it gets look 3 even if that means swapping two posts.

---

## 4. Avoid
- Art behind text, or a full-bleed scene under the hook.
- More than one hero object on slide 1 in looks 2, 4 and 5.
- Teal text on light grounds, and gold text anywhere.
- The same look on two consecutive posts, or more than 4 times in 12.
- Photos, AI images, child faces, emojis as icons.
- Performed child drama in the art (giant tantrum figures). Show the place and the objects; the copy carries the moment.
- The Batch 3 habit of a big motif in the lower half competing with long copy.

## 5. Production notes (kit)
- **Build on the Batch 3 kit** (`app/production-library/kit_b3/`) as a new `kit_b4/`. New components, prototyped in `visual/mock.py`:
  - `paper_waves(layers, colours, top|bottom)`
  - `deckled_card(x, y, w, h)` (a displacement filter plus a drop shadow)
  - `glow(cx, cy)` (radial gold)
  - `window_beams(n)`
  - `paper_bubble()`
  - `vignette(scene)` (majlis, shelf, counter, car seat, bath)
  - `paper_tag(text)`
- **Text-fit checks stay as they are** (verbatim, no «،» line endings, ≥44px). Add a check that **no text overlaps art**: art is allowed only outside the card or the text box.
- **Contrast checks (measured):**
  - ink is ≥8:1 on every ground
  - tealDeep highlight: 4.7:1 on pearl and 4.3:1 on tealMist, so use it only on bold lines of 50px or more
  - on **sand (3.7) and dusk (3.1)**, tealDeep fails: highlight with **deep `#005A70` bold** instead
