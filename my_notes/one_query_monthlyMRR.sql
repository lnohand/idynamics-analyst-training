-- ============================================================
-- Jan 2026 MRR Waterfall — Actuals
-- Idynamics Finance Analyst Training Program
-- Excel Assignment 06 — Actual vs Forecast: January 2026
-- ============================================================
--
-- Purpose: Calculate every MRR waterfall movement for January
--          2026 to populate the Actual column in the A vs F tab.
--
-- Self-check:
--   Opening MRR  → $143,069.50  (51 active subs, Dec 31)
--   + New MRR    →   $1,710.00  (1 new subscription)
--   + Expansion  →       $0.00  (no expansion events in Jan)
--   − Contraction→       $0.00  (no contraction events)
--   − Churned    →       $0.00  (no cancellations in Jan)
--   Closing MRR  → $144,779.50  (52 active subs, Jan 31)
-- ============================================================

WITH

-- ----------------------------------------------------------
-- MRR formula in one place — used by every CTE below
-- Annual plans store annual price_per_seat; divide by 12
-- ----------------------------------------------------------
sub_mrr AS (
    SELECT
        s.subscription_id,
        s.customer_id,
        s.plan_name,
        s.billing_cycle,
        s.start_date,
        s.cancelled_date,
        ROUND(
            s.seats
            * s.price_per_seat
            * (1 - s.discount_percent / 100.0)
            * CASE WHEN s.billing_cycle = 'Annual' THEN 1.0 / 12 ELSE 1 END
        , 2) AS mrr
    FROM subscriptions s
),

-- ----------------------------------------------------------
-- Opening: active subscriptions as of Dec 31, 2025
-- ----------------------------------------------------------
opening AS (
    SELECT
        COUNT(*)   AS sub_count,
        SUM(mrr)   AS opening_mrr
    FROM sub_mrr
    WHERE start_date     <= '2025-12-31'
      AND (cancelled_date IS NULL OR cancelled_date > '2025-12-31')
),

-- ----------------------------------------------------------
-- New MRR: subscriptions that first started in January 2026
-- ----------------------------------------------------------
new_mrr AS (
    SELECT
        COUNT(*)   AS new_count,
        SUM(mrr)   AS new_mrr
    FROM sub_mrr
    WHERE start_date BETWEEN '2026-01-01' AND '2026-01-31'
),

-- ----------------------------------------------------------
-- Expansion MRR: events that increased MRR in January 2026
-- Covers: seats added, plan upgrades, price increases
-- MRR delta = (new_seats − old_seats) × price_per_seat
-- Only seats_change handled here; plan/price changes follow
-- the same pattern with their respective field_changed value
-- ----------------------------------------------------------
expansion AS (
    SELECT
        COALESCE(SUM(
            (CAST(e.new_value AS NUMERIC) - CAST(e.old_value AS NUMERIC))
            * s.price_per_seat
            * (1 - s.discount_percent / 100.0)
            * CASE WHEN s.billing_cycle = 'Annual' THEN 1.0 / 12 ELSE 1 END
        ), 0) AS expansion_mrr
    FROM subscription_events e
    JOIN subscriptions s ON e.subscription_id = s.subscription_id
    WHERE e.event_date  BETWEEN '2026-01-01' AND '2026-01-31'
      AND e.event_type  IN ('seats_change', 'plan_upgrade', 'price_change')
      AND e.field_changed = 'seats'
      AND CAST(e.new_value AS NUMERIC) > CAST(e.old_value AS NUMERIC)
),

-- ----------------------------------------------------------
-- Contraction MRR: events that decreased MRR in January 2026
-- Covers: seats removed, plan downgrades, discounts added
-- ----------------------------------------------------------
contraction AS (
    SELECT
        COALESCE(ABS(SUM(
            (CAST(e.new_value AS NUMERIC) - CAST(e.old_value AS NUMERIC))
            * s.price_per_seat
            * (1 - s.discount_percent / 100.0)
            * CASE WHEN s.billing_cycle = 'Annual' THEN 1.0 / 12 ELSE 1 END
        )), 0) AS contraction_mrr
    FROM subscription_events e
    JOIN subscriptions s ON e.subscription_id = s.subscription_id
    WHERE e.event_date  BETWEEN '2026-01-01' AND '2026-01-31'
      AND e.event_type  IN ('seats_change', 'plan_downgrade', 'discount_added')
      AND e.field_changed = 'seats'
      AND CAST(e.new_value AS NUMERIC) < CAST(e.old_value AS NUMERIC)
),

-- ----------------------------------------------------------
-- Churned MRR: subscriptions cancelled in January 2026
-- Use MRR at the time of cancellation (pre-cancel snapshot)
-- ----------------------------------------------------------
churned AS (
    SELECT
        COUNT(*)   AS churned_count,
        SUM(mrr)   AS churned_mrr
    FROM sub_mrr
    WHERE cancelled_date BETWEEN '2026-01-01' AND '2026-01-31'
),

-- ----------------------------------------------------------
-- Closing: active subscriptions as of Jan 31, 2026
-- ----------------------------------------------------------
closing AS (
    SELECT
        COUNT(*)   AS sub_count,
        SUM(mrr)   AS closing_mrr
    FROM sub_mrr
    WHERE start_date     <= '2026-01-31'
      AND (cancelled_date IS NULL OR cancelled_date > '2026-01-31')
)

-- ----------------------------------------------------------
-- Final output — one row, all waterfall movements
-- ----------------------------------------------------------
SELECT
    o.sub_count                                                AS opening_subs,
    o.opening_mrr,

    n.new_count,
    n.new_mrr,

    ex.expansion_mrr,
    ct.contraction_mrr,

    ch.churned_count,
    ch.churned_mrr,

    n.new_mrr
        + ex.expansion_mrr
        - ct.contraction_mrr
        - ch.churned_mrr                                       AS net_new_mrr,

    cl.closing_mrr,
    cl.sub_count                                               AS closing_subs

FROM opening     o
JOIN new_mrr     n  ON TRUE
JOIN expansion   ex ON TRUE
JOIN contraction ct ON TRUE
JOIN churned     ch ON TRUE
JOIN closing     cl ON TRUE;
