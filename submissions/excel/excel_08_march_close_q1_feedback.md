# Feedback — Excel 08: March 2026 Close + Q1 Roll-Up
**Branch: student/excel_08_march_close_q1 | Reviewed: 2026-05-15 | Reviewer: David Chen**
**Status: Changes Requested — Round 1**

---

## Good News First

All six fixes from PR #9 Round 3 are confirmed clean in this workbook:

- Feb tab D7 F/U: inverted correctly ✅
- Feb tab C3: $146,831.05 (Jan forecast closing) ✅
- Mar tab C3: $150,592.60 (Feb forecast closing) ✅
- Mar tab D7 F/U: inverted correctly ✅
- Mar tab CAC Q1 to date: includes all three months ✅
- Mar tab KPI header: "March 2026 — SaaS KPIs" ✅

The overall structure here is strong. Both commentary sections are solid — you covered the expansion signal, the EBITDA trend across Q1, and gave a clear Q2 watch item. The Q1 Roll-Up section is built correctly and the LTV formula structure is right. Good work getting this far.

That said, there are four fixes required before this can merge.

---

## Process — Open the PR

You pushed to the branch but never opened a pull request. The push is not the submission — the PR is.

After pushing, go to GitHub and open a PR from `student/excel_08_march_close_q1` → `main`. Use the description template from the brief and paste in your completed self-check table. If a value in your self-check doesn't match the expected figure, investigate before submitting.

Going forward: push → open PR with self-check filled in → that's the submission.

---

## Fix 1 — Closing MRR is off by $200

Your March closing MRR is $153,485.50. The correct value is **$153,685.50**.

The gap is in Expansion MRR. You have $180 in B5 — the correct figure is $380. Re-run your `subscription_events` query for March:

```sql
SELECT *
FROM subscription_events
WHERE event_date BETWEEN '2026-03-01' AND '2026-03-31'
  AND event_type = 'seat_change';
```

You may have captured only part of the seat change for SUB012. The MRR delta from 23→27 seats should come to $380. Once you correct B5, the closing MRR, Q1 Closing MRR, Q1 Net New MRR, and all downstream totals will update automatically.

---

## Fix 2 — GRR and NRR are pointing at February, not March

Both metrics in your KPI section show 99.6%. That's February's value. March had zero churn and $180 of expansion — GRR and NRR for March cannot both be below 100%.

The root cause: you referenced `Retention!AA6` and `Retention!AA7`. Column AA is February. March is column AB.

| Cell | Current formula | Fix |
|------|----------------|-----|
| B34 (GRR) | `=Retention!AA6` | `=Retention!AB6` |
| B35 (NRR) | `=Retention!AA7` | `=Retention!AB7` |

With the fix applied:
- March GRR = **100%** (no churn)
- March NRR = **100.24%** (expansion present)

Rather than hardcoding a column letter, look at what row 4 of the Retention tab contains — it holds the month date for each column. That means you can look up the right column by date instead of by letter. Excel has functions that let you search a row for a value and return data from that position. Use that approach here: tell the formula which month you want, let it find the column. When you build April's tab, you change the month you're asking for and the formula points at the right column automatically — no manual incrementing, no risk of silently pulling the wrong month. Always follow this pattern instead of hardcoding column letters.

---

## Fix 3 — "vs Feb 2026" column compares against January

The comparison column is labelled "vs Feb 2026" but the XLOOKUP in every row points at KPI Tracker column B — that's January.

What it's actually showing:

| Metric | Shown (vs Jan) | Correct (vs Feb) |
|--------|---------------|-----------------|
| Active Customers | +3 | +1 |
| ARPA | -$57.88 | -$11.57 |
| GRR | -0.4% | 0.0% |
| NRR | -0.4% | 0.0% |
| S&M | -$1,000 | -$2,000 |
| CAC | -$15,500 | -$1,000 |

Fix by referencing the prior month's tab directly rather than looking up from the KPI Tracker. Instead of:

```
=B32 - XLOOKUP("ARPA", 'KPI Tracker'!$A$4:$A$16, 'KPI Tracker'!$B$4:$B$16)
```

use:

```
=B32 - 'Feb 2026 A vs F'!B32
```

Same cell, prior tab. When you build April's tab, one find-and-replace on `'Feb 2026 A vs F'` → `'Mar 2026 A vs F'` and every comparison formula updates. Always follow this pattern — the KPI Tracker approach requires you to manually increment a column letter each month, which is exactly the kind of thing that gets missed.

---

## Fix 4 — Q1 New Customers formula uses net customer change, not new logos acquired

Your Q1 Roll-Up has:

```
Q1 New Customers = B30 - 'KPI Tracker'!B5  →  42 - 39 = 3
```

That subtracts January's closing customer count from March's closing count — it gives you the net change in active customers over Q1, not the number of new logos signed.

Net change undercounts if any churn occurred during the quarter. If one customer left in February and two signed in March, your net is +1 but you acquired two new logos.

The correct approach is to sum new customers per month. You already have all three counts: Jan = 1 (from Jan tab), Feb = 2 (from Feb B39), Mar = 2 (from B39 here). Write the formula as a direct sum:

```
= [Jan new customers] + 'Feb 2026 A vs F'!B39 + B39
```

For Jan, reference the count from the Jan tab — the same cell you use as the denominator in your CAC-to-date formula in row 40.

With Q1 New Customers = 5:
- Quarterly CAC = $90,000 / 5 = **$18,000** (matches your CAC Q1-to-date in the Mar KPI section — they'll finally agree)
- LTV:CAC and CAC Payback will also update — recalculate and update your commentary if the narrative changes materially.

---

## Fix 5 — Update my-notes

No my-notes files were updated on this branch. The brief requires updating before every submission:

- `sql_queries.sql` — March snapshot query; `subscription_events` query for expansion MRR
- `kpi_definitions.md` — LTV, LTV:CAC, CAC Payback formulas; note that these are quarterly-only metrics and why
- `excel_techniques.md` — Q1 Roll-Up cross-tab aggregation; quarterly vs monthly metric structure

---

## Fix List

| # | Location | Fix |
|---|----------|-----|
| 0 | GitHub | Open a PR from this branch |
| 1 | Mar A vs F B5 | Expansion MRR: re-run SQL, correct value is $380 |
| 2 | Mar A vs F B34 | GRR: `=Retention!AA6` → `=Retention!AB6` |
| 3 | Mar A vs F B35 | NRR: `=Retention!AA7` → `=Retention!AB7` |
| 4 | Mar A vs F col C (KPI section) | All XLOOKUPs: `$B$4:$B$16` → `$C$4:$C$16` |
| 5 | Mar A vs F B90 | Q1 New Customers: sum monthly new logos (1+2+2=5), not net delta |
| 6 | my-notes/ | Update sql_queries.sql, kpi_definitions.md, excel_techniques.md |

Push all fixes on the same branch. The PR will update automatically.

---

*Excel Assignment 08 — March 2026 Close + Q1 Roll-Up*
*Idynamics Finance Analyst Training Program*
