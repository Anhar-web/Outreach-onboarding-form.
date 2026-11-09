import json, datetime
brief = r"""
### Batch 2 brief (draft, pre-filled from your Batch 1 instructions)

**Why this batch, now.** Batch 1 split in two. Bedtime (4.4K views, 36 saves) and Vacuum (3.9K views, 13 followers) broke out and are still growing. The other 8 stopped at TikTok's first test audience (~420–480 views). Business result: **0 assessment completions Nov 4–9** (Oct 23–28 had 8). The two posts that reached people had no CTA; the conversion posts had their CTA on the last slide, but viewers saw ~2 slides.

**The job.** No more attention vs conversion split. **Every post = real value + a CTA that feels like the logical next step** (Connect → Purpose → Direct, rotating Observation / Reflection / Direct). One link in bio → the free assessment.

**The hook shape (every post).** Her real moment + a true, ironic twist about *her*, framed so any parent of a young child recognises it. Models: «فصرتي تكنسي وهو نايم؟» and «وأنتي اللي نمتي؟». Not the child's behaviour as a problem to fix.

**Structure.**
- Slide 2 **escalates the problem** (scene, inner voice), it does not start the list.
- ~**7 slides**. No walls of text.
- The CTA must be **seen**: a soft CTA early (slide 2–3 or right after the first tip), the final CTA, the caption, and a **pinned comment**.
- Every post carries a **format label** (F1 HPSPC, F2 Story, F3 Two voices, F4 Metaphor, F5 Walk-through, F6 Checklist), varied across the batch so we can compare. F0 Steps is the baseline.
- Proof = the **method** in plain words (whole day, one area at a time, adjusts every two weeks, built from her observations). No testimonials, no client case.

**Topics.** Sequels to the two proven topics (**bedtime** and **chores / noise**) in new formats, plus new topics chosen by research. Every post names a visible behaviour, never a label or diagnosis.

**Audience.** A cold new mother who has never heard of Home Orbit, scrolling TikTok.

**Win.** Assessment starts and waitlist sign-ups first; then profile visits, saves, shares, swipe depth. Comments matter least.

**Cadence & tracking.** One post per day. Bio link tagged `?src=tiktok`. Track assessment **starts**, not only completions. Collect profile views per post.

**Off-limits (unchanged).** Autism or any diagnosis, therapy/specialists, promised results, medical causes, the client case, homework/quiz framing, generic or unrealistic tips, cups/plates in change posts, the em dash in Arabic.

### Assumptions I need you to confirm
1. **How many posts?** I propose **10** (ten days at one per day): 4 sequels (2 bedtime, 2 chores/noise) + 6 new topics from research.
2. **Platforms:** TikTok only (as in Batch 1), or TikTok + Instagram?
3. **Format:** static carousels again, with video still offered per concept at step 6?
4. **Tracking:** is the bio link already `?src=tiktok`, and is someone adding assessment *starts* to the base? (The base only logs completions; `startedAt` is empty.)
5. **The Nov 8 waitlist record** with no assessment data: a test, or a real sign-up?
"""
steps = [
 (1,"brief","Brief","The Strategist turns your answers into the brief every specialist works from.","Decide the job before the post","Most content fails because nobody decided what it was for.","Answer the five questions in chat, then confirm.","Looks right. Next step."),
 (2,"scorecard","Scorecard","The Strategist sets this batch's 100-point scorecard and the plan.","Define 'good' before anyone writes","If we agree on what a great post looks like now, the Test Panel can't move the goalposts later.","Approve the weights and the plan.","Go."),
 (3,"research","Research","Audience Researcher and Market Analyst work in parallel.","Her words, not ours","The best lines are the ones she has already said to her sister.","Read both reports.","Both look good. Next step."),
 (4,"hooks","Angles & hooks","The Hook Specialist builds angles and scored hooks.","The hook carries most of the result","Frame one decides whether the rest exists for her.","Pick, cut or rewrite hooks.","These are good. Build concepts."),
 (5,"concepts","Concepts","The Strategist assembles distinct concepts for you to pick.","Options, not one answer","A batch is a test. We need real variety to learn from.","Pick the concepts to produce.","Produce these."),
 (6,"format","Format","You decide static slides or video for each picked concept, and its format label.","Format follows the idea","Some ideas need to be swiped, some need to move.","Choose static or video (and the F-label) per concept.","Formats chosen."),
 (7,"production","Production","The Copywriter writes every picked post in Arabic.","Written last, never from a blank page","Every post starts from a picked concept, a chosen hook and her own words.","Read the drafts.","Looks good. Edit and test."),
 (8,"test","Arabic + Test","The Arabic Voice Editor, then the sceptical Test Panel.","Born in Arabic, tested cold","A line that sounds translated loses, whatever its score.","Choose what ships.","Ship the winners."),
 (9,"handoff","Handoff","The Strategist packages the final posts.","Finished when the numbers teach us","After posting, tell us the numbers and ask 'what's working?'.","Done.",None),
]
S=[]
for n,k,t,sub,it,ib,al,ph in steps:
    S.append({"n":n,"key":k,"title":t,"subtitle":sub,"status":"needs-you" if n==1 else "idle",
      "idea":{"title":it,"body":ib},"action":{"label":al,"phrase":ph},"report":brief.strip() if n==1 else ""})
state={
 "project":"Home Orbit — Batch 2 (Nov 2026)",
 "updatedAt":datetime.datetime.utcnow().isoformat()+"Z",
 "currentStep":1,"steps":S,
 "plan":{"specialists":[
  {"key":"st","name":"Strategist","role":"The brief, scorecard, concepts, handoff","status":"needs-you"},
  {"key":"ar","name":"Audience Researcher","role":"What mothers actually say","status":"idle"},
  {"key":"ma","name":"Market Analyst","role":"What the market has heard","status":"idle"},
  {"key":"hk","name":"Hook Specialist","role":"Angles and hooks","status":"idle"},
  {"key":"cw","name":"Copywriter","role":"Writes the posts","status":"idle"},
  {"key":"av","name":"Arabic Voice Editor","role":"Makes it sound native","status":"idle"},
  {"key":"tp","name":"Test Panel","role":"Sceptical mothers, scored","status":"idle"},
  {"key":"an","name":"Analyst","role":"Batch 1 read; next read after posting","status":"done"}]},
 "scorecard":{"total":100,"items":[{"name":a,"weight":w,"score":None} for a,w in [("Scroll-stop",18),("Recognition",15),("Emotion, not apathy",15),("Her own words",12),("One job",10),("Trust & safety",10),("Arabic naturalness",8),("The turn",6),("Next step",4),("Shareable",2)]]},
 "concepts":[],"posts":[],
 "performance":[
  {"postId":"B1 p3 Bedtime","postedOn":"Nov 6","job":"attention","format":"F0","views":4433,"likes":60,"saves":36,"comments":0,"shares":10,"profileVisits":None,"assessmentStarts":None,"note":"day 3, still growing"},
  {"postId":"B1 p5 Vacuum","postedOn":"Nov 4","job":"attention","format":"F0","views":3857,"likes":35,"saves":9,"comments":0,"shares":10,"profileVisits":None,"assessmentStarts":None,"note":"day 5, 13 followers"},
  {"postId":"B1 other 8 (range)","postedOn":"Nov 4–8","job":"mixed","format":"F0","views":448,"likes":None,"saves":None,"comments":0,"shares":None,"profileVisits":None,"assessmentStarts":0,"note":"416–483 views each; 0 assessments in window"}]
}
json.dump(state,open("state.json","w"),ensure_ascii=False,indent=1)
