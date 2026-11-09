from upd import *
for c in s["concepts"]: c["format"]="slides · "+c["angle"].split(']')[0][1:]
s["steps"][5]["status"]="done"; s["steps"][5]["report"]+="\n\n**Decided (Nov 9):** all 12 are **static slides**, with the labels as proposed."
s["currentStep"]=7; s["steps"][6]["status"]="working"; s["steps"][6]["report"]="*Two Copywriters are writing the 12 posts in parallel (c1–c6 and c7–c12)…*"
for p in s["plan"]["specialists"]:
    if p["key"]=="st": p["status"]="done"
    if p["key"]=="cw": p["status"]="working"
save()
import json
json.dump(s["concepts"],open("concepts.json","w"),ensure_ascii=False,indent=1)
