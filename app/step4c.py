from upd import *
final=[
("Bedtime: night waking","سريرك صار نصه لطفلك؟ كل ليلة الساعة اثنين يجي ينام جنبك؟","Anhar"),
("Bedtime: sneaking out","جلستي ساعة  تنوميه، وأول ما قُمتي من جمبه فتح عيونه؟","Anhar"),
("Bedtime: her evening","تبدئي تنوميه الساعة ثمانيه، وما تطلعي من غرفته إلا الساعة عشره؟","Anhar"),
("Bedtime: \"just today\"","قلتي له اليوم بس تنام جنبي، ودحين ما يرضى ينام لحاله؟","Anhar"),
("Chores: cooking at night","أول ما تدخلي المطبخ يتعلق فيكي، فصرتي تطبخي غدا بكرة وهو نايم؟","approved"),
("Chores: only after he sleeps","ما تقدري تكنسي وهو صاحي، ولا تطبخي إلا بعد ما ينام؟","Anhar"),
("Noise: hair dryer","ما تقدري تشغلي الاستشوار إلا لما يكون طفلك بعيد عنك؟","Anhar"),
("Noise: blender","كل ما تبغي تشغلي الخلاط، لازم تتأكدي إن طفلك بعيد؟","Anhar"),
("New: shower","يدق ويبكي على باب الحمام أول ما تسكريه، فصرتي تتروشي بعد ما ينام أو قبل ما يصحى؟","draft from Anhar's direction"),
("New: hair wash","تغسلي شعره وهو يصيح، وتطلعي من الحمام وأنتي اللي مبلولة أكثر منه؟","approved"),
("New: kids' salon","كل ما وديتيه صالون الاطفال، يبدأ الصراخ ويحاول يهرب؟","Anhar"),
("New: phone calls","ما تقدري تكملي مكالمة مع أمك إلا لما تدخلي الحمام وتقفلي الباب؟","Anhar"),
]
rows="\n".join(f"| {i+1} | {t} | {h} | {w} |" for i,(t,h,w) in enumerate(final))
s["steps"][3]["report"]=f"""### Final 12 hooks after Anhar's edits (Nov 9)
| # | Topic | Hook | Source |
|---|---|---|---|
{rows}

**Hook 9 (shower) is my draft from your direction.** Please confirm it or reword it.

### What I learned from your edits
I've saved these as rules for every future hook. They'll go into Airtable → Feedback & Lessons at handoff.
1. **One question, no second half.** You dropped every second half.
2. **«ما تقدري … إلا …» is your shape** for the workaround (3 of 12), alongside «فصرتي…».
3. **Past tense for one real time it happened** (جلستي، قمتي، قلتي له، وديتيه).
4. **Physics and real-habit check:** you can't hear footsteps over a blender, and parents don't blow-dry a child's hair.
5. **There must be a real problem at stake.** If it can wait (the haircut), it's a statement.
6. **End on the problem she has now** (ما يرضى ينام لحاله), not on clever irony.
7. **Complete the move** (go in *and lock the door*).
8. **Your spellings, kept as written:** تنوميه، اثنين، ثمانيه، عشره، الاستشوار، صالون الاطفال.

---
"""+s["steps"][3]["report"]
save()
