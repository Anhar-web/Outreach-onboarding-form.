# Test — after score: 82 / 100  (before was 61; raw audit 58)

Scope: the post-score experience in `index.html` (results page, Living Plan invite card, personalized landing, `?plan` / `?focus=` entries), on the same scorecard the Auditor used. Baseline is 61 / 100: the audit's raw 58, plus 3 on urgency (1 → 4) once the client confirmed the 10-place cap is real. Delta: **+21 vs 61** (+24 vs the raw 58).

Method: a fresh, independent read. I drove the page in headless Chromium at 390×844 with Playwright and ran three full assessments (profile 1 + food, profile 0 + «شيء ثاني» free text «وقت الاستحمام», profile 2 + anger) plus one sleep run. Each went results → invite card → landing → back → forward → refresh. I also opened `?focus=food`, `?focus=E`, `?focus=nonsense`, `?focus=` (empty), `?plan`, `?plan&focus=sleep`, and refreshed each one. All requests outside the page were blocked during the test, so **no test rows went to the Apps Script/Airtable endpoint** and the Google Form was never opened. Google Fonts were blocked too, so line counts were measured with fallback fonts. El Messiri may wrap slightly differently.

## Functional

| Check | Result |
|---|---|
| Results, all three profiles | Render correctly. Title, meaning, ring + three /12 bars, strength, opportunity, her Q14 chip, her Q15 words, and the first step. No duplicate title (the old `.lvl` repeat is gone). The page is 2,900 to 3,200px tall. The invite card starts at about 2,200 to 2,500px, roughly 2.6 to 3 screens down (before: about 2,900px). |
| Signal consistency | Fixed. The landing subheadline now uses `r.primary`, the same dimension shown in «فرصتك الجاية». I checked this in all runs, including Q13 overriding the lowest dimension. |
| Invite card → landing | Tapping «اكتشفي كيف تشتغل الخطة الحية» swaps to the landing and scrolls to the top. **The browser back button returns to the results** and forward returns to the landing. Good. |
| Personalized landing | The headline and the problem paragraph follow Q14 (food → food headline and food story; anger → anger headline and story). The old leak where the problem section was hard-coded to bedtime is fixed. The G free text is quoted at the top of the problem section («كتبتي إن الموقف اللي تبغيه يصير أسهل هو: «وقت الاستحمام»»), and Q15 is echoed above the final CTA («وكتبتي التغيير اللي تبغي تشوفيه: «…»»). |
| `?focus=food`, `?focus=E`, `?plan&focus=sleep` | Each shows the correct situation headline and problem, with the standard subheadline. Survives refresh. |
| `?focus=nonsense`, `?focus=`, `?plan` | Fall back to the default headline «نفس المواقف تتكرر كل يوم؟…» with the standard subheadline. Survive refresh. |
| CTA | Four visible instances (sticky nav, hero, price block, final section). One label, «احجزي مكانك في قائمة الانتظار», and one destination, `https://forms.gle/kvukC88bbAB6Wqi96`, opening in `_blank`. No on-page form and no fake success message. |
| Mobile 390px | No horizontal scroll (scrollWidth = 390). Hero at 390×844: the headline is 3 lines at 26px, the CTA sits at 374px, and «٧٤٩ ريال في الشهر، وتقدري تلغي في أي وقت.» ends at about 461px. Price, commitment and action are all above the fold. The landing is about 8,900px tall (about 10.5 screens; before it was 12,300px, about 14.5). |
| Hygiene | No English text and no em dash in the rendered page. No JS errors (the only console errors come from the blocked network). |
| **Refresh after the assessment** | **Loses the results.** Reloading on the results or landing view drops her back to the welcome screen with empty fields, because state is not persisted. The CTA opens in a new tab, so the normal path is safe. A mother who refreshes, or whose browser reloads the tab after the Google Form, loses her result with no way back. Suggest a `sessionStorage` snapshot of `state.answers`. |
| Polish | The invite-card button text renders **underlined** (anchor default `text-decoration`) on the gold button. It looks like a link rather than a button. |
| `[للتأكيد: …]` | Three placeholders show in «ايش يصير بعد ما تضغطي الزر؟» and one in the FAQ (cancel method), highlighted as intended. These are known client-owned gaps, but at the moment the next step after the form is literally blank on contact channel and timing, payment timing, and what happens if the batch fills. |
| Demo switcher | Appears only with `?demo`. Remove it before launch as the code comment says. |

## Persona reads (6)

