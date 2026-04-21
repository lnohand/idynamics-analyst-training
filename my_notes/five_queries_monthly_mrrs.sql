-- ============================================================
-- Jan 2026 Actuals — Verification Queries
-- Run each block separately in DBeaver to confirm every
-- number in the Assignment 06 solution guide.
-- ============================================================


-- ------------------------------------------------------------
-- 1. OPENING MRR — active subscriptions as of Dec 31, 2025
--    Expected: 51 subs | $143,069.50
-- ------------------------------------------------------------
SELECT
    COUNT(*)                                                AS sub_count,
    SUM(
        s.seats
        * s.price_per_seat
        * (1 - s.discount_percent / 100.0)
        * CASE WHEN s.billing_cycle = 'Annual' THEN 1.0 / 12 ELSE 1 END
    )                                                       AS opening_mrr
FROM subscriptions s
WHERE s.start_date     <= '2025-12-31'
  AND (s.cancelled_date IS NULL OR s.cancelled_date > '2025-12-31');


-- ------------------------------------------------------------
-- 2. NEW MRR — subscriptions that started in January 2026
--    Expected: 1 sub | $1,710.00
-- ------------------------------------------------------------
SELECT
    s.subscription_id,
    s.customer_id,
    s.plan_name,
    s.seats,
    s.price_per_seat,
    s.billing_cycle,
    s.seats
        * s.price_per_seat
        * (1 - s.discount_percent / 100.0)
        * CASE WHEN s.billing_cycle = 'Annual' THEN 1.0 / 12 ELSE 1 END AS mrr
FROM subscriptions s
WHERE s.start_date BETWEEN '2026-01-01' AND '2026-01-31'
ORDER BY s.start_date;


-- ------------------------------------------------------------
-- 3. EXPANSION MRR — events that increased MRR in Jan 2026
--    Expected: 0 events | $0.00
-- ------------------------------------------------------------
SELECT
    COUNT(*)                                                AS event_count,
    COALESCE(SUM(
        (CAST(e.new_value AS NUMERIC) - CAST(e.old_value AS NUMERIC))
        * s.price_per_seat
        * (1 - s.discount_percent / 100.0)
        * CASE WHEN s.billing_cycle = 'Annual' THEN 1.0 / 12 ELSE 1 END
    ), 0)                                                   AS expansion_mrr
FROM subscription_events e
JOIN subscriptions s ON e.subscription_id = s.subscription_id
WHERE e.event_date  BETWEEN '2026-01-01' AND '2026-01-31'
  AND e.field_changed = 'seats'
  AND CAST(e.new_value AS NUMERIC) > CAST(e.old_value AS NUMERIC);


-- ------------------------------------------------------------
-- 4. CONTRACTION MRR — events that decreased MRR in Jan 2026
--    Expected: 0 events | $0.00
-- ------------------------------------------------------------
SELECT
    COUNT(*)                                                AS event_count,
    COALESCE(ABS(SUM(
        (CAST(e.new_value AS NUMERIC) - CAST(e.old_value AS NUMERIC))
        * s.price_per_seat
        * (1 - s.discount_percent / 100.0)
        * CASE WHEN s.billing_cycle = 'Annual' THEN 1.0 / 12 ELSE 1 END
    )), 0)                                                  AS contraction_mrr
FROM subscription_events e
JOIN subscriptions s ON e.subscription_id = s.subscription_id
WHERE e.event_date  BETWEEN '2026-01-01' AND '2026-01-31'
  AND e.field_changed = 'seats'
  AND CAST(e.new_value AS NUMERIC) < CAST(e.old_value AS NUMERIC);


-- ------------------------------------------------------------
-- 5. CHURNED MRR — subscriptions cancelled in January 2026
--    Expected: 0 subs | $0.00
-- ------------------------------------------------------------
SELECT
    COUNT(*)                                                AS churned_count,
    COALESCE(SUM(
        s.seats
        * s.price_per_seat
        * (1 - s.discount_percent / 100.0)
        * CASE WHEN s.billing_cycle = 'Annual' THEN 1.0 / 12 ELSE 1 END
    ), 0)                                                   AS churned_mrr
FROM subscriptions s
WHERE s.cancelled_date BETWEEN '2026-01-01' AND '2026-01-31';


-- ------------------------------------------------------------
-- 6. CLOSING MRR — active subscriptions as of Jan 31, 2026
--    Expected: 52 subs | $144,779.50
-- ------------------------------------------------------------
SELECT
    COUNT(*)                                                AS sub_count,
    SUM(
        s.seats
        * s.price_per_seat
        * (1 - s.discount_percent / 100.0)
        * CASE WHEN s.billing_cycle = 'Annual' THEN 1.0 / 12 ELSE 1 END
    )                                                       AS closing_mrr
FROM subscriptions s
WHERE s.start_date     <= '2026-01-31'
  AND (s.cancelled_date IS NULL OR s.cancelled_date > '2026-01-31');


-- ------------------------------------------------------------
-- 7. ACTIVE CUSTOMERS — distinct customers as of Jan 31, 2026
--    Expected: 39 customers
-- ------------------------------------------------------------
SELECT
    COUNT(DISTINCT s.customer_id)                           AS active_customers
FROM subscriptions s
WHERE s.start_date     <= '2026-01-31'
  AND (s.cancelled_date IS NULL OR s.cancelled_date > '2026-01-31');
