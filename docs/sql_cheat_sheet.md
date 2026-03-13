# SQL Cheat Sheet
### Everything You've Learned — With Examples

> All examples use the **Idynamics** database unless noted.
> Reference this doc when you're stuck on syntax — not to copy, but to jog your memory.

---

## Table of Contents

1. [SELECT, FROM, LIMIT](#1-select-from-limit)
2. [WHERE](#2-where)
3. [ORDER BY](#3-order-by)
4. [Aggregates — SUM, COUNT, AVG, MIN, MAX](#4-aggregates)
5. [GROUP BY](#5-group-by)
6. [HAVING](#6-having)
7. [INNER JOIN & LEFT JOIN](#7-joins)
8. [Multi-Table JOIN (3+ tables)](#8-multi-table-join)
9. [CASE WHEN](#9-case-when)
10. [ROUND()](#10-round)
11. [COALESCE](#11-coalesce)
12. [IS NULL / IS NOT NULL](#12-is-null--is-not-null)
13. [COUNT(CASE WHEN)](#13-countcase-when)
14. [String Concatenation — `||`](#14-string-concatenation)
15. [STRING_AGG](#15-string_agg)
16. [Derived Tables (Subquery in FROM)](#16-derived-tables)
17. [CASE WHEN inside SUM / AVG](#17-case-when-inside-sum--avg)
18. [JOIN ON TRUE (Cross Join for Percentages)](#18-join-on-true)
19. [DATE_TRUNC & TO_CHAR](#19-date_trunc--to_char)
20. [Multi-Column GROUP BY](#20-multi-column-group-by)
21. [CTEs — WITH clause](#21-ctes--with-clause)
22. [Window Functions — SUM OVER & LAG](#22-window-functions)
23. [The Filter Consistency Rule](#23-the-filter-consistency-rule)

---

## 1. SELECT, FROM, LIMIT

Pull columns from a table. Use `AS` to rename a column in the output. Use `LIMIT` when exploring.

```sql
SELECT
    customer_id,
    company_name,
    industry AS customer_industry
FROM customers
LIMIT 10;
```

> **Rule:** Always `LIMIT` when exploring a new table. Real tables have millions of rows.

---

## 2. WHERE

Filter rows before returning results. Only rows where the condition is TRUE come through.

```sql
SELECT customer_id, company_name
FROM customers
WHERE industry = 'Technology'
  AND country = 'Canada';
```

**Common operators:**

| Operator | Meaning |
|---|---|
| `=` | Equals |
| `<>` or `!=` | Not equals |
| `>`, `<`, `>=`, `<=` | Comparisons |
| `AND`, `OR`, `NOT` | Combine conditions |
| `IN ('a', 'b')` | Matches any in the list |
| `LIKE 'Tech%'` | Pattern match (`%` = wildcard) |
| `BETWEEN x AND y` | Inclusive range |

---

## 3. ORDER BY

Sort results. `ASC` is the default (smallest → largest). `DESC` reverses it.

```sql
SELECT customer_id, company_name, mrr
FROM subscriptions
ORDER BY mrr DESC;
```

---

## 4. Aggregates

Collapse many rows into a single number.

```sql
SELECT
    COUNT(*)              AS total_customers,
    SUM(mrr)              AS total_mrr,
    AVG(mrr)              AS avg_mrr,
    MIN(mrr)              AS smallest_contract,
    MAX(mrr)              AS largest_contract
FROM subscriptions
WHERE status = 'active';
```

> **`COUNT(*)` vs `COUNT(column)`:** `COUNT(*)` counts all rows. `COUNT(column)` skips NULLs.

---

## 5. GROUP BY

Split rows into groups, then aggregate each group separately.

```sql
SELECT
    billing_cycle,
    COUNT(*)   AS customer_count,
    SUM(mrr)   AS total_mrr
FROM subscriptions
WHERE status = 'active'
GROUP BY billing_cycle;
```

> **Rule:** Every column in SELECT must either be in GROUP BY, or be inside an aggregate function.

---

## 6. HAVING

Filter *after* aggregation. `WHERE` filters rows. `HAVING` filters groups.

```sql
SELECT
    industry,
    COUNT(*) AS customer_count
FROM customers
GROUP BY industry
HAVING COUNT(*) >= 3;
```

> **Mental model:** `WHERE` = filter before grouping. `HAVING` = filter after grouping.

---

## 7. Joins

Combine rows from two tables based on a matching column.

**INNER JOIN** — only rows that match in *both* tables:

```sql
SELECT
    c.company_name,
    s.mrr,
    s.status
FROM customers c
INNER JOIN subscriptions s ON c.customer_id = s.customer_id;
```

**LEFT JOIN** — all rows from the left table, NULLs where there's no match on the right:

```sql
SELECT
    c.company_name,
    s.mrr
FROM customers c
LEFT JOIN subscriptions s ON c.customer_id = s.customer_id;
-- customers with no subscription will appear with NULL mrr
```

> **Key rule:** Always join on the correct key. Joining on the wrong column gives you silent, wrong results.

---

## 8. Multi-Table JOIN (3+ tables)

Chain joins one at a time. Each join adds one more table.

```sql
SELECT
    c.company_name,
    s.mrr,
    s.billing_cycle,
    i.amount,
    i.status AS invoice_status
FROM customers c
INNER JOIN subscriptions s ON c.customer_id = s.customer_id
INNER JOIN invoices i      ON s.subscription_id = i.subscription_id
WHERE s.status = 'active';
```

> **Mental model:** Think of it as building a table left to right. Each JOIN adds more columns.

---

## 9. CASE WHEN

Conditional logic inside a query. Works like an if/else statement.

```sql
SELECT
    company_name,
    mrr,
    CASE
        WHEN mrr >= 2000 THEN 'Enterprise'
        WHEN mrr >= 500  THEN 'Mid-Market'
        ELSE                  'SMB'
    END AS customer_segment
FROM subscriptions
WHERE status = 'active';
```

> SQL checks conditions top to bottom and stops at the first match.

---

## 10. ROUND()

Round a decimal to a specific number of places.

```sql
SELECT
    company_name,
    ROUND(mrr, 2)          AS mrr_rounded,
    ROUND(mrr / 1000.0, 1) AS mrr_in_thousands
FROM subscriptions;
```

> `ROUND(value, decimal_places)` — always specify decimal places explicitly.

---

## 11. COALESCE

Return the first non-NULL value in a list. Use it to replace NULLs with a fallback.

```sql
SELECT
    company_name,
    COALESCE(account_owner, 'Unassigned') AS account_owner
FROM customers;
```

> **Pattern:** `COALESCE(column, 'fallback_if_null')` — very common for display columns.

---

## 12. IS NULL / IS NOT NULL

NULLs can't be caught with `=`. You need `IS NULL` or `IS NOT NULL`.

```sql
-- Find customers with no account owner assigned
SELECT company_name
FROM customers
WHERE account_owner IS NULL;

-- Find customers who DO have an account owner
SELECT company_name
FROM customers
WHERE account_owner IS NOT NULL;
```

> **Critical:** `WHERE column = NULL` never works. Always use `IS NULL`.

---

## 13. COUNT(CASE WHEN)

Count rows that match a condition, without a separate query. Learned in the derived tables lesson.

```sql
SELECT
    billing_cycle,
    COUNT(*)                                          AS total,
    COUNT(CASE WHEN status = 'active' THEN 1 END)    AS active_count,
    COUNT(CASE WHEN status = 'churned' THEN 1 END)   AS churned_count
FROM subscriptions
GROUP BY billing_cycle;
```

> **How it works:** `CASE WHEN` returns `1` when the condition matches, NULL otherwise. `COUNT()` skips NULLs — so you get a count of only the matching rows.

---

## 14. String Concatenation

Join text values together with `||` (SQLite / PostgreSQL syntax).

```sql
SELECT
    first_name || ' ' || last_name AS full_name,
    city || ', ' || country        AS location
FROM customers;
```

> **Watch out for NULLs:** If any part is NULL, the whole result becomes NULL. Wrap in `COALESCE` if needed.

---

## 15. STRING_AGG

Combine multiple rows of text into a single comma-separated string.

```sql
SELECT
    account_owner,
    STRING_AGG(company_name, ', ') AS their_accounts
FROM customers
WHERE account_owner IS NOT NULL
GROUP BY account_owner;
```

> **Use case:** Listing all items in a group as one readable string (e.g., Sarah Chen's accounts).

---

## 16. Derived Tables

A subquery in the `FROM` clause. Gives the inner query a name, so the outer query can use it like a table. Your biggest breakthrough.

```sql
-- Step 1 (inner): Normalize MRR to monthly
-- Step 2 (outer): Aggregate the normalized numbers

SELECT
    billing_cycle,
    SUM(monthly_mrr) AS total_mrr
FROM (
    SELECT
        billing_cycle,
        CASE
            WHEN billing_cycle = 'annual'   THEN mrr / 12.0
            WHEN billing_cycle = 'quarterly' THEN mrr / 3.0
            ELSE mrr
        END AS monthly_mrr
    FROM subscriptions
    WHERE status = 'active'
) AS normalized
GROUP BY billing_cycle;
```

> **Rule:** The inner query runs first. The outer query sees its result as a clean table.

---

## 17. CASE WHEN inside SUM / AVG

Combine conditional logic with aggregation. Used for the MRR normalization formula.

```sql
SELECT
    SUM(
        CASE
            WHEN billing_cycle = 'annual'    THEN mrr / 12.0
            WHEN billing_cycle = 'quarterly' THEN mrr / 3.0
            ELSE mrr
        END
    ) AS normalized_mrr
FROM subscriptions
WHERE status = 'active';
```

> Same logic as a derived table — but collapsed into one query when you only need the total.

---

## 18. JOIN ON TRUE

A controlled cross join. Pairs every row in table A with every row in table B. Used to attach a single total to every row so you can calculate percentages.

```sql
SELECT
    s.billing_cycle,
    COUNT(*)                                AS segment_count,
    totals.grand_total,
    ROUND(COUNT(*) * 100.0 / totals.grand_total, 1) AS pct_of_total
FROM subscriptions s
JOIN (
    SELECT COUNT(*) AS grand_total
    FROM subscriptions
    WHERE status = 'active'
) AS totals ON TRUE
WHERE s.status = 'active'
GROUP BY s.billing_cycle, totals.grand_total;
```

> **When to use it:** Whenever you need to divide by a grand total in the same query. The `ON TRUE` means "always match" — every row gets the total attached.

---

## 19. DATE_TRUNC & TO_CHAR

**`DATE_TRUNC`** — round a date down to the start of a period (month, year, quarter, etc.):

```sql
SELECT
    DATE_TRUNC('month', start_date) AS cohort_month,
    COUNT(*)                         AS new_customers
FROM subscriptions
GROUP BY DATE_TRUNC('month', start_date)
ORDER BY cohort_month;
```

**`TO_CHAR`** — format a date as a readable string:

```sql
SELECT
    TO_CHAR(start_date, 'YYYY-MM') AS month_label,
    COUNT(*)                        AS new_customers
FROM subscriptions
GROUP BY TO_CHAR(start_date, 'YYYY-MM')
ORDER BY month_label;
```

> **Rule of thumb:** Use `DATE_TRUNC` when you need to sort or join on dates. Use `TO_CHAR` when you need a display label.

---

## 20. Multi-Column GROUP BY

Group by more than one column at a time. Every column in SELECT that isn't aggregated must be in GROUP BY.

```sql
SELECT
    c.industry,
    s.billing_cycle,
    COUNT(*)   AS customer_count,
    SUM(s.mrr) AS total_mrr
FROM customers c
INNER JOIN subscriptions s ON c.customer_id = s.customer_id
WHERE s.status = 'active'
GROUP BY c.industry, s.billing_cycle
ORDER BY c.industry, total_mrr DESC;
```

> **Common mistake:** Forgetting to add a column to GROUP BY after adding it to SELECT.

---

## 21. CTEs — WITH Clause

A CTE (Common Table Expression) is a named derived table written at the top of the query. Cleaner and easier to debug than nested subqueries.

```sql
-- Instead of nesting derived tables, name each step with a CTE

WITH active_subs AS (
    SELECT
        customer_id,
        mrr,
        billing_cycle,
        CASE
            WHEN billing_cycle = 'annual'    THEN mrr / 12.0
            WHEN billing_cycle = 'quarterly' THEN mrr / 3.0
            ELSE mrr
        END AS monthly_mrr
    FROM subscriptions
    WHERE status = 'active'
),

by_cycle AS (
    SELECT
        billing_cycle,
        COUNT(*)          AS customer_count,
        SUM(monthly_mrr)  AS total_mrr
    FROM active_subs
    GROUP BY billing_cycle
)

SELECT *
FROM by_cycle
ORDER BY total_mrr DESC;
```

> **Mental model:** A CTE is a derived table with a name. Write each logical step once at the top, then reference it by name below. Chain as many as you need.

---

## 22. Window Functions

Run a calculation *across* rows without collapsing them into a group. The rows stay intact — each one gets a new computed column.

**`SUM() OVER`** — running total:

```sql
SELECT
    month,
    mrr,
    SUM(mrr) OVER (ORDER BY month) AS cumulative_mrr
FROM monthly_mrr
ORDER BY month;
```

**`LAG()`** — look back at the previous row's value:

```sql
SELECT
    month,
    mrr,
    LAG(mrr) OVER (ORDER BY month)                         AS prior_month_mrr,
    mrr - LAG(mrr) OVER (ORDER BY month)                   AS mrr_change,
    ROUND(
        (mrr - LAG(mrr) OVER (ORDER BY month))
        / LAG(mrr) OVER (ORDER BY month) * 100.0
    , 1)                                                   AS pct_change
FROM monthly_mrr
ORDER BY month;
```

> **Key difference from GROUP BY:** `GROUP BY` collapses rows into one. Window functions *keep every row* and add a computed column alongside.

---

## 23. The Filter Consistency Rule

**The most important debugging rule you've learned.**

When you filter in a derived table (or CTE), you must apply the *same filter* in the outer query too — or your denominator and numerator will use different datasets and your percentages will be wrong.

```sql
-- WRONG: filters don't match
SELECT
    billing_cycle,
    COUNT(*) * 100.0 / totals.grand_total AS pct
FROM subscriptions                         -- no filter here
JOIN (
    SELECT COUNT(*) AS grand_total
    FROM subscriptions
    WHERE status = 'active'                -- filter here
) AS totals ON TRUE
GROUP BY billing_cycle, totals.grand_total;

-- CORRECT: same filter in both places
SELECT
    billing_cycle,
    COUNT(*) * 100.0 / totals.grand_total AS pct
FROM subscriptions
JOIN (
    SELECT COUNT(*) AS grand_total
    FROM subscriptions
    WHERE status = 'active'                -- ✅ filter here
) AS totals ON TRUE
WHERE status = 'active'                    -- ✅ and here (WHERE comes after all JOINs)
GROUP BY billing_cycle, totals.grand_total;
```

> **Checklist:** Before submitting any query with a percentage or ratio — ask: "Is the filter in my subquery the same as the filter in my outer query?"

---

## Quick Reference — Clause Execution Order

SQL doesn't run in the order you write it. Knowing this helps you understand error messages.

| Order | Clause | What it does |
|---|---|---|
| 1 | `FROM` / `JOIN` | Identifies the tables and combines them |
| 2 | `WHERE` | Filters rows (before grouping) |
| 3 | `GROUP BY` | Splits into groups |
| 4 | `HAVING` | Filters groups (after grouping) |
| 5 | `SELECT` | Picks columns and runs aggregates |
| 6 | `ORDER BY` | Sorts the final result |
| 7 | `LIMIT` | Cuts the result to N rows |

> This is why you can't use a SELECT alias in a WHERE clause — WHERE runs before SELECT.

---

*Last updated: March 2026*
