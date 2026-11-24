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
- **Dark stays the base (Anhar, from testing),** but not as one repeated look. Dark grounds rotate across four looks and two shades (night and deep), and a light cream page is mixed in about 1 post in 4.
- **The rules that stay:**
  - no photos or AI images (we build everything in the SVG kit)
  - no child faces (silhouettes are fine)
  - paper grain
  - fonts: El Messiri for hooks, Tajawal for body
  - brand colours
  - nothing under 44px
  - keep clear of the 60px grid crop

---

## 2. The system: "Paper & Light"
**One idea:** a sheet of paper carries the words, and the world is cut paper around it, lit by one warm light. Five looks share fonts, grain, the deckled pearl paper and the warm light, and differ in ground, depth and amount of art. The art always **frames** the copy and never sits behind it. **Dark grounds lead** (looks 1, 3, 4 and 5); the cream page (look 2) is the occasional light change of pace.

### Anhar's decisions (Nov 24)
- **Dark is the main thing.** In testing, dark posts always did better. About **3 of every 4 posts are dark**; light posts (look 2 only) are the occasional change of pace.
- **No dusty blue:** it was an old brand colour.
- **The solid deckled paper card stays** as built.
- **People, mainly silhouettes,** as in the legacy posts.

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
- **Text colours:**
  - ink on every light surface; **pearl** directly on dark grounds (pearl on night 10.4:1, on deep 7:1)
  - highlight words in **tealDeep** on pearl and tealMist, **deep** on sand, and **sand `#EBD6BC`** on dark grounds; never teal (teal on light fails contrast)
  - never gold text

### Type (unchanged)
- **Hook:** El Messiri 700, 80–96px, with one tealDeep highlight phrase per slide at most.
- **Body:** Tajawal 500, 50–56px; Tajawal 700 for a lead line.
- **Line breaks follow the copy's beats:** short lines, plenty of air.

### The five looks
| # | Look | Ground | How the art sits | Best for | Legacy root |
|---|---|---|---|---|---|
| **1** | **Layered Paper Night** | night / deep | 4–5 stacked paper wave layers (deep → tealDeep → sand → pearl) rising from the bottom, a darker layer at the top, one warm glow (moon, lantern or doorway), a few paper stars. Copy sits on an **opaque deckled pearl paper card** with a real shadow. *Not* the translucent box. On slide 1, a mother and child silhouette at the edge, walking toward the light. | **Logical-fallacy series** «الافتراض اللي يصعّب الموضوع», serious or tender topics, bedtime | A (203K / 39.5K / 38.4K) |
| **2** | **Cream Page** (the one light look) | pearl / sand / tealMist | Type-first. Thin gold line arcs in one corner, one soft tealMist circle bleeding off an edge, one small cut-paper object (star, shoe, cup) low in a corner. The headline is in tealDeep. | Funny story hooks, the problem + solution hook (Eid), punchy posts | D (159K / 13.4K) |
| **3** | **Paper Vignette** | **deep / night** (light only as the rare variant) | Big hook in the top 55%. Pearl type directly on the dark ground. A **cut-paper stage set** in the bottom 40%, softly lit by a warm glow, that names the place: a majlis cushion row and coffee tray, a supermarket shelf edge, a café counter, a car-seat corner, a bath tile line. **The witnesses are there as silhouettes** (seated relatives, a shopper, staff), plus the child as a small silhouette. | Public and family scenes with people reacting (the reach driver) | E's thumbnail idea, in paper |
| **4** | **Doorway Light** | **night / deep** | A warm gold light cone from a doorway or window at the edge falls across the dark floor. **Mother and child silhouettes** stand in or near the light. Pearl copy on the dark area above. | Mornings, bedtime, routines, home moments, time-cost hooks | B's warm light, moved to night |
| **5** | **Night Bubble** | **deep / night** | **One big deckled pearl paper object holds the copy:** a speech bubble, a note card, a plate. A few sand paper stars, one warm glow in a corner, and two small silhouettes (the people talking) at the bottom. Simplest dark look. | Short hooks, relatives' quotes, "what people say" posts, the problem + solution hook, CTA-heavy endings | F (L25), on dark |

### People: silhouettes
- **As in the legacy posts:** mother and child, and the people watching (relatives, shoppers, staff), as **flat paper silhouettes**.
- **No faces or features:** side or back views, readable from posture (hijab and abaya, a small child's round head, a raised arm).
- **On dark grounds:** silhouettes one step darker than the ground (ink or night), backlit by the warm glow.
- **On light grounds:** deep.
- **Placement:** at the edges and bottom only, never behind text. At most 4 figures on a slide.
- **No performed drama:** posture tells the moment (a child pulling away, a mother bent at a door), never cartoon tantrums.

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
3. **Dark is the base:** about **9 of 12** tiles are dark (looks 1, 3, 4 and 5), with 3 light (look 2). **Every row has at least 2 dark tiles**, and light tiles never touch (side or above/below).
4. **Grounds rotate inside a look:** the same look returns on a different ground (look 2 on pearl, then sand, then tealMist).
5. **About 2–3 posts per look per 12** (look 1 = the fallacy series, ~3).
6. **Look 1 is the "series" look,** so the fallacy posts are recognisable as a series without the rest of the feed looking the same.
7. **Every batch, retire or refresh one look** (new composition family, or a new accent object) so no look runs more than ~2 batches unchanged.

**Sample 12-post sequence** (`grid_sheet.png`, 9 dark and 3 light):

| Row | Slot 1 | Slot 2 | Slot 3 |
|---|---|---|---|
| 1 | Look 1, night | Look 3, deep | Look 2, pearl (light) |
| 2 | Look 4, night | Look 2, sand (light) | Look 5, deep |
| 3 | Look 3, night | Look 1, deep | Look 4, deep |
| 4 | Look 2, tealMist (light) | Look 5, night | Look 1, night |

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
