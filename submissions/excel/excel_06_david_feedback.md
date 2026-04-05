# Assignment 06 — Feedback
### From: David Chen, VP Finance
### To: Michael
### Re: Excel 06 — Actual vs Forecast, January 2026

---

Michael —

Good effort. The structure is right, the actuals are right, and you understand the waterfall
concept. That matters. But there are two errors that would send this back if you put it in
front of the CFO, and a commentary issue we need to fix before this goes anywhere.

Let me go through all of it.

---

## What You Got Right

**Actuals — all correct.**

| Line | Your Number | Expected |
|------|-------------|----------|
| Opening MRR (Dec 31) | $143,069.50 | $143,069.50 ✓ |
| New MRR | $1,710.00 | $1,710.00 ✓ |
| Expansion MRR | $0.00 | $0.00 ✓ |
| Contraction MRR | $0.00 | $0.00 ✓ |
| Churned MRR | $0.00 | $0.00 ✓ |
| Net New MRR | $1,710.00 | $1,710.00 ✓ |
| Closing MRR (Jan 31) | $144,779.50 | $144,779.50 ✓ |

You pulled these correctly from the database. Every single one matches. That's the foundation —
if the actuals are wrong, nothing else matters.

**Waterfall structure** — correct. You have Opening, movements, Net New, Closing. That's the
right shape.

**Forecast derivation (mostly)** — you understood that the Q1 quarterly numbers need to be
divided by 3. That's the right instinct. The execution had one error (see below), but the
method was correct.

**Churn variance** — you marked it favorable. That's right. $0 actual vs $953.80 forecast.
Less churn than expected is good news. Good instinct on the sign.

**OpEx** — $74,000 total, in line with plan. No variance. Correct.

**Formatting** — clean, readable, appropriate use of parentheses for unfavorable variances.

---

## Error 1 — Revenue Forecast: Wrong Number

This is the material error.

**Your revenue forecast: $154,354.15**
**Correct revenue forecast: $146,831.05**

That's a $7,522 difference in the forecast baseline. Which means your EBITDA variance is
wrong, your margin percentages are wrong, and the story you're telling the business is wrong.

Here is what happened. Your Q1 revenue forecast was $154,354.15. That number is correct —
it's the Q1 closing MRR balance. But that's not monthly revenue. January's revenue is
January's closing MRR, which is $146,831.05.

Think about it this way:

```
Q1 model assumed:
  Opening MRR:          $143,069.50
  + New MRR (3 months):  $12,000.00  ÷ 3 = $4,000/mo
  + Expansion (3 mo):     $2,146.04  ÷ 3 = $715.35/mo
  − Churn (3 months):    ($2,861.39) ÷ 3 = ($953.80)/mo
  Net New per month:      $3,761.55
  January closing MRR:  $146,831.05  ← this is January revenue
  February closing MRR: $150,592.60
  March closing MRR:    $154,354.15  ← this is Q1 closing MRR (the full quarter)
```

You used the Q3 end-of-quarter balance as January's revenue. That's three months of growth
baked into one month's forecast. Every month thereafter would be wrong by a different amount
if you carried that logic forward.

**The fix:** January revenue forecast = January closing MRR = Opening + one month of net new
= $143,069.50 + $3,761.55 = **$146,831.05**

With the correct forecast, your P&L looks like this:

| Line | Actual | Forecast | $ Var | % Var | F/U |
|------|--------|----------|-------|-------|-----|
| Revenue | $144,779.50 | $146,831.05 | ($2,051.55) | (1.4%) | U |
| COGS | ($43,433.85) | ($44,049.32) | $615.47 | (1.4%) | F |
| Gross Profit | $101,345.65 | $102,781.74 | ($1,436.09) | (1.4%) | U |
| Gross Margin % | 70.0% | 70.0% | 0.0 pp | — | — |
| Total OpEx | ($74,000.00) | ($74,000.00) | $0 | 0.0% | — |
| EBITDA | $27,345.65 | $28,781.74 | ($1,436.09) | (5.0%) | U |
| EBITDA Margin % | 18.9% | 19.6% | (0.7 pp) | — | U |

