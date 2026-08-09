/* C1 */
select c.company_name from customers c where region = 'Eastern Canada'

/* C2 */
select count(s.subscription_id) as subscription_count, c.region from subscriptions s 
left join customers c on s.customer_id = c.customer_id where s.status = 'active' group by c.region order by subscription_count desc;

/* C3 */
select sum(seats * price_per_seat * (1 - discount_percent / 100.0)) as monthly_mrr, s.plan_name from subscriptions s where s.billing_cycle = 'Monthly' and s.status = 'active' 
group by plan_name order by monthly_mrr desc 

/* C4 */
select s.plan_name, count(s.subscription_id) as subscription_count from subscriptions s where s.status = 'active' group by s.plan_name having count(s.subscription_id) > 9 order by subscription_count desc;

/* C5 */
select c.company_name, s.status from customers c
left join subscriptions s on c.customer_id = s.customer_id and s.status = 'active' where s.subscription_id is NULL