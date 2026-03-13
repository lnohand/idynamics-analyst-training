--  Query 1
select
	s.subscription_id,
	s.customer_id,
	c.company_name,
	c.account_owner,
	c.region,
	s.plan_name,
	s.billing_cycle,
	case
		when s.billing_cycle = 'Monthly' then ROUND(seats * price_per_seat * (1 - discount_percent / 100.0))
		when s.billing_cycle = 'Annual' then ROUND((seats * price_per_seat * (1 - discount_percent / 100.0)/ 12))
	end as mrr
from
	subscriptions s
inner join customers c on
	s.customer_id = c.customer_id
where
	s.status = 'active'
order by
	mrr desc;
