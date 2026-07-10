# SQL Assignment 05: Aggregates & HAVING
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Round 2 — you asked for more
>
> Good — the joins came back clean, so let's level up one notch. This set
> moves from *counting* rows to *summing money*, and introduces exactly one
> new keyword: `HAVING`. Everything else you've already done: the same
> tables, the same joins, the same MRR arithmetic from your snapshot work.
>
> Same rules as last time: validate against the self-checks, and if a
> number doesn't reconcile, say so — don't explain it away.
>
> — David

---

## Step 0 — Fix one status value first (my bug, not yours)

The April DB update I sent you set SUB045's status to `'churned'`. That
breaks our convention — this database uses only `'active'` / `'cancelled'`
(we cleaned that up back in April, remember). Run this once before anything
else:

```sql
UPDATE subscriptions SET status = 'cancelled' WHERE status = 'churned';
```

Then confirm: `SELECT status, COUNT(*) FROM subscriptions GROUP BY status;`
must return exactly 2 rows — **active 55 / cancelled 12**.

---

## Setup

- Same PostgreSQL database, same three tables: `customers`,
  `subscriptions`, `subscription_events`.
- **Monthly MRR formula** (you know this from the snapshot work):
  `seats * price_per_seat * (1 - discount_percent / 100.0)`
- **Scope note:** for every money question below, filter to
  `billing_cycle = 'Monthly'`. For annual subscriptions `price_per_seat`
  is an annual rate (÷12 to get MRR) — we'll fold those in when we bring
  back CASE WHEN. Today: the monthly-billed book only.

**New concept — `HAVING`:**

`WHERE` filters **rows** before they're grouped. `HAVING` filters
**groups** after the aggregate is computed. You physically cannot write
`WHERE COUNT(*) > 5` — at the time WHERE runs, there is no count yet.
The order Postgres thinks in:

```
FROM → WHERE (keep/drop rows) → GROUP BY → HAVING (keep/drop groups) → ORDER BY
```

So "active subscriptions only" is a WHERE job, and "only plans with more
than 9 of them" is a HAVING job — same query, two different filters, two
different clauses.

---

## Question 1 — Warm-up: SUM instead of COUNT

**Business context:** Product wants seat volume by plan — not how many
subscriptions, how many *seats*.

**Task:** For **active** subscriptions (all billing cycles — seats are
seats), total the seats per plan.

- **Columns:** `plan_name`, `total_seats`
- **Filter:** `status = 'active'`
- **Group:** `plan_name`
- **Sort:** `total_seats` descending

**Self-check:** **6 rows.** Top row is Marketing Pro with **350** seats.
All six values sum to **1,366**.

---

## Question 2 — Money: MRR by plan

**Business context:** Which plans actually carry the revenue? Seat counts
flatter the cheap plans; MRR doesn't.

**Task:** For **active, monthly-billed** subscriptions, compute total MRR
per plan using the MRR formula above.

- **Columns:** `plan_name`, `monthly_mrr`
- **Filter:** `status = 'active' AND billing_cycle = 'Monthly'`
- **Group:** `plan_name`
- **Sort:** `monthly_mrr` descending

**Self-check:** **6 rows.** Top row is Sales Hub at **$30,470.00**. The six
values sum to **$120,075.00** — and here's why you should believe that
number: add the annual-billed book ($36,755.50/mo, the same seven
subscriptions from your reconciliation) and you land on **$156,830.50**,
your own April closing MRR. The database ties to your close.

---

## Question 3 — HAVING: filter the groups

**Business context:** Leadership only wants to hear about plans with real
adoption — a plan with 5 subscriptions isn't worth a slide.

**Task:** List the plans that have **more than 9 active subscriptions**,
with their counts.

- **Columns:** `plan_name`, `active_subs`
- **Filter (rows):** `status = 'active'`
- **Filter (groups):** count > 9 — this is the HAVING clause
- **Sort:** `active_subs` descending

**Self-check:** **3 rows** — counts **14, 12, 10**. (Three plans drop out:
8, 6 and 5 active subs.)

---

## Question 4 — Join + SUM + HAVING together

**Business context:** Which regions are big enough to get their own line
in the board deck? Cutoff: $20K monthly-billed MRR.

**Task:** For **active, monthly-billed** subscriptions, total MRR per
region (join to `customers`, like your refresher Q4) — but only return
regions whose total is **over $20,000**.

- **Columns:** `region`, `monthly_mrr`
- **Join:** `subscriptions` INNER JOIN `customers` ON `customer_id`
- **Filter (rows):** `status = 'active' AND billing_cycle = 'Monthly'`
- **Filter (groups):** SUM over $20,000
- **Sort:** `monthly_mrr` descending

**Self-check:** **2 rows** — **$57,315.00** and **$52,170.00**. The third
region ($10,590.00) is filtered out by HAVING, not by WHERE. Make sure you
understand why it *couldn't* be WHERE.

---

## Question 5 — Top-N: biggest customers

**Business context:** The classic ask — "who are our five biggest
customers?"

**Task:** For **active, monthly-billed** subscriptions, total MRR per
**customer** (a customer can hold several subscriptions — that's why you
group), and return only the top 5.

- **Columns:** `company_name`, `monthly_mrr`
- **Join:** `subscriptions` INNER JOIN `customers` ON `customer_id`
- **Filter:** `status = 'active' AND billing_cycle = 'Monthly'`
- **Group:** `company_name`
- **Sort + limit:** `monthly_mrr` descending, `LIMIT 5`

**Self-check:** **5 rows.** #1 is **$9,275.00**, #5 is **$5,250.00**.

---

## Before you submit

- Run each query and confirm it matches the self-check.
- Branch `submission/sql-05-aggregates`, your `.sql` file(s) in
  `submissions/sql/`, PR with your **actual result numbers** pasted in the
  description.
- In the PR description, also answer in one line each:
  1. When does a query need GROUP BY — and when does it not?
  2. What's the difference between WHERE and HAVING?
- If anything doesn't reconcile, say so in the PR — don't hide a mismatch.
