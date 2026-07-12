CREATE TABLE lab_customers (customer_id TEXT, company_name TEXT);
INSERT INTO lab_customers VALUES
  ('C1','Aurora Analytics'), ('C2','Borealis Media'), ('C3','Cascade Retail'),
  ('C4','Dominion Freight'), ('C5','Evergreen Health');

CREATE TABLE lab_invoices (invoice_id TEXT, customer_id TEXT, amount NUMERIC);
INSERT INTO lab_invoices VALUES
  ('I1','C1',500), ('I2','C1',300), ('I3','C3',450),
  ('I4','C6',700), ('I5','C7',250);

select * from lab_customers

select * from lab_invoices;

SELECT c.customer_id, c.company_name, i.invoice_id, i.amount
FROM lab_customers c
left JOIN lab_invoices i ON i.customer_id = c.customer_id;

/* Exercise 1 */
select lc.company_name, li.invoice_id, li.amount from lab_customers lc
left join lab_invoices li on lc.customer_id = li.customer_id where li.invoice_id is null;

/* Exercise 2 */
select c.company_name from customers c 
left join subscriptions s on c.customer_id = s.customer_id where s.subscription_id is null;

/* Exercise 3 */
select c.company_name, c.region, s.status from customers c
left join subscriptions s on c.customer_id = s.customer_id and s.status = 'active' where s.customer_id is null;

/* Exercise 4 */
select c.company_name, coalesce(sum(seats * price_per_seat * (1 - discount_percent / 100.0)), 0) as total_mrr from customers c
left join subscriptions s on c.customer_id = s.customer_id and status = 'active' and s.billing_cycle = 'Monthly' group by c.customer_id order by total_mrr desc;

DROP TABLE lab_customers;
DROP TABLE lab_invoices;
