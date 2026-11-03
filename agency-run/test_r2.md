# Test — after score: 87 / 100  (before was 61; round 1 after-score was 82)

Round 2 re-score of `index.html` after the Gate 3 decisions (brief §15–§17) and the client's own copy edits. Same ten items, same standard as round 1 and the audit. Delta: **+5 vs round 1 (82)**, **+26 vs the adjusted baseline (61)**, +29 vs the raw audit (58).

Method: a fresh read. I drove the page in headless Chromium at 390×844 with Playwright, with every request outside the page blocked. Nothing went to the Apps Script endpoint, the waitlist endpoint is empty anyway, and Google Fonts fell back. I ran four full assessments: profile 0 with «شيء ثاني» («وقت الاستحمام»), profile 1 with food, profile 2 with anger, and profile 1 with communication. Each went results → invite card → landing → back, with a refresh on results and on the landing. On the food run I went on through CTA → form → validation → submit → thank-you → refresh → «رجوع لنتيجتي». I also opened `?focus=food|E|nonsense|communication`, `?plan` (including the full form → thank-you → back path), `?plan&focus=sleep` and `?demo`, set `CONFIG.waitlistCount` to 9, 10 and 30, and checked the nav at 1100px. The copy was read in full from a text-only copy of the page against `source/arabic_language_file.txt` and `arabic_language_addendum_lessons.md`.

## Functional

