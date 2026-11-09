from upd import *
s["steps"][0]["status"]="done"
s["steps"][0]["report"]+="""

### Confirmed (Nov 9)
Anhar confirmed the brief. The proposed defaults stand: **10 posts**, TikTok, static carousels unless step 6 chooses video for a concept. Still open, but not blocking the writing: whether the bio link is tagged `?src=tiktok`, whether someone is tracking assessment starts, and whether the Nov 8 waitlist record was a test."""
s["currentStep"]=2
s["steps"][1]["status"]="needs-you"
items=[("Scroll-stop (winning hook shape)",16),("Recognition",12),("Emotion, not apathy",12),("Her own words",10),("Usable value («رؤوس أقلام»)",12),("Trust & safety (gate)",10),("Arabic naturalness",8),("The turn / perspective shift",8),("CTA: seen and earned",10),("Save / share-worthy",2)]
s["scorecard"]["items"]=[{"name":a,"weight":w,"score":None} for a,w in items]
s["steps"][1]["report"]="""### Batch 2 scorecard (reweighted, still 100)

Batch 1 taught us three things. Reach came from the hook shape. Saves came from real, usable steps. Business died because nobody saw a CTA. The weights move to match that.

| Item | B1 | B2 | Why it moved |
|---|---|---|---|
| Scroll-stop (winning hook shape) | 18 | **16** | Still the biggest item. It is now judged against the proven shape: her moment plus a true, ironic twist about her. |
| Recognition | 15 | **12** | Folded partly into the hook shape. |
| Emotion, not apathy | 15 | **12** | Still a fail line: if nothing is felt, it fails. |
| Her own words | 12 | **10** | |
| **Usable value («رؤوس أقلام»)** | new | **12** | Replaces "One job". Could she do something different tonight? Is it generic? Is it realistic in her home? Bedtime's 36 saves came from this. |
| Trust & safety (gate) | 10 | **10** | A violation still caps the post. |
| Arabic naturalness | 8 | **8** | |
| The turn / perspective shift | 6 | **8** | Hook Point driver 1: a surprising but true take beats a predictable one. |
| **CTA: seen and earned** | 4 | **10** | There's an early soft CTA, a final CTA in the Connect → Purpose → Direct shape, and a pinned comment. It must read as the next step, not a lead grab. |
| Save / share-worthy | 2 | **2** | |

**Why "One job" was dropped:** every Batch 2 post has the same job (value, then the assessment), so it no longer tells posts apart. It becomes a pass/fail check.

### Pass/fail checks (the Test Panel ticks these on every post)
- Slide 2 escalates the problem with a scene or her inner voice. It does not start the list.
- Around 7 slides. Big type, few words.
- A soft CTA by slide 3 (or right after the first tip), and a final CTA. No repeated CTA slide.
- A format label (F1–F6) is recorded. Formats vary across the 10.
- Proof, where used, is the method. No testimonials, no client case.
- Steps are labelled in full («الخطوة الأولى:»). No em dash. تبدئي / ابدئي.
- Hand her the value; don't order her. No homework, no quiz.

### Agency plan
| Step | Who | What |
|---|---|---|
| 3 | **Audience Researcher + Market Analyst, in parallel** | Her words on bedtime, chores/noise and new candidate moments; the market stage and the open lane. They get the Batch 1 results as input. |
| 4 | Hook Specialist (Hook Point mechanics) | 3 angles × 4–6 hooks, all in the winning shape, scored on the 4 performance drivers. |
| 5 | Strategist | About 14 concepts so you can pick 10: 4 sequels and the rest new. Each gets a suggested format label. |
| 6 | **You** | Static or video, plus the format label, for each concept. |
| 7 | Copywriter | Reads your Arabic file and the addendum first, then writes all 10 with captions and pinned comments. |
| 8 | Arabic Voice Editor, then Test Panel | Native edit (Original → Corrected → Why), then 3 sceptical mothers and this scorecard. |
| 9 | Strategist | Handoff, Airtable rows, posting order (one a day). |
"""
for p in s["plan"]["specialists"]:
    if p["key"]=="st": p["status"]="needs-you"
save()
