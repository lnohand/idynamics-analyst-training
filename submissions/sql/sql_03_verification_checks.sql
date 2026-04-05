-- SQL 03 — Verification Checks
-- Run each block in order. Paste the results as a comment on the PR.
-- All checks must pass before this PR can be merged.

-- ============================================================
-- STEP 1 — Database Cleanup Verification
-- Run these first. If any fail, run the cleanup UPDATEs from
-- the feedback file before proceeding.
-- ============================================================

-- 1a. Should return 0 rows. If any rows appear, run the cleanup UPDATE first.
SELECT subscription_id, status
FROM subscriptions
WHERE status = 'churned';

-- 1b. Should return exactly: active = 51, cancelled = 11
SELECT status, COUNT(*) AS count
FROM subscriptions
GROUP BY status
ORDER BY status;

-- 1c. Every cancelled event must show new_value = 'cancelled' (not 'churned')
SELECT event_id, event_type, new_value
FROM subscription_events
WHERE event_type = 'cancelled'
ORDER BY event_id;

-- ============================================================
-- STEP 2 — Query 1: MRR Snapshot
-- Run your mrr_snapshot.sql, then run these against the results.
-- ============================================================

-- 2a. Row count — expected: 51
SELECT COUNT(*) AS row_count
FROM (
    SELECT
        s.subscription_id,
        s.customer_id,
        c.company_name,
        c.account_owner,
        c.region,
        s.plan_name,
        s.billing_cycle,
        CASE
            WHEN s.billing_cycle = 'Monthly' THEN ROUND(s.seats * s.price_per_seat * (1 - s.discount_percent / 100.0), 2)
            WHEN s.billing_cycle = 'Annual'  THEN ROUND(s.seats * s.price_per_seat * (1 - s.discount_percent / 100.0) / 12, 2)
        END AS mrr
    FROM subscriptions s
    INNER JOIN customers c ON s.customer_id = c.customer_id
    WHERE s.status = 'active'
) snapshot;

-- 2b. SUM of MRR — expected: $144,185.50
SELECT ROUND(SUM(mrr), 2) AS total_mrr
FROM (
    SELECT
        CASE
            WHEN s.billing_cycle = 'Monthly' THEN ROUND(s.seats * s.price_per_seat * (1 - s.discount_percent / 100.0), 2)
            WHEN s.billing_cycle = 'Annual'  THEN ROUND(s.seats * s.price_per_seat * (1 - s.discount_percent / 100.0) / 12, 2)
        END AS mrr
    FROM subscriptions s
    WHERE s.status = 'active'
) snapshot;

-- 2c. Region values — expected: Eastern Canada, Western Canada, Central Canada (3 distinct)
SELECT DISTINCT c.region
FROM subscriptions s
INNER JOIN customers c ON s.customer_id = c.customer_id
WHERE s.status = 'active'
ORDER BY c.region;

-- ============================================================
-- STEP 3 — Query 2: Events Export
-- Run your mrr_events.sql, then verify with these.
-- ============================================================

-- 3a. Row count — expected: 97
SELECT COUNT(*) AS row_count
FROM subscription_events;

-- 3b. Distinct event types — expected: 7 types
-- (created, seats_change, price_change, plan_upgrade, plan_downgrade, discount_added, cancelled)
SELECT event_type, COUNT(*) AS count
FROM subscription_events
GROUP BY event_type
ORDER BY event_type;

-- 3c. Confirm seats column is in the subscriptions table (sanity check)
SELECT column_name
FROM information_schema.columns
WHERE table_name = 'subscriptions'
  AND column_name = 'seats';

-- 3d. Date range — expected: earliest 2024-01-08, latest 2026-02-20
SELECT MIN(event_date) AS earliest, MAX(event_date) AS latest
FROM subscription_events;

-- ============================================================
-- STEP 4 — Query 3: Monthly Revenue Trend
-- NOTE: Your submitted mrr_trend.sql is a copy of mrr_snapshot.sql.
-- This needs to be rewritten as the CTE + window functions query.
-- Run the correct query below and verify the results.
-- ============================================================

-- 4a. The correct Query 3 structure — run this and verify all checks pass:
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', payment_date) AS month,
        COUNT(*) AS invoice_count,
        SUM(subtotal) AS revenue
    FROM invoices
    WHERE payment_status = 'paid'
    GROUP BY DATE_TRUNC('month', payment_date)
)
SELECT
    TO_CHAR(month, 'YYYY-MM') AS month,
    invoice_count,
    ROUND(revenue, 2) AS revenue,
    ROUND(SUM(revenue) OVER (ORDER BY month), 2) AS running_total,
    ROUND(LAG(revenue) OVER (ORDER BY month), 2) AS prev_month_revenue,
    ROUND(
        (revenue - LAG(revenue) OVER (ORDER BY month))
        / LAG(revenue) OVER (ORDER BY month) * 100
    , 1) AS mom_pct_change
FROM monthly_revenue
ORDER BY month;

-- 4b. Row count — expected: 26
-- 4c. First row month — expected: 2024-01
-- 4d. Last row running_total — expected: $2,475,630.00
-- 4e. First row prev_month_revenue — expected: NULL
-- 4f. First row mom_pct_change — expected: NULL

-- Run this to confirm the last row:
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', payment_date) AS month,
        COUNT(*) AS invoice_count,
        SUM(subtotal) AS revenue
    FROM invoices
    WHERE payment_status = 'paid'
    GROUP BY DATE_TRUNC('month', payment_date)
)
SELECT
    TO_CHAR(month, 'YYYY-MM') AS month,
    ROUND(SUM(revenue) OVER (ORDER BY month), 2) AS running_total
FROM monthly_revenue
ORDER BY month DESC
LIMIT 1;
-- Expected: 2026-02 | $2,475,630.00
