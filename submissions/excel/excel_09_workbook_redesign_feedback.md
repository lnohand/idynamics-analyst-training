# Excel 09 — Workbook Redesign: Feedback
**PR #11 | Branch: `student/excel_09_workbook_redesign`**

---

## What's Working

The technical infrastructure is solid. The Actuals tab is correctly structured — input cells separated from formula cells, the MRR chain derives correctly (Opening → Closing cascades across months), and the March Expansion MRR is $380. The Q1 New Customers formula sums monthly new logos (1+2+2=5) rather than computing a net delta, and Quarterly CAC = $18,000.

The config block works as intended. The current month date cell drives the INDEX/MATCH lookups throughout the tab — every actual on the waterfall and P&L pulls from Actuals via that single reference. The "Actual - Mar 26" header derives from the config cell via TEXT(). The month-end date (EOMONTH) is correctly derived, not typed.

The GRR and NRR formulas contain no column letters or hardcoded numbers. Both use INDEX/MATCH to find the right month in the Retention tab by date. That's the right design — it will work correctly for every future month without any manual update.

The formula-driven summary line in the commentary section is correct and updates automatically.

---

## Fixes Required

### 1 — Delete the April dry run tab

The brief is explicit: *"Delete the April test tab when you're done. It was a dry run, not a real close."* The `Apr 2026 A vs F` tab is still in the workbook. Remove it before resubmitting.

### 2 — Qualitative commentary contains wrong numbers

This is the most important fix, because it is the central lesson of this assignment.

The assignment exists because typed numbers go stale the moment a formula changes. You built the formula-driven summary line correctly — it always reflects the current calculated values. Then you typed wrong numbers in the paragraphs directly below it.

**March tab:**
- "March closed at $153,486 MRR" — your formula shows $153,686
- "$180 of expansion MRR" — the correct value is $380. This is the original wrong number from Excel 08, which you fixed in Actuals. The formula is right. The sentence is still carrying the old number.

**Q1 Roll-Up:**
- "$448,571 in revenue" — formula shows $448,771
- "$91,999 of EBITDA" — formula shows $92,139
- "LTV:CAC of 1.71x" — your formula shows **2.86x**
- "CAC Payback of 11.7 months" — your formula shows **7.03 months**

The LTV:CAC and CAC Payback errors are large — these aren't rounding differences. You wrote those sentences when your formulas had different inputs, then corrected the formulas without updating the text. That is exactly the failure mode this assignment was designed to prevent.

Two things worth addressing directly.

First, the "don't touch anything" instruction. That applies to the protected tabs listed in the brief — Retention, Engine, Waterfall, Unit Economics, January, February. Your commentary on the March tab and Q1 Roll-Up is your own work written for this assignment. It is not a protected tab. You are responsible for keeping it accurate.

Second, this check wasn't on the self-check list — that's a fair point, and it's an oversight in the brief. But the rule was stated plainly in Part 4: *"numbers are never typed."* The self-check had one entry for commentary: "Commentary key metrics line updates when actuals change." That refers to the formula-driven summary line, which you did correctly. The qualitative paragraphs beneath it were not explicitly listed — but they contain numbers, and those numbers are wrong. The absence of a checkbox doesn't change the standard.

Go through every sentence in every commentary section and verify each figure against its formula cell.

---

## Notes on Your `excel_techniques.md`

Point 6 (the four-step monthly close workflow) adds "Update the Retention Tab" as Step 2. That's correct for real monthly closes — the Retention tab does need a new column each month. Good catch; the brief's four steps assumed a static Retention tab for the exercise.

One correction to make: Point 4 says "I used the Indirect function." Look at your workbook — INDIRECT does not appear anywhere in it. What you actually did was solve the prior-month comparison using `DATE(YEAR($I$2),MONTH($I$2)-1,1)` to derive the prior month's date and look it up directly in Actuals. That approach is better than INDIRECT (INDIRECT is volatile — it recalculates on every worksheet change, which slows large workbooks), and your note about when not to use it shows you understood the trade-off.

But your notes should reflect what you actually built, not what you considered and discarded. Update Point 4 to describe the INDEX/MATCH-on-Actuals approach you used and why you chose it over INDIRECT.

Related: the `Prior month tab` cell in your config block (I3 = "Feb 2026 A vs F") is never referenced by any formula in the workbook. Nothing reads it. Either wire it into something or remove it — a config cell that doesn't drive anything is misleading documentation.

---

## `sql_queries.md` — One Error

The "Opening MRR as of March 31, 2026" section has the correct query, but the Expected Result block below it shows December 31 figures (51 rows, $143,069.50). That's a copy-paste error. The March 31 snapshot should return 54 rows and $153,685.50. Fix the expected result.

---

## Summary

| | |
|---|---|
| Actuals tab structure | ✅ |
| March Expansion MRR = $380 | ✅ |
| Q1 New Customers = 5, CAC = $18K | ✅ |
| Config cell drives all actuals | ✅ |
| GRR/NRR — no column letters | ✅ |
| Formula-driven commentary line | ✅ |
| April dry run tab deleted | ❌ |
| Qualitative commentary — no typed numbers | ❌ |
| Notes accurate to what was built | ❌ |

Three fixes. Push to the same branch when done.
