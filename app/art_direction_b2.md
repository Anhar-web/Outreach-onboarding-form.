# Batch 2 art direction (Visual Researcher + Art Director)

## Read first
- Handbook Part C (visual rules) and Airtable → Visual Style.
- `b1_ref/art_direction.md` and `b1_ref/qa_report.md`, the Batch 1 system and its QA lessons.
- Anhar's reference screenshots (Batch 1 finals): vacuum s1/s2, bedtime s1, shoes s1. That is the look: **flat grained grounds, big pearl El Messiri text top-right, objects as layered cut paper with soft cast shadows, a few warm gold accents, lots of breathing room.**

## The through-line (hold it on every post)
1. **Cut paper.** Every object is built from layered paper sheets (kit `paper()` / `torn_*`): grain, slightly displaced cut edges, torn edges on notes and strips, contact and cast shadows, light from the top-right. No photos, no realism, no gradients beyond the kit glows.
2. **Brand colours.** Deep `#005A70` / night `#003F4F` lead the batch. Accents are pearl, gold and teal. Light grounds are tealMist / sandLight, and one pearl post at most. Teal is never a ground.
3. **Type.** El Messiri 700 for hooks: pearl on dark grounds, ink on light grounds, top-right, 88–104px. Tajawal for body: lead 60px / support 50px (amber slides set the whole body at 50px). Steps and labels sit in the torn gold step tab, top-right.
4. **Progress dots:** gold, RTL, none on slide 1.
5. **Never a child's face.** Hands, the back of a head, feet, a silhouette under a duvet, or the child off-frame. Mum is shown as a hand, a sleeve, a hem or her back.

## Batch 2 rules (new)
- **No line ends with a comma** (Anhar). The kit hides the comma wherever a line breaks at it and glues short list commas. `render.js` FAILs any visible line that ends with a comma. Never change the words to fix a layout; choose the break points instead.
- **The soft CTA line** is set on a small torn **gold** strip with ink text (`soft_tag()`), low on the slide and above the dots. It reads as an aside, not a banner.
- **CTA end slide** (the last slide of every post): **gold ground, ink text.** The final «الرابط في البايو.» line goes on the pearl torn tag with a punched hole and a deep string (`conversion_tag`). The post's own motif sits small (~25–35%) in a corner. Vary its corner and pose post by post.
- **Story slides stay airy:** at most about 5 text lines plus the art. If a slide is long, let the art go smaller, not the text. Never go under 50px for body text, except the 44px soft CTA.
- Blue dominates the grid. Light and dark grounds alternate through the posting order.
- **Fight sameness.** Every post below has its own composition, and none repeats a Batch 1 layout back to back. The motif *evolves* across the slides (moves, shrinks, changes state) so the swipe feels like a story, not 8 copies of one picture.

