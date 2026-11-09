from upd import *
import json
P=json.load(open("posts_a.json"))+json.load(open("posts_b.json"))
s["posts"]=[]
for p in P:
    body="\n\n".join(f"({i}) {sl.replace('[soft CTA] ','⟵ soft CTA: ')}" for i,sl in enumerate(p["slides"],1))
    body+="\n\n— التعليق المثبت —\n"+p["pinned_comment_ar"]
    s["posts"].append({"id":p["id"],"conceptId":p["conceptId"],"title":p["title"],"format":p["format"]+" · CTA: "+p["cta_variation"],
      "status":"draft","score":None,"body_ar":body,"caption_ar":p["caption_ar"],
      "notes":"Back-translation: "+" | ".join(p["backtranslation"])+"\n\nCopywriter: "+p["notes"]})
s["steps"][6]["status"]="needs-you"
s["steps"][6]["report"]="""### 12 drafts are in
Every post has your hook verbatim on slide 1, a scene or inner-voice slide 2, one soft CTA under the first step (marked ⟵ on the cards), steps labelled in full, a final Connect → Purpose → Direct CTA ending «الرابط في البايو», a caption whose first line carries the CTA, and a pinned comment "part two". 7–8 slides each. Proof slides (method only) on the three F1 posts. Automatic checks: no em dash, hooks verbatim.

The full slides are in **The posts** section below.

### Director's flags (the Arabic Voice Editor fixes these next unless you say otherwise)
1. **p3 uses the "X ما تبدأ … تبدأ من العصر" line twice** (slides 3 and 8). That's the «الزيارة تبدأ في السيارة» pattern you rejected. It will be rewritten plainly.
2. **p12 final slide «…بدل ما تقفلي الباب كل ما رن جوالك» leans toward a promise.** It will be softened.
3. **p10 slide 7 «ويمكن هذي المرة تطلعي … ناشفة أكثر منه»** is a callback joke. It may read as forced or as a promise, so it's a candidate to cut.
4. **p7 slide 4 «الكل يقولك…»** is the F5 twist that breaks advice she's heard. Is that OK, or does it feel like the «قالوا لك» angle you didn't want?
5. **The method slide says «الخطة الحية»** (p1, p5). Is that the Arabic name you use publicly, or should it say «في مدار البيت»?

### Your realism checks
- **p2:** leave while he's still awake, «برجع لك بعد شوي», and come back after 1, then 2, then 5 minutes.
- **p3:** wake him a bit earlier from the afternoon nap («ولو نص ساعة»). Realistic?
- **p4:** start with the **midday nap** in his own bed. Do most of your audience's children still nap?
- **p8:** a folded towel under the blender, and he puts the banana in himself.

### Word questions, in one batch
| Word | Used for | Question |
|---|---|---|
| سوالف / يسولف | chatting | Natural for you? |
| توسعي له مكان | make room for him | OK? |
| ذيك الليلة | that night | or «هذيك الليلة»? |
| نومة الظهر / نومة العصر | the afternoon nap | which one do you say? |
| بلوزتك | your top | OK? |
| وعاء / طاسة | a bowl | which? |
| ودك | you'd like | OK? |
| الصالة | living room | OK? |
| الدش | hand shower | or «الشطاف» / «رشاش الشاور»? |
| مفصول | unplugged | OK? |
| المكينة، ترج | clipper, its buzz | OK? |
| سناكه، السبيكر | his snacks, speakerphone | keep, or Arabic? |
| من جهته هو | from his side | or «من برا الباب»? |
"""
for p in s["plan"]["specialists"]:
    if p["key"]=="cw": p["status"]="done"
    if p["key"]=="st": p["status"]="needs-you"
save()
