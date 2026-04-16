# Feedback — Excel 07: February 2026 Monthly Close
**PR #9 | Reviewed: 2026-04-16 | Reviewer: David Chen**
**Status: Changes Requested — Round 3**

---

## Round 3 Review — April 16

Good progress. Two of three fixes from Round 2 are clean. One remains in the Feb tab, and I want to walk through a concept issue that affects both Feb and March before you push anything else.

---

## What's Working

- D7 dollar amount now correct — +$359.80 in the Feb tab ✅
- WaterfallData: Feb Opening MRR back at the top of the Feb block ✅
- Commentary row 61: EBITDA and margin figures updated ✅
- March tab structure is solid — good initiative building it before being assigned ✅
- KPI Tracker March column wired by formula ✅
- WaterfallData March rows wired to Mar tab ✅

---

## Fix 1 — Feb tab D7: F/U label still wrong

The dollar amount is right (+$359.80) but the F/U label shows **U**.

Your IFS formula is: `IFS(D7>0, "U", D7<0, "F")` — that's the standard direction for revenue lines. On the churn row, positive variance means we churned less than expected, which is favorable. You need to invert the logic for this row:

```
=IFS(D7>0, "F", D7<0, "U", D7=0, "-")
```

Same fix applies in the March tab D7.

---

## Fix 2 — Forecast Opening MRR: Feb tab C3 and March tab C3

This one is a teaching moment, not a simple typo.

**The problem:** Both tabs are using the prior month's *actual* closing MRR as the forecast opening. That mixes actuals into the forecast column — if January missed plan, that miss disappears from February onward. The forecast column should always reflect the original plan.

**Why we haven't given you a monthly forecast closing MRR:** Our forecast is quarterly. To get monthly figures, divide by 3. Here's the derived chain:

| Month | Forecast Closing MRR | How |
|-------|---------------------|-----|
| Jan | $146,831.05 | Opening ($143,069.50) + Q1 Net New / 3 ($3,761.55) |
| Feb | $150,592.60 | Jan forecast closing + $3,761.55 |
| Mar | $154,354.15 | Feb forecast closing + $3,761.55 |

**What to fix:**

- **Feb tab C3:** Change from `='Jan 2026 A vs F '!B9` to `$150,592.60` — or better, derive it: Jan forecast closing + Q1 Net New MRR / 3. You can hardcode for now since we'll build a proper monthly forecast for Q2.
- **March tab C3:** Change from `='Jan 2026 A vs F '!B9` to `$150,592.60` — that's February's forecast closing, which becomes March's forecast opening.

Note: once you fix C3, your Opening MRR variance (D3) will no longer be zero in months where actuals diverged from plan. That's correct — it's telling you the story of how you entered the month vs expectations.

---

## Fix 3 — March tab: CAC Q1 to date skips February

Your Q1-to-date CAC formula in March adds Jan S&M and Mar S&M, but leaves out February entirely.

Current result: ($30,000 + $29,000) / (1 + 2) = **$19,667**

Correct Q1 to date: ($30,000 + $31,000 + $29,000) / (1 + 2 + 2) = **$18,000**

Update the formula to include February's S&M and new customer count. Reference the Feb tab directly — don't hardcode.

---

## Fix 4 — March tab: KPI section header

Row 27 says **"February 2026 — SaaS KPIs"**. Update to **"March 2026 — SaaS KPIs"**.

---

## Fix List

| # | Tab | Fix |
|---|-----|-----|
| 1 | Feb A vs F | D7 F/U: change to `IFS(D7>0, "F", D7<0, "U", D7=0, "-")` |
| 2 | Feb A vs F | C3: change to $150,592.60 (Feb forecast closing = Jan FC closing + Q1 Net New / 3) |
| 3 | Mar A vs F | C3: change to $150,592.60 (Feb forecast closing = March's forecast opening) |
| 4 | Mar A vs F | D7 F/U: same fix as Feb |
| 5 | Mar A vs F | CAC Q1 to date: include Feb S&M and new customers in the formula |
| 6 | Mar A vs F | KPI section header: "March 2026 — SaaS KPIs" |

Push all fixes on the same branch. Commentary for March can stay incomplete for now — finish it when you're done with the numbers.

---

*Excel Assignment 07 — February 2026 Monthly Close*
*Idynamics Finance Analyst Training Program*
