# **MRR Analysis — January 2026**

---

## **Total Opening MRR (as of December 31, 2025\)**

SELECT  
    sum(CASE  
        WHEN s.billing\_cycle \= 'Monthly' THEN ROUND(s.seats \* s.price\_per\_seat \* (1 \- s.discount\_percent / 100.0), 2\)  
        WHEN s.billing\_cycle \= 'Annual'  THEN ROUND(s.seats \* s.price\_per\_seat \* (1 \- s.discount\_percent / 100.0) / 12, 2\)  
    end) AS mrr  
FROM subscriptions s  
INNER JOIN customers c ON s.customer\_id \= c.customer\_id  
WHERE s.start\_date     \<= '2025-12-31'  
  AND (s.cancelled\_date IS NULL OR s.cancelled\_date \> '2025-12-31')  
ORDER BY mrr DESC;

## **Opening MRR (as of December 31, 2025\)**

SELECT  
   s.subscription\_id,  
   s.customer\_id,  
   c.company\_name,  
   s.plan\_name,  
   s.billing\_cycle,  
   CASE  
       WHEN s.billing\_cycle \= 'Monthly' THEN ROUND(s.seats \* s.price\_per\_seat \* (1 \- s.discount\_percent / 100.0), 2\)  
       WHEN s.billing\_cycle \= 'Annual'  THEN ROUND(s.seats \* s.price\_per\_seat \* (1 \- s.discount\_percent / 100.0) / 12, 2\)  
   END AS mrr  
FROM subscriptions s  
INNER JOIN customers c ON s.customer\_id \= c.customer\_id  
WHERE s.start\_date \<= '2025-12-31'  
 AND (s.cancelled\_date IS NULL OR s.cancelled\_date \> '2025-12-31')  
ORDER BY mrr DESC;

**Expected Result:**

* Rows: **51**  
* Total MRR: **$143,069.50**

**Explanation:**  
 This captures subscriptions that:

* Started **on or before Dec 31**  
* Were **still active** on Dec 31

This is a **point-in-time snapshot**.

---

## **Closing MRR (as of January 31, 2026\)**

SELECT  
    sum(CASE  
        WHEN s.billing\_cycle \= 'Monthly' THEN ROUND(s.seats \* s.price\_per\_seat \* (1 \- s.discount\_percent / 100.0), 2\)  
        WHEN s.billing\_cycle \= 'Annual'  THEN ROUND(s.seats \* s.price\_per\_seat \* (1 \- s.discount\_percent / 100.0) / 12, 2\)  
    end) AS mrr  
FROM subscriptions s  
INNER JOIN customers c ON s.customer\_id \= c.customer\_id  
WHERE s.start\_date \<= '2026-01-31'  
 AND (s.cancelled\_date IS NULL OR s.cancelled\_date \> '2026-01-31')  
ORDER BY mrr DESC;

**Condition to change date to 2026-01-31**  
WHERE s.start\_date \<= '2026-01-31'  
 AND (s.cancelled\_date IS NULL OR s.cancelled\_date \> '2026-01-31')

**Expected Result:**

* Rows: **52**  
* Total MRR: **$144,779.50**

---

## **List of New MRR (January 2026\)**

SELECT  
   s.subscription\_id,  
   s.customer\_id,  
   s.plan\_name,  
   s.start\_date,  
   ROUND(  
       s.seats \* s.price\_per\_seat \* (1 \- s.discount\_percent / 100.0)  
       \* CASE WHEN s.billing\_cycle \= 'Annual' THEN 1.0 / 12 ELSE 1 END  
   , 2\) AS new\_mrr  
FROM subscriptions s  
WHERE s.start\_date BETWEEN '2026-01-01' AND '2026-01-31'  
ORDER BY s.start\_date;

## **Total New MRR (January 2026\)**

SELECT  
   ROUND(sum(  
       s.seats \* s.price\_per\_seat \* (1 \- s.discount\_percent / 100.0)  
       \* CASE WHEN s.billing\_cycle \= 'Annual' THEN 1.0 / 12 ELSE 1 end)  
   , 2\) AS new\_mrr  
FROM subscriptions s  
WHERE s.start\_date BETWEEN '2026-01-01' AND '2026-01-31'  
group by s.start\_date ORDER BY s.start\_date;

**Expected Result:**

* Rows: **1**  
* New MRR: **$1,710.00**

---

## **Churned MRR (January 2026\)**

SELECT  
   s.subscription\_id,  
   s.customer\_id,  
   s.plan\_name,  
   s.cancelled\_date,  
   ROUND(  
       s.seats \* s.price\_per\_seat \* (1 \- s.discount\_percent / 100.0)  
       \* CASE WHEN s.billing\_cycle \= 'Annual' THEN 1.0 / 12 ELSE 1 END  
   , 2\) AS churned\_mrr  
FROM subscriptions s  
WHERE s.cancelled\_date BETWEEN '2026-01-01' AND '2026-01-31';  
**Total Churned MRR (January 2026\)**

SELECT  
   ROUND(sum(  
       s.seats \* s.price\_per\_seat \* (1 \- s.discount\_percent / 100.0)  
       \* CASE WHEN s.billing\_cycle \= 'Annual' THEN 1.0 / 12 ELSE 1 end)  
   , 2\) AS churned\_mrr  
FROM subscriptions s  
WHERE s.cancelled\_date BETWEEN '2026-01-01' AND '2026-01-31'  
group by s.cancelled\_date ORDER BY s.cancelled\_date;

**Expected Result:**

* Rows: **0**  
* Churned MRR: **$0.00**

---

## **Expansion / Contraction Events (January 2026\)**

SELECT  
   e.event\_id,  
   e.subscription\_id,  
   e.event\_type,  
   e.event\_date,  
   e.field\_changed,  
   e.old\_value,  
   e.new\_value  
FROM subscription\_events e  
WHERE e.event\_date BETWEEN '2026-01-01' AND '2026-01-31'  
ORDER BY e.event\_date;

**Expected Result:**

* 1 event: **EVT096**  
* Type: **created**

**Conclusion:**

* Expansion MRR: **$0.00**  
* Contraction MRR: **$0.00**

---

## **Actual COGS (as of January 31, 2026\)**

SELECT  
   ROUND(SUM(  
       s.seats  
       \* s.cost\_per\_seat  
       \* (1 \- s.discount\_percent / 100.0)  
       \* CASE WHEN s.billing\_cycle \= 'Annual' THEN 1.0 / 12 ELSE 1 END  
   ), 2\) AS actual\_cogs  
FROM subscriptions s  
WHERE s.start\_date \<= '2026-01-31'  
 AND (s.cancelled\_date IS NULL OR s.cancelled\_date \> '2026-01-31');

**Expected Result:**

* **$43,433.85**

**Note:**

* This equals **30% of total MRR ($144,779.50)** in this dataset.  
* In real scenarios, **always calculate COGS from actual data**, not a flat percentage. 

