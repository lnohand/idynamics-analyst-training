# Feedback — Window Functions: Practice 1 & 2
**Submitted:** March 2026
**Reviewed by:** Instructor
**Result:** ⚠️ Pass with notes — one fix required, one concept to learn before the Final

---

## Overall Assessment

The hard part is correct. You understood the `SUM(SUM()) OVER` pattern, applied `LAG()` correctly, and your self-check values match exactly. That's the substance of this lesson — and you got it right both times.

There is one issue that appears in both queries. It's a small thing, but it's the same mistake twice, so it's worth naming clearly.

---

## Practice 1

**Logic:** ✅ Correct
**Self-check:** ✅ 25 rows, last running_total = $2,509,347.00

**Issue:** `monthly_revenue` is not rounded. The assignment says *"Round both to 2 decimal places"* — that means `monthly_revenue` and `running_total`, not just `running_total`.

```sql
-- What you wrote
sum(subtotal) as monthly_revenue

-- What it should be
ROUND(SUM(subtotal), 2) AS monthly_revenue
```

---

## Practice 2

**Logic:** ✅ Correct
**Self-check:** ✅ 25 rows, NULL on first row, spot-check values match

**Issue:** Same as Practice 1 — `monthly_revenue` is not rounded.

Everything else is right: `prev_month_revenue`, `mom_change`, the Oct–Nov 2025 $0.00 MoM logic — all correct.

---

## Why Rounding Matters — and Why Instructions Must Be Followed Exactly

**Why rounding matters:**
PostgreSQL stores decimal calculations with floating-point precision. Without ROUND, a value that should be $10,515.00 might come out as $10,514.9999999997 or $10,515.0000000001. That's invisible in a query result but breaks things downstream — Excel formulas that compare values, reports where numbers don't add up cleanly, and dashboards where totals are off by a few cents. ROUND is not a cosmetic step. It's what makes financial output reliable.

**Why instructions must be followed exactly:**
In analyst work, requirements come from stakeholders — a CFO, a manager, a client. When they say "round to 2 decimal places" they mean every number, not just the ones you added. Partial compliance is still non-compliance. The output either matches the specification or it doesn't.

This is the third or fourth time you've gotten the hard logic right and missed a stated requirement in the same query. Before submitting, re-read the requirements line by line and check every output column against them. That habit is what separates a reliable analyst from one who needs constant supervision.

---

## The Final Query — What You Need to Know First

You said Q5 felt too long and too complicated. That's a fair reaction — but the reason it felt that way is that it uses a JOIN type you haven't seen yet: **FULL OUTER JOIN**. That's on the assignment, not on you. You can't write something you were never taught.

So before you attempt the Final query, read this section carefully.

---

### FULL OUTER JOIN — What It Is

You already know two JOIN types:

- **INNER JOIN** — returns only rows that match in both tables. Rows that exist in one table but not the other are dropped.
- **LEFT JOIN** — returns all rows from the left table, and matching rows from the right. Non-matching right rows are dropped.

**FULL OUTER JOIN** returns all rows from both tables, matching where it can and filling in NULL where it can't.

This matters in the Final query because `new_mrr` and `churned_mrr` don't always have the same months. Some months have new subscriptions but no churn. Some have churn but no new subscriptions. If you use an INNER JOIN, those months disappear entirely — a silent data error. If you use a LEFT JOIN, you keep all new_mrr months but lose churn-only months. FULL OUTER JOIN keeps everything.

---

### Example — The Problem It Solves

Imagine these two CTEs:

```
new_mrr                     churned_mrr
-----------                 -------------
month      | new_mrr        month      | churned_mrr
2024-01    | 5800           2025-07    | 1760
2024-02    | 8615           2025-08    | 4680
2024-03    | 3200
```

Notice: `churned_mrr` has no rows for 2024 at all — no churn happened yet. And `new_mrr` has no rows for 2025-07 or 2025-08 — no new subscriptions those months.

```sql
-- INNER JOIN: only returns rows with a match in both — returns nothing here
--             since no month appears in both tables
-- LEFT JOIN:  returns all new_mrr months, drops 2025-07 and 2025-08 entirely

-- FULL OUTER JOIN: keeps everything
SELECT
    COALESCE(n.month, c.month) AS month,
    COALESCE(n.new_mrr, 0)     AS new_mrr,
    COALESCE(c.churned_mrr, 0) AS churned_mrr
FROM new_mrr n
FULL OUTER JOIN churned_mrr c ON n.month = c.month
```

Result:
```
month    | new_mrr  | churned_mrr
2024-01  | 5800     | 0           ← no churn row existed, COALESCE fills 0
2024-02  | 8615     | 0           ← no churn row existed, COALESCE fills 0
2024-03  | 3200     | 0           ← no churn row existed, COALESCE fills 0
2025-07  | 0        | 1760        ← no new_mrr row existed, COALESCE fills 0
2025-08  | 0        | 4680        ← no new_mrr row existed, COALESCE fills 0
```

Two things to notice:

**`COALESCE(n.month, c.month)`** — when a row comes only from `new_mrr`, `c.month` is NULL. When it comes only from `churned_mrr`, `n.month` is NULL. COALESCE takes the first non-NULL value, so you always get the correct month regardless of which side it came from.

**`COALESCE(n.new_mrr, 0)`** — when a month has no new subscriptions, there is no row in `new_mrr`, so `n.new_mrr` is NULL after the join. COALESCE converts it to 0 so your arithmetic works correctly. Without this, `NULL - 1760 = NULL` instead of `-1760`.

---

### How to Approach the Final Query

The Final query is built with three CTEs followed by a main SELECT — a structure you already know from earlier assignments. The difference here is that the CTEs feed into each other, and the third one uses FULL OUTER JOIN to combine the first two.

```sql
WITH new_mrr AS (
    -- Step 1
),
churned_mrr AS (
    -- Step 2
),
monthly_mrr AS (
    -- Step 3 — joins new_mrr and churned_mrr
)
SELECT ...
FROM monthly_mrr
ORDER BY month;
```

Build and test each CTE separately before assembling the full query.

**Step 1 — Write `new_mrr` on its own**

Query the `subscriptions` table. Group by the month of `start_date`. Calculate MRR using the formula you already know — remember to handle monthly vs annual billing_cycle with a CASE WHEN.

Run it as a standalone SELECT first (without the CTE wrapper) and verify: your first two rows should show 2024-01 with $5,800.00 and 2024-02 with $8,615.00.

**Step 2 — Write `churned_mrr` on its own**

Same structure as `new_mrr`, but group by the month of `cancelled_date`. Filter to rows where `cancelled_date IS NOT NULL AND cancelled_date <> ''`. Same MRR formula.

Run it as a standalone SELECT and verify: your first churn row should be 2025-07 with $1,760.00.

**Step 3 — Write `monthly_mrr` and the main SELECT**

Once both CTEs work individually, write `monthly_mrr` using FULL OUTER JOIN as shown in the example above. Add `net_mrr_change` and the `SUM() OVER` running total for `total_mrr`.

Then in the main SELECT, add `LAG(total_mrr)` for `prev_total_mrr` and the subtraction for `mom_change`.

Self-check: 23 rows. Last row `total_mrr` = **$142,110.50**.

---

## Next Step

1. Fix the `ROUND()` issue in Practice 1 and Practice 2
2. Attempt the Final query using the three-step approach above
3. Submit all three queries in one `.sql` file

Once all three pass, this assignment is closed and you move to Excel.

---

*Window Functions Feedback | Idynamics Analyst Training | March 2026*
