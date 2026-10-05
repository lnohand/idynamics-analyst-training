-- Step 1
select 
sum(
case 
	when billing_cycle = 'Annual' then round(seats*price_per_seat/12 * (1 - discount_percent / 100), 2)
	when billing_cycle = 'Monthly' then round(seats*price_per_seat * (1 - discount_percent / 100), 2)
end) as total_mrr, count(subscription_id) as subscription_count, count(distinct customer_id) as customer_count from subscriptions where start_date <= '2026-04-30' and (cancelled_date is null or cancelled_date > '2026-04-30');

-- Total MRR: 156,815.5
-- Subscription Count: 55
-- Customer Count: 44

-- Step 2

-- Actual Closing MRR: $156,830.50
-- Actual Subscription Count: 55
-- Actual Customer Count: 44

-- They do not match.

-- Step 3

-- It is in the Engine tab. In May, we had 2 new customers, 1 cancelled customer, and 2 seat changes. The seat changes are responsible for the difference in MRR. 
-- The first seat change was a downsizing of 4 seats which resulted in a loss of $440. The second seat change was an upsize of 5 seats which resulted in a gain of $425.
-- Combining these two gives us $15 which is the exact difference between step 1 and step 2. 

-- Step 4

-- This affected MRR because the subscriptions changed their billing status which changed their revenue. 
-- The subscription count or customer count wasn't affected because the change did not add or remove any distinct customers from the April 30th customer set.

-- Step 5
select subscription_id, customer_id, plan_name, billing_cycle, seats, price_per_seat, discount_percent,
case 
	when billing_cycle = 'Annual' then round(seats*price_per_seat/12 * (1 - discount_percent / 100), 2)
	when billing_cycle = 'Monthly' then round(seats*price_per_seat * (1 - discount_percent / 100), 2)
end as mrr from subscriptions where start_date <= '2026-05-31' and (cancelled_date is null or cancelled_date > '2026-05-31') order by subscription_id;

