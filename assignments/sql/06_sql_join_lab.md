# SQL Assignment 06: The Join Lab — INNER / LEFT / RIGHT / FULL OUTER
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Why your LEFT JOINs "worked" — and why that was luck
>
> In SQL 05 you used LEFT JOIN where the task called for INNER, and got
> identical results. That wasn't correct — it was lucky: our data happens
> to have no unmatched rows on that key, so the two joins collapse into
> the same thing. The day the data has a gap, the wrong join silently
> gives a wrong answer. This lab makes the four join types produce four
> *different* answers, so you can see exactly what each one keeps and
> drops. Then we use the right ones on the real database.
>
> Format is different this time: for Q1 you **predict before you run**.
> Write your predictions down first — that's the deliverable I care about.
>
> There's a reference at `docs/sql_joins_cheatsheet.md`. Rule: consult it
> **after** you've made your predictions, not before.
>
> — David

---

## Question 1 — Build the lab, predict, then run

Create these two throwaway tables in your database — paste exactly as-is
(this setup is given; the exercise starts after it):

```sql
CREATE TABLE lab_customers (customer_id TEXT, company_name TEXT);
INSERT INTO lab_customers VALUES
  ('C1','Aurora Analytics'), ('C2','Borealis Media'), ('C3','Cascade Retail'),
  ('C4','Dominion Freight'), ('C5','Evergreen Health');

CREATE TABLE lab_invoices (invoice_id TEXT, customer_id TEXT, amount NUMERIC);
INSERT INTO lab_invoices VALUES
  ('I1','C1',500), ('I2','C1',300), ('I3','C3',450),
  ('I4','C6',700), ('I5','C7',250);
```

Study the data for a minute: some customers have no invoices, some have
two, and two invoices point at customers that don't exist (imported from
the old billing system, say).

**Before running anything, write down in your `.sql` file as a comment: how
many rows will each of these four queries return?**

```sql
SELECT * FROM lab_customers c INNER JOIN lab_invoices i ON c.customer_id = i.customer_id;
SELECT * FROM lab_customers c LEFT JOIN lab_invoices i ON c.customer_id = i.customer_id;
SELECT * FROM lab_customers c RIGHT JOIN lab_invoices i ON c.customer_id = i.customer_id;
SELECT * FROM lab_customers c FULL OUTER JOIN lab_invoices i ON c.customer_id = i.customer_id;
```

Then run all four. **In the PR description, paste a small table: join type,
your predicted count, actual count — plus one sentence per join naming
exactly which rows appeared or vanished and why.** If any prediction was
wrong, that sentence is where you work out what you'd missed. (Now is when
the cheatsheet earns its keep.)

**Self-check:** the four actual counts are all different, and they are
**3, 6, 5, 8** in the order listed above.

---

## Question 2 — The audit question (this is what RIGHT/OUTER joins are for)

Write a query that returns the invoices whose `customer_id` does not exist
in `lab_customers` — return exactly three columns: `invoice_id`,
`customer_id`, `amount`.

**Self-check:** 2 rows — I4 and I5, amounts totalling **$950**.

**In the PR, one line:** you can write this with a RIGHT JOIN from
`lab_customers`, or as a LEFT JOIN with the tables swapped. Why are those
the same query — and which one would you rather read?

---

## Question 3 — Real database: is anything unmatched?

Write a query that returns any customer in `customers` that has **zero
rows at all** in `subscriptions` — return exactly `customer_id`,
`company_name`.

**Self-check: 0 rows.** That empty result is not a broken query — it *is*
the answer, and it's the exact reason your SQL 05 LEFT JOINs matched the
INNER results. **In the PR, one line:** state the rule for when LEFT JOIN
and INNER JOIN return identical results.

---

## Question 4 — Real database: who has no ACTIVE subscription?

Now the question that actually bites. Write a query returning every
customer with **no active subscription** — exactly `customer_id`,
`company_name`. You'll need a LEFT JOIN, the IS NULL trick, and the
`status = 'active'` condition placed **in the ON clause**.

**Self-check: exactly 1 row.** It's a company from Eastern Canada.

Then run the variant with `status = 'active'` moved to the WHERE clause
instead, and note its row count. **In the PR, paste both row counts and
one line explaining the difference** — this is the single most common
LEFT JOIN bug in real analyst work, and it's also what quietly happened
in your SQL 05 Q5.

---

## Question 5 — Redo of SQL 05 Q5, done right

"Top customers" hid the zeros. The board question is really: **all 45
customers with their active monthly-billed MRR, including the ones at
$0** — return exactly `company_name`, `monthly_mrr`, highest first, no
LIMIT. Zeros must show as `0`, not NULL (COALESCE), and both the
`status = 'active'` and `billing_cycle = 'Monthly'` conditions belong in
the ON clause — think about why.

**Self-check:** **45 rows**; top customer **$9,275.00**; the whole column
sums to **$120,075.00** (same monthly book as SQL 05 — it must still tie);
and **exactly 3 customers show $0**.

**In the PR, one line:** those three $0 customers are not the same story.
One of them genuinely has nothing active — which one? — and something
different is true of the other two. What is it? (Hint: it's a column
you've been filtering on all assignment.)

---

## Cleanup

When you're done, drop the lab tables so the database stays canonical for
future assignments:

```sql
DROP TABLE lab_customers;
DROP TABLE lab_invoices;
```

## Submission

- Branch `submission/sql-06-join-lab`, file
  `submissions/sql/06_sql_join_lab.sql` (predictions included as comments).
- PR description must contain: the Q1 predicted-vs-actual table with your
  four sentences, the Q2/Q3/Q4/Q5 one-liners, Q4's two row counts, and
  your actual Q5 top-5 values.
- If anything doesn't reconcile, say so in the PR — don't hide a mismatch.
