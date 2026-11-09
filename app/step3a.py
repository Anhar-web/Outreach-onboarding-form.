from upd import *
s["steps"][1]["status"]="done"; s["currentStep"]=3; s["steps"][2]["status"]="working"
s["steps"][2]["report"]="*The Audience Researcher and Market Analyst are working in parallel…*"
for p in s["plan"]["specialists"]:
    if p["key"]=="st": p["status"]="done"
    if p["key"] in("ar","ma"): p["status"]="working"
save()
