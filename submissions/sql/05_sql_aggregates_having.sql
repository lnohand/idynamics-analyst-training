/* Question 1 */
select plan_name, sum(seats) as total_seats from subscriptions where status = 'active' group by plan_name order by total_seats desc;

/* Question 2, This question does not work because the plan names do not group. I believe there is an invisible character in each variation of the name. */
select plan_name, seats * price_per_seat * (1 - discount_percent / 100.0) as monthly_mrr from subscriptions where status = 'active' and billing_cycle = 'Monthly' group by plan_name, monthly_mrr order by monthly_mrr desc;

/* Question 3 */
select plan_name, count(subscription_id) as subscription_count from subscriptions where status = 'active' group by plan_name having count(subscription_id) > 9 order by subscription_count desc;

/* Question 4 */
select c.region, sum(seats * price_per_seat * (1 - discount_percent / 100.0)) as total_mrr from subscriptions s 
left join customers c on s.customer_id = c.customer_id where s.status = 'active' and s.billing_cycle = 'Monthly' group by c.region having sum(seats * price_per_seat * (1 - discount_percent / 100.0)) > 20000 order by total_mrr desc;

/* Question 5 */
select c.customer_id, sum(seats * price_per_seat * (1 - discount_percent / 100.0)) as total_mrr from customers c
left join subscriptions s on c.customer_id = s.customer_id where status = 'active' and s.billing_cycle = 'Monthly' group by c.customer_id order by total_mrr desc limit 5;