**1. The exhausted mother (high urgency, sleep).** On arrival she sees «كل ليلة نفس المعركة؟ خلي وقت النوم أهدى، وروتينه أوضح، ولياليكم أخف.» and thinks: that's my night. What catches her is the problem paragraph («ساعة وأكثر وأنتي تحاولي… وآخر اليوم ما يبقى لك وقت ولا طاقة لنفسك»), which is her life, written without blame. Nothing confuses her, and the CTA plus the price are in the first screen. What builds trust: «الخطة ما تضيف لك جدول جديد» and «تحدي واحد بس». She might hesitate because she doesn't know *who* she will be reviewing with or how («أراجع معاكي» on a phone call? WhatsApp?). **Would she act?** Yes, likely. She can get the value and the step in under a screen, and the waitlist is low-commitment.

**2. The sceptical mother (has tried things, seen promises).** On arrival: "another plan". What catches her is the reframe «أغلب النصائح مكتوبة لكل الأطفال، مو لطفلك. تجيك لموقف واحد، وما يرجع أحد يسألك ايش صار بعدها.» That is a real, specific differentiator: follow-up, not tips. Case 1 makes the mechanism concrete («بدل ما يكون التركيز على التصرف وحده، كانت الأسئلة عن يومه كامل») and has a real verbatim result. Trust comes from honesty: «ما فيه وعد إن كل خطوة بتنجح من أول مرة»، «هذي تجارب أمهات، مو نتيجة مضمونة»، «ما تناسبك إذا…». She hesitates because cases 2 and 3 are thin («سلوكيات جديدة بدأت تظهر» means what?) and because there is no person, credential or background anywhere. The only "I" on the page («أراجع معاكي… تشوفي معاي») is never introduced. **Would she act?** Maybe. Monthly with cancel-anytime lowers the bar enough for a waitlist sign-up, but she'll ask "مين هي؟" first.

**3. The curious beginner (low awareness, profile 0).** The result screen is kind: «الرقم يوصف طريقتك الحالية، مو طفلك ولا أمومتك.» The first step is concrete (note three things in your phone a minute after the moment). One snag: with 3/12 she is told «أقوى شي في إجاباتك إنك تعدّلي طريقتك حسب طفلك», which is technically her highest dimension but feels hollow at 3/12. The invite card is short and clear: one imagined line, one line saying what the Living Plan is, and a button. She isn't talked down to. **Would she act?** She'll tap through to the landing. Whether she joins depends on the price, and «٧٤٩ ريال مو مبلغ بسيط» answers that respectfully. She may stay on the email list instead, which the page allows («نتيجتك تبقى لك، سواء كملتي أو لا»).

**4. The research-oriented mother.** «كيف تشتغل الخطة الحية؟» is clear: four steps, the tagline «يومه كامل، تحدي واحد، ومراجعة كل أسبوعين», and five deliverables. Missing for her: the review format (call, voice notes, written?), how long a review takes, who designs the plan and what their background is, and when خريطة نقطة البداية arrives. The FAQ on "how can it fit my child when nobody has seen him?" is answered well. **Would she act?** Probably not yet. She'll want the "who" and the "how exactly" before signing up.

**5. The ready-to-buy mother.** Price, monthly terms and cancel-anytime appear in the hero, in the price block, in an objection card and in the FAQ. The CTA is everywhere and identical. The friction is «ايش يصير بعد ما تضغطي الزر؟», which currently reads «يوصلك تواصل [للتأكيد: عن طريق ايش، وخلال كم يوم]» and «[للتأكيد: متى وكيف يكون الدفع]». That is honest, but it's a blank exactly where she wants certainty. «التسجيل في القائمة مو حجز مؤكد» is honest and good. **Would she act?** Yes, once the placeholders are filled. Today she will still click.

**6. The hostile critic.** I hunted line by line.
- *Blame:* none. «هل أنا السبب؟» is answered with the language file's own model line («مو كل موقف يصير مع طفلك يعني إنك سويتي شي غلط»).
- *Labels:* none. The children are described by actions («يرمي الأغراض»، «يمسك يدك ويوديك للمطبخ»).
- *Fake urgency:* none. The cap appears once, with a reason («عشان كل أم تاخذ متابعة كاملة»), with no countdown and no repetition.
- *Outcome promises:* explicitly denied in three places.
- *Clinical cause:* one borderline line. Case 1 says «بان إن الحساسية والضغط جزء مهم من الصورة». In Saudi everyday Arabic «الحساسية» reads first as *allergy*, and if read as sensory sensitivity it names a cause the page can't evidence. It is hedged («جزء من الصورة») but should be made observable.
- *Outcome-flavoured headlines:* «…وبدون معارك» (food) and «ولياليكم أخف» (sleep) are aspirations stated as imperatives, not guarantees. They are acceptable alongside the explicit no-guarantee FAQ.
- «تدوري علاج يشيل التوحد» is honest disqualifying copy, but "remove autism" will jar some mothers. «تدوري علاج للتوحد» is softer and says the same thing.
- *About Anhar instead of her?* No. Anhar is nowhere in the hero, sub or CTA. The only first person is step 4, which the client permitted. The flip side is that the delivering person is now invisible (see the fixes below).

