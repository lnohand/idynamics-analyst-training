-- Query 2

select
	se.event_id,
	se.subscription_id,
	se.customer_id,
	c.company_name,
	c.region,
	to_char(se.event_date, 'YYYY-MM') as month,
	se.event_date,
	se.event_date,
	se.event_type,
	se.old_value,
	se.new_value,
	se.field_changed,
	se.reason,
	s.plan_name,
	s.billing_cycle,
	s.price_per_seat,
	s.discount_percent
from
	subscription_events se
inner join subscriptions s on
	se.subscription_id = s.subscription_id
inner join customers c on
	s.customer_id = c.customer_id
order by
	event_date,
	event_id;