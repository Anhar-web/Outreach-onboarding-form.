"""Build app/state.json for Batch 4 and an embedded-state copy of the dashboard (b4/dashboard_b4.html)."""
import json, datetime, os
here = os.path.dirname(os.path.abspath(__file__)); app = os.path.dirname(here)
report = open(os.path.join(here, "b4_step1_analysis_brief.md"), encoding="utf-8").read()
steps = [
 (1,"brief","Brief","The Analyst reads Batch 3 and the legacy posts; the Strategist turns it into the Batch 4 brief.","Decide the job before the post","Most content fails because nobody decided what it was for.","Read the analysis and the brief, answer the three questions, then confirm.","Looks right. Next step."),
 (2,"scorecard","Scorecard","The Strategist sets this batch's 100-point scorecard and the plan.","Define 'good' before anyone writes","If we agree on what a great post looks like now, the Test Panel can't move the goalposts later.","Approve the weights and the plan.","Go."),
 (3,"research","Research","Audience Researcher and Market Analyst work in parallel.","Her words, not ours","The best lines are the ones she has already said to her sister.","Read both reports.","Both look good. Next step."),
 (4,"hooks","Angles & hooks","The Hook Specialist builds angles and scored hooks in your legacy voice.","The hook carries most of the result","Frame one decides whether the rest exists for her.","Pick, cut or rewrite hooks.","These are good. Build concepts."),
 (5,"concepts","Concepts","The Strategist assembles distinct concepts for you to pick.","Options, not one answer","A batch is a test. We need real variety to learn from.","Pick the concepts to produce.","Produce these."),
 (6,"format","Format","You decide static slides or video for each picked concept.","Format follows the idea","Some ideas need to be swiped, some need to move.","Choose static or video per concept.","Formats chosen."),
 (7,"production","Production","The Copywriter writes every picked post in Arabic.","Written last, never from a blank page","Every post starts from a picked concept, a chosen hook and her own words.","Read the drafts.","Looks good. Edit and test."),
 (8,"test","Arabic + Test","The Arabic Voice Editor, then the sceptical Test Panel.","Born in Arabic, tested cold","A line that sounds translated loses, whatever its score.","Choose what ships.","Ship the winners."),
 (9,"handoff","Handoff","The Strategist packages the final posts with their QR codes.","Finished when the numbers teach us","After each evening, log day 1 and read Visits and Submissions by post tag.","Done.",None),
]
S=[{"n":n,"key":k,"title":t,"subtitle":sub,"status":"needs-you" if n==1 else "idle",
    "idea":{"title":it,"body":ib},"action":{"label":al,"phrase":ph},"report":report if n==1 else ""}
   for n,k,t,sub,it,ib,al,ph in steps]
perf=[("B3 p1 ملكة","Nov 17",1729,8,0,1),("B3 p2 جمعة","Nov 18",1008,2,0,3),("B3 p12 Jacket","Nov 19",948,4,1,3),
      ("B3 p10 Nails","Nov 20",587,1,0,0),("B3 p5 Biscuit","Nov 17",579,1,0,0),("B3 p11 Hand dryer","Nov 16",552,1,0,0),
      ("B3 p9 No","Nov 21",469,2,0,4),("B3 p3 Checkout","Nov 16",450,0,0,0),("B3 p8 Ride","Nov 21",442,1,0,0),
      ("B3 p6 Tower","Nov 20",416,1,0,0),("B3 p4 Fast food","Nov 22",413,2,0,0),("B3 p7 Losing game","Nov 23",378,0,0,0)]
state={"project":"Home Orbit — Batch 4 (Nov 2026)","updatedAt":datetime.datetime.utcnow().isoformat()+"Z","currentStep":1,"steps":S,
 "plan":{"specialists":[
  {"key":"st","name":"Strategist","role":"The brief, scorecard, concepts, handoff","status":"needs-you"},
  {"key":"ar","name":"Audience Researcher","role":"What mothers actually say","status":"idle"},
  {"key":"ma","name":"Market Analyst","role":"What the market has heard","status":"idle"},
  {"key":"hk","name":"Hook Specialist","role":"Angles and hooks, legacy voice","status":"idle"},
  {"key":"cw","name":"Copywriter","role":"Writes the posts","status":"idle"},
  {"key":"av","name":"Arabic Voice Editor","role":"Makes it sound native","status":"idle"},
  {"key":"tp","name":"Test Panel","role":"Sceptical mothers, scored","status":"idle"},
  {"key":"an","name":"Analyst","role":"B3 + legacy read done; next read after B4 evenings","status":"done"}]},
 "scorecard":{"total":100,"items":[{"name":a,"weight":w,"score":None} for a,w in [("Scroll-stop",18),("Recognition",15),("Emotion, not apathy",15),("Her own words",12),("One job",10),("Trust & safety",10),("Arabic naturalness",8),("The turn",6),("Next step",4),("Shareable",2)]]},
 "concepts":[],"posts":[],
 "performance":[{"postId":p,"postedOn":d,"job":"value + CTA","format":"static","views":v,"likes":None,"saves":sv,"comments":c,"shares":sh,"profileVisits":None,"assessmentStarts":None,"note":"day 1"} for p,d,v,sv,c,sh in perf]}
json.dump(state,open(os.path.join(app,"state.json"),"w"),ensure_ascii=False,indent=1)
html=open(os.path.join(app,"dashboard.html"),encoding="utf-8").read()
html=html.replace("<title>Home Orbit Agency Board</title>","<title>Home Orbit Batch 4 Board</title>",1)
blob="window.__STATE__ = "+json.dumps(state,ensure_ascii=False).replace("</","<\\/")+";\n"
i=html.index("<script>")+len("<script>")
open(os.path.join(here,"dashboard_b4.html"),"w",encoding="utf-8").write(html[:i]+"\n"+blob+html[i:])
print("ok")
