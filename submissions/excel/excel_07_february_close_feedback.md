# Feedback — Excel 07: February 2026 Monthly Close
**PR #9 | Reviewed: 2026-04-09 | Reviewer: David Chen**
**Status: Changes Requested — 3 fixes required**

---

## What's Working

Strong submission overall. The structure is clean, all required tabs are present,
and the numbers are mostly right. Specific things done well:

- Opening MRR referenced from the Jan tab — not typed in ✅
- Closing MRR, Active Customers, ARPA, GRR, NRR, Quick Ratio all correct ✅
- Churned variance sign is right: you used Forecast − Actual on the churn row,
  which gives a positive (favorable) variance when actual churn is less than plan ✅
- Churn commentary correctly distinguishes subscription churn from customer churn —
  CUST007 still active, only one subscription cancelled ✅
- XLOOKUP for prior-month KPI comparisons is working ✅
- TEXT/DATE for month labels in WaterfallData is correct ✅
- KPI Tracker Feb column linked by formula, not hardcoded ✅
- PR description and self-check complete ✅

---

## Fix 1 — S&M Actual is Wrong (cascades to 5 cells)

**Cell:** `Feb 2026 A vs F` → B18 (Sales & Marketing, Actual column)
**Your value:** $30,000
**Correct value:** $31,000

Your formula references `Forecast Assumptions!B26/3` — that's the plan number, not the actual.
Lisa sent the February actuals in #finance on April 8th: S&M was $31,000.
The brief is explicit: *S&M comes from Lisa's message. The database does not have OpEx.*

This one error cascades to five downstream cells — fix B18 and the rest update automatically:

| Cell | Currently shows | Should show |
|------|----------------|-------------|
| Total OpEx (B21) | $74,000 | $75,000 |
| EBITDA (B22) | $31,214 | $30,214 |
| EBITDA Margin % (B23) | 20.8% | 20.1% |
| CAC — this month (B38) | $15,000 | $15,500 |
| CAC — Q1 to date (B40) | $20,000 | $20,333 |

---

## Fix 2 — Commentary: S&M Line Did Not Come in on Plan

**Row 64:** "All of the OpEx lines were the same as expectation..."
This is incorrect. S&M ran $1,000 over plan ($31K actual vs $30K forecast).

Once you fix B18, your P&L will show the miss. Rewrite row 64 to cover:
- Which cost line ran over and by how much
- What it did to EBITDA (revenue beat of $1,764 partially offset by $1K S&M overrun → net EBITDA beat of ~$235)
- Why the COGS variance is mechanical (it moves with revenue, not a controllable miss)

Commentary is a hard gate — the PR won't be merged without this corrected.

---

## Fix 3 — WaterfallData Excel Table Not Extended to Cover February Rows

The Excel Table (`WaterfallData`) currently has a ref of `A1:E9`. That covers the
header plus the 7 January rows plus only the first February row (Opening MRR).
Rows 10–15 — February's New MRR, Expansion, Contraction, Churned, Net New, and
Closing — are sitting outside the table.

When Power BI refreshes, it reads from the table, not the tab. It will only see
partial February data.

**Fix:** Click any cell inside the table. Drag the resize handle in the bottom-right
corner of the table down to row 15. Verify the table border now wraps all 14 data rows.

---

## Note on Your Cell Comment

You flagged that "The Jan 2026 A vs F file does not include Contraction MRR."
That's correct — it's one of the outstanding fixes on PR #8. Once that's resolved,
the Jan Contraction row in WaterfallData will reference the right cell instead of 0.
Good catch keeping track of it.

---

## Fix List

1. `Feb 2026 A vs F` B18 — change S&M actual from `Forecast Assumptions!B26/3` to `31000` (hardcode Lisa's actual)
2. `Feb 2026 A vs F` Row 64 — rewrite commentary to reflect S&M overrun and correct EBITDA story
3. `Waterfall Data` tab — extend WaterfallData table from `A1:E9` to `A1:E15`

Fix on this branch and push — the PR will update automatically.

---

*Excel Assignment 07 — February 2026 Monthly Close*
*Idynamics Finance Analyst Training Program*
