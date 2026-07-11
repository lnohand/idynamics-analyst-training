# SQL JOINs — Quick Reference

> Companion to SQL 06 (Joins Refresher). The two joins below cover ~99% of
> analyst work.

---

## The Golden Rule

```
INNER JOIN = only rows that match in BOTH tables          (a filter)
LEFT JOIN  = ALL rows from the left table + matches from
             the right — NULL where there's no match      (protective)
```

The question to ask before every join: **"if something on the left has no
match, do I want to see it or not?"** See it → LEFT. Matches only → INNER.

---

## Visual — the SQL 06 lab tables

```
lab_customers                 lab_invoices
customer_id | company         invoice_id | customer_id | amount
------------+---------        -----------+-------------+-------
C1          | Aurora          I1         | C1          | 500
C2          | Borealis        I2         | C1          | 300
C3          | Cascade         I3         | C3          | 450
C4          | Dominion        I4         | C6  ← no such customer
C5          | Evergreen       I5         | C7  ← no such customer
```

| Join | Result | Rows |
|---|---|---|
| INNER | C1×2, C3 — matches only; Borealis/Dominion/Evergreen and I4/I5 vanish | **3** |
| LEFT | all 5 customers; Borealis/Dominion/Evergreen kept with NULL invoice columns | **6** |

---

## Common asks → which join

| Ask | Join |
|---|---|
| "invoices with their customer names" | INNER |
| "all customers with their MRR, including $0" | LEFT |
| "customers with NO purchases" | LEFT + `IS NULL` |
| "only subscriptions that have a matching customer" | INNER |

---

## The IS NULL trick — finding what's missing

Unmatched rows come back with NULL in the right table's columns. Filter on
that NULL and the join becomes an audit:

```sql
-- customers who have never had a subscription
SELECT c.customer_id, c.company_name
FROM customers c
LEFT JOIN subscriptions s ON s.customer_id = c.customer_id
WHERE s.subscription_id IS NULL;
```

**0 rows is a real answer.** "Nothing is missing" is exactly what an audit
wants to hear.

---

## ⚠ THE trap: extra conditions go in ON, not WHERE

With a LEFT JOIN, where you put a filter changes what the query means:

```sql
-- ✅ condition in ON: keep ALL customers; match only their ACTIVE subs
FROM customers c
LEFT JOIN subscriptions s
       ON s.customer_id = c.customer_id AND s.status = 'active'
-- customers with no active sub survive, with NULL sub columns

-- ❌ condition in WHERE: silently becomes an INNER JOIN
FROM customers c
LEFT JOIN subscriptions s ON s.customer_id = c.customer_id
WHERE s.status = 'active'
-- NULL rows can't pass "status = 'active'" (NULL is never equal to
-- anything), so every unmatched customer is thrown away
```

**Rule:** with LEFT JOIN, conditions about the *right* table belong in the
ON clause. WHERE runs *after* the join and executes NULL rows on sight.
(With INNER JOIN placement makes no difference — nothing is NULL — which
is why this bug hides until the data has a gap.)

---

## NULL + aggregates: COALESCE

Unmatched rows make `SUM()` return NULL, and NULL propagates through
arithmetic. Convert at the point of use:

```sql
SELECT c.company_name, COALESCE(SUM(i.amount), 0) AS total_billed
FROM lab_customers c
LEFT JOIN lab_invoices i ON i.customer_id = c.customer_id
GROUP BY c.company_name
ORDER BY total_billed DESC;
-- Borealis/Dominion/Evergreen show 0, not NULL
```

---

## When do LEFT and INNER give identical results?

When every row on the left has at least one match on the right — no
unmatched rows, no NULLs, nothing for LEFT to preserve. That's a fact
about *today's data*, not about your query: **write the join the question
means, not the one that happens to work.**

---

## The other two (rare — for completeness)

- **RIGHT JOIN** — LEFT JOIN with the tables swapped. Analysts almost never
  write it; they reorder the FROM clause and use LEFT, because "keep
  everything from the table I started with" reads top-down.
- **FULL OUTER JOIN** — keeps unmatched rows from *both* sides. Useful when
  neither list is complete — you used it in SQL 02 to line up new-MRR
  months against churn months.

## One-sentence summary

**INNER is a filter; LEFT is protective — choose by deciding whether
unmatched rows deserve to be seen.**
