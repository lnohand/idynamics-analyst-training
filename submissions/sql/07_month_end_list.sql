-- Step 1
select subscription_id, customer_id, status, start_date, cancelled_date from subscriptions order by start_date;
select count(*) from subscriptions;
-- 69

-- Step 2
select subscription_id, customer_id, status, start_date, cancelled_date from subscriptions where start_date <= '2026-05-31' order by start_date;
select count(subscription_id) as sub_count from subscriptions where start_date <= '2026-05-31';
-- 69

-- Step 3
select subscription_id, customer_id, status, start_date, cancelled_date from subscriptions where start_date <= '2026-05-31' AND(cancelled_date is null or cancelled_date > '2026-05-31') order by start_date;
select count(subscription_id) as sub_count from subscriptions where start_date <= '2026-05-31' AND(cancelled_date is null or cancelled_date > '2026-05-31');
-- 56

-- Step 4
select count(subscription_id) from subscriptions where start_date > '2026-05-31';
select count(subscription_id) from subscriptions where cancelled_date <= '2026-05-31';
select count(subscription_id) from subscriptions where start_date <= '2026-05-31' AND(cancelled_date is null or cancelled_date > '2026-05-31');

-- Step 5
select subscription_id, customer_id, billing_cycle, seats, price_per_seat, discount_percent, status, start_date, cancelled_date,
case 
	when billing_cycle = 'Annual' then round(seats*price_per_seat/12 * (1 - discount_percent / 100), 2)
	when billing_cycle = 'Monthly' then round(seats*price_per_seat * (1 - discount_percent / 100), 2)
end as mrr from subscriptions where start_date <= '2026-05-31' and (cancelled_date is null or cancelled_date > '2026-05-31') order by start_date;

-- SUB 003 MRR: 1955 (23 * 85)
-- SUB 002 MRR: 3900 (26 * 1800 / 12)
-- SUB 054 MRR: 1985.5 (22 * 1140 * 0.95 / 12)

-- Step 6
select 
sum(
case 
	when billing_cycle = 'Annual' then round(seats*price_per_seat/12 * (1 - discount_percent / 100), 2)
	when billing_cycle = 'Monthly' then round(seats*price_per_seat * (1 - discount_percent / 100), 2)
end) as total_mrr, count(subscription_id) as subscription_count, count(distinct customer_id) as customer_count from subscriptions where start_date <= '2026-05-31' and (cancelled_date is null or cancelled_date > '2026-05-31');

-- Step 7
select subscription_id, customer_id, status, start_date, cancelled_date from subscriptions where start_date <= '2026-04-30' and(cancelled_date > '2026-04-30' or cancelled_date is null) order by subscription_id;
select subscription_id, customer_id, status, start_date, cancelled_date from subscriptions where status = 'active' and start_date <= '2026-04-30' order by subscription_id;

select count(subscription_id) as sub_count from subscriptions where start_date <= '2026-04-30' and(cancelled_date > '2026-04-30' or cancelled_date is null);
select count(subscription_id) as sub_count from subscriptions where status = 'active' and start_date <= '2026-04-30';


-- When there's a cancelled date after the deadline  (in this case, April 30th 2026), the active status doesn't account for it. This results in a mismatch of 1 subscription because there is an account with a cancellation of May 23rd which is after the deadline and therefore not included. If it is queried by just the active status, it will not appear because the cancelled date isn't being checked.