## Per post (posting order)
| Day | Post | Ground | Composition (new for B2) | Hero motif and how it evolves |
|---|---|---|---|---|
| 1 | p10 Hair wash | deep | **Vertical cascade**: a shower head top-left, torn teal water strips falling diagonally | s1 water pours over a small head (back view) and mum's wet pearl sleeve and droplets. s2 water splashing everywhere. s4 a small hand holds a sandLight towel over the eyes. s5 ten small gold paper discs (counting), water cut at ten. s6 a small hand holds the hand shower and the stream is gentle. s7 the three items in a row. |
| 2 | p5 Cooking | sandLight | **Child's-eye low angle**: the counter edge as a band across the frame, a pot with steam above, a small hand gripping mum's hem below | s2 hand on the hem, a pearl sleeve stirring. s3 the hem released. s4 a chair pulled up to the counter (child from behind, at mum's height). s5 a zabdiya bowl with cucumbers and water. s6 two speech bubbles (wordless: an onion and rice grains). s7 method: three torn notes. |
| 3 | p2 Sneaking out | night | **Threshold**: a dark bedroom, the door ajar, a vertical sliver of pearl light | s2 small footprint steps toward the light, a pearl «ماما»-style speech bubble (wordless) at the door. s3 back beside the bed. s4 the door half open, mum's silhouette leaving. s5 three torn gold tags 1 / 2 / 5 on the door frame (numerals only as shapes, dots: 1, 2, 5 dots). s6 the door open and closed as a loop arrow of torn strips. |
| 4 | p9 Shower | deep | **Door as the divider**: a tall door down the middle, outside on the right (RTL reading starts there), inside on the left | s2 OUTSIDE: a small fist knocking, teal tear drops, knock marks. s3 INSIDE: shower steam, water strips, a pearl bubble. s4 both sides. s5 a snack bowl outside. s6 sound-wave strips passing through the door. s7 a small chair with a folded towel by the door. |
| 5 | p6 Only after he sleeps | tealMist (ink text) | **Pinned notes on a wall**: three torn paper notes, each with an icon | The notes reveal one per slide: s4 ear + vacuum with an end mark, s5 small hand + laundry, s6 cloth + small hand wiping. s2 a moon over a pile of chores (vacuum, pot, basket). s1 vacuum and pot greyed under a crescent moon. |
| 6 | p4 "Just today" | night | **Moons multiply**: one crescent becomes a row of crescents | s1 a big bed with two shapes under one duvet, a small bed empty beside it. s2 one moon. s3 the row of moons (every night). s4 a single gold sun (the day). s5 nap: a sun over a small bed. s6 a pearl speech bubble. s7 a dashed path from the big bed back to the small bed. |
| 7 | p7 Hair dryer | pearl (deep type; the batch's only pearl post) | **Mirror frame**: a big oval mirror, the dryer held at the edge, noise arcs | s2 a small figure on the bed edge covering his ears, torn noise arcs. s4 the dryer with three level marks, the lowest lit. s5 a small finger on the button. s6 the bed corner far from the mirror, the child seated with space around him. |
| 8 | p3 8 to 10 | deep | **Day band**: a horizontal torn-paper strip of the day, from afternoon sun to evening moon | s2 a long dark band 8→10 (two clock discs). s3 the strip from asr to bedtime. s4 the nap segment highlighted (sun low). s5 the activity segment: a screen and a running shoe give way to a ball and a cup. s6 a guest night (coffee dallah, door). s7 three segments with one ticked. |
| 9 | p12 Phone calls | tealMist (ink text) | **Tug of war**: a big phone across the middle, mum's hand holding it high, a small hand reaching | s3 metaphor: a favourite toy (car) held up out of reach. s4 the phone with sound waves. s5 an open box of crayons and stickers. s6 the phone on the table with speaker waves, far from the small hand. s7 a sticker sheet and paper. |
| 10 | p1 Night waking | night | **Top-down bed**: the big bed seen from above, a small duvet shape taking half, mum on the edge | s2 footsteps in the dark at 2am. s3 mum's eyes half-closed (closed-eye arcs, no face). s4 a clock disc at night and a gold tab. s5 a small hand led by a big hand along a dashed path, dim lamp. s6 a chair by the small bed. s7 method: a day/night strip. |
| 11 | p8 Blender | deep | **Macro crop through the jar**: the blender jar huge, cut off by the frame, banana slices inside | s2 jar full, the doorway lit beyond. s3 the jar back on the shelf. s4 big noise strips. s5 a folded towel under the base (striped sandLight). s6 short pulse marks (dash, gap, dash). s7 a small hand dropping a banana slice in. |
| 12 | p11 Kids' salon | sandLight | **The chair as a stage**: the salon chair centred under a gold spotlight cone, a mirror behind | s2 the empty chair, scattered hair clippings, half a haircut. s3 the chair, the clipper buzz strips, a strange hand. s4 a morning sun through the salon window, no queue. s5 mum's lap watching another child (back view). s6 a clipper in a small hand, buzz strips. s7 a small toy car in a hand. |

The CTA end is gold on all 12. Slide 8 (or the last slide) holds a small version of the post's hero motif, its pose varied per post.
