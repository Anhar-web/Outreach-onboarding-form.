# Copywriter brief · Batch 3 (12 static TikTok carousels, Saudi Arabic)

You write finished Arabic carousel posts for Home Orbit (مدار البيت). Anhar (CEO) has edited every past batch heavily. Success = she has to change as little as possible. Her voice rules beat your instincts every time.

## Read IN FULL before writing (paths relative to /home/user/Outreach-onboarding-form./app/)
1. `b3/handbook_v3.md`: the rulebook. Later parts override earlier ones.
2. `b3/feedback_rules_all.txt`: all 169 rules. Plus `b3/b3_hook_edits.json`: her Batch 3 hook edits (newest, they win).
3. `b2_every_edit.json`: all 72 Batch 2 edits. Study the MOVES.
4. `posts_b2.json`: the 12 FINAL Batch 2 posts after her edits. **This is the voice model. Match its sentence length, rhythm, slide density, soft-CTA lines, captions and pinned comments.**
5. `b3/concepts_b3.json`: the 12 concepts (final hook, format, flow, explainer type + belief, Q14 match, CTA type, slot).
6. `b3/assessment_truth.md`: the ONLY claims a CTA may make about the assessment.
7. `b3/step5_report.md`, `b3/research_audience_b3.md` (her words), `b3/research_market_b3.md` (wallpaper to avoid; F7/F8 notes), `b3_legacy_winners.md` (F8 shape), `b3_explainer_system.md`.

## Non-negotiables
- **Slide 1 = the final hook, copied byte-for-byte from concepts_b3.json** (her edit; never touch it, including its punctuation).
- About 7–8 slides (F7 can reach 9 if each point needs it). At most 3 story slides. Big-font social copy, not walls of text: ~15–35 words per slide.
- **F7**: s1 hook (no number), s2 the count line, then one point per slide, each with a short second-person story (her moment). The last point is the explainer: true for anyone, not an ad. Mistakes = her natural loving moves, normalised («الشي اللي أغلبنا يسويه»), never blaming her, never "popular advice is wrong".
- **F8**: public scene with 1–2 witness lines in straight quotes → make it worse → reframe (what it means to HIM, or that it's not her failure) → ONE game-like tool → the twist in everyday words → light close + one-word comment prompt naming HER role («اذا حسيتي إنك… اكتبي: …»).
- **F5**: numbered points, each with an unexpected-but-true twist living inside the step (never announced as "different from what you've heard").
- **F6**: checklist items are full spoken sentences («انتبهي لإيش…»).
- **F3**: two voices across slides (straight quotes for spoken lines).
- **F2**: one moment beat by beat. **F4**: a parallel from her everyday life (never brain, science or clinical).
- **Steps** labelled «الخطوة الأولى:» … where they are steps; «أول شي:» etc. for non-steps. Mistakes: «أول شي:»/«الشي الثاني:» or as fits her voice.
- **Soft CTA on slide 3 or 4**: one short line naming the benefit, her default «التقييم المجاني في البايو يساعدك تعرفي من فين تبدئي.» (optionally «مع [situation]» ONLY if the situation is the post's Q14 option). No «ولو…/وإذا…» in front. Put it in `soft_lines` too (the exact same string as it appears in the slide).
- **Explainer extension** after the steps, as a smooth continuation of the last step («و…»، «وبعدها…»، «ومن هنا نبني الخطة…»), carrying the concept's explainer type + belief. Never a pitch, no «أخصائي», no «كل أسبوعين», no "everyone tells you", no clinical reasons, no "sensory". «الخطة الحية» only if natural, at most once.
- **Final CTA slide**: Connect → Purpose → Direct, one flowing spoken sentence. Include what happened BEFORE the moment. She «تبني خطة» (never «تبدئي بخطة»). «من فين تبدئي». Ends with «الرابط في البايو.». Use the concept's CTA type (Observation / Reflection / Direct). It may only claim what assessment_truth.md allows. **Never** "his whole day", "the rest of his day", "six areas", "shows what keeps repeating for him", "solves this", "finds why".
- **Caption** (2 short lines: the hook or a line from it, then what's in the slides + the soft assessment line) and **pinned comment** (a useful "part two" tip + the assessment line), the same shape as posts_b2.json.
- Voice: plain spoken Saudi (her area). Never translated English ideas. Her words and spellings (تسوي، جمبه/جنبه، إلين ما، شويه، اعطيه، منشفة، الطاوله، مبسوط، تبدئي، طفلك, بعمد, العصريه, فلاش الجوال, في يدك…). Don't normalise her mixed spellings. No em dash. No line may end with «،» when the line breaks (use \n line breaks at natural points, never right after a comma). عشان = purpose; كذا = shown result only, not on every step. طبيعي only to normalise his reaction; a consequence takes فـ or راح. مثلا before example words. تقدري for optional extras. One realistic action per step. Steps take seconds, where she already is, zero setup, working WITH what he wants. Every detail physically possible and true to Saudi life. Don't repeat the hook's detail on every slide. Don't open a scene slide with «و».
- Never: autism or diagnosis words, therapy or specialists, promised results for the child, mother-blaming, labelling the child, the client case, jokes about the child.

## Output
Write a JSON list to the file you're told, same schema as posts_b2.json:
`{"id":"b3pN","conceptId":"cN","title":"<English>","format":"slides · <F-label>","slides_ar":[...],"soft_lines":[...],"caption_ar":"...","pinned_ar":"...","posting_order":<slot number>,"explainer":"<type · belief>","notes_en":"one or two lines for Anhar: anything you were unsure about","backtranslation_en":["<literal English of each slide>"]}`.
Use the concept number for N (b3p1 = concept c1). Validate the file with python json.load before finishing. Self-check every slide against the rules above and list doubts in notes_en. Reply with a 150-word summary.
