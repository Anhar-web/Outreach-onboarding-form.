from upd import *
h=open("hooks.md").read().strip()
note="""### Director's review (read first)
The board is strong. The **A** hooks copy the winners' grammar almost exactly («فصرتي…», «وأنتي اللي…»). Before you pick, here are four flags I'm raising against your own past corrections:

1. **The "X يبدأ قبل…" second halves in Angle B echo a line you already rejected.** In Batch 1 you cut «الزيارة تبدأ في السيارة» as headline-like and jarring. B1 («الطلعة من غرفته تبدأ قبل ما تنسدحي»), B4 («الشاور يبدأ قبل ما تسكري الباب») and B6 («القصة تبدأ في البيت») use the same pattern. **My recommendation:** run B1, B4 and B6 with the **first line only**. The winners had no second half either, and the "it starts earlier" idea can open slide 2 instead. Keep B2's and B5's second halves; they promise something concrete.
2. **A5 uses «يشد يدك».** Your voice file says pull a hand = **يسحب**, and you approved «يسحبك من يدك» in Batch 1. Fixed suggestion: «أول ما تردي على الجوال يسحبك من يدك ويعلي صوته، فصرتي تكلمي أمك من الحمام؟»
3. **Many (b) halves start with «هذي ثلاث أشياء تسويها…».** That's fine once or twice (you approved «هذي ثلاث أشياء تلاحظيها…»), but across 12 posts it becomes a template. At concepts, each post gets its own second half, or none.
4. **Two are held for you:**
   - **C2:** husband sleeping alone. It's real, backed by Gulf forum titles, but sensitive.
   - **A6:** cutting his hair while he sleeps. It's unverified and may draw safety comments.

   Say if you want either in.

**Word questions, in one batch:**
- **(a)** «على أطراف أصابعك» or «على رؤوس أصابعك»?
- **(b)** «أكلم أمي من الحمام» or «من دورة المياه»?
- **(c)** «غدا بكرة», is that how you'd say "tomorrow's lunch"?
- **(d)** «السشوار», is that your word for hair dryer?

**Hook Specialist's top 12** (4 bedtime, 4 chores/noise, 4 new):
- **Bedtime:** A4 night waking · B1 sneaking out · B2 her evening lost · C1 "just tonight"
- **Chores/noise:** A2 cooking at night · C4 the "after he sleeps" list · A3 hair dryer · B5 blender
- **New:** A1 shower · C3 hair wash · B6 haircut · A5 phone calls

**Reserves:** B4, C5, B3, C6.

---

"""
r=s["steps"][3]; r["status"]="needs-you"; r["report"]=note+h
for p in s["plan"]["specialists"]:
    if p["key"]=="hk": p["status"]="done"
    if p["key"]=="st": p["status"]="needs-you"
save()