## Scorecard (ten rows, after)

| # | Item | Before (adj.) | After | Evidence |
|---|---|---|---|---|
| 1 | Clear in five seconds | 8 | **12 / 15** | The hero now says what it is (eyebrow «الخطة الحية من مدار البيت»; sub «خطة شخصية مبنية على يوم طفلك كامل… وتتعدل كل أسبوعين»), that it's paid (749/month under the CTA), and what to do, all above the fold. Still unsaid: who is behind it and in what form (person? app? PDF?). |
| 2 | Headline promise | 8 | **12 / 15** | Each is one voice and one thought, her scene then the outcome, 3 lines at 390px: «كل عزيمة صارت همّ؟ روحي وأنتي مرتاحة، واستمتعي بوقتك مع أهلك.» is excellent. Weaker cells: F «يومك كله على أعصابك؟ اعرفي ايش يسبق انفعاله…» (odd collocation, and «اعرفي» is the knowledge outcome §13 calls lukewarm), C «افهمي إشاراته» (knowledge again), and default «وقفي الحلول المتفرقة» (abstract). |
| 3 | Message–market match | 7 | **10 / 12** | Natively Saudi throughout. The locked spellings hold (ايش، فين، شي، أنتي، معاكي), there's no MSA FAQ, no يمكن/ممكن, no tanween, no em dash, no typos found. About 6 lines still read translated or clumsy (listed below). |
| 4 | Reframe and mechanism | 8 | **11 / 14** | The reframe «المشكلة مو إنك ما حاولتي كفاية» + «تجيك لموقف واحد، وما يرجع أحد يسألك ايش صار بعدها» names the real gap (no follow-up). The mechanism is named («يومه كامل، تحدي واحد، ومراجعة كل أسبوعين») and case 1 demonstrates it. It is still partly copyable, because nothing shows *how* the whole-day view is built or by whom. |
| 5 | Proof | 5 | **6 / 10** | The same three owner cases, now placed before the price, with an honest disclaimer, and case 1 tied to the mechanism. Case 2 stays vague and case 3 has no outcome. No person, credentials or context, and the "I" in step 4 is never introduced. |
| 6 | Offer clarity | 5 | **6 / 8** | Inclusions, both bonuses, «٧٤٩ ريال / الشهر», «اشتراك شهري، وتقدري تلغي في أي وقت» and a "what happens after the button" section are all present. Held back by the four `[للتأكيد]` gaps (contact channel and timing, payment timing, batch-full, cancel method) and by no review format or deliverer. |
| 7 | Objections and risk | 7 | **9 / 10** | Six distinct objections (the duplicate money/price cards are merged), cancel-anytime stated four times, a "fits / doesn't fit" block, an honest no-guarantee, and "works alongside therapy". Missing: "who will I actually be talking to?" |
| 8 | One clear action | 6 | **7 / 8** | One label and one destination everywhere. On the results page there is one gold button with the correct label, and the opt-in now sits below the card instead of under the button. Minor: the button text is underlined, and the landing is one tap away rather than visible. |
| 9 | Honest urgency | 4 | **5 / 5** | The confirmed cap appears once, with a reason and no countdown, and «التسجيل في القائمة مو حجز مؤكد» is honest about what the click does. |
| 10 | Skim path and length | 3 | **4 / 5** | Clear subheads and a nav with three jump links. About 10.5 screens instead of 14.5. «كل أسبوعين» appears 2 times in the body copy instead of 14. The invite card is still about 3 screens down on the results page (acceptable, since the results are the value). |
| | **Total** | **61** | **82 / 100** | |

**Critical success factors:**
- Personalization: pass. Headline, problem, sub, G text and Q15 all carry through.
- Reciprocity: pass. The results stand alone.
- Persuasion without manipulation: pass.
- Arabic: mostly pass, with the residual lines listed below.
- Belief / love: the battle-led headlines carry feeling. The invite card's body is still calm-to-lukewarm.

