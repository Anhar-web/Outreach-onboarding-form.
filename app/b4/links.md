# Batch 4 destination links (Anhar, Nov 23)
| Key | URL | Goes to |
|---|---|---|
| assessment | https://madar-albayt.tiiny.site/ | the assessment, then everything else |
| plan | https://madar-albayt.tiiny.site/?plan | general landing page (skips the assessment) |
| sleep | https://madar-albayt.tiiny.site/?focus=sleep | sleep/bedtime landing |
| outings | https://madar-albayt.tiiny.site/?focus=outings | outings/visits landing |
| communication | https://madar-albayt.tiiny.site/?focus=communication | communication landing |
| food | https://madar-albayt.tiiny.site/?focus=food | food/eating landing |
| transitions | https://madar-albayt.tiiny.site/?focus=transitions | screen time/transitions landing |
| emotions | https://madar-albayt.tiiny.site/?focus=emotions | emotions/meltdowns landing |

Every `?focus=` and `?plan` link skips the assessment.

**QR tag (confirmed by Anhar, Nov 23: tags carry into the assessment row):** append `src=qr&post=<post id>` (e.g. `?focus=outings&src=qr&post=b4p3`, or `?src=qr&post=b4p1` on the main link). Make the codes with `make_qr.py` once the post IDs and destinations are set.

## Where the tags land (assessment base appxFnfLWBVqgv8sO)
- **Visits** (tbls13mjUAix09hOE): one row per page load, deduped per phone per session, before any personal data. Fields: session_id, visited_at, src, post, focus, entry (landing/assessment). session_id = the Submissions id if she starts.
- **Submissions:** src, post, focus_tag, last_q (1–15, shows the drop-off point), plus waitlist_source / waitlist_focus.
- **Privacy:** read only non-personal fields (dates, status, q14, flags, tags, last_q). Never name or email.
- **Nov 23 check, resolved:** Anhar confirmed the two completions at 19:04–19:05 (Saudi time) were her tests and deleted them. Visits is empty because she tested it and deleted the row, so visit logging works.
