# Rebuilds state.json posts[] from posts_draft.json, keeping each post's status/score.
import json,datetime
s=json.load(open("state.json")); D=json.load(open("posts_draft.json"))
old={p["id"]:p for p in s.get("posts",[])}
ar="٠١٢٣٤٥٦٧٨٩"; num=lambda n:"".join(ar[int(d)] for d in str(n))
posts=[]
for p in D:
    o=old.get(p["id"],{})
    body="\n\n".join(f"({num(i)})\n{t}" for i,t in enumerate(p["slides_ar"],1))
    gl="\n".join(f"{i}. {g}" for i,g in enumerate(p["gloss_en"],1))
    notes=p.get("panel_en") or ("**Copywriter's flag:** "+p["notes_en"])
    posts.append({"id":p["id"],"conceptId":p["conceptId"],"title":f"{p['title']} ({p['job']}, {len(p['slides_ar'])} slides)","format":"slides",
      "status":p.get("status",o.get("status","draft")),"score":p.get("score",o.get("score")),
      "body_ar":body,"caption_ar":p["caption_ar"],"cta_ar":p["cta_ar"],"notes":notes+"\n\n**Back-translation:**\n\n"+gl})
s["posts"]=posts
s["updatedAt"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
json.dump(s,open("state.json","w"),ensure_ascii=False,indent=2)
