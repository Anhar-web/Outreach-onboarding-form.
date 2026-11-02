# Agency Brief — مدار البيت | الخطة الحية (post-assessment experience)

Client: Anhar. Brand: مدار البيت (Home Orbit). Product: الخطة الحية (The Living Plan).
Audience: Saudi mothers of autistic children, arriving mostly from TikTok, on mobile.

## 1. The live page (the "before")
- Full file (with embedded photos, 1.4MB): `agency-run/source/index_before.html`
- Same file with base64 photos replaced by `IMG` (read THIS one): `agency-run/source/index_before_noimages.html`
- It is ONE single-page app: welcome → 15 questions → results page → Living Plan invite card (`LIVING_PLAN`) → personalized landing (`landingHTML`, `LP_HEAD`, `LP_SUPPORT`).
- `?plan` in the URL opens the landing directly with a fixed, non-personalized headline (used in emails).
- Source copy docs: `agency-run/source/assessment_copy.txt` (assessment blueprint, scoring, result copy, Living Plan transition) and `agency-run/source/landing_instructions_old.txt` (old landing build rules + full old landing copy).

## 2. Scope (client decision)
Rebuild everything AFTER the score: the results page (result card), the Living Plan invite card, and the personalized landing.
DO NOT change: the welcome screen, the 15 questions and answers, the scoring model (Q1–12, A3/B2/C1/D0, three dimensions out of 12, total out of 36, profile bands 0–12 / 13–24 / 25–36), the data sent to the Apps Script endpoint (`sendResults`), the opt-in checkbox, or the embedded images.

## 3. The offer
- الخطة الحية: personalized guidance that evolves with the child, reviewed every two weeks.
- Includes: extended intake questionnaire (communication, routine, mood, sensitivities, environment, past experiences); a personal plan focused on ONE main area at a time; interactive review every 2 weeks; ongoing adjustments based on the child's response (incl. hard days, regressions, routine changes); tracking to see patterns over time; whole-life view (sleep, siblings, routine, environment). "انا والقروب معاك" — Anhar + the group are with her between reviews.
- Bonuses (only these two): خريطة نقطة البداية; مجتمع واتساب.
- Price: exactly ٧٤٩ ريال / الشهر. Monthly.
- Terms: **monthly, cancel anytime.** No refund promise. No outcome guarantee (never promise developmental/behavioral results).
- After she clicks: she goes to the external Google Form waitlist. Places are for a **limited first group of 10 mothers** (confirmed real cap by the client: «الدفعة الأولى تستقبل ١٠ أمهات فقط» is true and may be used once, honestly). Honest scarcity only: no countdowns, no invented deadlines.
- Not a replacement for therapy/speech/specialists; complementary.

## 4. Real case stories (owner-supplied; do not add details, names, photos)
1. الولد الغاضب: always angry, says unkind words, hard to calm. Asked about his whole day; sensitivity and pressure emerged as part of the picture. After two weeks the mother: "كان يصحى معصب كل يوم. هالأسبوع صحى معصب مرة وحدة."
2. التواصل: mother found a post, reached out; communication was the area needing support; communication plan; after two weeks new behaviors started appearing.
3. الأكل: short list of accepted foods; extra questions first to avoid missing other needs; gradual introduction while keeping safe foods.
No other testimonials, stats, credentials or client counts exist. Do not invent any.

## 5. Personalization (the focus list)
The landing headline is personalized from the mother's actual assessment answers, not the skill's default 5 focuses. Inputs available in the app:
- **Q14 situation** (sitKey): A وقت النوم والاستعداد له · B الخروج من البيت والزيارات العائلية · C التواصل والتعبير عن احتياجاته · D الأكل وتجربة الأطعمة · E الانتقال من نشاط لنشاط أو التوقف عن شيء يحبه · F التعامل مع الغضب والانفعال · G شيء ثاني (free text).
- **Lowest-scoring dimension**: 0 فهم الأنماط المتكررة · 1 تخصيص الطريقة لطفلك · 2 وضوح الخطة واستمراريتها.
- **Overall profile**: 0 البداية تحتاج وضوح · 1 عندك أساس، والخطوة الجاية تنظيمه · 2 عندك طريقة واضحة، وحان وقت تطويرها.
- Q13 (perceived need) and Q15 (desired change in her words) are also available.
Rule: headline = situation × lowest-dimension angle; subheadline shaped by profile. Never put all three into the headline. Never show variable names. Fallbacks required for missing values and for `?plan` (email entry). Also support `?focus=<A–F or sleep|outings|communication|food|transitions|emotions>` so external links (TikTok/email) can deep-link a personalized landing.

## 6. CTA + destination
- Label (locked): **احجزي مكانك في قائمة الانتظار**
- Destination (locked): `CONFIG.waitlistUrl = "https://forms.gle/kvukC88bbAB6Wqi96"` (opens in new tab). No on-page form, no payment flow, no fake success message, never claim her place is confirmed.
- On the results page, the invite card's button leads to the landing (currently "اكتشفي كيف تشتغل الخطة الحية").

## 7. Locked constraints
- Brand: مدار البيت / الخطة الحية. Assessment title: ليش نفس المواقف تتكرر مع طفلك؟
- Colors: Deep Sea Blue #005A70 · Teal #00A9A5 · Creamy Pearl #F6F3EB · Sunrise Gold #C9935A. Fonts in use: El Messiri (display) + Tajawal (body). Calm, refined, grounded. No childish illustrations, no sad imagery, no clinical look, no red warning colors.
- Price ٧٤٩ ريال/الشهر. Review cycle every two weeks. Only the two bonuses.
- Results must stay fully accessible whether or not she joins. Never make the result conditional on buying.
- Saudi Arabic voice: ايش (not وش), تساعدي/تحسي/تقدري (no extra ن), no "يمكن/ممكن" hedging about what the service includes, no blame, no labeling the child, no outcome promises, no fear/shame/artificial urgency.
- Core message: انتي مو محتاجة تجمعي نصائح أكثر. تحتاجي طريقة واضحة تناسب طفلك وحياتكم.

## 8. Gates
Client chose to stop at every gate (1: audit+research+market+positioning, 2: headline pick, 3: after-score).