The actual miss is $1,436. That's a 5% EBITDA variance — notable but not alarming for one
month. Your version showed a $6,702 EBITDA miss and a 19.7% variance. That's a crisis-level
number that would trigger an emergency call with the CFO. And it's wrong.

**Fix this first. Everything downstream flows from the correct revenue forecast.**

---

## Error 2 — Opening MRR: Don't Mark a Zero Variance as Unfavorable

Your opening MRR variance is $0.00. You marked it unfavorable (red / parentheses).

Opening MRR is a balance carried forward — it's identical in both columns by construction.
The forecast starting point is the same as the actual starting point. There is no variance.
A zero variance has no direction. It should be marked as a dash (—) or N/A, not unfavorable.

This is a small error but it signals a mechanical formula issue — you probably applied a
sign formula to every row without thinking about whether the row has a meaningful direction.
Before you submit a variance table, scan every row: does the favorable/unfavorable designation
make sense? Opening balances, headcount metrics, and percentage rows often need a different
treatment than movement lines.

---

## Error 3 — Commentary Needs Work

Here is what you wrote (paraphrased):

> "January results were mixed. The actuals came in slightly below forecast. I wasn't
> given the numbers for some items so I estimated."

This is not management commentary. I'd send it back without reading the rest.

Problems:
1. "Mixed" and "slightly" are not numbers. What is the miss in dollars and percent?
2. "Wasn't given the numbers" — you had the Assumptions tab. Everything you needed was there.
   If something was missing, that's a question before submission, not an excuse in the commentary.
3. No mention of what drove the miss. Is it new customers? Churn? A one-time item?
4. No forward-looking statement. What does this mean for Q1?

Management commentary exists for one purpose: to tell the reader what happened and what it
means, so they don't have to read the table themselves. If I can get the same information by
looking at the numbers directly, you haven't added any value.

**Here is the level I expect:**

> January closed at $144,780 MRR, $2,052 (1.4%) below plan. The miss was driven entirely
> by new customer volume — one customer signed in January versus the plan assumption of
> approximately 1.3 per month, and that customer's MRR of $1,710 came in below the
> $3,000/customer planning rate. No expansion activity was recorded. Partially offsetting,
> there were no cancellations in the month, resulting in a $954 favorable churn variance.
> EBITDA of $27,346 missed plan by $1,436 (5.0%), driven entirely by the gross profit
> shortfall; operating expenses were in line. At current run rate, Q1 is tracking
> approximately $6,000 below plan — a gap that a strong February could close.

Notice:
- Opens with the number and the percent, immediately
- Names the specific driver (new customer count and MRR per customer)
- Calls out both unfavorable (new MRR) and favorable (churn) — don't hide the good news
- Connects to Q1 trajectory
- No filler words, no hedging

Rewrite your commentary using this as a model. You don't need to copy it — use your own
words. But it needs to have the dollar, the percent, the driver, and the implication.

---

## The Right Way to Pull January Actuals from SQL

You had the right instinct — go to the database first, then build the spreadsheet. But
you used `status = 'active'` in your queries. That filters for what is active *today*, not
what was active on December 31 or January 31. For historical reporting, you always filter
by date, not by status.

Here is the correct approach for each number you needed.

---

**Opening MRR — active subscriptions as of December 31, 2025**

```sql
SELECT
    s.subscription_id,
    s.customer_id,
    c.company_name,
    s.plan_name,
    s.billing_cycle,
    CASE
        WHEN s.billing_cycle = 'Monthly' THEN ROUND(s.seats * s.price_per_seat * (1 - s.discount_percent / 100.0), 2)
        WHEN s.billing_cycle = 'Annual'  THEN ROUND(s.seats * s.price_per_seat * (1 - s.discount_percent / 100.0) / 12, 2)
    END AS mrr
FROM subscriptions s
INNER JOIN customers c ON s.customer_id = c.customer_id
WHERE s.start_date     <= '2025-12-31'
  AND (s.cancelled_date IS NULL OR s.cancelled_date > '2025-12-31')
ORDER BY mrr DESC;
```

