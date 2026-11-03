# مدار البيت: handoff for wiring the page

Give this note to the new chat together with `index.html`. The file is one self-contained page, about 1.4MB because the photos are embedded. It contains the assessment, the results, the Living Plan landing, the on-page waitlist form and the thank-you screen.

The copy is approved. Don't rewrite any Arabic text while wiring.

## What still needs to be made functional

All settings are in `CONFIG`, at the top of the main `<script>`:

| Setting | What it does | Status |
|---|---|---|
| `endpoint` | Sends the assessment results (answers, scores, profile) to the existing Google Apps Script relay, which writes to Airtable. | Already live. Don't change it. |
| `waitlistEndpoint` | Where the on-page waitlist form sends name + email. | **Empty.** Connect it to the Airtable "Waitlist" table. |
| `whatsappGroupUrl` | The invite link for the WhatsApp waitlist group (announcement-only), used by the button on the thank-you screen. | **Empty.** Paste the link here. |
| `capacity` | Number of places in the first group. | 10 |
| `waitlistCount` | Number of people on the waitlist, shown in the top bar. | `null` (set by hand). Can be fetched from Airtable later. |

### Waitlist form
The form calls `submitWaitlist()` and sends a POST with a JSON body (`Content-Type: text/plain`, `no-cors`, `keepalive`):

```
{ action:'waitlist', id, name, email, sitKey, primary, profile, total, source, focus, ts }
```

- `id`: the same id the assessment record uses, so the two can be linked.
- `sitKey`: her Q14 answer (A–G).
- `primary`: the dimension shown as her next opportunity.
- `profile`: 0, 1 or 2.
- `total`: her overall score.
- `source`: `results`, `focus` or `plan`.
- `focus`: the `?focus=` value, if she came from a link.

The comment "TODO connect to Airtable here" marks the spot in the code. The simplest option is to add an `action === 'waitlist'` branch to the existing Apps Script relay that upserts by email.

### Top bar (counter)
- While `waitlistCount` is `null` or below `capacity`, the bar shows: «الدفعة الأولى تستقبل ١٠ أمهات فقط».
- Once `waitlistCount` is at or above `capacity`, it shows: «١٠ أماكن في الدفعة الأولى، و{n} أم في قائمة الانتظار».
- Rule agreed with the client: never show a small waitlist number, and never use countdowns or "spots left".
- To make the count automatic, fetch it from Airtable on page load, then set `CONFIG.waitlistCount` and call `updateCapBar()`.

### Before launch
- Delete the demo switcher. It's the "DEMO SWITCHER" blocks in the CSS and the script, and it only appears with `?demo` in the URL.
- The checklist comment at the very top of the file lists the remaining placeholders. The only one left is the WhatsApp link.

## Links that open the landing directly
- `?plan`: the general landing, used in the email link.
- `?focus=` with one of `sleep`, `outings`, `communication`, `food`, `transitions`, `emotions` (or the letters A–F): the personalized landing, for TikTok and email.
- `?demo`: the owner preview switcher. Remove before launch.

## Where to edit the copy
- Personalized headlines, problem lines and invite lines: the `FOCUS` object.
- Subheadlines: the `SUBS` object.
- Arabic rules: `agency-run/source/arabic_language_file.txt` and `agency-run/arabic_language_addendum_lessons.md`.
