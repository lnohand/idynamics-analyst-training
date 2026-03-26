# Excel Assignment 04 — Unit Economics
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Unit Economics tab — the investor question
>
> Michael — you've built the growth story and the retention picture.
> Now the board is going to ask the question that comes after both:
> "Does the math work on each customer?"
>
> That's unit economics. How much does a customer pay us? How much
> does it cost us to serve them? How long do they stay? How much are
> they worth over their lifetime? And how much did we spend to get
> them?
>
> A business can grow fast and still lose money on every customer.
> If it costs $50K to acquire a customer who's only worth $30K, then
> growth makes the problem worse, not better. The faster you grow,
> the faster you burn.
>
> Lisa from Accounting sent over our Sales & Marketing spend data
> for the last 14 months. It's in the Master Prompt under "Sales &
> Marketing Spend." That's your input for the CAC calculation.
>
> Build the Unit Economics tab. Same workbook. This one ties
> everything together.
>
> — David

---

## Why Unit Economics Exist

Growth tells you speed. Retention tells you leakage. Unit economics
tells you whether the business model actually works — whether each
customer generates more value than it costs to acquire and serve.

A company with $1.8M ARR and 40% YoY growth looks impressive on the
Growth tab. But if each customer costs $50K to acquire and generates
$30K in lifetime value, the company is destroying value with every
sale. The board doesn't just want to know "are we growing?" They
want to know "should we be growing?"

Unit economics answers that with three questions:

1. **What is each customer worth?** (LTV)
2. **What does it cost to get each customer?** (CAC)
3. **Is the ratio healthy?** (LTV:CAC)

If LTV > 3× CAC, the model works. If LTV < CAC, every new customer
loses money. Everything in between is a conversation about efficiency.

---

## The Metrics

### ARPA — Average Revenue Per Account

Total MRR divided by active customers. Not active subscriptions —
active *customers*. A customer with two subscriptions is one account.

This is the "per-customer" building block that feeds into LTV. It
also tells you about your customer mix — if ARPA is rising, you're
moving upmarket. If falling, you're acquiring smaller accounts or
existing accounts are shrinking.

### Gross Margin

Revenue minus the direct cost of delivering the service, as a
percentage. For SaaS, this is mostly hosting infrastructure, support
staff allocated to delivery, and third-party software costs baked
into the product.

Idynamics has a `cost_per_seat` field in the subscriptions table.
The cost data is also on the Ref tab (you'll need to add it — see
below). Gross margin tells you how much of each revenue dollar is
actually profit versus cost of delivery.

SaaS companies are expected to have gross margins above 70%. Below
60% and investors start questioning whether you're really a software
company or a services business.

### Customer Lifetime

How long a customer stays before churning. Two ways to measure it:

**Formula method:** `1 / monthly churn rate`. If your monthly gross
churn rate is 0.85%, the implied lifetime is 118 months (~10 years).
This is forward-looking — it estimates what would happen if current
churn continues indefinitely.

**Observed method:** Average the actual lifetimes of customers who
already churned. Look at each cancelled subscription's start date
and cancelled date, compute the difference in months, and average.
This is backward-looking — it only counts customers who left.

These two numbers will be very different for Idynamics. The formula
gives a long lifetime because current monthly churn is low. The
observed average is shorter because early customers churned faster
when the product was immature. Both are useful. The truth is
somewhere in between.

### LTV — Customer Lifetime Value

How much total gross profit a customer generates over their lifetime.
Not revenue — gross profit. The cost of serving them matters.

**Simple LTV** = ARPA / monthly churn rate.
This overstates value because it ignores delivery costs.

**Gross-margin-adjusted LTV** = ARPA × gross margin / monthly churn rate.
This is the version investors care about. It tells you the actual
profit a customer generates, not just the revenue.

### CAC — Customer Acquisition Cost

Total Sales & Marketing spend divided by new customers acquired in
the same period.

The catch: CAC is only meaningful over periods where you actually
acquired customers. If you spent $29K in July 2025 and acquired zero
customers, the monthly CAC is undefined — you can't divide by zero.
That's not a formula error. It's a business problem.

This is why analysts use trailing-period CAC (6-month, 12-month)
instead of monthly. It smooths out the months where spend happens
but deals haven't closed yet.

### LTV:CAC Ratio

