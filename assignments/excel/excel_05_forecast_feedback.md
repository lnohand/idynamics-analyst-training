# Excel Assignment 05 — 2026 Annual Forecast: Feedback

### Reviewer: David Chen, VP Finance

---

## Overall

Strong model, Michael. The structure is right, the formula
discipline is what I asked for, and you were honest about the
self-check mismatches instead of hiding them. Three fixes
needed — the opening MRR (already discussed), and two small
counting errors in the Historical Baseline.

---

## What's Working

**Every formula references the Assumptions tab.** I changed the
Q3 new customer count from 9 to 7 and the entire model
recalculated instantly. That's the whole point — one tab
controls the model. You built it the way I asked.

**The H1/H2 S&M split is handled correctly.** You referenced
the Assumptions cells, not hardcoded $90K/$108K. If I change
the H2 rate, six cells update. Good.

**P&L flows cleanly from MRR.** Revenue → COGS → GP → OpEx →
EBITDA, all formulas, no manual entries. The FY column correctly
sums flows and takes Q4 closing for balances. You didn't sum
Ending MRR across quarters — that's a mistake I see constantly
and you avoided it.

**Self-check section is honest.** You marked every mismatch as ✗
with the exact dollar difference and added a note explaining why
your opening differs. That's the right instinct. If the numbers
don't match, say so and explain — don't pretend they do.

**You brought the supporting tabs.** Waterfall, Retention, Unit
Economics, and Ref are all in the workbook so I can trace any
number to its source. That's professional. A model without an
audit trail is just a spreadsheet with opinions.

**Retention and Unit Economics tabs are solid.** The retention
analysis write-up — distinguishing subscription churn from logo
churn, noting that 8 of 11 cancellations were product drops not
customer exits — shows you understand what the numbers mean, not
just how to calculate them.

---

## Must Fix

### 1. Opening MRR — already discussed

Change to $143,069.50. Self-checks will match after this.

### 2. New customer counts: Q3/Q4 2025 swapped

Your Historical Baseline shows Q3 2025 = 1 new customer and
Q4 2025 = 0. But your own Waterfall tab shows $0 new MRR in
Jul–Sep and $935 new MRR in Oct. You can't have a new customer
with no new MRR. SUB062 started October 15 — that's Q4.

Fix: Q3 = 0, Q4 = 1.

### 3. Q1 2025 new customers: 6 → 7

Your Unit Economics tab has the S&M data: Jan = 2, Feb = 2,
Mar = 3. That's 7 for Q1, not 6. Check whether you grouped
a March customer into Q2.

---

## Minor

**CMGR self-check marked ✓ but doesn't match.** Your CMGR is
3.9% (from the inflated opening). Expected is 4.0%. After you
fix the opening MRR this will resolve, but double-check —
don't mark something ✓ without comparing the actual values.

**Q3 2025 avg MRR per new customer shows $0.** Your Waterfall
has $0 new MRR in Q3 and you have 1 new customer — the formula
divides $0 by 1 and shows $0. Once you fix the customer count
to 0, this cell becomes a divide-by-zero. Handle it with an
IFERROR or IF wrapper so it shows "N/A" like your Q4 cell does.

**2024 cost data.** Your estimates for R&D, G&A, and S&M in
2024 are reasonable ramp-up numbers. That's fine — I told you
to estimate and you did. Just make sure the Source column says
"Estimated — no accounting data available for 2024" so anyone
reading the workbook knows those aren't actuals.

---

## Grading

| Category | Weight | Score | Notes |
|----------|--------|-------|-------|
| Slack message | 20% | 17/20 | Clean format, sourced. Reconciliation note present but explanation was off — now corrected. |
| Historical Baseline | 15% | 11/15 | Complete and sourced. Two counting errors (Q3/Q4 swap, Q1 off by 1). |
| Forecast accuracy | 30% | 25/30 | Formulas are mechanically perfect. Opening MRR was wrong — all mismatches trace to that single input. |
| Formula discipline | 20% | 20/20 | No hardcodes. All refs to Assumptions. H1/H2 split handled properly. |
| Formatting & PR | 15% | 13/15 | Clean layout, tab colors, supporting tabs included. Self-check CMGR marked ✓ incorrectly. |

**Total: 86/100**

After the three fixes, this is a 95+ model. The structure is
right and the formulas work — the issue was one wrong input
that cascaded everywhere. That's actually the lesson: in a
financial model, the assumptions drive everything. One bad
starting number and the whole plan is off by $65K in EBITDA.

---

## What Comes Next

Submit the corrected workbook. Then we're moving to Actual vs
Forecast — where the 2026 budget you just built becomes the
"plan" column and we compare it against what actually happened
in H1. The structure you built here is exactly what we need
for that comparison.

---

*Feedback issued April 2026*
*Excel Assignment 05 — 2026 Annual Forecast*
