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

## 9. Gate 1 decision (client)
Positioning approved as written ("Whole day. One area. Every two weeks."). Anhar is named as the person behind the plan; Arabic spelling used: أنهار (client approved the positioning that uses it; reconfirm before launch). Page may say plainly who it's not for. Plan works alongside therapy.

## 10. LATER (client note, do not build in this run unless asked)
Waitlist flow change requested for a later step: clicking «احجزي مكانك في قائمة الانتظار» should open an on-page form (name + email). After submit, a thank-you page encourages her to join the WhatsApp waitlist group, explaining why (emails can get lost in spam/promotions; WhatsApp gets seen) and how to join. Needs: WhatsApp group invite link and where name/email are stored (likely the existing Apps Script → Airtable endpoint). Copy for these two screens can be drafted by the Copywriter as an appendix so it's ready.

## 11. Gate 2 feedback (client, binding) — headlines REJECTED, redo
Client verdict on all 15 headlines: they sound clumsy and translated, "not an expert's work"; scores are high in theory but not real when read. Specific problems:
- "نفس الغضب يتكرر كل يوم؟" reads like a literal translation ("The same anger repeats every day").
- **Half-written headlines**: first half (her scene) and second half (our method) sound like two different writers stitched together. E.g. «تقولي خلاص نسكّر الآيباد وتبدأ المشكلة؟ نشوف ايش يسبقها في يومه.» doesn't make sense as one thought. Applies to ALL situations. A headline must be ONE complete, coherent thought in one voice.
- **Vague**: she has to work to figure out what we mean. Breaks "clear in 5 seconds".
- **Lukewarm / apathetic**: violates Extreme Love ("never market with apathy; love or hate, never apathy"). Use words that make her FEEL. Her example for bedtime: "every day the same battle" (كل ليلة نفس المعركة).
- Reference style: Mindvalley Mastery headlines (bold, identity/outcome-led, instantly clear, one confident voice, sub explains who/what/how). Client examples:
  1. "Be the top 0.1% with Mindvalley Mastery" / sub: "Stay ahead of the curve ... elite Mastery programs designed to position you as a world leading expert..."
  2. "Be in the Top 0.1% of Founders, CEOs & Executives Using AI" / sub: "Scale your income, reduce your workload, and future-proof your business — with hands-on, real-world AI mastery"
  3. "Get More Followers. Build Real Authority. Join the Top 0.1% Who Monetize Their Message." / sub: "This is the proven system used by ... to grow fast, stand out online, and get paid for what they know — without wasting years trying to figure it out alone."
  4. "MINDVALLEY MANIFESTING MASTERY"  5. "Master your own body, age gracefully and live a life of radiant health"  6. "MINDVALLEY SPEAKING & INFLUENCE MASTERY"
- **First person, singular**: never refer to Anhar in third person («مع أنهار» is banned), and never sound like a company/team. Use «معاي», «أشتغل معاكي», «أراجع معاكي». Avoid «نحن/نشوف/نبدأ/نبني» where it implies a team; use singular «أشوف/أبدأ معاكي» or address her directly. (The WhatsApp group of mothers can still be «القروب».)

## 12. Arabic language file (client, binding; overrides voice.md where they differ)
`source/arabic_language_file.txt` is the Home Orbit Arabic Language & Voice System. Every Arabic-writing specialist must read it in full. Key overrides of voice.md: use **شي** (not شيء) in all new copy (locked Q14 answer labels inside the unchanged assessment stay as they are); use **أنتي / وأنتي** (not أنتِ, not انتي); **معاكي**; correct ما vs مو; no tanween-fath endings (تدريجيًا → بالتدريج); no em dash; no literal translation; native-speaker read-aloud test on every line.

## 13. Gate 2 round 2 feedback (client, binding)
- Formula: **start with her challenge/scene, then turn it into a desirable outcome** (Mindvalley starts with the outcome; we start with the challenge and continue to the outcome). Study the Mindvalley examples in §11 as the model.
- **The page is about HER, never about Anhar.** No «أنا معاكي», no «أنا أنهار», no founder in the headline, subheadline, or anywhere persuasive. It read as self-centred and "misery loves company". Mindvalley only names teachers in a dedicated teachers section. First person is allowed ONLY when explaining how the Living Plan works (e.g. «تجاوبي على أسئلة، وبعدها أجهز لك خطة لأسبوعين»), and even there, prefer phrasing about what SHE gets («توصلك خطة...»).
- "Understand why…" outcomes are lukewarm: understanding isn't a result; it sounds like a PDF. Outcomes must be things she wants to live (a calmer bedtime, a visit she enjoys), not knowledge.
- Direction 3 ("against ready-made advice") rejected.
- Supersedes positioning/offer wherever they put Anhar in the hero/sub (e.g. «أنا أنهار، وأنا اللي بشتغل معاكي…» above the CTA): remove.

## 14. Gate 2 DECISION (client): approved
Headlines = `headlines_v3.json` direction **m2** ("her battle, then stacked outcomes"), all situations A–F + default, exactly as written. Subheadline = `headlines_v3.json` `sub` (standard) and `dimension_subs` (by lowest dimension). English glosses are review-only: NO English text anywhere in the final build.

## 15. Gate 3 decisions (client)
- Apply all Test Panel fixes (9 Arabic rewrites, result persistence across refresh, honest wording for low strength scores, remove invite-button underline, «علاج يشيل التوحد» → «علاج للتوحد»).
- Headlines: F → «طول اليوم وأنتي على أعصابك؟ خلي يومكم أهدى، وتعاملي مع انفعاله وأنتي عارفة ايش تسوي.» C and default stay as they are (proposed versions rejected as translated/off).
- Remove the welcome-screen line «نحفظ نتيجتك ونقدر نرسلها لك. بياناتك تبقى خاصة.» (results emailing isn't set up).
- Real work process (replaces "how it works"): onboarding file + first questionnaire → child profile → second questionnaire → two-week plan emailed → after two weeks Anhar checks in (what happened, what worked, what didn't, what she noticed) → next plan → repeat until the solution is part of their life, then optionally a new challenge. Don't specify HOW the questionnaires arrive (page vs email undecided).
- Waitlist moves ON the page (drop-off after the external Google Form): CTA opens an on-page form (name + email) → submit → thank-you screen with confetti → encourage joining the WhatsApp waitlist group (emails get lost; WhatsApp is seen). Airtable connection later: build the hook, don't connect.
- Capacity bar at the top (Priestley "oversubscribed" signal). Client does NOT want a small waitlist number shown. Rule: show capacity only («الدفعة الأولى ١٠ أمهات فقط») until the waitlist count reaches/exceeds capacity; then show capacity + demand. Count is manual in CONFIG for now; later can come from Airtable.
- Client will review the page herself after this round and send her own copy edits before re-measuring.
