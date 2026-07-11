# SQL Assignment 06: Joins Refresher — INNER vs LEFT
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** A 30-minute join tune-up
>
> Reviewing SQL 05 I noticed you used LEFT JOIN where the task called for
> INNER — and it *happened* to give identical results. That's luck, not
> correctness, and the day the data has a gap the wrong join silently
> gives a wrong answer. It's been a while since you worked with joins
> daily, so here's a short refresher: the concept first, shown end to
> end, then four quick exercises. In practice INNER and LEFT cover ~99%
> of analyst work, so that's all we do here.
>
> — David

---

## The concept, shown once

Two tiny throwaway tables. Create them in your database — paste as-is:

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

Note what's lopsided about this data: **C2, C4, C5 have no invoices**, and
**I4, I5 point at customers that don't exist** (imported from the old
billing system, say).

**INNER JOIN = only rows that match on both sides.** Run it:

```sql
SELECT c.customer_id, c.company_name, i.invoice_id, i.amount
FROM lab_customers c
INNER JOIN lab_invoices i ON i.customer_id = c.customer_id;
```

```
customer_id | company_name     | invoice_id | amount
------------+------------------+------------+-------
C1          | Aurora Analytics | I1         | 500
C1          | Aurora Analytics | I2         | 300
C3          | Cascade Retail   | I3         | 450
```

3 rows. Borealis, Dominion, Evergreen are **gone** — no invoice, no row.
The orphan invoices I4/I5 are gone too. INNER JOIN is a *filter*.

**LEFT JOIN = every row from the left table survives; where there's no
match, the right side comes back as NULL.** Same query, one word changed:

```sql
SELECT c.customer_id, c.company_name, i.invoice_id, i.amount
FROM lab_customers c
LEFT JOIN lab_invoices i ON i.customer_id = c.customer_id;
```

```
customer_id | company_name     | invoice_id | amount
------------+------------------+------------+-------
C1          | Aurora Analytics | I1         | 500
C1          | Aurora Analytics | I2         | 300
C2          | Borealis Media   | NULL       | NULL
C3          | Cascade Retail   | I3         | 450
C4          | Dominion Freight | NULL       | NULL
C5          | Evergreen Health | NULL       | NULL
```

6 rows. Nobody vanished — the customers with no invoices are kept, with
NULLs. LEFT JOIN is *protective*.

**That's the whole difference.** The question to ask before every join:
*"if something on the left has no match, do I want to see it or not?"*
Want to see it → LEFT. Only care about matches → INNER.

Two working consequences of those NULLs:

1. **The IS NULL trick:** filter `WHERE i.invoice_id IS NULL` on the LEFT
   JOIN above and you get exactly the customers with no invoices — the
   unmatched rows. A LEFT JOIN plus IS NULL is an audit.
2. **⚠ The trap — extra conditions go in ON, not WHERE.** If you want
   "all customers, matched only against their *large* invoices", the
   `amount > 400` condition must live in the ON clause:
   `LEFT JOIN lab_invoices i ON i.customer_id = c.customer_id AND i.amount > 400`.
   Put it in WHERE instead and the NULL rows get executed on sight
   (NULL is never `> 400`) — your LEFT JOIN silently becomes an INNER
   JOIN. This exact bug is what happened in your SQL 05 Q5.

(There are two more types — RIGHT JOIN, which is just LEFT with the tables
swapped, and FULL OUTER JOIN, which keeps unmatched rows from *both* sides;
you used that one in SQL 02's waterfall. Both are rare in practice. Details
in `docs/sql_joins_cheatsheet.md` if you're curious.)

---

## Now you — four quick exercises

Same rules as SQL 06 onward: business ask + self-check, no how-hints. The
concept section above is all you need.

### Exercise 1 — on the lab tables
Sales wants to call every customer who has never received an invoice.
Who are they?

**Self-check: 3 rows.**

### Exercise 2 — real database
Data-quality check: do we have any customer on the books with no
subscription history at all — not even a cancelled one?

**Self-check: 0 rows** — and that empty result *is* the answer: nothing is
unmatched. It's also exactly why your SQL 05 LEFT JOINs matched the INNER
results. **In the PR, one line:** when do LEFT and INNER return identical
results?

### Exercise 3 — real database
Customer success wants the win-back list: which customers currently have
**no active subscription**? They need company names to call.

**Self-check: exactly 1 row** — a company from Eastern Canada. If you get
0 rows, re-read the trap in the concept section; don't explain the
mismatch away.

Then: your query has an `active` condition somewhere. **Move it to the
other possible place (ON ↔ WHERE), run again, and paste both row counts in
the PR with one line on why they differ.**

### Exercise 4 — redo of SQL 05 Q5, done right
The board question was never "top 5" — it's **all 45 customers with their
active monthly-billed MRR, including the $0 ones**, highest first. The $0
customers must show a real `0` the board can read, not a blank.

**Self-check:** 45 rows; top customer **$9,275.00**; the column sums to
**$120,075.00** (same monthly book as SQL 05 — it must still tie);
**exactly 3 customers show $0**. **In the PR, one line:** those three $0
customers are not the same story — one has nothing active at all, but
something different is true of the other two. What?

---

## Cleanup

```sql
DROP TABLE lab_customers;
DROP TABLE lab_invoices;
```

## Submission

- Branch `submission/sql-06-join-lab`, file
  `submissions/sql/06_sql_join_lab.sql`.
- PR description: your actual row counts for every exercise, Exercise 3's
  two counts, and the three one-liners (Ex 2, Ex 3, Ex 4).
- If anything doesn't reconcile, say so in the PR — don't hide a mismatch.
