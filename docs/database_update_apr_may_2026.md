# Database Update — April & May 2026
### iDynamics Finance Analyst Training Program
*From: David Chen | To: Michael | Student-facing — run these queries in your DB*

---

> Michael — same drill as February and March: before you run each monthly
> close, load that month's activity into the database. Two months are ready,
> but **run them one at a time** — April's block when you close April, May's
> block when you close May. Don't load May early; it will change seat counts
> that throw off your April 30 snapshot.
>
> One housekeeping fix first. — David

---

## Step 0 — Prerequisite: bring SUB012 current (run once, now)

Your March close booked $380 of expansion for SUB012 (Maritime E-commerce —
23 seats → 27 in March). Check whether your database actually reflects it:

```sql
SELECT subscription_id, seats, updated_at
FROM subscriptions
WHERE subscription_id = 'SUB012';
```

If `seats` shows **23**, your DB is behind your own workbook. Bring it current:

```sql
UPDATE subscriptions
SET seats = 27, updated_at = '2026-03-15 00:00:00'
WHERE subscription_id = 'SUB012';

-- log the event if it isn't there yet
INSERT INTO subscription_events
  (event_id, subscription_id, customer_id, event_date, event_type,
   old_value, new_value, field_changed, reason, created_at)
SELECT 'EVT101', 'SUB012', 'CUST012', '2026-03-15', 'seats_change',
       '23', '27', 'seats', 'Team expansion', '2026-03-15'
WHERE NOT EXISTS (SELECT 1 FROM subscription_events WHERE event_id = 'EVT101');
```

**Confirm:** SUB012 now shows 27 seats. Your March 31 snapshot should read
**54 subscriptions | $153,685.50** — if it doesn't, stop and re-check this step
before loading anything below.

---

## Stage 1 — APRIL 2026 (run when you close April)

### Load the data

```sql
-- New customers
INSERT INTO customers (customer_id, company_name, industry, city, province, signup_date, lead_source, account_owner, region, created_at)
VALUES
  ('CUST044', 'Lakeside Retail Group', 'Retail',     'Mississauga', 'ON', '2026-04-09', 'Referral',     'Sarah Chen',        'Central Canada', '2026-04-09 10:20:00'),
  ('CUST045', 'Summit Software Co',    'Technology', 'Kelowna',     'BC', '2026-04-21', 'Demo Request', 'Michael Rodriguez', 'Western Canada', '2026-04-21 15:05:00');

-- New subscriptions
INSERT INTO subscriptions (subscription_id, customer_id, plan_name, seats, price_per_seat, cost_per_seat, billing_cycle, status, start_date, end_date, trial_start_date, trial_end_date, cancelled_date, cancellation_reason, discount_percent, created_at, updated_at)
VALUES
  ('SUB066', 'CUST044', 'Marketing Pro',    18, 85.0, 25.5, 'Monthly', 'active', '2026-04-09', NULL, NULL, NULL, NULL, NULL, 0, '2026-04-09 10:20:00', '2026-04-09 10:20:00'),
  ('SUB067', 'CUST045', 'Analytics Growth', 24, 95.0, 28.5, 'Monthly', 'active', '2026-04-21', NULL, NULL, NULL, NULL, NULL, 0, '2026-04-21 15:05:00', '2026-04-21 15:05:00');

-- Expansion: SUB035 seats 20 -> 24
UPDATE subscriptions SET seats = 24, updated_at = '2026-04-14 00:00:00' WHERE subscription_id = 'SUB035';

-- Cancellation: SUB045
UPDATE subscriptions SET status = 'churned', cancelled_date = '2026-04-24',
  cancellation_reason = 'Price too high', updated_at = '2026-04-24 00:00:00'
WHERE subscription_id = 'SUB045';

-- Events
INSERT INTO subscription_events (event_id, subscription_id, customer_id, event_date, event_type, old_value, new_value, field_changed, reason, created_at)
VALUES
  ('EVT102', 'SUB066', 'CUST044', '2026-04-09', 'created',   NULL,  NULL,  NULL,    NULL,             '2026-04-09'),
  ('EVT103', 'SUB035', 'CUST035', '2026-04-14', 'seats_change', '20', '24', 'seats', 'Team expansion', '2026-04-14'),
  ('EVT104', 'SUB067', 'CUST045', '2026-04-21', 'created',   NULL,  NULL,  NULL,    NULL,             '2026-04-21'),
  ('EVT105', 'SUB045', 'CUST010', '2026-04-24', 'cancelled', 'active','churned','status','Price too high','2026-04-24');
```

### Confirm the load (not the close — these just prove the data landed)

```sql
-- Should return 2 rows: SUB066, SUB067
SELECT subscription_id, customer_id, seats, price_per_seat
FROM subscriptions WHERE start_date BETWEEN '2026-04-01' AND '2026-04-30';

-- SUB035 should show 24 seats; SUB045 should show status 'churned'
SELECT subscription_id, seats, status FROM subscriptions WHERE subscription_id IN ('SUB035','SUB045');
```

