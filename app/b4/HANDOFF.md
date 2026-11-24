# Batch 4 handoff (Home Orbit / مدار البيت social media agency)
Written Nov 24, 2026, at the end of the Batch 3 chat. Repo: Anhar-web/Outreach-onboarding-form., branch `claude/zealous-thompson-8v31dc`.

## Where things stand
- **Batch 3 is finished:** all 12 posts are live and logged in Airtable. The analysis and the draft Batch 4 brief are written but not yet confirmed by Anhar.
- **The new landing page is live,** with tagged links and a Visits table.
- **Batch 4 hasn't started:** no hooks or copy yet. The next step is to confirm the brief with Anhar, then Research, then hooks.

## Read these first, in this order
1. **Airtable base "Home Orbit, Social Media Agency" (`appNJkIPFr6tPW6nP`):**
   - **Legacy Posts** (`tbls7mHqANNieD2n7`): all 25 of Anhar's pre-agency posts, with full Arabic text and analytics. **Her natural voice. Read every row before writing anything.**
   - **Feedback & Lessons:** every rule. The newest win. The "B4 rule ·" rows are the Batch 4 decisions.
   - **Batches, Posts, Post Performance, Conversion Windows, Formats, Visual Style.**
2. **Assessment base (`appxFnfLWBVqgv8sO`):**
   - **Submissions:** read only status, dates, q14, the click/waitlist flags, src, post, focus_tag and last_q. **Never names or emails.**
   - **Visits:** page loads with src, post, focus and entry.
3. **Repo files:**
   - `app/b4/step1_report.md`: the Batch 3 analysis plus the **draft Batch 4 brief**. Part 2b has the revisions.
   - `app/b4/legacy_voice_analysis.md`: why the old posts beat ours, measured, plus the **voice spec**.
   - `app/b4/legacy_analysis_notes.md`: notes on each of the 25 posts.
   - `app/b4/cta_method.md`: Anhar's custom CTA method, tone rules, and the soft-CTA decision.
   - `app/b4/links.md` and `app/b4/make_qr.py`: landing links and the tagged QR generator.
   - **`app/b4/VISUAL_STYLE_B4.md`: the Batch 4 visual system "Paper & Light" (5 looks plus feed-grid rules). Mockups are in `app/b4/visual/`. Use it for art direction and production.**
   - `app/b3/assessment_truth.md`: what CTAs may claim.
   - `app/ANHAR_FEEDBACK_HANDBOOK.md`: Parts M–P are the newest.

## Batch 4 decisions already made with Anhar
**Voice**
- **Her legacy voice is the default:**
  - short beats of 2–5 words a line, with «…» pauses
  - a stamp opening, then a contrast that turns to her («وأنتي؟»)
  - call-and-response escalation, then «وفجأة»
  - 2–4 real quoted lines from the people around her
  - ONE comic image that casts HER in an adult role
  - one love line that clears her
  - a named tool shown in action
  - a playful ending
- **First person is allowed** («خليني أوريك», «قوليلي», «بيننا»). "We" parents stays banned.
- **Humour:** funny, never performed or cringe. Conversational, extreme love.
- **Banned:** «طبيعي», brain/nervous-system lines, emoji bullets, medical disclaimers, acting out the child's drama, homework endings.
- **"One flowing sentence" and "full spoken sentences"** apply only to the final CTA and to checklist items.

**Structure (Part O)**
- One tool: 4–5 slides. Three steps: 6 at most.
  1. Hook: pain plus her cost.
  2. Deepen.
  3. The solution, on slide 3.
  4. Proof: **our method described**, never testimonials (it can carry explainer content).
  5. Twist plus CTA.
- **The twist is the unexpected, not a reframe:** a confession at the end that makes her laugh at herself (legacy L18, the coffee shop).
- **Revive the logical-fallacy series** «الافتراض اللي يصعّب الموضوع» (her 200K format): new on-brand look, fewer words per slide, no translucent box.

**Hooks and topics**
- **Test the problem + solution hook** (legacy L25, Eid).
- **What drives reach:** people reacting with lines in the scene (relatives, staff, strangers), the cost landing on her, and universal or strange-but-common moments.
- **Don't end a hook on his behaviour.** «ما تقدري… إلا» is retired.
- **Topics:**
  - a few old legacy topics with a new moment or tool (her own recreations of the diaper and grandma posts underperformed), plus new ones
  - emotions and outbursts lead
  - 1 bedtime post
  - no repeats of Batch 1–3 topics

**Give first and CTAs**
- **No ask of any kind before the last slide:** no soft CTA, no mid-post follow or comment.
- **An optional "keep reading" line** on longer posts is a promise only, tested with and without.
- **CTA method:**
  - Name the outcome she desperately wants in this situation, with certainty («يمكن», «جربي», «لو حابة» are banned), and never as homework («عبي التقييم» is banned).
  - The assessment is the bridge, never the promise.
  - Test: would she click without knowing what the assessment is?

**QR codes and tracking**
- One QR per post, made with `make_qr.py`.
- Odd posts go to the matching `?focus=` landing page, even posts to the assessment.
- Tags: `src=qr&post=b4pN`. The bio link is `?src=bio`.

**Comments, visuals, posting**
- **Comment prompt:** a one-word question about HER child's preference, tied to the tool (legacy L21: 75 comments). Generic questions get 0.
- **Visual:**
  - copy is the star, and the slide-1 image supports it
  - quiet motifs or colour later
  - a fresh look (Batch 3 used one teal style 12 times)
  - test a cream text-only slide 1 against dark
- **Posting:** 2 a day, about 7:00 PM, then 8:00–8:30 PM.

## Open items
- Anhar is checking why `last_q` stopped at 12 for a mother who answered Q14. It's our drop-off metric.
- **Confirm the draft brief with Anhar** (12 posts, the slate, the tests), then run Research, Hooks, Concepts and Copy with the skills.
- **After each Batch 4 evening:** log day 1 in Post Performance, then check Visits and Submissions by `post` tag.

## Key numbers
- **Legacy (25 posts):**
  - median ~3.4K views; only 1 under 1K
  - 4.3 slides
  - 3.3 words per line
  - 48–63% of slides viewed
- **Batch 3 (12 posts):**
  - 378–1,729 views
  - 2 completed assessments (1 per ~4K views), both anger/outbursts
  - 0 waitlist joins
  - best posts: ملكة 1.7K, جمعة 1.0K, jacket 948 (relatives reacting)
