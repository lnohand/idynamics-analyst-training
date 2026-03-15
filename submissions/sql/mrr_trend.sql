-- Query 3: cash trend
with monthly_revenue as (
select
	to_char(date_trunc('month', invoice_date), 'YYYY-MM') as month,
	count(invoice_id) as invoice_count,
	sum(subtotal) as revenue
from
	invoices
where
	payment_status = 'paid'
group by
	month)
select
	month,
	invoice_count,
	revenue,
	sum(revenue) over (
	order by month) as running_total,
	lag(revenue) over (
	order by month) as prior_month_revenue,
	round((revenue - lag(revenue) over (order by month)) / lag(revenue) over (order by month) * 100.0, 1) as pct_change
from
	monthly_revenue
group by
	month,
	invoice_count,
	revenue
order by
	month;
