from upd import *
for c in s["concepts"]: c["status"]="picked"
s["steps"][4]["status"]="done"; s["steps"][4]["report"]+="\n\n**Picked (Nov 9):** Anhar approved all 12 concepts."
s["currentStep"]=6; s["steps"][5]["status"]="needs-you"
rows="\n".join(f"| {c['id']} | {c['title']} | {c['angle'].split(']')[0][1:]} | static (proposed) |" for c in s["concepts"])
s["steps"][5]["report"]=f"""### Static slides or video, for each concept?
Nothing gets written until you decide. **Proposed:** all 12 as static carousels, the same as Batch 1, so the format labels (F1–F6) are the only thing that changes and the comparison stays clean.

| # | Concept | Format label | Static / video |
|---|---|---|---|
{rows}

**Concepts that could also work as video** (a concept can be both):
- **c2 Sneaking out (F2 Story):** the slow arm-slide and creaking floor are real movement and sound.
- **c9 Shower (F3 Two voices):** the knocking and crying at the door, heard from inside.
- **c8 Blender (F2 Story):** the before/after sound of the towel trick is something you hear, not read.

Video would need a script plus faceless footage or animation, which is a separate production run."""
save()
