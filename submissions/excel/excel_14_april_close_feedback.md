# Feedback — Excel 14: April 2026 Close

**PR #14 · branch `student/excel_14_april_close`**

*(Updated review — supersedes the first pass. Two corrections to the earlier
version: the S&M issue was on us, not you; and I've now reviewed the Billing
Reconciliation tab, which the first pass missed.)*

The four-step close worked end to end — Closing MRR ties to the penny
($156,830.50), Opening MRR derives from March's Closing, GRR/NRR are dynamic with
no hardcoded columns, the KPI Tracker pulls April without disturbing prior months,
and the churn write-up nails the hard gate. The reconciliation you carried into
this file now ties on both bridges — good work; the annuals you were stuck on are
sorted. Below are the close fixes and the reconciliation cleanup.

---

## A — On S&M: that one was on us

You were right — there was no April OpEx message in #finance, so you had no source
and carried March's $29,000 forward. That's the sensible thing to do with missing
data, and you shouldn't have been dinged for it. **Lisa has now posted April's
numbers** to #finance:

| Line | April actual |
|------|--------------|
| S&M | $32,000 |
| R&D | $23,000 |
| G&A | $20,000 |
| **Total OpEx** | **$75,000** |

Update the three INPUT cells in the `Actuals` Apr column from her message. That
changes Total OpEx to $75,000, EBITDA to $34,750 (22.16% margin), and monthly CAC
to $16,000 — then re-read your cost commentary against the corrected figures (see
Fix A3).

---

## B — Close fixes

### B1 — Active Subscriptions: you have 54, should be 55
Your `Actuals` Apr column shows **54**, and the KPI row reports the
month-over-month change as **0**. April had new subscriptions *and* the one
cancellation — net the snapshot out and you should land one ahead of March's 54.
This is also why your commentary says *"only bringing in 1"* new logo while your
own Actuals show **2 new customers** (E14 = 2). Reconcile the two.

### B2 — WaterfallData has no April rows
Part 7 asks for April's rows directly below March; the table stops at March's
Closing MRR (row 22). Add the seven movement rows (Opening, New, Expansion,
Contraction = 0, Churned, Net New, Closing) with the `Apr-26` label from the same
`TEXT/DATE` pattern, so Power BI's month slicer picks April up.

### B3 — Cost commentary needs a rewrite against the corrected OpEx
Once you enter the real numbers, the cost story flips. With S&M $32k / R&D $23k /
G&A $20k:
- **Total OpEx is $75,000 vs $74,000 plan — $1,000 *over*** (not under).
- S&M $2k over, **G&A $1k over** (your draft said G&A *fell* — it rises either way),
  R&D $2k under.
- EBITDA $34,750 is still a touch above the $34,048 plan, so the headline is
  "roughly on plan," not a beat driven by light spend.

### B4 — "Retention metrics aren't affected" is wrong
The *logo / customer count* is unaffected by a revenue churn — that part you
explained well. But a revenue churn **does** lower NRR and GRR; it's exactly why
your NRR landed at 99.6%. Reword: the logo is retained, the revenue is not, and
the retention metrics reflect the lost revenue.

### B5 — Update your notes
The brief lists four `my-notes/` updates (April snapshot query, revenue-vs-logo
churn, the four-step close in practice). The branch changed only the workbook.

*(Minor: KPI section still titled "March 2026 — SaaS KPIs" and the forecast column
header still reads "Forecast - Mar 26" on the April tab — stale labels copied from
March. File also sits at repo root rather than `submissions/excel/`.)*

---

## C — Billing Reconciliation tab (the column-E version)

Both bridges tie to zero in both months, and the hard part is right: you found all
five prior-billed annuals (SUB006/009/016/025/031 = $30,870/mo) for January, and
correctly extended it to seven for February once the two Pacific annuals also stop
billing ($36,755.50). The `SUMIF(...,"Annual",...) * 11/12` for billing excess is
clean. Four things to finish it:

### C1 — February Total Invoiced: $114,144 vs $113,974.29
The Feb billing file sums to **$113,974.29** — the −$169.71 SUB050 credit note is
in it. You add the $169.71 *back* to report $114,144, then net it out again in
Bridge 2. That contradicts both the billing file and your own Part 6 note ("Total
billed will also be reduced"). Pick the treatment your commentary already
describes: leave the credit note *in* Total Invoiced (= $113,974.29). Then Bridge 2
needs only the +$675 SUB028 line — drop the separate SUB050 line.

### C2 — Don't hardcode the annual-MRR line
`F13`/`G13` type the seats and prices as literals (`31*180 + 36*150 + …`). The
values are right, but it's the same trap as a stale self-check cell — the day a
seat count changes, this silently goes wrong and no one notices. Reference the
subscription cells (Engine / your sub base) so the line recomputes itself.

### C3 — Quantify the deferred revenue
Commentary point 3 asks for the **balance**, named. You say it was "high." State
it: **$64,740.50 at January 31**, created by the two Pacific Analytics annuals
(SUB002 $46,800, SUB054 $23,826) — cash collected, not yet earned.

### C4 — Delete the stale left-hand reconciliation (columns A–C)
The old version is still on the tab and still *doesn't* tie (differences of
$30,870 / $30,276). Two reconciliations side by side, one broken, is exactly what
an auditor flags. Remove the A–C block so only the correct column-E version
remains.

---

## What's Good

| | |
|---|---|
| Four-step close worked: one Actuals column + two config cells | ✅ |
| April Closing MRR = $156,830.50; Opening derives from March | ✅ |
| NRR = 99.6% — correctly lands just under 100% | ✅ |
| GRR/NRR dynamic, no hardcoded column letters | ✅ |
| KPI Tracker April column wired; prior months intact | ✅ |
| Churn correctly identified as revenue, not logo (hard gate) | ✅ |
| Reconciliation: both bridges tie; all 5 (Jan) / 7 (Feb) annuals found | ✅ |
| Annual billing excess via SUMIF × 11/12 | ✅ |
| Part 5 (SUB012 = $2,185 for January) — correct | ✅ |

The close fixes are data accuracy (subs, OpEx now sourced, waterfall rows) and a
commentary rewrite; the reconciliation is cleanup, not a redo. Push to the same
branch when done.
