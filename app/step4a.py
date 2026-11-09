from upd import *
s["steps"][2]["status"]="done"; s["currentStep"]=4
s["steps"][0]["report"]+="\n\n**Update (Nov 9):** Anhar set the batch to **12 posts**."
s["steps"][3]["status"]="working"; s["steps"][3]["report"]="*The Hook Specialist is building angles and hooks…*"
for p in s["plan"]["specialists"]:
    if p["key"]=="st": p["status"]="done"
    if p["key"]=="hk": p["status"]="working"
save()