The headline number. Lifetime value divided by acquisition cost.

The benchmarks are well-established across the SaaS industry:

| LTV:CAC | What it means |
|---|---|
| > 5.0x | Very capital-efficient — may be under-investing in growth |
| 3.0 – 5.0x | Healthy — the model works |
| 1.0 – 3.0x | Marginal — unit economics are tight |
| < 1.0x | Losing money on every customer |

### Payback Period

How many months until a customer's gross profit repays the
acquisition cost. `CAC / (ARPA × gross margin)`.

Payback under 12 months is strong. Under 18 is acceptable for
venture-backed. Over 24 months means you're tying up a lot of
capital in acquisition that takes years to recover.

---

## What to Build

Add a **Unit Economics** tab to the workbook. Four sections.

### Section 1 — Revenue Per Customer

Calculate current-state metrics from the snapshot:

- Active customers (unique customer count — not subscription count)
- Active subscriptions
- Total MRR
- ARPA (MRR / active customers)
- ARPS (MRR / active subscriptions)

Then break ARPA down by plan: for each plan, show the number of
subscriptions, total MRR, and average MRR per subscription. This
shows which plans drive the most revenue per account.

**Watch the denominator.** ARPA divides by *customers with at least
one active subscription*, not total customers in the database. If a
customer churned and has no active subs, they don't count. Check
your snapshot — how many unique customer IDs appear?

### Section 2 — Gross Margin

Add `monthly_cost` and `gross_margin` columns to your plan pricing
table on the Ref tab:

| plan_name | monthly_price | monthly_cost | gross_margin |
|---|---|---|---|
| Analytics Starter | 45 | 13.50 | 70% |
| Analytics Growth | 95 | 28.50 | 70% |
| Analytics Enterprise | 180 | 54.00 | 70% |
| Marketing Pro | 85 | 25.50 | 70% |
| Sales Hub | 110 | 33.00 | 70% |
| Platform Suite | 150 | 45.00 | 70% |

Then on the Unit Economics tab, calculate:
- Total monthly cost (using cost per seat × seats, adjusted for
  billing cycle and discount, same pattern as MRR)
- Total gross profit (MRR − cost)
- Blended gross margin % (gross profit / MRR)
- Monthly gross profit per customer (gross profit / active customers)

All plans happen to have 70% margin. In a real company, margins vary
by plan. Build the formula to handle plan-level differences even
though the result is uniform here — that's how you make a model that
scales.

### Section 3 — Customer Lifetime & LTV

Calculate both lifetime estimates:

**Formula-based lifetime:** 1 / trailing 12-month average gross churn
rate (pull from your Retention tab). This is the forward-looking
estimate.

**Observed lifetime:** You have 11 churned subscriptions. For each
one, calculate (cancelled_date − start_date) in months. Show the
average and median. This is the backward-looking reality.

Then calculate LTV three ways:
- **Simple LTV** = ARPA / monthly gross churn rate
- **GM-adjusted LTV** = ARPA × gross margin / monthly gross churn rate
- **Observed LTV** = ARPA × observed average lifetime × gross margin

Add a note explaining why these three numbers are so different and
which one you'd use in an investor conversation (GM-adjusted with
the formula-based lifetime, because it's forward-looking and
accounts for delivery costs).

### Section 4 — CAC & LTV:CAC

This section uses the S&M spend data from Accounting (in the Master
Prompt). Create a table on the Unit Economics tab:

**Monthly S&M detail** — one row per month (Jan 2025 – Feb 2026),
columns for each spend category, total S&M, and new customers
acquired. Paste the data from the Master Prompt as values.

Then calculate:

| Metric | Period | Formula |
|---|---|---|
| CAC | H1 2025 (Jan–Jun) | Total S&M / New customers |
| CAC | H2 2025 (Jul–Dec) | Undefined — zero customers |
| CAC | Full year 2025 | Total S&M / New customers |
| CAC | Jan–Feb 2026 | Total S&M / New customers |
| CAC | Trailing 12 months | Total S&M / New customers |
| **LTV:CAC** | Using H1 2025 CAC | GM-adjusted LTV / CAC |
| **LTV:CAC** | Using trailing 12mo CAC | GM-adjusted LTV / CAC |
| **Payback** | Using H1 2025 CAC | CAC / monthly gross profit per customer |
| **Payback** | Using trailing 12mo CAC | CAC / monthly gross profit per customer |

