import json,sys
from upd import s,save
pid,idx,text=sys.argv[1],int(sys.argv[2]),sys.argv[3]
f="posts_a.json" if int(pid[1:])<=6 else "posts_b.json"
P=json.load(open(f))
p=[x for x in P if x["id"]==pid][0]
print("OLD:",p["slides"][idx-1]); p["slides"][idx-1]=text
json.dump(P,open(f,"w"),ensure_ascii=False,indent=1)
for q in s["posts"]:
    if q["id"]==pid:
        parts=q["body_ar"].split("\n\n")
        assert parts[idx-1].startswith(f"({idx})")
        parts[idx-1]=f"({idx}) "+text.replace("[soft CTA] ","⟵ soft CTA: ")
        q["body_ar"]="\n\n".join(parts)
save()
