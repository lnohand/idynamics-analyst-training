# Feedback — Excel 08: March 2026 Close + Q1 Roll-Up
**Branch: student/excel_08_march_close_q1 | Reviewed: 2026-05-16 | Reviewer: David Chen**
**Status: Changes Requested — Round 2**

---

## Round 1 Fixes — All Confirmed

Every fix from Round 1 is in. Good execution.

| Fix | Status |
|-----|--------|
| PR opened with description | ✅ |
| Expansion MRR corrected to $380 | ✅ |
| GRR → `Retention!AB6` (100%) | ✅ |
| NRR → `Retention!AB7` (100.24%) | ✅ |
| "vs Feb" column uses direct tab references | ✅ |
| Q1 New Customers = 5 | ✅ |
| `kpi_definitions.md` updated | ✅ |

---

## On Your -$6.81 Question

You were right to flag it — but -$6.81 is correct.

In Round 1, Expansion MRR was $180 (wrong). With $180, March closing MRR was $153,485.50 and ARPA was $3,654.42 — making the vs-Feb gap -$11.57. After you corrected Expansion MRR to $380, closing MRR became $153,685.50, ARPA became $3,659.18, and the gap became -$6.81.

The target shifted when you fixed Fix 1. Nothing to change here.

---

## Fix 1 — Commentary references a number that no longer exists

Your March commentary (row 61) says: *"March closed at $153,486 MRR."*

The correct figure — the one in your own cell B9 — is **$153,685.50**. The same $199.50 gap shows up in the Q1 commentary (row 97): *"$448,571 in revenue"* should be **$448,770.50**.

What happened: you wrote the commentary before fixing Expansion MRR, then corrected the formula but not the text. This is a recurring risk whenever numbers are hardcoded into prose. Update both figures now.

---

## Fix 2 — Q1 commentary unit economics are from a previous version

Row 98 currently says:
- LTV:CAC = **1.71x** — your actual (B93) is **2.86x**
- CAC Payback = **11.7 months** — your actual (B94) is **7.03 months**

The narrative built around these numbers no longer holds. At 2.86x LTV:CAC and 7 months payback the picture is meaningfully different from what you wrote — not alarm-free, but not the "well below the 3x threshold" story either. Rewrite that paragraph to reflect what the numbers actually say.

---

## Fix 3 — `excel_techniques.md` is empty

You said there was nothing to add. There is.

This assignment introduced two techniques you hadn't used before:

**Cross-tab aggregation.** You pulled the same line item from three different monthly tabs and summed them in the Q1 Roll-Up. That's not something you'd done before January close. Your notes should cover: how you structured the formulas, what breaks if a tab is renamed, and how you verified the sums were picking up the right cells from each tab.

**Quarterly vs monthly metric structure.** You know *why* LTV, LTV:CAC, and CAC Payback are quarterly-only from `kpi_definitions.md`. Add the Excel side here: what you actually built differently for those rows (dashes in Jan and Feb columns, values only in Q1), why you structured it that way, and what someone would need to know to maintain it correctly next quarter.

---

## Fix 4 — Self-check table still missing from PR description

The brief specifies the exact format. Open the PR, edit the description, and paste in the completed self-check table using your current submission values.

---

## Fix List

| # | Location | Fix |
|---|----------|-----|
| 1 | Mar tab row 61 | Update MRR figure in commentary: $153,486 → $153,685.50 |
| 2 | Mar tab row 97 | Update revenue figure in Q1 commentary: $448,571 → $448,770.50 |
| 3 | Mar tab row 98 | Rewrite unit economics paragraph: LTV:CAC is 2.86x, CAC Payback is 7.03 months |
| 4 | `excel_techniques.md` | Add notes on cross-tab aggregation and quarterly metric structure |
| 5 | PR description | Add completed self-check table |

Push on the same branch — the PR updates automatically.

---

*Excel Assignment 08 — March 2026 Close + Q1 Roll-Up*
*Idynamics Finance Analyst Training Program*
