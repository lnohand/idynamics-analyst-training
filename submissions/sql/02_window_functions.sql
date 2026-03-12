
```sql
-- SQL 02: Window Functions
-- Submitted by: Michael
-- Date: March 11th 2026

-- Practice 1
select subscription_id, plan_name, billing_cycle, seats, price_per_seat, case when status = 'active' then 'Active' else 'Inactive' end as status_label from subscriptions group by subscription_id  order by status_label, plan_name;

-- Practice 2
select billing_cycle,count(subscription_id) as subscription_count,
ROUND(SUM(case WHEN billing_cycle = 'Annual' THEN seats * price_per_seat * (1 - discount_percent / 100.0) / 12 else seats * price_per_seat * (1 - discount_percent / 100.0) END), 2) AS new_mrr
FROM subscriptions GROUP BY billing_cycle ORDER BY new_mrr desc;

-- Practice 3
select plan_name, count(subscription_id) as churned_subscriptions, ROUND(SUM(case WHEN billing_cycle = 'Annual' THEN seats * price_per_seat * (1 - discount_percent / 100.0) / 12 else seats * price_per_seat * (1 - discount_percent / 100.0) END), 2) AS churned_mrr
from subscriptions where cancelled_date is not null group by plan_name order by churned_mrr desc;