Expected: 51 rows, SUM = **$143,069.50**

The two date conditions together mean: "started on or before Dec 31, AND either never
cancelled or cancelled after Dec 31." That is a point-in-time snapshot.

---

**Closing MRR — active subscriptions as of January 31, 2026**

Same query, move the dates forward one month:

```sql
WHERE s.start_date     <= '2026-01-31'
  AND (s.cancelled_date IS NULL OR s.cancelled_date > '2026-01-31')
```

Expected: 52 rows, SUM = **$144,779.50**

---

**New MRR — subscriptions that started in January**

```sql
SELECT
    s.subscription_id,
    s.customer_id,
    s.plan_name,
    s.start_date,
    ROUND(
        s.seats * s.price_per_seat * (1 - s.discount_percent / 100.0)
        * CASE WHEN s.billing_cycle = 'Annual' THEN 1.0 / 12 ELSE 1 END
    , 2) AS new_mrr
FROM subscriptions s
WHERE s.start_date BETWEEN '2026-01-01' AND '2026-01-31'
ORDER BY s.start_date;
```

Expected: 1 row, **$1,710.00**

---

**Churned MRR — subscriptions cancelled in January**

```sql
SELECT
    s.subscription_id,
    s.customer_id,
    s.plan_name,
    s.cancelled_date,
    ROUND(
        s.seats * s.price_per_seat * (1 - s.discount_percent / 100.0)
        * CASE WHEN s.billing_cycle = 'Annual' THEN 1.0 / 12 ELSE 1 END
    , 2) AS churned_mrr
FROM subscriptions s
WHERE s.cancelled_date BETWEEN '2026-01-01' AND '2026-01-31';
```

Expected: 0 rows, **$0.00**

---

**Events — check for expansion or contraction in January**

```sql
SELECT
    e.event_id,
    e.subscription_id,
    e.event_type,
    e.event_date,
    e.field_changed,
    e.old_value,
    e.new_value
FROM subscription_events e
WHERE e.event_date BETWEEN '2026-01-01' AND '2026-01-31'
ORDER BY e.event_date;
```

Expected: 1 row — EVT096, type 'created'. Only a new subscription, no seat changes.
Expansion and contraction are both $0.00.

---

**Actual COGS — don't use a percentage, pull it from the database**

The subscriptions table has a `cost_per_seat` column. Use it. The formula is identical
to MRR, with `cost_per_seat` replacing `price_per_seat`:

```sql
SELECT
    ROUND(SUM(
        s.seats
        * s.cost_per_seat
        * (1 - s.discount_percent / 100.0)
        * CASE WHEN s.billing_cycle = 'Annual' THEN 1.0 / 12 ELSE 1 END
    ), 2) AS actual_cogs
FROM subscriptions s
WHERE s.start_date     <= '2026-01-31'
  AND (s.cancelled_date IS NULL OR s.cancelled_date > '2026-01-31');
```

Expected: **$43,433.85** — exactly 30% of $144,779.50 in this case, because all our plans
happen to have a 30% cost margin. In a real company, margins vary by plan and customer, so
you always pull COGS from the database rather than calculating it as a flat percentage.

---

**Save these queries.**

Create a file called `submissions/sql/jan_2026_actuals.sql`. Put all five queries in it,
one after the other, with comments explaining what each one does. This is now your reference
document. Every time you close a month, you copy this file, change the dates, and run it.

You do not build these from scratch each month. You maintain one file and update the dates.
That is how analysts work.

---

## Resubmit

Four things to fix:

1. **Revenue forecast** — use January closing MRR ($146,831.05), not the Q1 closing balance
2. **COGS** — run the query above and use the database number ($43,433.85). Remove the 30% formula. Label the row "COGS", not "COGS (30%)"
3. **Opening MRR F/U** — change from unfavorable to a dash (—)
4. **Commentary** — rewrite using the model above

The waterfall actuals are correct. Don't touch those.

— David

---

*Assignment 06 — Feedback*
*Excel: Actual vs Forecast — January 2026*
*April 2026*
