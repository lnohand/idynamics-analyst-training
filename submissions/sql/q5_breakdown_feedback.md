# Q5 Breakdown — Practices 1, 2, 3 Feedback
## Idynamics Analyst Training | March 2026

---

## Practice 1 — ⚠️ Pass with corrections

Your CASE WHEN logic is correct — `status = 'active' → 'Active'`, everything else `→ 'Inactive'`. That part works.

Two issues:

**Wrong columns returned.** The assignment asked for:
`subscription_id`, `plan_name`, `billing_cycle`, `status`, `status_label`

You returned `seats` and `price_per_seat` instead of `status`. The `status` column matters here — it's what you're using in the CASE WHEN, and a reader needs to see it alongside `status_label` to verify the label is correct.

**Unnecessary GROUP BY.** This is a simple SELECT — no aggregation, no GROUP BY needed. `GROUP BY subscription_id` works here by accident because `subscription_id` is the primary key (each row is already unique). In PostgreSQL, selecting `plan_name` and `billing_cycle` without grouping or aggregating them would throw an error. Remove the GROUP BY entirely.

Corrected query:

```sql
SELECT
    subscription_id,
    plan_name,
    billing_cycle,
    status,
    CASE
        WHEN status = 'active' THEN 'Active'
        ELSE 'Inactive'
    END AS status_label
FROM subscriptions
ORDER BY status_label, plan_name;
```

Self-check: 60 rows. 49 `'Active'`, 11 `'Inactive'`.

---

## Practice 2 — ❌ Fail — missing filter

You asked what you're missing. Here it is.

Your formula and GROUP BY are correct. The problem is that your query includes **all 60 subscriptions** — active, churned, and cancelled — when the question is asking for current active MRR only.

The document said "same filter, different GROUP BY" — that was a wording error on my end. Step C intentionally has no filter because it's measuring new MRR: every subscription that ever started, including ones that later churned. But Practice 2 is a different question — *what MRR does Idynamics have right now, split by billing cycle?* That's current state, which means active subscriptions only.

The clue was in the question itself: it said "group **active** MRR." And in Step A's self-check, the 42 `'Monthly — use as-is'` rows came from active subscriptions only. That 42 matches the 42 Monthly rows you should get here.

Add one line before your GROUP BY:

```sql
FROM subscriptions
WHERE status = 'active'
GROUP BY billing_cycle
ORDER BY new_mrr DESC;
```

Expected result:

| billing_cycle | subscription_count | total_mrr |
|---|---|---|
| Monthly | 42 | $105,355.00 |
| Annual | 7 | $36,755.50 |

Both rows sum to **$142,110.50** — the same active MRR you calculated in the MRR Snapshot assignment.

---

## Practice 3 — ✅ Pass

All four rows correct. Values match exactly.

| plan_name | churned_subscriptions | churned_mrr |
|---|---|---|
| Analytics Growth | 4 | $7,989.50 |
| Analytics Enterprise | 1 | $4,680.00 |
| Analytics Starter | 5 | $2,844.00 |
| Sales Hub | 1 | $1,760.00 |

Total: **$17,273.50** ✅

Notice that $17,273.50 + $105,355.00 + $36,755.50 = your wrong Practice 2 answer of $159,384.00. Your query was including churned revenue on top of active revenue. Practice 3 proves exactly where the extra amount came from.

---

## Next Step — The Deliverable

Fix Practice 1 and Practice 2, then move to the deliverable. The deliverable is **Steps C, D, and F** from the breakdown document — all three already in your hands:

- **Step C** — New MRR by start month (you already ran this and verified it)
- **Step D** — Churned MRR by cancellation month (same)
- **Step F** — The complete Final query with CTEs, FULL OUTER JOIN, and LAG

Submit all three as a single `.sql` file. Update your branch and open the PR when ready.

---

*Q5 Breakdown Feedback | Idynamics Analyst Training | March 2026*
