from upd import *
import json
s["steps"][7]["status"]="done"
s["steps"][7]["report"]+="\n\n**Decision (Nov 9):** no further edits. Anhar: her edited slides are final, and the suggested wording fixes \"don't sound like me\". All posts ship exactly as she edited them."
s["currentStep"]=9; s["steps"][8]["status"]="done"
F=json.load(open("posts_final.json"))
order=sorted(F,key=lambda f:f["posting_order"])
rows="\n".join(f"| {f['posting_order']} | {f['id']} | {f['title']} | {f['format'].replace('slides · ','')} | {len(f['slides'])} | {f['test_panel_score']} |" for f in order)
s["steps"][8]["report"]=f"""### Batch 2 handoff: 12 posts, final
Every slide is exactly as Anhar approved it. Captions and pinned comments are on each post card and in Airtable.

| Day | Post | Concept | Format | Slides | Panel |
|---|---|---|---|---|---|
{rows}

One a day. Topics are alternated, and the four bedtime posts are kept apart.

### Logged
- **Airtable → Batches:** "Batch 2: 12 static carousels (Nov 2026)".
- **Airtable → Posts:** 12 rows (B2-p1 … B2-p12) with the final slides, caption, pinned comment, format label, posting order, score and who wrote what.
- **Airtable → Feedback & Lessons:** 29 new Batch 2 rows covering every edit, with before → after → her reason → rule: hooks, structure, CTA, realism, connectors and her word list.
- **Handbook:** `app/ANHAR_FEEDBACK_HANDBOOK.md` now has **Part H (Batch 2 lessons)**. Attach this version to the next chat.
- **Repo** (branch `claude/adoring-planck-83m3n1`): `app/posts_final.json`, `app/lessons_batch2.md`, `app/test_panel.json`.

### Next
- **Visuals:** run the Creative Production skill on `app/posts_final.json`. Consider a small «التقييم المجاني في البايو» footer on every slide, since viewers see about 2 slides.
- **Tracking:** tag the bio link `?src=tiktok` and record assessment *starts*.
- **After posting:** send the numbers and say **"what's working?"**."""
for p in s["plan"]["specialists"]:
    if p["key"]=="st": p["status"]="done"
for q in s["posts"]: q["status"]="final"
s["performance"]=[r for r in s["performance"]]+[{"postId":f"B2 {f['id']}","postedOn":"","job":"value + CTA","format":f["format"].replace("slides · ",""),"views":None,"likes":None,"saves":None,"comments":None,"shares":None,"profileVisits":None,"assessmentStarts":None,"note":f"day {f['posting_order']}"} for f in order]
save()
