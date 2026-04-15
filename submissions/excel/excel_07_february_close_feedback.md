# Feedback — Excel 07: February 2026 Monthly Close
**PR #9 | Reviewed: 2026-04-14 | Reviewer: David Chen**
**Status: Changes Requested — Round 2**

---

## Round 2 Review — April 14

You fixed S&M, extended the WaterfallData table, and updated row 64. Those are done.

Two things I want to be upfront about. First, the churn sign issue below was already wrong in your original submission — I missed it in round 1. Second, when you made your fixes, you introduced a new problem in WaterfallData that wasn't there before. So the fix list this round is: one carryover I should have caught, one thing you broke in the process of fixing, and commentary you half-updated.

---

## What's Working

- Opening MRR referenced from the Jan tab — not typed in ✅
- Closing MRR, Active Customers, ARPA, GRR, NRR, Quick Ratio, CAC — all correct ✅
- Churn commentary correctly distinguishes subscription churn from customer churn ✅
- XLOOKUP for prior-month KPI comparisons is working ✅
- TEXT/DATE for month labels in WaterfallData is correct ✅
- KPI Tracker Feb column linked by formula, not hardcoded ✅

---

## Fix 1 — Churn variance sign wrong in Feb A vs F tab (D7)
*[was present in original submission — missed in round 1]*

**Your value:** −$359.80
**Expected:** +$359.80

Your formula is `=B7-C7` — Actual minus Forecast. The brief said don't do that on the churn row. When actual churn is less than forecast, the variance should be positive. You tried to paper over it by inverting the IFS logic (`D7<0 → F`), which makes the F/U label look right, but the dollar figure is still wrong. A finance reader looking at that table sees −$360 on a favorable line.

Your WaterfallData tab already has this right: `=D13-C13` = Forecast − Actual = +$359.80. Use the same approach in D7.

---

## Fix 2 — WaterfallData: Feb Opening MRR moved to the last row
*[introduced in round 2 fix]*

Your original submission had this correct — Feb Opening MRR was row 9, first in the February block. When you extended the table, you moved it to row 15 (last). The order now reads: New → Expansion → Contraction → Churned → Net New → Closing → Opening.

That breaks the waterfall chart. Power BI reads rows in order — Opening has to come first so the chart knows where February starts. Move it back to the top of the February block.

---

## Fix 3 — Commentary row 61: EBITDA figures not updated
*[introduced in round 2 fix]*

You corrected row 64 (OpEx sentence) but left row 61 with the old numbers:

> *"EBITDA to $31,214... margin of 20.8%"*

Those figures came from when S&M was $30,000. Now that S&M is $31,000, your model shows EBITDA = $30,213.85 and margin = 20.1%. Update the sentence to match.

---

## Fix List

1. D7 in Feb A vs F — change formula to `=C7-B7` (Forecast − Actual) → +$359.80
2. WaterfallData — move Feb Opening MRR back to the first row of the Feb block
3. Commentary row 61 — update EBITDA to ~$30,214 and margin to 20.1%

---

## A Note on my-notes/

I'm not grading you on the notes files, but you need to keep them accurate — they're your own reference and they're part of the submission requirement.

**`excel_techniques.md` is empty.** This assignment introduced two things worth writing down:
- `TEXT(DATE(2026,2,1),"mmm yyyy")` — how to generate a month label dynamically instead of typing it
- Cross-tab references — syntax for pulling a value from another tab (`='Jan 2026 A vs F'!B9`) and when to use it vs hardcoding

**`kpi_definitions.md` has the wrong content** — it contains git fix commands from Excel 06, copy-pasted in by mistake. Replace the whole file with:
- XLOOKUP — what it does, the syntax you used (`=XLOOKUP("Jan 2026", KPITracker[Month], KPITracker[ARPA])`), and when to use it over a direct cell reference
- NRR = GRR — what it means when they're equal (no expansion or contraction MRR, only churn affects both the same way)
- CAC Q1 to date — the formula: cumulative S&M ÷ cumulative new customers across all closed months in the quarter

**`sql_queries.md` — COGS query uses the wrong date.** The query filters to `2026-01-31`. Add a February version below the January one with `2026-02-28`. Don't overwrite the January entry.

Sort these out when you push the fixes. They don't block the merge but they should be right.

---

*Excel Assignment 07 — February 2026 Monthly Close*
*Idynamics Finance Analyst Training Program*