**Handle H2 2025 explicitly.** Don't hide the divide-by-zero. Show
the spend ($165,600), show the zero customers, and display "N/A" or
"undefined" for CAC. Then add a note: "S&M spend continued at
$25–33K/month with zero acquisitions for six consecutive months.
This is why monthly CAC is unreliable — use trailing periods."

### Written Summary — Two Paragraphs

**Paragraph 1 — The unit economics story.** What does the LTV:CAC
ratio tell you about Idynamics? Is the model healthy? How does the
answer change depending on which CAC period you use? What's the
payback period and is it acceptable?

**Paragraph 2 — The S&M efficiency problem.** What happened in H2
2025? The team kept spending ~$28K/month on sales and marketing but
acquired zero customers for six months. What does that tell you about
the GTM motion? What would you recommend — cut spend, reallocate it,
or wait for the pipeline to restart?

---

## Self-Check Values

| Check | Expected |
|---|---|
| Active customers (unique in snapshot) | 39 |
| Active subscriptions | 51 |
| ARPA | $3,697.06 |
| ARPS | $2,827.17 |
| Blended gross margin | 70.0% |
| Monthly gross profit per customer | $2,587.94 |
| Avg observed lifetime (churned subs) | ~11.5 months |
| GM-adjusted LTV (formula-based) | ~$303,000 (varies with churn rate used) |
| CAC, H1 2025 | $13,523 |
| CAC, FY 2025 | $26,262 |
| CAC, Jan–Feb 2026 | $51,800 |
| CAC, trailing 12 months | $33,740 |
| LTV:CAC (H1 2025 CAC) | ~22x |
| LTV:CAC (trailing 12mo CAC) | ~9x |
| Payback (H1 CAC) | ~5 months |
| Payback (trailing 12mo CAC) | ~13 months |

> **The LTV number is very large.** That's because the trailing
> 12-month gross churn rate is low (~0.85%). A small denominator
> creates a large LTV. This is common for early-stage companies
> without much churn history. Don't treat it as gospel — flag it
> as sensitive to the churn assumption and show what happens if
> churn were 2× higher.
>
> **39 customers, not 40.** The customers table has 40 rows, but
> CUST005 (Atlantic Media Corp) churned and never came back. They
> have zero active subscriptions. ARPA uses active customers only.
> If you get $3,604.64 you divided by 40 instead of 39.

---

## Formatting

- Same conventions as Growth and Retention tabs
- Section headers: bold white on dark blue
- Dollar values: accounting format
- Percentages: 1 decimal place
- Ratios (LTV:CAC): 1 decimal place with "x" suffix
- Payback: 1 decimal place with "months" label
- S&M data table: formatted as Excel Table for structured references
- H2 2025 CAC cell: yellow background with "N/A" — make the anomaly
  visible, don't hide it
- Freeze column A and header row

---

## Submission

Save the workbook. Commit to your repo:

```
submissions/excel/04_unit_economics.xlsx
```

Branch: `student/excel-04-unit-economics`

PR description:

```
## What this does
Unit Economics tab: ARPA, gross margin, customer lifetime (formula
+ observed), LTV (simple + GM-adjusted), CAC by period, LTV:CAC
ratios, payback period, and written interpretation.

## Self-check
Active customers: 39 (not 40 — CUST005 has no active subs) ✅
ARPA: $3,697.06 ✅
Gross margin: 70.0% ✅
CAC H1 2025: $13,523 ✅
LTV:CAC (trailing 12mo): ~9x ✅
Payback (H1 CAC): ~5 months ✅

## Interpretation
[One sentence: what do the unit economics say about this business?]

## Questions for reviewer
[Anything you're unsure about]
```

---

## What Comes Next

Two tabs remain:

- **MRR Mix** — pivot tables breaking down MRR by plan, region,
  billing cycle, and account owner. This is the "where does our
  revenue come from" view.
- **Dashboard** — the board-ready summary. Six KPI cards, key
  charts, one screen that tells the whole story.

After the Dashboard, the workbook is complete and the Excel module
closes. Then we move to Actual vs Budget variance — where the
numbers you've built become the "actuals" side of the equation.

---

*Idynamics Finance Analyst Training Program*
*Excel Assignment 04 — Unit Economics*
*March 2026*