## Arabic lines I would rewrite

| Line on page | Problem | Natural rewrite |
|---|---|---|
| «بدون ما تضيعي شهور وأنتي تجربي نصائح متفرقة لحالك.» / «بدون ما يفاجئك نفس الموقف كل مرة.» (sub tails) | A standalone «بدون ما…» sentence is the English "…without wasting months" tail, cut off by a full stop. The second one is also illogical: a *repeating* situation "surprising" her. | «…وتتعدل كل أسبوعين حسب استجابته، وما تضيعي شهور تجربي نصائح متفرقة لحالك.» / «…وتعرفي الموقف قبل لا يجي، بدل ما يفاجئك كل مرة.» |
| «يومك كله على أعصابك؟» (F headline) | A day can't be «على أعصابك». The phrase describes her, not the day. | «طول اليوم وأنتي على أعصابك؟» |
| «مراجعة تفاعلية منتظمة» | A literal "interactive review". | «مراجعة معاكي كل أسبوعين» |
| «…جزء من الخطة، مو فشل لها.» | A literal "not a failure of it". | «…جزء من الخطة، مو دليل إنها ما نفعت.» |
| «وتحطي انتباهك على أهم خطوة» (bonus) | A literal "put your attention". | «وتركزي على أهم خطوة» |
| «يوصلك تواصل […] يوضح لك…» | "A contact reaches you" is translated. | «يوصلك رد […] يوضح لك إذا فيه مكان لك في الدفعة الأولى.» |
| «بان إن الحساسية والضغط جزء مهم من الصورة» (case 1) | «الحساسية» reads as *allergy* and implies a cause. | «وبان إن فيه أشياء في يومه تضايقه وتضغط عليه، وهذا جزء مهم من الصورة.» |
| «وتساعدك تدخلي اللي يتعلمه هناك في يومه في البيت» (FAQ) | The double «في» stumbles. | «وتساعدك تنقلي اللي يتعلمه في الجلسة ليومه في البيت.» |
| «لكن الطريقة اللي تنفع ما تمشي دايم بنفس الوضوح.» (results, profile 1) | "The method doesn't walk with the same clarity" is a mixed metaphor. | «بس اللي ينفع مرة، مو دايم يكون واضح قدامك المرة الجاية.» |
| «يصحى متضايق، ويرمي الأغراض، ويصعب يهدأ.» (F problem) | «ويصعب يهدأ» has no subject or impersonal frame. | «…ويرمي الأغراض، وما يهدأ بسهولة.» |

Headlines and subs are client-approved verbatim (§14), so the first two rows are flagged for the client's decision, not silently changed.

## What still needs fixing (ranked)

1. **No one is behind the plan, and the review has no shape.** Step 4 says «أراجع معاكي… تشوفي معاي», but the "I" is never introduced and nothing says what the review is (call? voice notes? WhatsApp? how long?). This now costs more than it did before. It caps clarity (1), proof (5), offer (6) and the sceptical and research personas. Fix within §13: a short, factual "مين بيشتغل معاكي" block *after* the proof (the Mindvalley "teachers section" exception), plus one line in step 4 on the review format. Needs client input.
2. **Fill the `[للتأكيد]` gaps before launch.** Contact channel and timing, payment timing, what happens if the batch fills, and the cancel method. «ايش يصير بعد ما تضغطي الزر؟» is the right section, but today it is blank where the ready-to-buy mother needs certainty.
3. **The residual translated lines** in the table above, especially the two «بدون ما…» sub tails that appear on every landing hero and the «الحساسية» line in case 1.
4. **Headline cells F, C and default.** Two use the knowledge outcomes the client called lukewarm (اعرفي/افهمي), and F's opener is unnatural. Offer the client the F rewrite above and outcome versions such as «…وخليه يهدأ أسرع وتهدي معاه» (no guarantee implied).
5. **Results persistence.** A refresh after the assessment loses the result entirely. Store a session snapshot so the result "stays hers" as the page promises.
6. **Small polish.** Remove the underline on the invite button. Profile-0 strength copy should acknowledge a low score honestly (e.g. «أكثر جانب عندك فيه بداية…» rather than «أقوى شي»). «علاج يشيل التوحد» → «علاج للتوحد». Remove the `?demo` switcher before launch.
7. **Proof depth (owner-limited).** Cases 2 and 3 are thin by the brief's limits. If the owner can supply even one more concrete detail or verbatim line per case, add it. Do not invent any.
