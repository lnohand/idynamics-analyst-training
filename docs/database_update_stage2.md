# Database Update — Stage 2
## Idynamics Analyst Training | March 2026

---

## Why We're Doing This

So far the `subscriptions` table only stores current state — what a
subscription looks like *right now*. That means we could only ever see
two MRR movements: new subscriptions and cancelled ones. We had no way
of knowing that a customer added seats in March, or upgraded their plan
in August, or got a discount before churning. That history was invisible.

We've now built a `subscription_events` table that logs every change
that ever happened to every subscription — seat increases, plan upgrades,
price changes, discounts, cancellations. With that history, we can
calculate all five MRR movements: New, Expansion, Contraction, Churned,
and Reactivation. That's the full waterfall CFOs and investors expect
to see.

Because the events change what invoices should have looked like at
various points in time, the invoices table has also been regenerated
to be consistent with that history.

---

## Steps — Run in DBeaver in This Order

### Step 1 — Clear the old data

```sql
TRUNCATE invoices;
TRUNCATE subscriptions;
```

`TRUNCATE` deletes every row in a table instantly — it's like
`DELETE FROM table` but faster and cleaner. We do invoices first
because it references subscriptions via a foreign key. If you tried
to truncate subscriptions first, PostgreSQL would refuse — it won't
let you delete a row that another table is still pointing to.

---

### Step 2 — Import subscriptions_v2.csv

Right-click the `subscriptions` table in DBeaver → Import Data → CSV
→ select `subscriptions_v2.csv`.

**Expected:** 62 rows (60 original + 2 returning customers).

---

### Step 3 — Import invoices_v2.csv

Same process → select `invoices_v2.csv`.

**Expected:** 764 rows.

---

### Step 4 — Create the events table

Run this in the SQL editor:

```sql
CREATE TABLE subscription_events (
    event_id        VARCHAR(10)   PRIMARY KEY,
    subscription_id VARCHAR(10)   NOT NULL,
    customer_id     VARCHAR(10)   NOT NULL,
    event_date      DATE          NOT NULL,
    event_type      VARCHAR(50)   NOT NULL,
    old_value       VARCHAR(255),
    new_value       VARCHAR(255),
    field_changed   VARCHAR(50),
    reason          VARCHAR(255),
    created_at      TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
);
```

---

### Step 5 — Import subscription_events.csv

Right-click the new `subscription_events` table → Import Data → CSV
→ select `subscription_events.csv`.

**Expected:** 97 rows.

---

### Step 6 — Verify

```sql
SELECT COUNT(*) FROM subscriptions;        -- expect 62
SELECT COUNT(*) FROM invoices;             -- expect 764
SELECT COUNT(*) FROM subscription_events;  -- expect 97
```

If all three match, you're ready for the MRR analysis.

---

*Idynamics Analyst Training | March 2026*
