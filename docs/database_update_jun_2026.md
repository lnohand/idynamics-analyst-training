# Database Update — June 2026
### iDynamics Finance Analyst Training Program
*From: David Chen | To: Michael | Student-facing — run this once in DBeaver*

---

> Michael — June's activity is ready to load. Finish and commit your May workbook
> first. May's list is already saved in `closes/2026-05/`, so loading June can't
> change it. Run the whole block below once, then run the check at the end. — David

---

```sql
-- ============================================================
-- June 2026 — load into Neon PostgreSQL
--
-- Run this ONCE, in DBeaver, when David says June's data is ready to load.
-- Run the whole file top to bottom. Then run the check at the end.
--
-- ⚠ Only run this if May is loaded and nothing after it. Check first:
--      SELECT COUNT(*) FROM subscriptions;               -- must be 69
--      SELECT MAX(event_date) FROM subscription_events;  -- must be 2026-05-23
--    If those don't match, stop and message David.
-- ============================================================


-- ============================================================
-- STEP 1 — two new customers
-- ============================================================
INSERT INTO customers (customer_id, company_name, industry, city, province,
                       signup_date, lead_source, account_owner, region, created_at)
VALUES
  ('CUST048', 'Lakeshore Property Group', 'Real Estate', 'Hamilton', 'ON',
   '2026-06-09', 'Paid Search', 'Jennifer Lee', 'Central Canada', '2026-06-09 10:20:00'),
  ('CUST049', 'Northern Lights Energy', 'Energy', 'Calgary', 'AB',
   '2026-06-26', 'Sales Outreach', 'Michael Rodriguez', 'Western Canada', '2026-06-26 15:05:00');


-- ============================================================
-- STEP 2 — three new subscriptions
-- ============================================================
INSERT INTO subscriptions (
  subscription_id, customer_id, plan_name, seats, price_per_seat, cost_per_seat,
  billing_cycle, status, start_date, end_date, trial_start_date, trial_end_date,
  cancelled_date, cancellation_reason, discount_percent, created_at, updated_at
)
VALUES
  ('SUB070', 'CUST048', 'Sales Hub',            22, 110.0, 33.0, 'Monthly', 'active',
   '2026-06-09', NULL, NULL, NULL, NULL, NULL, 0,
   '2026-06-09 10:20:00', '2026-06-09 10:20:00'),
  ('SUB071', 'CUST040', 'Marketing Pro',        14,  85.0, 25.5, 'Monthly', 'active',
   '2026-06-16', NULL, NULL, NULL, NULL, NULL, 0,
   '2026-06-16 11:30:00', '2026-06-16 11:30:00'),
  ('SUB072', 'CUST049', 'Analytics Enterprise', 20, 180.0, 54.0, 'Monthly', 'active',
   '2026-07-01', NULL, NULL, NULL, NULL, NULL, 0,
   '2026-06-26 15:05:00', '2026-06-26 15:05:00');


-- ============================================================
-- STEP 3 — changes to existing subscriptions
-- ============================================================

UPDATE subscriptions
SET seats = 40, updated_at = '2026-06-10 00:00:00'
WHERE subscription_id = 'SUB037';

UPDATE subscriptions
SET seats = 12, updated_at = '2026-06-18 00:00:00'
WHERE subscription_id = 'SUB020';

UPDATE subscriptions
SET discount_percent = 10, updated_at = '2026-06-20 00:00:00'
WHERE subscription_id = 'SUB037';

UPDATE subscriptions
SET status = 'cancelled',
    cancelled_date = '2026-06-25',
    end_date = '2026-06-25',
    cancellation_reason = 'Switched to competitor',
    updated_at = '2026-06-25 00:00:00'
WHERE subscription_id = 'SUB028';


-- ============================================================
-- STEP 4 — the event log
-- ============================================================
INSERT INTO subscription_events (
  event_id, subscription_id, customer_id, event_date,
  event_type, old_value, new_value, field_changed, reason, created_at
)
VALUES
  ('EVT111', 'SUB070', 'CUST048', '2026-06-09',
   'created', NULL, NULL, NULL, NULL, '2026-06-09'),
  ('EVT112', 'SUB037', 'CUST037', '2026-06-10',
   'seats_change', '35', '40', 'seats', 'Team expansion', '2026-06-10'),
  ('EVT113', 'SUB071', 'CUST040', '2026-06-16',
   'created', NULL, NULL, NULL, NULL, '2026-06-16'),
  ('EVT114', 'SUB020', 'CUST020', '2026-06-18',
   'seats_change', '15', '12', 'seats', 'Team downsizing', '2026-06-18'),
  ('EVT115', 'SUB037', 'CUST037', '2026-06-20',
   'discount_added', '0', '10', 'discount_percent', 'Volume discount on seat expansion', '2026-06-20'),
  ('EVT116', 'SUB028', 'CUST028', '2026-06-25',
   'cancelled', 'active', 'cancelled', 'status', 'Switched to competitor', '2026-06-25');


-- ============================================================
-- STEP 5 — CHECK IT LOADED. Expected: 49 | 72 | 116 | 2026-06-25
-- ============================================================
SELECT (SELECT COUNT(*) FROM customers)                 AS customers,
       (SELECT COUNT(*) FROM subscriptions)             AS subscriptions,
       (SELECT COUNT(*) FROM subscription_events)       AS events,
       (SELECT MAX(event_date) FROM subscription_events) AS latest_event;

-- If you see 49 | 72 | 116 | 2026-06-25, June is loaded. Tell David.
-- If you ran this file twice you'll get duplicate-key errors on the INSERTs —
-- that's the database protecting you. Nothing was loaded twice.
```