| Check | Result |
|---|---|
| Results, all profiles | Render correctly. Low scores now get the honest lead: a 5/12 top dimension reads «أكثر جانب عندك فيه بداية هو…» instead of «أقوى شي…». The invite card starts at 2,360 to 2,630px, and the results page is 3,060 to 3,330px. |
| **Refresh keeps the result** | **Fixed.** A `sessionStorage` snapshot restores the results, the landing, and the thank-you screen after a reload, and it never re-sends the results (`sent:true`). Back and forward between results and landing still work. |
| Invite card → landing | «اعرفي أكثر عن الخطة الحية» (client's label) has no underline anymore. The page smooth-scrolls to the top and the hero is fully visible about 0.8s after the tap. |
| Personalization | Headline and problem follow Q14, and the sub follows `r.primary`. G free text is quoted at the top of the problem section, and Q15 is echoed above the final CTA. `?focus=food`, `E`, `communication` and `?plan&focus=sleep` are correct. `nonsense` and `?plan` fall back to the default. |
| CTA → on-page form | Four CTAs share one label and all open the same on-page form (`pushState`, so back closes it). Name and email are **prefilled from the assessment**. That means one tap to submit, which is excellent. On `?plan` the fields are empty, as expected. |
| Validation | An empty name shows «اكتبي اسمك.» and a bad email shows «تأكدي من الإيميل.», inline, with `aria-invalid` set and focus moved to the first bad field. |
| Submit → thank-you | Confetti, «سارة، أنتي دحين في قائمة الانتظار», the WhatsApp reason, and the WhatsApp button showing the `[للتأكيد: رابط القروب]` placeholder (owner gap). The thank-you survives a refresh. «رجوع لنتيجتي» returns to the results. |
| **Back label on `?plan` / `?focus`** | **Bug.** Mothers arriving from email or TikTok have no result, but the thank-you button still says «رجوع لنتيجتي», and it takes them to the landing. It should say «رجوع للصفحة» when `!state.done`. |
| Waitlist endpoint | `CONFIG.waitlistEndpoint` is empty, so **no sign-up is stored** while the thank-you says she is on the list. This is a known owner gap, not a copy flaw, but it **blocks launch**: every sign-up before it is connected is lost. |
| Capacity bar | Shows on the landing, the form and the thank-you, but not on the results (good for reciprocity). With the count at 9 or null it reads «الدفعة الأولى تستقبل ١٠ أمهات فقط». At 30 it reads «١٠ أماكن في الدفعة الأولى، و٣٠ أم في قائمة الانتظار», which is correct and follows the client rule. **At exactly 10** it reads «و١٠ أم» (grammar: should be «١٠ أمهات»), because the counted noun is singular for 11 and up but plural for 3 to 10. |
| Mobile 390px | No horizontal scroll. The hero CTA bottom sits at about 457px, with the cap bar above the nav. The landing is about 8,650px (about 10.3 screens) and 985 words, and «كل أسبوعين» appears 4 times. No em dash, no Latin text, no JS errors. |
| Desktop 1100px | The cap bar (34px) and the nav stick together. The nav has the brand, three centred jump links and the CTA on one row. Clean. |
| `?demo` | The owner panel still mounts. Remove it before launch, as the code comment says. |

## Persona reads (6)

**1. The exhausted mother (sleep, from TikTok `?focus=sleep`).** The first thing she sees is the thin bar «الدفعة الأولى تستقبل ١٠ أمهات فقط», then «كل ليلة نفس المعركة؟ خلي وقت النوم أهدى، وروتينه أوضح، ولياليكم أخف.» She thinks: that's my night. The sub tells her what it is in one breath, and the button is in the first screen. The price is no longer in the hero (the client removed it), so she taps without knowing the cost. That's fine for a free waitlist, and the price block is honest further down. The form is two fields and the thank-you is warm. **Would she act?** Yes. It's the fastest path on the page.

**2. The sceptical mother.** The reframe («أغلب النصائح مكتوبة بشكل عام، مو لكل طفل. تجيك لموقف واحد، وما يرجع أحد يسألك ايش صار بعدها.») and the new five-step process win her more than round 1 did. The process is concrete: a starting file, a first set of questions, her child's profile, a second, more detailed set, a plan by email, then «بعد أسبوعين، أرجع لك… أسألك ايش صار، وايش نفع، وايش ما نفع». That is something she can picture, and it is not a PDF. Case 1 now reads cleanly («فيه أشياء في يومه تضايقه وتضغط عليه»). She still hesitates on two things: who the «أرجع لك» is (never introduced; client decision, see below), and case 2's «سلوكيات جديدة بدأت تظهر» (vague; owner-limited). **Would she act?** Likely yes for the waitlist, since it's free and «مو حجز مؤكد». At the paid step she will want the "who".

**3. The curious beginner (profile 0).** The result is kind and honest now. The low-score lead says «أكثر جانب عندك فيه بداية…» instead of praising a 3/12. The edge case is the **all-tie**: if all three of her scores are equal, she gets «عندك أساس في أكثر من جانب» even at 0/0/0 or 3/3/3. That line is the old dishonesty back on a different path. The invite card is short and the landing doesn't talk down to her. **Would she act?** She'll tap through. Whether she joins depends on the price, which the price block and the «٧٤٩ ريال مو مبلغ بسيط» card handle with respect.

**4. The research-oriented mother.** This is the biggest improvement of the round. «كيف تشتغل الخطة الحية؟» is now a real process, not a slogan, and «ايش يصير بعد ما تضغطي الزر؟» answers what round 1 left blank: weekly updates, the opening date and time announced in advance, first come first served, the starting file after joining, and staying on the list if the batch fills. Still missing for her: whether the two-week check-in is written or a call (step 4 only says «أسألك»), and who designs the plan. **Would she act?** Yes, for the waitlist. That's a change from round 1.

**5. The ready-to-buy mother.** Price, «اشتراك شهري، وتقدري تلغي في أي وقت.» and the cap are all in one block, followed by the CTA. The prefilled form makes joining one tap. **Does the first-come explanation make the next step clear and honest?** Yes, mostly. The five steps are factual, nothing says her place is reserved, and «التسجيل في القائمة مو حجز مؤكد» repeats it on the form. Three soft spots:
- (a) The thank-you screen doesn't restate the mechanism. After submitting she reads only "join WhatsApp". One line («قبل الفتح، ينزل موعد الفتح في القروب وعلى الإيميل، والأماكن بالأسبقية.») would close the loop exactly when she cares.
- (b) «وأي خبر عن الدفعة الأولى يوصلك هناك أول» suggests WhatsApp members hear first. In a first-come race, that is either a real advantage (then it's fine, and it is the strongest honest reason to join) or it isn't true (brief §17 says the date is announced "in the group and by email"), in which case it is a soft manufactured nudge. The owner should confirm.
- (c) «الدفعة الجاية» has no time frame. §17 allows an honest «بعد كم أسبوع».

**Would she act?** Yes.

**6. The hostile critic.** I hunted line by line.
- *Founder:* not in the hero, the sub, any persuasive section, or the CTA. The only first person is in the how-it-works steps («أجهز»، «أرجع لك»), which §13 permits.
- *Sessions, specialists, autism:* none in the rendered page or the meta (checked with grep: no توحد / جلس / أخصائي / علاج). The single health line stays: «خذي رأي الطبيب».
- *Outcome promises:* «ما في وعد…ولا وعد بنتيجة معيّنة», «هل فيه نتيجة مضمونة؟ لا.», and «هذي تجارب أمهات، مو نتيجة مضمونة لكل طفل». The food headline «…وبدون معارك» is still the boldest line. It's acceptable as an aspiration next to three explicit no-guarantee statements.
- *Blame:* none. «هل أنا السبب؟» is answered with the language file's own model line.
- *Fake urgency:* none manufactured. The cap is real, given a reason once («لأن البداية فيها أسئلة وتواصل وبناء خطة لكل طفل»), and repeated in the bar and the after-steps. That makes three mentions, but no countdown, and the demand number only shows when it is real and ≥ the cap. Watch «يوصلك هناك أول» (above) and «باقي خطوة وحدة عشان ما يفوتك شي». The second one is honest, mild, and fine.
- *Privacy, a new risk:* the thank-you asks her to join a WhatsApp **group**. In a normal WhatsApp group every member's phone number is visible to the others. For a Saudi mother with a child who may not be diagnosed, that is a real reason not to tap. A line like «القروب للإعلانات بس، وما أحد يشوف رقمك» (only if true: use a Community announcement group or a channel) removes it. Separately, the waitlist «قروب» and the bonus «مجتمع واتساب… تسألي، وتشاركي» are two different groups with the same name. She may expect to chat in the first one.

## Scorecard (ten rows, after)

| # | Item | Before (adj.) | R1 | **R2** | Evidence |
|---|---|---|---|---|---|
| 1 | Clear in five seconds | 8 | 12 | **12 / 15** | The cap bar, the eyebrow «الخطة الحية من مدار البيت», the headline, «خطة شخصية مبنية على يوم طفلك كامل…» and the CTA are all above the fold. The price micro-line left the hero (client decision), and who delivers it is still unsaid. Gains and losses even out. |
| 2 | Headline promise | 8 | 12 | **13 / 15** | F is fixed to the client's line («طول اليوم وأنتي على أعصابك؟…»), which is natural and outcome-led. C still uses «افهمي إشاراته» (a knowledge outcome) and «وخليه يوصل لك اللي يحتاجه», a phrase the addendum §5 itself lists as "translated and off". The default «وقفي الحلول المتفرقة» stays abstract (kept by the client). |
| 3 | Message–market match | 7 | 10 | **11 / 12** | 8 of the 10 lines I flagged in round 1 are fixed exactly as the addendum records. دحين / ما في / شي / أنتي / معاكي / ايش / فين all hold. No em dash, no tanween in the new copy, no يمكن / ممكن. A handful of lines remain (table below), and the most visible is the C headline. |
| 4 | Reframe and mechanism | 8 | 11 | **12 / 14** | The real process replaces the generic loop: two rounds of questions build a child profile, then a two-week plan by email, then a check-in with four exact questions, then the next plan, «لين تصير جزء من يومكم». It is specific and hard to copy in spirit. Still faceless, and the check-in format is unstated. |
| 5 | Proof | 5 | 6 | **6 / 10** | The same three owner cases. Case 1's «الحساسية» line is fixed. Case 2 is vague and case 3 has no outcome (owner-limited). There is no person behind the plan (client decision). |
| 6 | Offer clarity | 5 | 6 | **7 / 8** | All `[للتأكيد]` gaps in the copy are gone. «ايش يصير بعد ما تضغطي الزر؟» now explains the whole first-come flow, and price plus monthly cancel-anytime are in one block. Missing: the check-in format, and the timing of «الدفعة الجاية». |
| 7 | Objections and risk | 7 | 9 | **9 / 10** | Six objection cards, four FAQs, a fit / no-fit block, and an honest no-guarantee. The therapy answer was removed by client rule (§16) and is not penalized. Unanswered: "who will I be dealing with?" and, new, "will others see my number in the WhatsApp group?" |
| 8 | One clear action | 6 | 7 | **8 / 8** | One label, one on-page form, prefilled from the assessment, a two-field submit, and back closes it. The underline is fixed. The WhatsApp join comes after the conversion as a deliberate second step, so it doesn't compete. |
| 9 | Honest urgency | 4 | 5 | **5 / 5** | A real cap with a real reason. Demand appears only when ≥ the cap, with no countdown, and «مو حجز مؤكد» is stated twice. Keep it at 5 only if «يوصلك هناك أول» is true (see fix 3). |
| 10 | Skim path and length | 3 | 4 | **4 / 5** | Clear subheads, a sticky nav with three jump links, and about 10.3 screens. The new after-steps add length but earn it. The invite card is still about 2.8 screens down the results (acceptable, since the results are the value). |
| | **Total** | **61** | **82** | **87 / 100** | |

**Critical success factors:**
- Personalization: pass.
- Reciprocity: pass (no cap bar on the results; «نتيجتك تبقى لك، سواء كملتي أو لا», and now it really does survive a refresh).
- Persuasion without manipulation: pass, pending the «أول» check.
- Arabic: pass with residual lines.
- Belief: the battle-led heroes carry feeling, and the thank-you is warm.
- Mother-centred: pass (founder absent from everything persuasive).

## Round 1 issue → status

| Round 1 issue | Status |
|---|---|
| 1. No one behind the plan; review has no shape | **Client decided** (brief §13: page is about her, founder only in a dedicated section, which was not commissioned). Review shape **partly fixed**: step 4 now lists what she's asked and the plan arrives by email. Residual risk: the sceptic and the research mother still ask "مين؟", and the check-in format (written or call) is unstated. |
| 2. `[للتأكيد]` gaps (contact, payment timing, batch full, cancel method) | **Fixed.** The after-steps were rewritten to the real first-come flow. The cancel-method FAQ was removed by the client (waitlist page, no checkout details, §15 / addendum rule 6). Only the WhatsApp link placeholder remains (owner). |
| 3a. «بدون ما…» sub tails | **Fixed** in the standard sub and SUBS 1. **Still open** in SUBS 0: «…حسب استجابته. وتعرفي الموقف قبل لا يجي، بدل ما يفاجئك كل مرة.» |
| 3b. «مراجعة تفاعلية منتظمة» | **Fixed** → «مراجعة معاكي كل أسبوعين». |
| 3c. «مو فشل لها» | **Fixed** → «مو دليل إنها ما نفعت». |
| 3d. «وتحطي انتباهك» | **Fixed** → «وتركزي على أهم خطوة». |
| 3e. «يوصلك تواصل» | **Fixed** (section rewritten). |
| 3f. «الحساسية» (case 1) | **Fixed.** |
| 3g. FAQ double «في» | **Client decided**: the sessions FAQ was removed (§16). |
| 3h. Profile 1 «ما تمشي دايم بنفس الوضوح» | **Fixed.** |
| 3i. «ويصعب يهدأ» | **Fixed** → «وما يهدأ بسهولة». |
| 4. Headline cells F, C, default | F **fixed** (client's line). C and default **client decided** to keep (§15), but C's «وخليه يوصل لك اللي» is now listed as rejected in the client's own addendum §5, so it is **still open** and needs a client call. |
| 5. Results lost on refresh | **Fixed** (session snapshot; also covers the landing and the thank-you). |
| 6a. Invite button underline | **Fixed.** |
| 6b. Honest wording for low strength | **Fixed** for a single strongest dimension. **Still open** for the all-tie case («عندك أساس في أكثر من جانب» at equal low scores). |
| 6c. «علاج يشيل التوحد» | **Client decided**: the line was removed entirely (§16). |
| 6d. `?demo` switcher | **Still open** (pre-launch owner task). |
| 7. Proof depth (cases 2 and 3) | **Still open** (owner-limited; nothing invented). |

## Arabic lines I would rewrite

| Line on page | Problem | Natural rewrite |
|---|---|---|
| «تخمّني طول اليوم ايش يبغى؟ افهمي إشاراته، وخليه يوصل لك اللي يحتاجه بطريقته.» (C headline) | «خليه يوصل لك اللي» is the exact phrase the addendum §5 rejects as translated. «افهمي» is a knowledge outcome (§13). | «تخمّني طول اليوم ايش يبغى؟ خلي التواصل بينكم أسهل، وطلباته أوضح، ويومكم أهدى.» (client to approve) |
| «تخيلي يكون عندك طريقة واضحة تساعدي فيها طفلك يوصل لك اللي يبغاه…» (C invite) | Same «يوصل لك اللي» construction. | «تخيلي يكون عندك طريقة واضحة يطلب فيها طفلك اللي يبغاه، بدل ما تخمّني طول اليوم.» |
| «…حسب استجابته. وتعرفي الموقف قبل لا يجي، بدل ما يفاجئك كل مرة.» (SUBS 0) | A sentence opening with «و» after a full stop (the same fault as the «بدون ما» tail). "Know the situation" is odd, and it is a knowledge outcome. | «…وتتعدل كل أسبوعين حسب استجابته، وتكوني مستعدة للموقف قبل لا يجي، بدل ما يفاجئك كل مرة.» |
| «ويوصلك فيه كل أسبوع كل جديد عن الخطة الحية والدفعة الأولى. وإذا ما انضميتي، يوصلك على الإيميل.» (after-step 2) | A double «كل», and the second «يوصلك» has no subject. | «وكل أسبوع ينزل فيه جديد الخطة الحية والدفعة الأولى. وإذا ما انضميتي، توصلك نفس الأخبار على الإيميل.» |
| «أول ١٠ أمهات يشتركوا يدخلوا الدفعة الأولى، وبعدها يوصلهم ملف البداية.» (after-step 4) | Shifts to third person plural in a list addressed to her. | «الأماكن بالأسبقية: إذا كنتي من أول ١٠ أمهات يشتركوا، تدخلي الدفعة الأولى ويوصلك ملف البداية.» |
| «أكثر جانب عندك فيه بداية هو…» (low-strength lead) | "The aspect in which you most have a beginning" stumbles when read aloud. | «أوضح بداية عندك هي انتباهك للمواقف اللي تتكرر مع طفلك.» (and so on for the other two) |
| «عندك أساس في أكثر من جانب.» (all-tie, any score) | Untrue at 0/0/0 or 3/3/3. | When the tied score is 6 or less: «نتيجتك متقاربة في الجوانب الثلاثة، وهذا يعني إنك تقدري تبدأي من أي جانب. والخطوة الجاية إنك تختاري واحد تركزي عليه.» |
| «و١٠ أم في قائمة الانتظار» (cap bar at count = 10) | The counted noun after 3 to 10 must be plural. | Use «أمهات» when n ≤ 10, and «أم» from 11 up. |
| «هل فيه نتيجة مضمونة؟» (FAQ) | The project preference is «في» (addendum §5). | «هل في نتيجة مضمونة؟» |
| «رجوع لنتيجتي» (thank-you, `?plan` / `?focus` visitors) | They have no result. | «رجوع للصفحة» when there is no result. |

## What still needs fixing (ranked)

1. **Connect the waitlist endpoint and the WhatsApp link before any traffic** (owner). Today the thank-you tells her she's on the list while nothing is saved. That is the only thing on the page that could turn honest copy into a broken promise.
2. **C headline and C invite.** This is the most visible Arabic flaw left, it is on every communication landing hero, and it contradicts the client's own addendum. Offer the rewrite above for the client's approval.
3. **Close the first-come loop on the thank-you screen, and verify «أول».** Add one line restating "the date is announced in the group and by email, places go in order". Confirm whether WhatsApp members really hear first. If not, change it to «…يوصلك هناك على طول». Add «القروب للإعلانات بس» plus number privacy (only if true), and name it differently from the bonus «مجتمع واتساب».
4. **Residual Arabic** (SUBS 0, after-steps 2 and 4, the low-strength lead, «هل في»).
5. **Small logic and copy bugs:** «رجوع لنتيجتي» on `?plan` / `?focus`; «١٠ أم» at count = 10; the all-tie strength line at low scores.
6. **The "who" and the check-in format** (client decision pending). The client chose a mother-centred page, correctly. A short factual "مين بيشتغل معاكي" block placed after the proof (the Mindvalley teachers-section exception the client herself cited), plus «المراجعة تكون…» in step 4, would lift proof, clarity and the sceptic and research personas. This is now the largest remaining point cap (items 1, 4, 5 and 7).
7. **Pre-launch:** remove the `?demo` switcher. If the owner can add one more concrete verbatim detail to case 2 or 3, do it. Never invent one.
