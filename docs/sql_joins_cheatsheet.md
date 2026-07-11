# SQL JOINs — Quick Reference (all four types)

> Companion to SQL 06 (Join Lab). Consult **after** making your predictions.

---

## The Golden Rules

```
INNER JOIN       = only rows that match in BOTH tables
LEFT JOIN        = ALL rows from the left table  + matches from the right (else NULL)
RIGHT JOIN       = ALL rows from the right table + matches from the left  (else NULL)
FULL OUTER JOIN  = ALL rows from BOTH tables — matched where possible, NULL elsewhere
```

**RIGHT JOIN is just LEFT JOIN with the tables swapped.** Most analysts
never write RIGHT — they reorder the FROM clause and use LEFT, because we
read queries top-down and "keep everything from the table I started with"
is easier to reason about.

---

## Visual — the Join Lab tables

```
lab_customers                 lab_invoices
customer_id | company         invoice_id | customer_id | amount
------------+---------        -----------+-------------+-------
C1          | Aurora          I1         | C1          | 500
C2          | Borealis        I2         | C1          | 300
C3          | Cascade         I3         | C3          | 450
C4          | Dominion        I4         | C6  ← no such customer
C5          | Evergreen       I5         | C7  ← no such customer

Matches: C1↔I1, C1↔I2, C3↔I3
Unmatched left:  C2, C4, C5   (customers, no invoices)
Unmatched right: I4, I5       (invoices, no customer)
```

| Join | Keeps | Rows |
|---|---|---|
| INNER | matches only | **3** |
| LEFT | 3 matches + C2, C4, C5 with NULL invoice | **6** |
| RIGHT | 3 matches + I4, I5 with NULL customer | **5** |
| FULL OUTER | 3 matches + C2, C4, C5 + I4, I5 | **8** |

---

## Decision Tree

```
Which rows must survive the join?
│
├─ Only rows that exist on both sides        → INNER JOIN
│     "invoices with their customer names"
│
├─ Everything from my main table, matched or not → LEFT JOIN
│     "all customers with their MRR, including $0"
│
├─ Everything from the OTHER table              → swap the tables + LEFT
│     (or RIGHT JOIN, same thing)
│
└─ Everything from both sides                   → FULL OUTER JOIN
      "line up new-MRR months with churn months — neither list is complete"
      (you used this in SQL 02's monthly waterfall)
```

---

## The IS NULL trick — finding what's missing

Unmatched rows come back with NULL in the other table's columns. Filter on
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
-- ✅ condition in ON: keep ALL customers; only match their ACTIVE subs
FROM customers c
LEFT JOIN subscriptions s
       ON s.customer_id = c.customer_id AND s.status = 'active'
-- customers with no active sub survive, with NULL sub columns

-- ❌ condition in WHERE: silently becomes an INNER JOIN
FROM customers c
LEFT JOIN subscriptions s ON s.customer_id = c.customer_id
WHERE s.status = 'active'
-- the NULL rows can't pass "status = 'active'" (NULL is never equal
-- to anything), so every unmatched customer is thrown away
```

**Rule:** with LEFT JOIN, conditions about the *right* table belong in the
ON clause. WHERE runs *after* the join and executes NULL rows on sight.
(With INNER JOIN it makes no difference — nothing is NULL — which is why
this bug hides until the data has a gap.)

---

## NULL + aggregates: COALESCE

Unmatched rows make `SUM()` return NULL, and NULL propagates through
arithmetic. Convert at the point of use:

```sql
SELECT c.company_name,
       COALESCE(SUM(s.seats * s.price_per_seat * (1 - s.discount_percent / 100.0)), 0) AS monthly_mrr
FROM customers c
LEFT JOIN subscriptions s
       ON s.customer_id = c.customer_id
      AND s.status = 'active' AND s.billing_cycle = 'Monthly'
GROUP BY c.company_name
ORDER BY monthly_mrr DESC;
```

---

## When do LEFT and INNER give identical results?

When every row on the left has at least one match on the right — no
unmatched rows, no NULLs, nothing for LEFT to preserve. That's a fact
about *today's data*, not about your query: write the join the question
means, not the one that happens to work.

## One-sentence summary

**INNER is a filter. LEFT/RIGHT protect one side. FULL OUTER protects
both. The join you choose is a statement about which missing rows you
care about.**
