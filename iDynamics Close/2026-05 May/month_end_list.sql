-- Step 5
select subscription_id, customer_id, plan_name, billing_cycle, seats, price_per_seat, discount_percent,
case 
	when billing_cycle = 'Annual' then round(seats*price_per_seat/12 * (1 - discount_percent / 100), 2)
	when billing_cycle = 'Monthly' then round(seats*price_per_seat * (1 - discount_percent / 100), 2)
end as mrr from subscriptions where start_date <= '2026-05-31' and (cancelled_date is null or cancelled_date > '2026-05-31') order by subscription_id;
