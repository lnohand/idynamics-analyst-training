# Feedback — SQL 07: Who Was Paying Us on 31 May?

**PR #28 · branch `student/sql_07_month_end_list`**

Good restart, Michael. The hard part of this assignment is Step 3, and you got it
exactly right:

```sql
where start_date <= '2026-05-31'
  AND (cancelled_date is null or cancelled_date > '2026-05-31')
```

The `OR` is in brackets, the empty date is tested with `IS NULL` (not `= NULL`), and
both boundaries point the right way — `<=` for "started by", `>` for "cancelled
after". A missing bracket or a wrong boundary would still have given 56 on this data,
so getting those right means you read the query, not just the result. Your MRR `CASE`
rounds each row, divides annual plans by 12, and your three hand calculations are
written down and correct.

Every number ties:

| Check | Yours |
|---|---|
| Step 1 / 2 | 69 / 69 ✅ |
| Step 3 active on 31 May | 56 ✅ |
| Step 5 SUB003 / SUB002 / SUB054 | 1,955.00 / 3,900.00 / 1,985.50 ✅ |
| Step 6 MRR / subscriptions / customers | 160,075.50 / 56 / 45 ✅ |
| Step 7 dates vs status, 30 April | 55 vs 54, SUB026 ✅ |

Four fixes before this merges. The first one matters most.

---

## 1 — Your Step 4 check doesn't check your Step 3 query

The brief's three groups are: not started, already cancelled, and **active (your
Step 3)**. Your third count is:

```sql
select count(subscription_id) from subscriptions where status = 'active';
```

That's a different query from Step 3. It happens to give 56 today, so the check adds up
to 69 — but it would add up to 69 **whatever your Step 3 said**. Try it: change your
Step 3 to `cancelled_date = null` and it returns 0, yet your Step 4 still prints
0 + 13 + 56 = 69. A check that can't fail isn't a check.

**Fix:** the third count must use the same `WHERE` as your Step 3, word for word.
(And it should use dates, not `status` — Step 7 shows why.)

## 2 — Step 7 needs count queries

Your Step 7 lists both sets of rows but has no count query, so 55 and 54 weren't counted
by a query. The brief: *every "count" means a query that counts.* Keep the two lists (they're how you
found SUB026), and add a `COUNT(*)` version of each.

## 3 — Step 7: say *why*, not just *what*

You found the right subscription, and you correctly described what happened: SUB026
was cancelled on 23 May, so the status query leaves it out. Now go one level deeper:
**why** is that wrong for 30 April? Think about *when* the `status` column was last
written, and what it would have said on 30 April. One sentence on that is the answer —
and it's the reason every close query in this course uses dates.

## 4 — File name (small)

The brief asks for `submissions/sql/07_sql_month_end_list.sql`; yours is
`sql_07_month_end_list.sql`. Rename it in the same commit.

---

## Two small notes (no change needed)

- The brief hinted `100.0` rather than `100`. Postgres stores `discount_percent` as a
  decimal so `/ 100` works here, but in a column of whole numbers `/ 100` throws the
  decimals away. Writing `100.0` is a cheap habit.
- Your `CASE` has no `ELSE`. Every subscription today is `Annual` or `Monthly`, so it
  changes nothing — but if a third value ever appeared, those rows would get a blank MRR
  and `SUM` would skip them without warning.

## Resubmit

Commit the fixes to the **same branch** and push — PR #28 updates itself. In the PR
description, update Step 4 with your new third count and Step 7 with your new
explanation.
