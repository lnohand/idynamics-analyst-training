# SQL 03 — PR Review Feedback
### Idynamics Finance Analyst Training Program

---

> **PR:** Complete: SQL 03 #3
> **Branch:** `submission/sql-03-excel-data-pull`
> **Reviewer:** Instructor
> **Status:** Changes requested — 4 items

---

## Before you fix anything: Database Cleanup

You need to run two UPDATE statements before re-exporting your queries.
Right now 9 cancelled subscriptions are marked `'churned'` in the
database and 2 are marked `'cancelled'`. Same thing, two labels. If
you export now, your events CSV will have that inconsistency baked in,
and every Excel filter on cancelled events will silently miss rows.

Run these in DBeaver:

```sql
-- Fix 1: subscriptions table — standardize status
UPDATE subscriptions
SET status = 'cancelled'
WHERE status = 'churned';
```

```sql
-- Fix 2: subscription_events table — standardize the new_value
UPDATE subscription_events
SET new_value = 'cancelled'
WHERE event_type = 'cancelled'
  AND new_value = 'churned';
```

**Verify:**

```sql
-- Should return zero rows
SELECT * FROM subscriptions WHERE status = 'churned';

-- Should return: active = 51, cancelled = 11
SELECT status, COUNT(*) FROM subscriptions GROUP BY status;

-- Every cancelled event should show new_value = 'cancelled'
SELECT event_id, new_value
FROM subscription_events
WHERE event_type = 'cancelled';
```

Once verified, move on to the three query fixes below.

---

## Fix 1 — mrr_events.sql: Remove duplicate event_date

**Line 10–11:** `se.event_date` appears twice. Delete one.

```sql
-- BEFORE (wrong — duplicate column)
    se.event_date,
    se.event_date,

-- AFTER (correct)
    se.event_date,
```

---

## Fix 2 — mrr_events.sql: Add s.seats

This is the critical one. Without `seats`, Excel cannot calculate the
MRR delta for 85 out of 97 events. Here's why:

- A `created` event has no old_value/new_value. The only way to get
  that subscription's MRR is seats × price × (1 − discount/100).
  Without seats, Excel can't compute it.
- Same for `cancelled` — old_value is just `'active'`, new_value is
  `'cancelled'`. Useless for dollar math without seats.
- `price_change` gives you old and new price, but the delta is
  seats × (new − old) × (1 − discount/100). No seats, no delta.
- `discount_added` — same problem. You need seats to turn a
  percentage change into a dollar amount.

Add `s.seats` between `s.billing_cycle` and `s.price_per_seat`:

```sql
-- BEFORE
    s.plan_name,
    s.billing_cycle,
    s.price_per_seat,
    s.discount_percent

-- AFTER
    s.plan_name,
    s.billing_cycle,
    s.seats,
    s.price_per_seat,
    s.discount_percent
```

---

## Fix 3 — mrr_snapshot.sql: ROUND needs 2 decimal places

Your ROUND() calls have no second argument:

```sql
-- BEFORE (rounds to whole dollars — wrong)
ROUND(seats * price_per_seat * (1 - discount_percent / 100.0))

-- AFTER (rounds to 2 decimal places — correct)
ROUND(seats * price_per_seat * (1 - discount_percent / 100.0), 2)
```

Fix both branches of the CASE WHEN. Without `, 2`, PostgreSQL rounds
to the nearest integer. Your SUM will not match the self-check value
of $144,185.50.

---

## After fixing — re-verify all self-checks

Run the cleanup first, then re-run all three queries and verify:

| Check | Expected |
|---|---|
| Subscriptions: `SELECT status, COUNT(*) GROUP BY status` | active = 51, cancelled = 11 |
| Q1 row count | 51 |
| Q1 SUM(mrr) | **$144,185.50** |
| Q2 row count | 97 |
| Q2 distinct event_type count | 7 |
| Q2 all cancelled events `new_value` | `'cancelled'` (not `'churned'`) |
| Q3 row count | 26 |
| Q3 last running_total | **$2,475,630.00** |

---

## How to submit the fix

Same branch, same PR — commit the corrections and push:

```
git add submissions/sql/mrr_snapshot.sql
git add submissions/sql/mrr_events.sql
git commit -m "Fix: SQL 03 — add s.seats, fix ROUND, remove duplicate, cleanup verified"
git push origin submission/sql-03-excel-data-pull
```

The PR updates automatically. Reply to each review comment on GitHub
confirming the fix, then mark as resolved.

---

*SQL 03 PR Review | Idynamics Finance Analyst Training | March 2026*
