# Excel 06b Feedback — KPIs, Tracker, WaterfallData
**PR:** #8 | **Reviewed by:** David Chen

---

## What's Working

The structure is solid. KPI section is in the right place, all required
metrics are present, the notes on Quick Ratio and quarterly metrics are
correct, and you caught the N/A case cleanly. KPI Tracker pulls Jan values
by formula from the A vs F tab — right instinct. WaterfallData is formatted
as an Excel Table named `WaterfallData` with 7 rows. Good.

Four things need fixing before this merges.

---

## Fix 1 — PR description is empty

The brief required a self-check table in your PR description:

```
ARPA:                  $___
GRR:                   ___%
NRR:                   ___%
Quick Ratio:           ___
CAC (monthly):         $___
WaterfallData rows:    ___
```

The submission rule is: no merge without self-check. This isn't optional —
it's how I know you verified your own numbers before submitting. Fill it in
and update the PR description.

---

## Fix 2 — ARPA: wrong source, wrong number

Your KPI section pulls ARPA from Unit Economics B7 = **$3,604.64**.

Your own KPI section shows Active Customers = 39 (Jan 31 snapshot) and your
Closing MRR = $144,779.50. That gives **$3,712.29** — a different number.

Before you fix it, I want you to understand why they differ.

Unit Economics was built in Excel 04 using Table1, which is the MRR events
log — 97 rows covering every event across all time. When it counts active
customers with `COUNTA(UNIQUE(customer_id))`, it's counting unique customer
IDs across every event that ever happened, including churned ones. It returns
40, not 39. It is not reading Jan 31 state.

That tab was built as a live reference to understand how unit economics
formulas work. It was never designed to produce point-in-time numbers for a
monthly close. If someone opens this workbook in June, your Jan ARPA should
still say January's ARPA — not whatever the database looks like in June.

**Fix:** Calculate ARPA directly on the Jan A vs F tab using your snapshot
values. Don't reference Unit Economics for any KPI in the monthly close
section.

**Before you fix it, answer this in the PR description:**
What is the correct source for Jan ARPA and why? If Unit Economics is a live
view and the KPI section is a historical record, should they ever be linked?

---

## Fix 3 — Contraction MRR row missing from Jan A vs F waterfall

You flagged this yourself in a cell comment on WaterfallData: *"The Jan 2026
A vs F file does not include Contraction MRR."* You're right — and that's a
problem you need to fix, not work around.

Your waterfall currently goes:

```
Opening MRR
+ New MRR
+ Expansion MRR
− Churned MRR
= Net New MRR
= Closing MRR
```

Contraction is missing. January had $0 contraction, so the math works out
for now. But February may not. The row needs to exist in the architecture
regardless of the value.

Add `− Contraction MRR` between Expansion and Churned on the Jan A vs F tab.
Value = 0, with formula structure consistent with the other rows.

This also cascades into Fix 4.

---

## Fix 4 — WaterfallData: two rows reference wrong tabs

Once you add the Contraction row to Jan A vs F, fix WaterfallData:

- **Contraction row:** Currently `=Waterfall!E27`. Should reference the new
  Contraction row on `Jan 2026 A vs F`.
- **Churned row:** Actual column uses `=Waterfall!F27`, but Forecast uses
  `='Jan 2026 A vs F'!C6`. These should both come from `Jan 2026 A vs F`.
  Inconsistent sourcing is how errors compound across months.

The brief is clear: all WaterfallData values come from `Jan 2026 A vs F`. No
exceptions. When February closes, you'll add 7 more rows sourced from
`Feb 2026 A vs F`. The pattern has to be consistent from day one.

---

## Fix 5 — KPI Tracker month headers are date serial numbers

Your column headers show as `46023`, `46054`, `46082`. These are Excel date
serial numbers, not text labels. Depending on column formatting they may
display as dates or as raw numbers — either way, they should be plain text:
`Jan 2026`, `Feb 2026`, `Mar 2026`, `Q1 2026`.

This tab will feed Power BI later. Text labels, not date serials.

---

## Fix 6 — my-notes not updated

Your branch contains only the xlsx file. The brief requires updating
`my-notes/kpi_definitions.md` and `my-notes/excel_techniques.md` before
submitting. You learned four new KPI definitions and used Excel Tables for
the first time in this assignment. Write them down before you close this out.

---

## Summary

| # | Issue | Action |
|---|-------|--------|
| 1 | PR description empty | Add self-check values |
| 2 | ARPA wrong source | Answer the question, then fix to use Jan 31 snapshot |
| 3 | Contraction row missing from A vs F | Add the row |
| 4 | WaterfallData wrong sources | Fix after Fix 3 |
| 5 | KPI Tracker date serials | Change to text labels |
| 6 | my-notes not updated | Update both files, push to branch |

Fix all six, then reply here with what you changed and why ARPA needed a
different source. I'll re-review.
