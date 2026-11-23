# مدار البيت: handoff for the Airtable / deploy chat

Give this note to the new chat together with `index.html`.

`index.html` is one self-contained page (about 1.6MB, with all images embedded). It runs the whole flow: the welcome screen, 15 questions, the name and email step, the results, the Living Plan landing for 7 focus areas, the waitlist form and the thank-you screen.

**The copy and design are final and approved.** Don't rewrite any Arabic text and don't change the styling while wiring.

## Already wired (from the earlier wiring chat)
These values are in `CONFIG`, at the top of the main `<script>`:

| Key | What it does |
|---|---|
| `endpoint` | Google Apps Script relay to Airtable. It receives the assessment results. |
| `waitlistEndpoint` | The same relay. It receives the on-page waitlist signup (`action:'waitlist'`). |
| `whatsappGroupUrl` | The WhatsApp waitlist group link, used on the thank-you screen. |
| `capacity` | 10. |
| `waitlistCount` | Filled live from the relay (JSONP) when available. |

The top bar shows only the capacity until the waitlist count reaches it. After that it shows capacity plus demand.

## What changed since that wiring chat (copy and design only)
None of the data payloads changed. What the relay receives is exactly the same.

- A new per-focus section «خطتك في … مرحلة بعد مرحلة», built from the `CURRICULUM` object: 3 stages plus «اتجاه النمو».
- Per-focus hero subheadlines (`FOCUS[x].sub`), plus hero images for bedtime and outings (`IMAGES.HERO_A`, `IMAGES.HERO_B`).
- New copy throughout: the objections, the invite card, «ايش يوصلك كل أسبوعين», and the waitlist steps.
- The "Deep Sea Editorial" dark visual theme. It's one CSS layer at the end of `<style>`.
- The headings use IBM Plex Sans Arabic, loaded from Google Fonts.
- No word for "assessment" appears to the mother any more, and the meta description is removed.
- No line ends with a comma. `glueCommas()` keeps each Arabic comma attached to the next word.
- The image on the question screens is removed.

## Before deploy
- Delete the `?demo` switcher. It's the blocks marked "DEMO SWITCHER" in the CSS and in the script.
- Test the full flow live once: finish the assessment, check the row appears in Airtable, join the waitlist, check the waitlist row appears, and check the WhatsApp button opens the group.
- Link the TikTok and email traffic to these addresses:
  - `?plan`: the general landing
  - `?focus=sleep|outings|communication|food|transitions|emotions`: the personalized landing for that area

## Preview tool (not for deploy)
`board_pages.html` is an owner-only preview of every page and screen. It's built from `index.html` by `agency-run/tools/build_board.py`. Don't deploy it.
