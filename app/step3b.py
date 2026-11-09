from upd import *
a=open("research_audience.md").read().strip()
m=open("research_market.md").read().strip()
syn="""### Director's synthesis (read this first)
- **Both reports agree on the main open lane: "the workarounds".** Nobody in the market names the life she has quietly rearranged around him: vacuuming at night, lying down until he sleeps, cooking after he sleeps, showering only when he's asleep. Our two winners sat exactly there. The Market Analyst calls it a Stage-5 voice (identity: *she* adapted) carrying Stage-3 substance (real, ordered steps).
- **Second lane: "it starts before the moment".** The hard moment is shaped earlier in his day. This is also the most honest bridge to the assessment, which looks at his whole day.
- **Strongest new topics with evidence:**
  1. **Night waking: he comes to her bed.** There are several real Gulf forum titles, including mothers sleeping in a separate room from their husband.
  2. **"After he sleeps" is her whole to-do list**, including cooking at night.
  3. **The shower on his schedule.** Strong in English; the Arabic evidence is weak.
  4. **Haircut / hair wash.**
  
  Also possible: the hair dryer or blender (no quotes found), and phone calls (English only).
- **Watch-outs that change our copy:**
  - The chair step-back is now generic, and it was our own last post. Bedtime sequels need *new* steps.
  - "Warn him before you turn on the vacuum" is the most-repeated tip in the market, and we used it in p5. Chores sequels need fresher steps.
  - No sensory or "exposure" language, no headphones as the fix, no "independent sleeper" promise, no comment-for-link mechanics.
- **The CTA lane:**
  - An early one-line soft CTA under the first step.
  - The final CTA in the "one workaround of many" shape, tied back to the hook.
  - Line 1 of the caption carries the hook plus the CTA.
  - The pinned comment works as "part two": one extra step plus the assessment.
- **Honest limits:**
  - The forum pages were blocked in this environment, so the Arabic quotes are real thread titles and search snippets, not full threads.
  - Before any quote goes on a slide, someone opens the thread.
  - Batch 1 had 0 comments, so there is no comment bank to harvest yet.
  - Anhar: if you've received DMs or replies with mothers' words, they are the best source we could have.

---
"""
r=s["steps"][2]; r["status"]="needs-you"; r["report"]=syn+a+"\n\n---\n\n"+m
for p in s["plan"]["specialists"]:
    if p["key"] in("ar","ma"): p["status"]="done"
    if p["key"]=="st": p["status"]="needs-you"
save()
