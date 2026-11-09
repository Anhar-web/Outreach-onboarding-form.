from upd import *
import re
# fix hook 9 to Anhar's wording
rep=s["steps"][3]["report"]
rep=rep.replace("| 9 | New: shower | يدق ويبكي على باب الحمام أول ما تسكريه، فصرتي تتروشي بعد ما ينام أو قبل ما يصحى؟ | draft from Anhar's direction |",
 "| 9 | New: shower | يدق باب الحمام ويبكي  أول ما تسكريه، فصرتي تتروشي بعد ما ينام أو قبل ما يصحى؟ | Anhar |")
rep=rep.replace("**Hook 9 (shower) is my draft from your direction.** Please confirm it or reword it.\n\n","")
s["steps"][3]["report"]=rep; s["steps"][3]["status"]="done"
s["currentStep"]=5; s["steps"][4]["status"]="needs-you"
C=[
("c1","Night waking: half your bed is his","F1 HPSPC","Reflection",
 "سريرك صار نصه لطفلك؟ كل ليلة الساعة اثنين يجي ينام جنبك؟","Your bed has become half your child's? Every night at two he comes to sleep beside you?",
 "Problem: at 2am she's half asleep, and letting him in is the only easy choice; by morning she's on the edge of her own bed. Solution: (1) decide what you'll do at 2am *before* the night, so you're not deciding half asleep; (2) walk him back every time with the same two words, e.g. \"يلا سريرك\", lights low, no talk; (3) if you need to stay, sit by *his* bed and don't lie down. Proof: the method line. CTA (Reflection): the 2am visit is one moment of many; the assessment shows where to start."),
("c2","Sneaking out: he opens his eyes","F2 Story","Observation",
 "جلستي ساعة  تنوميه، وأول ما قُمتي من جمبه فتح عيونه؟","You sat an hour getting him to sleep, and the moment you got up from beside him he opened his eyes?",
 "Story beats: the hour, sliding her arm out, the floor creaks, his eyes open, back to zero. Turn: he fell asleep with you there, so when he half-wakes and you're gone, it's a new place. Move (not the chair method): tell him \"برجع لك بعد شوي\" and leave while he's still awake, then really come back after a minute, then two, then five. He learns you come back. CTA (Observation): notice how he falls asleep each night; those details build the plan."),
("c3","Your evening: 8 to 10","F6 Checklist","Observation (Anhar's bedtime CTA)",
 "تبدئي تنوميه الساعة ثمانيه، وما تطلعي من غرفته إلا الساعة عشره؟","You start putting him to sleep at eight, and you don't leave his room until ten?",
 "Self-check, one part per slide: (1) what time did his afternoon nap end? (2) what was the last thing he did before pyjamas (screen, running around, a bath)? (3) did bedtime move tonight because of a visit or guests? One small move for each. The «رؤوس أقلام» are the three checks themselves. CTA = Anhar's own: «لاحظي ايش يصير خلال اليوم قبل وقت النوم…»."),
("c4","\"Just today\" became every night","F3 Two voices","Direct",
 "قلتي له اليوم بس تنام جنبي، ودحين ما يرضى ينام لحاله؟","You told him 'just today you'll sleep beside me', and now he refuses to sleep on his own?",
 "Two voices: the her of that night («اليوم بس، تعبانة») and the her of now. Normalise: it wasn't wrong. Move (new): start with the **afternoon nap** in his own bed, not the night; the day is easier for both of you. Then the same two words at night, and return him without lying down again. CTA (Direct)."),
("c5","Cooking: he hangs on you","F1 HPSPC","Direct",
 "أول ما تدخلي المطبخ يتعلق فيكي، فصرتي تطبخي غدا بكرة وهو نايم؟","As soon as you enter the kitchen he clings to you, so now you cook tomorrow's lunch while he's asleep?",
 "Problem: he wants *you*, not the kitchen; cooking at night costs her sleep. Seconds-long moves, zero prep: (1) one low kitchen drawer that's his (plastic containers, wooden spoons); (2) a job beside you, away from the stove: washing cucumbers in a bowl of water; (3) say out loud what you're doing (\"دحين بنقطع البصل\"), so he's with you without being on you. Proof: method. CTA (Direct)."),
("c6","Only after he sleeps","F6 Checklist","Reflection",
 "ما تقدري تكنسي وهو صاحي، ولا تطبخي إلا بعد ما ينام؟","You can't vacuum while he's awake, and you don't cook until after he sleeps?",
 "Checklist build: the 'after he sleeps' list she's built (vacuum, cooking, a shower, a call). Turn: you don't need to win them all back, just one. Moves: pick the shortest; do it at the same time each day so he knows it's coming; give him a part in it (he presses the button, carries the dustpan). CTA (Reflection): which one weighs most? The assessment helps set the starting point."),
("c7","Hair dryer: only when he's far","F5 Walk-through","Direct",
 "ما تقدري تشغلي الاستشوار إلا لما يكون طفلك بعيد عنك؟","You can't turn on the hair dryer unless your child is far from you?",
 "Walking listicle, a twist in each: (1) not 'warn him first' (she's heard it) but let him see it *off* first and hold it; (2) start on the lowest setting, pointed away from him, from across the room; (3) he's the one who presses the button. Fast close + CTA (Direct)."),
("c8","Blender: make sure he's far","F2 Story","Observation",
 "كل ما تبغي تشغلي الخلاط، لازم تتأكدي إن طفلك بعيد؟","Every time you want to turn on the blender, you have to make sure your child is far away?",
 "Story: she wants a juice, checks where he is, waits, he walks in, she gives up, puts it back. Moves (seconds): a folded towel under the blender (it really is quieter); short pulses instead of one long run; he sees it before it starts. CTA (Observation): notice which sounds he moves away from and which he doesn't."),
("c9","Shower: knocking and crying","F3 Two voices","Reflection",
 "يدق باب الحمام ويبكي  أول ما تسكريه، فصرتي تتروشي بعد ما ينام أو قبل ما يصحى؟","He knocks on the bathroom door and cries the moment you close it, so now you shower after he sleeps or before he wakes?",
 "Two voices: him at the door, her inside rushing. Moves: (1) shower right after he's started something he likes, not when he's free; (2) keep talking or singing through the door so he hears you're there; (3) give him a job: he holds your towel outside and hands it to you when you come out. CTA (Reflection)."),
("c10","Hair wash: you come out wetter","F5 Walk-through","Observation",
 "تغسلي شعره وهو يصيح، وتطلعي من الحمام وأنتي اللي مبلولة أكثر منه؟","You wash his hair while he screams, and you come out of the bathroom wetter than him?",
 "Walk-through with twists: (1) a dry face towel he holds over his own eyes; (2) count out loud to the same number every time, then stop (\"لين عشرة\"), so he knows when it ends; (3) let him hold the shower head. Fast close + CTA (Observation)."),
("c11","Kids' salon: screaming and running","F1 HPSPC","Direct",
 "كل ما وديتيه صالون الاطفال، يبدأ الصراخ ويحاول يهرب؟","Every time you take him to the kids' salon, the screaming starts and he tries to run?",
 "Problem: the whole visit is a battle, and she leaves with half a haircut. Moves: (1) حاولي the quietest time (weekday morning); (2) the first time, just sit and watch another child, no haircut; (3) let him feel the clipper's buzz on your arm, then his hand, before his head; (4) something of his own to hold. Proof: method. CTA (Direct)."),
("c12","Phone calls: only behind a locked door","F4 Metaphor","Reflection",
 "ما تقدري تكملي مكالمة مع أمك إلا لما تدخلي الحمام وتقفلي الباب؟","You can't finish a call with your mum unless you go into the bathroom and lock the door?",
 "Metaphor from his side: on the phone you're in front of him, but your voice and eyes went somewhere else, like when someone talks to you while looking at their phone. Moves: (1) a small box of things that only comes out during calls; (2) let him say hi to grandma on speaker first; (3) keep a hand on him while you talk. CTA (Reflection)."),
]
s["concepts"]=[{"id":i,"title":t,"job":f"value + CTA ({cta})","angle":f"[{fmt}] {body}","hook_ar":h,"hook_gloss":g,"status":"proposed","format":None} for i,t,fmt,cta,h,g,body in C]
rows="\n".join(f"| {i} | {t} | {fmt} | {cta} |" for i,t,fmt,cta,h,g,body in C)
s["steps"][4]["report"]=f"""### 12 concepts, one per approved hook
Each card on the dashboard has the hook and its value: the «رؤوس أقلام» she can use tonight. Every post also gets an early soft CTA right under its first step, a final CTA, a caption whose first line carries the CTA, and a pinned comment that works as a "part two".

| # | Concept | Suggested format | Final CTA variation |
|---|---|---|---|
{rows}

**The format spread:** F1 ×3, F2 ×2, F3 ×2, F4 ×1, F5 ×2, F6 ×2. Every new format is tested at least once, and F1 is the control. You confirm the formats at step 6.

**The rules I held to:**
- The sequels use **new** steps. There's no chair step-back and no "warn him before the vacuum".
- Every tip takes seconds or uses what she already has.
- No cups or plates in a change post.
- Nothing promises a result for the child.
- Proof is the method only.

**Watch these four:**
- **c7 hair dryer and c8 blender are close cousins** (noise, keep him far). I suggest posting them at least four days apart.
- **c2's move has her leaving while he's still awake**, telling him she'll come back, then coming back. It's a known approach, but it's new to our feed. Is that realistic for your audience?
- **c11:** «حاولي» is used for the quiet salon time, because she doesn't control the salon's schedule.
- **c12 is the only metaphor post.** "On the phone, you're in front of him but somewhere else" is told from his side, with no clinical claim.

**Suggested posting order (one a day, topics alternating):** c1, c5, c9, c3, c8, c10, c2, c6, c11, c4, c7, c12."""
for p in s["plan"]["specialists"]:
    if p["key"]=="st": p["status"]="needs-you"
save()
