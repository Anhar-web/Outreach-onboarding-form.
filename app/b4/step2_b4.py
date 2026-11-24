"""B4 step 2: scorecard + plan. Updates state.json and re-embeds it into b4/dashboard_b4.html."""
import json, os, datetime
here=os.path.dirname(os.path.abspath(__file__)); app=os.path.dirname(here)
s=json.load(open(os.path.join(app,"state.json"),encoding="utf-8"))
items=[("Scroll-stop",18),("Recognition: people reacting + her cost",14),("Emotion, not apathy",13),("Her legacy voice",14),
       ("Value by slide 3",10),("Trust & safety (gate)",10),("Arabic naturalness",6),("The twist",5),("Next step (CTA)",5),("Shareable",5)]
assert sum(w for _,w in items)==100
s["scorecard"]={"total":100,"items":[{"name":n,"weight":w,"score":None} for n,w in items]}
report=r"""
## Step 1 confirmed (Nov 24)
These are taken as agreed: 12 posts with the 4 / 5 / 3 split and the slot plan; the two hook and two cream rule suspensions (labelled tests only); the «الافتراض» label always naming the room's assumption, never hers; and odd posts' CTAs never mentioning the assessment.

**Still open, asked again before they matter:**
- the start evening (needed at handoff)
- the three `src=bio` visits and the abandoned-start test (needed before the first evening)
- your Arabic voice files (needed before step 7)

## The Batch 4 scorecard (reweighted, total 100)
| # | Item | B3 | **B4** | Why it moved |
|---|---|---|---|---|
| 1 | Scroll-stop | 18 | **18** | Slide 1 still decides everything. Most viewers never pass slide 2–3. |
| 2 | Recognition: **people reacting + her cost** | 15 | **14** | Now judged on the two reach drivers: lines from the people in the scene (or a universal or strange-but-common moment), and the cost landing on her in the first lines. A hook ending on his behaviour scores low. |
| 3 | Emotion, not apathy | 15 | **13** | Still the core; partly carried by #2 and #4 now. |
| 4 | **Her legacy voice** (was "Her own words") | 12 | **14** | The single biggest gap between legacy (median 3.7K) and us (~500). Scored on short beats, «…» pauses, the stamp → «وأنتي؟» → «وفجأة» rhythm, 2–4 real quoted lines, ONE comic image on her, one love line. |
| 5 | **Value by slide 3** (was "One job") | 10 | **10** | There's no job split any more. Is the named tool on slide 3, shown working, and could she use it tonight? |
| 6 | Trust & safety | 10 | **10** | **Gate.** Never blames her, no diagnosis, no cause, no promise, no therapy, nothing acted out about the child. |
| 7 | Arabic naturalness | 8 | **6** | Still checked line by line by the Arabic Voice Editor; partly overlaps #4. |
| 8 | **The twist** (was "The turn") | 6 | **5** | An unexpected confession that makes her laugh at herself (the coffee-shop model), not a reframe. |
| 9 | Next step (CTA) | 4 | **5** | Custom CTA: the outcome she wants, said with certainty, matched to the post's QR route, and it passes the "would she click without knowing what it is?" test. |
| 10 | Shareable | 2 | **5** | Shares were the breakout marker in legacy (1,598 and 1,106 on the two biggest posts). Would she send it to her sister? |

**How it's used:** the Hook Specialist uses #1–#4 to filter hooks; the Test Panel scores every post on all ten at step 8. **The score is a flag, not proof.** A post that reads aloud like you beats a higher number.

## The agency plan
| Step | Who | What they deliver for B4 |
|---|---|---|
| 3 · Research | **Audience Researcher** and **Market Analyst**, in parallel | **Researcher:** what Saudi and Gulf mothers actually say in the 13 candidate moments, especially **the lines relatives, guests and strangers say to them**, plus her inner voice, as a quote bank (Arabic + gloss, no invented quotes). It ranks the candidates by how universal they are and how much people react in them. **Analyst:** what's wallpaper in this niche now (calm-down tips, "be patient", emotion charts) and the open lane for the «الافتراض» series and for trick-like tools. |
| 4 · Hooks | Hook Specialist | Angles and 4–6 hooks per angle in **your legacy voice**, covering the 12 slots, including the 2 problem + solution hooks and the 4 «الافتراض» openings. Each hook is scored against #1–#4 and tagged with its slot and QR route. |
| 5 · Concepts | Strategist | One concept per slot, plus spares: the named tool, the deepen beat, the proof (method), the twist and the comment question. You pick. |
| 6 · Format | You | Static or video per concept. The default proposal is static, since the slot plan is built for carousels. |
| 7 · Copy | Copywriter | Every post in Arabic, written after reading all 25 Legacy Posts and your voice files. Delivered as a .txt file you can edit (Part M4). |
| 8 · Edit + test | Arabic Voice Editor, then the Test Panel | Native-voice edit; three sceptical mothers react to each post; scored with this card. |
| 9 · Handoff | Strategist | Final posts, captions, a QR code per post (`make_qr.py`), the posting order, and the Airtable rows. |
| After each evening | Analyst | Logs day 1 in Post Performance and reads Visits and Submissions by `post` tag. |

Visual production (the fresh look, the cream test, the «الافتراض» series look) runs afterwards in the Creative Production skill.
"""
st=s["steps"]
st[0]["status"]="done"; st[1]["status"]="needs-you"; st[1]["report"]=report.strip()
st[1]["action"]["label"]="Approve the weights and the plan, or tell me what to change."
s["currentStep"]=2
s["updatedAt"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
json.dump(s,open(os.path.join(app,"state.json"),"w"),ensure_ascii=False,indent=1)
p=os.path.join(here,"dashboard_b4.html"); h=open(p,encoding="utf-8").read()
a=h.index("window.__STATE__ = "); b=h.index(";\n",a)+2
h=h[:a]+"window.__STATE__ = "+json.dumps(s,ensure_ascii=False).replace("</","<\\/")+";\n"+h[b:]
open(p,"w",encoding="utf-8").write(h); print("ok")
