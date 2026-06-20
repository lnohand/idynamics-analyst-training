# Feedback — Excel 14: April 2026 Close

**PR #14 · branch `student/excel_14_april_close`**

The plumbing held up. You added one Actuals column, copied the March tab,
changed two config cells, and the workbook recalculated April end to end —
that's the payoff the redesign was built for, and it worked. Closing MRR ties
to the penny ($156,830.50), Opening MRR derives from March's Closing, GRR/NRR
are dynamic with no hardcoded columns, and the KPI Tracker pulls April without
disturbing the prior months. The churn write-up nails the hard gate.

But three input/data errors and two commentary errors made it through, and a
couple of them cascade. This needs another pass before it merges.

---

## Fix 1 — S&M is wrong: $29,000 entered, should be $32,000

The brief tells you explicitly in Part 1: *"Read April's S&M of $32,000 off
[Lisa's] message and enter it from there."* You entered **$29,000** — March's
number, carried forward. Check the `Actuals` Apr column (E7).

This one cascades through the whole cost story:

| Line | You have | With S&M = $32,000 |
|------|----------|--------------------|
| Total OpEx | $73,000 | $76,000 |
| EBITDA | $36,781 | ~$33,781 |
| EBITDA margin | 23.5% | ~21.5% |
| Monthly CAC | $14,500 | $16,000 |
| OpEx vs plan | $1k favorable | ~$2k **un**favorable |

So the headline "EBITDA beat plan / OpEx came in light" is an artifact of the
wrong input. Fix the input first, then re-read your commentary against the
corrected numbers.

## Fix 2 — Active Subscriptions: you have 54, it should be 55

The self-check expects **55**. Your `Actuals` Apr column shows **54**, and the
A-vs-F KPI row reports the month-over-month change as **0** — i.e. you've
recorded no net movement in subscriptions. But April had both new
subscriptions *and* the one cancellation. Net it out from the snapshot: the new
subs added this month, minus the single cancelled subscription, should leave
you one ahead of March's 54. Go back to the April 30 snapshot and reconcile the
count.

This is also why your commentary says *"only bringing in 1"* new logo while
your own Actuals and KPI tab show **2 new customers** (E14 = 2). Those two
numbers can't both be right — line them up.

## Fix 3 — WaterfallData has no April rows

Part 7 asks you to add April's rows directly below March. They aren't there —
the table stops at March's Closing MRR (row 22). Your PR self-check marked this
✅, but it wasn't done. Add the seven movement rows (Opening, New, Expansion,
Contraction = 0, Churned, Net New, Closing) with the `Apr-26` label generated
by the same `TEXT/DATE` pattern, so Power BI's month slicer picks April up.

## Fix 4 — Cost commentary contradicts the tab

You wrote that OpEx fell *"in each of the three categories... a decrease of
$3,000 in both R&D and G&A."* Look at your own P&L:

- R&D: $25,000 → $22,000 = **−$3,000** ✅
- G&A: $19,000 → $22,000 = **+$3,000** — G&A *rose* $3,000, it didn't fall
- S&M: −$1,000 (and that's before Fix 1 corrects it upward)

G&A went the opposite direction from what you wrote. Once Fix 1 lands, the
whole paragraph flips anyway — OpEx is over plan, not under — so rewrite this
section from the corrected figures.

## Fix 5 — "Retention metrics aren't affected" is wrong

In the churn paragraph you say the revenue churn means *"our active customer
count [stays] the same and our retention metrics aren't affected."* Half right.
The **logo / customer count** is unaffected — that's the correct insight, and
you explained it well. But **revenue retention is absolutely affected**: a
revenue churn reduces NRR and GRR. That's literally why your NRR landed at
99.6% instead of above 100%. Tighten the wording: the *logo* is retained, the
*revenue* is not — and the retention metrics reflect the lost revenue.

## Fix 6 — Update your notes

The brief lists four `my-notes/` updates (April snapshot query, revenue-vs-logo
churn, the four-step close in practice). Your branch changed only the workbook —
no notes were touched, though the PR says they were. Add them.

(Minor, while you're in there: the KPIs section is still titled "March 2026 —
SaaS KPIs" and the forecast column header still reads "Forecast - Mar 26" on
the April tab — stale labels copied from March. And the file sits at the repo
root rather than `submissions/excel/`.)

---

## What's Good

| | |
|---|---|
| Four-step close worked: one Actuals column + two config cells | ✅ |
| April Closing MRR = $156,830.50 | ✅ |
| Opening MRR derives from March Closing (not typed) | ✅ |
| NRR = 99.6% — correctly lands just under 100% | ✅ |
| GRR/NRR dynamic, no hardcoded column letters | ✅ |
| Config block: only the two cells changed | ✅ |
| KPI Tracker April column wired; prior months intact | ✅ |
| Quarterly metrics left as dashes | ✅ |
| Commentary key-metrics line is formula-driven | ✅ |
| Churn correctly identified as revenue, not logo (hard gate) | ✅ |

Six fixes. The structure is sound — the failures are data accuracy (S&M, sub
count, missing waterfall rows) and commentary that didn't get re-read against
the numbers. Fix the S&M input first; several of the others fall out of it.
Push to the same branch when done.
