from upd import *
s["steps"][6]["status"]="done"
s["steps"][6]["report"]+="\n\n**Anhar's edit round (Nov 9):** about 35 slide-level edits across all 12 posts, made through dashboard comments. Every one was applied verbatim and studied into rules in `app/lessons_batch2.md`. She moved on to testing."
s["currentStep"]=8; s["steps"][7]["status"]="working"; s["steps"][7]["report"]="*The Arabic Voice Editor is doing a light pass on the parts you didn't touch. Your edited slides are locked. The Test Panel runs after the editor.*"
for p in s["plan"]["specialists"]:
    if p["key"]=="st": p["status"]="done"
    if p["key"]=="av": p["status"]="working"
save()