**Self-check after your close:** April 30 closing MRR = **$156,830.50** across
**55 subscriptions** (New $3,810, Expansion $440, Churn $1,105). If your snapshot
doesn't hit that, re-check Step 0 and the load before debugging your formulas.

---

## Stage 2 — MAY 2026 (run when you close May — not before)

### Load the data

```sql
-- New customers
INSERT INTO customers (customer_id, company_name, industry, city, province, signup_date, lead_source, account_owner, region, created_at)
VALUES
  ('CUST046', 'Fraser Valley Logistics', 'Transportation', 'Abbotsford', 'BC', '2026-05-07', 'Content Marketing', 'Michael Rodriguez', 'Western Canada', '2026-05-07 09:40:00'),
  ('CUST047', 'Capital Health Partners',  'Healthcare',     'Ottawa',     'ON', '2026-05-19', 'Referral',          'Sarah Chen',        'Central Canada', '2026-05-19 13:55:00');

-- New subscriptions
INSERT INTO subscriptions (subscription_id, customer_id, plan_name, seats, price_per_seat, cost_per_seat, billing_cycle, status, start_date, end_date, trial_start_date, trial_end_date, cancelled_date, cancellation_reason, discount_percent, created_at, updated_at)
VALUES
  ('SUB068', 'CUST046', 'Sales Hub',        21, 110.0, 33.0, 'Monthly', 'active', '2026-05-07', NULL, NULL, NULL, NULL, NULL, 0, '2026-05-07 09:40:00', '2026-05-07 09:40:00'),
  ('SUB069', 'CUST047', 'Analytics Growth', 26,  95.0, 28.5, 'Monthly', 'active', '2026-05-19', NULL, NULL, NULL, NULL, NULL, 0, '2026-05-19 13:55:00', '2026-05-19 13:55:00');

-- Expansion: SUB029 seats 22 -> 27
UPDATE subscriptions SET seats = 27, updated_at = '2026-05-15 00:00:00' WHERE subscription_id = 'SUB029';

-- Contraction: SUB051 seats 23 -> 19  (NEW movement type this month)
UPDATE subscriptions SET seats = 19, updated_at = '2026-05-12 00:00:00' WHERE subscription_id = 'SUB051';

-- Cancellation: SUB026
UPDATE subscriptions SET status = 'churned', cancelled_date = '2026-05-23',
  cancellation_reason = 'Missing features', updated_at = '2026-05-23 00:00:00'
WHERE subscription_id = 'SUB026';

-- Events
INSERT INTO subscription_events (event_id, subscription_id, customer_id, event_date, event_type, old_value, new_value, field_changed, reason, created_at)
VALUES
  ('EVT106', 'SUB068', 'CUST046', '2026-05-07', 'created',      NULL,  NULL,  NULL,    NULL,               '2026-05-07'),
  ('EVT107', 'SUB051', 'CUST014', '2026-05-12', 'seats_change', '23',  '19',  'seats', 'Team downsizing',  '2026-05-12'),
  ('EVT108', 'SUB029', 'CUST029', '2026-05-15', 'seats_change', '22',  '27',  'seats', 'Team expansion',   '2026-05-15'),
  ('EVT109', 'SUB069', 'CUST047', '2026-05-19', 'created',      NULL,  NULL,  NULL,    NULL,               '2026-05-19'),
  ('EVT110', 'SUB026', 'CUST026', '2026-05-23', 'cancelled',    'active','churned','status','Missing features','2026-05-23');
```

### Confirm the load

```sql
-- Should return 2 rows: SUB068, SUB069
SELECT subscription_id, customer_id, seats, price_per_seat
FROM subscriptions WHERE start_date BETWEEN '2026-05-01' AND '2026-05-31';

-- SUB029 -> 27 seats; SUB051 -> 19 seats; SUB026 -> 'churned'
SELECT subscription_id, seats, status FROM subscriptions WHERE subscription_id IN ('SUB029','SUB051','SUB026');
```

**Heads-up — new this month:** SUB051 dropped from 23 to 19 seats. That is a
**contraction** — an existing subscription shrinking, not a cancellation. It is
its own line in the waterfall, separate from churn. Make sure your monthly tab
has a Contraction row; if it only has New / Expansion / Churn, you'll need to
add it.

**Self-check after your close:** May 31 closing MRR = **$160,075.50** across
**56 subscriptions** (New $4,780, Expansion $425, Contraction −$440, Churn
$1,520).

---

## After loading — do your monthly close

This brief only loads the data. The close itself is your usual routine: write
your own snapshot and movement queries, build the month's tab, run variance
against forecast, and write the commentary. Same process you've run for
January, February, and March — new data, same drill.

---

*Verified against the subscription base June 13, 2026 — both months tie to the
self-check totals above. Instructor source: `sql_07_apr_may_2026_inserts.sql`.*
