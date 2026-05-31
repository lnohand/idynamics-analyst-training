# Excel 09 — Workbook Redesign: Feedback
**PR #11 | Branch: `student/excel_09_workbook_redesign`**  
**Review round:** 2

---

The fixes from the first review are done — commentary numbers are formula-driven, April tab is deleted. The core redesign is solid and the GRR/NRR dynamic lookups are working correctly. Two more things before this merges.

---

## Fix 1 — Self-check cross-reference cells are stale (March tab, rows 55–56)

Your self-check table has a "formula check" column. Those cells currently hardcode a specific column in the Retention tab:

- C55: `=Retention!AA6` → returns 99.6%
- C56: `=Retention!AA7` → returns 99.6%

Column AA is **February**. March is column AB. So your self-check is comparing your March GRR (100.0%) against February's value (99.6%) and calling that a verification. It isn't.

Your actual GRR and NRR formulas in B34/B35 are correct. The self-check cells are the problem.

This is the same failure mode the whole assignment was designed to fix — you built something that requires a manual update every month, and it went stale immediately. A self-check that needs updating every month isn't a check. It's just another cell that will be wrong.

**The fix — make them dynamic.** You already know how to look up the current month's GRR from Retention without hardcoding a column. You did it in B34. Use the same INDEX/MATCH pattern in C55 and C56. When the formula check uses the same logic as the formula it's checking, the two values will always match — unless something is actually wrong, which is the whole point.

Be more diligent about this. Every cell you build for verification purposes should be held to the same standard as the formulas it's verifying. If a validation cell can go stale, it will.

---

## Fix 2 — April dummy data remains in Actuals (column E)

The April test tab was correctly deleted. But column E in the Actuals tab still holds the April dry-run numbers — Opening MRR, New MRR, Expansion, Churn, S&M, R&D, G&A, customer counts. Clear that column. The Actuals tab should only contain closed months.

---

## What's Good

| | |
|---|---|
| Actuals tab structure — INPUT vs FORMULA cells | ✅ |
| March Expansion MRR = $380 | ✅ |
| Opening MRR chain: prior Closing → next Opening | ✅ |
| All actuals pull from Actuals via INDEX/MATCH on config date | ✅ |
| GRR/NRR — no hardcoded column letters | ✅ |
| March GRR = 100.0%, NRR = 100.24% | ✅ |
| Comparison column — no hardcoded tab names | ✅ |
| Formula-driven commentary line (TEXT concatenation) | ✅ |
| Q1 New Customers = 5, Quarterly CAC = $18,000 | ✅ |
| Qualitative commentary — numbers match formulas | ✅ |
| April test tab deleted | ✅ |
| `excel_techniques.md` updated | ✅ |

Two fixes. Push to the same branch when done.
