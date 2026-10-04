# SQL Assignment 07: Who Was Paying Us on 31 May?
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Back to basics — one query, built slowly
>
> It's been over a month, so we're restarting gently. This assignment is one
> question, answered with one query that you build a step at a time:
>
> *Which subscriptions were active on 31 May 2026, and what was each one worth
> per month?*
>
> That list is the foundation of every monthly close — MRR, customer counts,
> churn all start from it. The next assignments build on it, so take your time
> and get it right. Expect about 3–4 hours.
>
> — David

---

## Three things to remember before you start

### 1. An empty cell is `NULL`, and you test it with `IS NULL`

A subscription that was never cancelled has **no** `cancelled_date` — the cell is
empty. SQL calls that `NULL`. `NULL` is not a date and not zero, and it is never
"equal" to anything, not even itself. So:

```sql
-- subscriptions that started WITHOUT a free trial (trial_start_date is empty)
SELECT COUNT(*) FROM subscriptions WHERE trial_start_date IS NULL;   -- ✅ correct
SELECT COUNT(*) FROM subscriptions WHERE trial_start_date = NULL;    -- ❌ always 0, no error

-- subscriptions that DID start with a trial
SELECT COUNT(*) FROM subscriptions WHERE trial_start_date IS NOT NULL;
```

Run the first two yourself: one counts most of the table, the other counts nothing — and
nothing warns you.

### 2. `AND` is evaluated before `OR` — use brackets

```sql
SELECT COUNT(*) FROM subscriptions
WHERE plan_name = 'Sales Hub' AND (seats > 20 OR billing_cycle = 'Annual');
```

This means: Sales Hub, **and** (either more than 20 seats **or** annual). Without
the brackets SQL reads it as (Sales Hub and more than 20 seats) **or** (any annual
subscription) — a different question.

**Run it twice — with the brackets and without them — and compare the two counts.**
That difference is why, when a condition mixes `AND` and `OR`, you always bracket the
`OR` part. On some data the two versions happen to give the same answer, so you can't
rely on the result to warn you; you have to write it correctly.

### 3. `CASE` — a different calculation depending on a value

```sql
SELECT subscription_id,
       seats,
       CASE WHEN seats >= 30 THEN 'Large'
            ELSE 'Small'
       END AS size_band
FROM subscriptions;
```

Read it as: *when* the condition is true, *then* use this value, *else* that one.
It always ends with `END`. You can put a calculation after `THEN` and `ELSE`, not
just a label.

---

## The exercises

Write every step in **one file**, with a comment line above each step's queries
(`-- Step 1`, `-- Step 2`, …). Some steps need more than one query. Run each one in DBeaver before moving on.
Write the results down as you go — you will need them in your PR.

**Every "count" in this assignment means a query that counts** (`COUNT(*)`) — never
scrolling through results and counting rows yourself. DBeaver's row counter at the bottom
of the results is a good way to double-check, but the number you report comes from the query.

### Step 1 — Look at the data

List every subscription with `subscription_id`, `customer_id`, `status`,
`start_date` and `cancelled_date`, ordered by `start_date`. Scroll through it.
Notice which rows have an empty `cancelled_date`.

Then write a second query that counts all the rows in the table:

```sql
SELECT COUNT(*) FROM subscriptions;
```

**Write the number down.** Every later count in this assignment is this same query with a
`WHERE` added.

### Step 2 — Started on or before 31 May

Count the subscriptions whose `start_date` is on or before 31 May 2026.

*Hint:* dates are written in quotes: `'2026-05-31'`. "On or before" is `<=`.

### Step 3 — Still active on 31 May

A subscription was active on 31 May if it had **started** by then **and** had
**not been cancelled** by then. "Not cancelled by then" has two possibilities:
it was never cancelled, or it was cancelled *after* 31 May.

List these subscriptions (all the columns from Step 1), then count them.

*Hint:* the second part is an `OR` — reread point 2 above.

**Use the dates, not the `status` column.** Step 7 shows you why.

### Step 4 — Check your own work

Every subscription in the table is in exactly **one** of three groups on 31 May:

- not started yet (started after 31 May)
- already cancelled (cancelled on or before 31 May)
- active (your Step 3)

Write a count query for each of the first two groups. **The three counts must add
up to your Step 1 total.** If they don't, one of your conditions is wrong — find
it before you go on.

This is the most important habit in this assignment: checking your own number
instead of waiting for someone to tell you. Be clear about what this check proves:
that no subscription was **lost or counted twice**. It does not prove each condition is
written correctly — a missing bracket, for example, can still pass it. That is why
you also reread your query against point 2.

### Step 5 — Add each subscription's monthly value (MRR)

Take your Step 3 list, add the columns `billing_cycle`, `seats`, `price_per_seat` and
`discount_percent`, and then a column named `mrr`:

- **seats × price_per_seat**, reduced by the discount: × (1 − discount_percent ÷ 100)
- **Annual** plans: `price_per_seat` is a yearly price, so divide by 12.
  Monthly plans stay as they are.
- Round to 2 decimals: `ROUND(value, 2)`

*Hint:* use `CASE` on `billing_cycle` (point 3 above). Write `100.0`, not `100`.

**Check it by hand.** Take three subscriptions — **SUB003** (monthly), **SUB002**
(annual) and **SUB054** (annual, with a discount) — and work out their MRR with a
calculator from the seats, price, discount and billing cycle in your list. Your query
must give the same three numbers. Write the three calculations down.

### Step 6 — Totals

Now one row with three numbers: total MRR, number of subscriptions, and number of
**different** customers.

*Hints:* `SUM(...)` around your MRR calculation; `COUNT(*)`;
`COUNT(DISTINCT customer_id)` — some customers have more than one subscription.

Write the three numbers down. The next assignment starts from them.

### Step 7 — Why dates and not `status`?

Run your Step 3 count again, but for **30 April 2026** instead of 31 May.
Then run a second count for 30 April using `status = 'active'` (and started on or
before 30 April) instead of the cancelled-date condition.

The two counts are different. Find the subscription that is in one result and not
the other, and explain in 2–3 sentences **why** the `status` version gets it wrong.

*Hint:* list both results ordered by `subscription_id` and compare them. Or use
`EXCEPT`: *(the dates query)* `EXCEPT` *(the status query)* returns the rows that are in
the first result but not in the second — the order matters.

---

## Before you submit — git

**Do not start a new branch or switch branches until your May workbook is safe** — see
David's email.
Write your queries in DBeaver in the meantime and save the file somewhere you can
find it. Once we've sorted the workbook, create the branch as in
`docs/git_workflow_reference.md` ("Every Time You Start a New Assignment"), then save
your file into the `submissions/sql/` folder under the name below before you commit.

## Submission

- Branch `student/sql_07_month_end_list`, file
  **submissions/sql/07_sql_month_end_list.sql** with all seven steps.
- PR description:
  - **Step 4:** your three group counts and the total they add up to
  - **Step 5:** your three hand calculations
  - **Step 6:** your three totals
  - **Step 7:** the two counts, the subscription that differs, and your explanation
- If something doesn't add up and you couldn't find out why, say so in the PR.
  That's a good answer. Hiding it isn't.
