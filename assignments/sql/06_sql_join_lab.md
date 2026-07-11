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
> Format is different this time, and it's how assignments will work from
> now on: **you get the business ask and a self-check — no column lists,
> no "use this clause" hints.** In real life nobody tells you which
> columns to use; you get the right data for the ask, and the self-check
> tells you whether you did. For Q1 specifically, you **predict before
> you run** — write your predictions down first; that's the deliverable
> I care about.
>
> There's a reference at `docs/sql_joins_cheatsheet.md`. Rule: consult it
> **after** you've attempted, not before.
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

Finance needs to chase the bad invoices from the old billing system: which
invoices point at a customer that doesn't exist? They'll need to know which
invoice, who it claims to bill, and for how much.

**Self-check:** 2 rows — I4 and I5, amounts totalling **$950**.

**In the PR, one line:** you can write this with a RIGHT JOIN from
`lab_customers`, or as a LEFT JOIN with the tables swapped. Why are those
the same query — and which one would you rather read?

---

## Question 3 — Real database: is anything unmatched?

Data-quality check on our real tables: do we have any customer on the
books with no subscription history at all — not even a cancelled one?

**Self-check: 0 rows.** That empty result is not a broken query — it *is*
the answer, and it's the exact reason your SQL 05 LEFT JOINs matched the
INNER results. **In the PR, one line:** state the rule for when LEFT JOIN
and INNER JOIN return identical results.

---

## Question 4 — Real database: who has no ACTIVE subscription?

Now the question that actually bites. Customer success wants the win-back
list: **which customers have no active subscription?** They need to know
who to call, so identify the company, not just an ID.

**Self-check: exactly 1 row.** It's a company from Eastern Canada. If you
get 0 rows, the self-check is telling you your query is wrong — don't
explain it away; the cheatsheet's trap section is your friend.

Once you have the 1-row version: your query has an `active` condition
somewhere. **Move that condition to the other possible place (ON clause ↔
WHERE clause), run it again, and paste both row counts in the PR with one
line explaining the difference.** This is the single most common LEFT JOIN
bug in real analyst work — and it's what quietly happened in your
SQL 05 Q5.

---

## Question 5 — Redo of SQL 05 Q5, done right

"Top customers" hid the zeros. The board question is really: **all 45
customers with their active monthly-billed MRR, including the ones at $0**
— highest first, and the $0 customers must show an actual `0` the board
can read, not a blank or NULL. Q4 just taught you the trap this question
is built on; this is where you prove the lesson transferred.

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
