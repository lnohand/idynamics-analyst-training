# SQL Assignment: Excel Data Pull
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Data pull for the MRR workbook — need this before Monday
>
> Hey Michael — we're building out the MRR workbook in Excel and I need
> three clean SQL exports before the board prep session Monday morning.
>
> Nothing complex — I just need the data in the right shape so we can
> paste it straight into the workbook without touching it. Get the queries
> right the first time. I'll be checking the self-check values before we
> import anything.
>
> Tables: `customers`, `subscriptions`, `subscription_events`, `invoices`
>
> PostgreSQL. Export each query result to CSV when you're done.
>
> — David

---

## What You're Building

These three queries produce the raw data that feeds the Excel MRR workbook.
You will run them, validate the outputs against the self-check values below,
then import the results into Excel at the end of this assignment.

Each query has a name that matches the tab it feeds:

| Query | File | Feeds |
|---|---|---|
| Query 1 — MRR Snapshot | `mrr_snapshot.sql` | [RAW] Snapshot tab |
| Query 2 — Events Export | `mrr_events.sql` | [RAW] Waterfall tab |
| Query 3 — Monthly Revenue Trend | `mrr_trend.sql` | [RAW] Waterfall tab |

---

## Before you start — understand why these three queries

A real finance analyst does not build everything in SQL. SQL's job is to
get clean, structured data out of the database. The analysis happens in Excel.

Here is how the work splits:

**SQL owns:**
- Joining tables to bring together data that lives in separate places
- Filtering to the right records (active only, paid only, etc.)
- Calculating MRR from raw fields (seats × price × billing cycle adjustment)
- Formatting dates so Excel can group them

**Excel owns:**
- Classifying events into movement categories (New, Expansion, Contraction, Churned, Reactivation)
- Calculating the MRR impact of each event
- Building the waterfall: opening MRR → movements → closing MRR
- Charts, conditional formatting, KPI cards

You will do the Excel work in the next assignment. Right now your job is
to get the data right.

---

## Query 1 — MRR Snapshot

**Business context:**
The MRR snapshot is a point-in-time view of the business. It answers one
question: *how much recurring revenue do we have right now, and where does
it come from?*

Every board presentation starts with this number. When David says
"our MRR is $144,185", this is the query behind that number.

**Your task:**
You already wrote this query in the MRR Snapshot assignment. Open your
existing `mrr_snapshot.sql` and make one update: add the `region` column
from the `customers` table.

The column already exists in `customers` — you just need to add it to
your SELECT list. It will be used in Excel for the "MRR by Region" pivot.

**Return these columns, in this order:**

| Column | Source | Notes |
|---|---|---|
| subscription_id | subscriptions | |
| customer_id | subscriptions | |
| company_name | customers | |
| account_owner | customers | |
| region | customers | Eastern Canada / Western Canada / Central Canada |
| plan_name | subscriptions | |
| billing_cycle | subscriptions | |
| mrr | calculated | `ROUND(seats × price_per_seat × (1 - discount_percent/100.0) [÷12 if Annual], 2)` |

**Filter:** Active subscriptions only (`status = 'active'`)

**Sort:** `mrr` descending

```sql
-- Update your existing mrr_snapshot.sql
-- Add region to the SELECT list and sort by mrr DESC
```

**Self-check:**

| Check | Expected |
|---|---|
| Row count | **51 rows** |
| SUM of mrr column | **$144,185.50** |
| Distinct values in region | Eastern Canada, Western Canada, Central Canada |

> If your SUM is not exactly $144,185.50, do not move on. Check your
> CASE WHEN for billing cycle. Annual subscriptions must be divided by 12.

> **Why 51, not 49?** After the Stage 2 database update, two customers
> who previously churned reactivated and started new subscriptions
> (CUST013 in May 2025 and CUST023 in October 2025). Both are currently
> active, so they appear in the snapshot. This is expected.

---

## Query 2 — Events Export

**Business context:**
The `subscription_events` table is the audit trail of everything that
has ever changed about a subscription. Every new customer, every seat
increase, every cancellation — it is all in here as a row with a date
and a before/after value.

This table is how finance teams reconstruct what happened to MRR over
time. In Excel, you will look at each row and classify it as a waterfall
movement (New, Expansion, Contraction, Churned, or Reactivation). But
to do that classification, Excel needs context from the subscriptions
and customers tables — the plan name, price, billing cycle, and region
do not live in the events table. That is what this join provides.

**Your task:**
Join `subscription_events` to `subscriptions` and `customers`. Export
every event with enough context for Excel to classify it and calculate
the MRR impact.

**Return these columns, in this order:**

| Column | Source | Notes |
|---|---|---|
| event_id | subscription_events | |
| subscription_id | subscription_events | |
| customer_id | subscription_events | |
| company_name | customers | |
| region | customers | |
| month | calculated | `TO_CHAR(event_date, 'YYYY-MM')` |
| event_date | subscription_events | The actual date, not just the month |
| event_type | subscription_events | created, seats_change, plan_upgrade, etc. |
| old_value | subscription_events | Value before the change |
| new_value | subscription_events | Value after the change |
| field_changed | subscription_events | Which field was affected |
| reason | subscription_events | Why the change happened |
| plan_name | subscriptions | Plan at time of event |
| billing_cycle | subscriptions | Monthly or Annual |
| price_per_seat | subscriptions | Current price per seat |
| discount_percent | subscriptions | Current discount |

**No filter** — export all 97 events. David needs the complete history.

**Sort:** `event_date` ascending, then `event_id` ascending

```sql
-- New file: mrr_events.sql
-- Three-table join: subscription_events + subscriptions + customers
-- No WHERE clause needed — all events
-- Add the month column using TO_CHAR
```

**Self-check:**

| Check | Expected |
|---|---|
| Row count | **97 rows** |
| Earliest event_date | 2024-01-08 |
| Latest event_date | 2026-02-20 |
| Distinct values in event_type | created, seats_change, price_change, plan_upgrade, plan_downgrade, discount_added, cancelled |

> Scan the event_type column after you run this. You should see all the
> types listed above. If any are missing, check your join — you may be
> losing rows.

---

## Query 3 — Monthly Revenue Trend

**Business context:**
The events export tells you *what changed*. This query tells you *how much
cash came in each month*. These are two different things — and the
difference matters in finance.

An annual customer pays 12 months of revenue upfront in January. The events
table shows one "created" event in January. But that customer's invoices
show one large payment in January and nothing for 11 months. The monthly
invoice trend captures actual cash collections — what actually hit the bank.

This query produces the trend line you will chart in Excel: 26 months of
paid revenue with a running total and month-over-month change.

**Your task:**
Using a CTE, calculate monthly paid revenue from the `invoices` table.
Then add window functions for the running total and month-over-month comparison.

**Structure:**

```sql
WITH monthly_revenue AS (

    -- Step 1: group paid invoices by month
    -- DATE_TRUNC to get the month bucket
    -- SUM(subtotal) for revenue
    -- COUNT(*) for invoice count
    -- WHERE payment_status = 'paid'

)

-- Step 2: add window functions on top of the CTE
SELECT
    TO_CHAR(month, 'YYYY-MM')  AS month,
    invoice_count,
    revenue,
    -- running total using SUM() OVER
    -- previous month revenue using LAG()
    -- month-over-month % change using both
FROM monthly_revenue
ORDER BY month;
```

**Return these columns, in this order:**

| Column | Calculation | Notes |
|---|---|---|
| month | `TO_CHAR(month, 'YYYY-MM')` | Format the DATE_TRUNC result |
| invoice_count | `COUNT(*)` in CTE | How many invoices were paid that month |
| revenue | `SUM(subtotal)` in CTE | Total paid revenue that month |
| running_total | `SUM(revenue) OVER (ORDER BY month)` | Cumulative paid revenue to date |
| prev_month_revenue | `LAG(revenue) OVER (ORDER BY month)` | Previous month's revenue (NULL for first row) |
| mom_pct_change | `ROUND((revenue - prev) / prev * 100, 1)` | Month-over-month % change (NULL for first row) |

> For `mom_pct_change`, reference your LAG window function inline rather
> than repeating the full `LAG()` expression. You can do this by wrapping
> the whole SELECT in a derived table or by accepting that you will write
> the LAG expression twice. Either approach is fine.

**Self-check:**

| Check | Expected |
|---|---|
| Row count | **26 rows** (one per month, Jan 2024 – Feb 2026) |
| First row month | 2024-01 |
| Last row month | 2026-02 |
| Last row running_total | **$2,475,630.00** |
| First row prev_month_revenue | NULL |
| First row mom_pct_change | NULL |

> The running total in the last row is the total paid invoice revenue
> since the company's first customer in January 2024. Every row you
> build in Excel for the trend chart comes from this output.

---

## Submission Checklist

Before you submit your SQL files, verify:

- [ ] Query 1: 51 rows, SUM(mrr) = $144,185.50, region column present
- [ ] Query 2: 97 rows, all event types present, no missing rows
- [ ] Query 3: 26 rows, last running_total = $2,475,630.00, first two window columns NULL

All three checks must pass. If any fail, fix the query before submitting.

**Three files to commit:**
```
sql/mrr_snapshot.sql      (updated — region column added)
sql/mrr_events.sql        (new)
sql/mrr_trend.sql         (new)
```

Branch: `submission/sql-03-excel-data-pull`

---

## After Submission Is Approved — Import to Excel

Once your instructor confirms all three self-checks pass, do the following.

> **Do not import until your queries are validated.**
> Wrong data in Excel produces wrong charts. The self-checks exist for this reason.

### Step 1 — Export each query to CSV

In DBeaver, after running each query:
1. Right-click anywhere in the results grid
2. Select **Export Data**
3. Choose **CSV**
4. File name: `mrr_snapshot.csv`, `mrr_events.csv`, `mrr_trend.csv`
5. Settings: comma delimiter, include column headers, UTF-8 encoding
6. Click through to export

### Step 2 — Open the workbook

Open `idynamics_mrr_workbook.xlsx`.

### Step 3 — Paste into [RAW] Snapshot

1. Navigate to the `[RAW] Snapshot` tab
2. Open `mrr_snapshot.csv` in Excel (separate window)
3. Select all data (Ctrl+A), copy (Ctrl+C)
4. In the workbook, click cell A1 of `[RAW] Snapshot`
5. **Paste Special → Values only** (Ctrl+Shift+V or right-click → Paste Special → Values)
6. Format as Excel Table: Ctrl+T, confirm range, name it `tbl_Snapshot`
7. Verify: the check cell below the table `=SUM(tbl_Snapshot[mrr])` shows **$144,185.50**

### Step 4 — Paste into [RAW] Waterfall

The `[RAW] Waterfall` tab holds both events and trend data:

**Upper section — Events (tbl_Movements):**
1. Paste `mrr_events.csv` starting at row 2 (row 1 has the label "Events Export")
2. Format as Excel Table, name it `tbl_Movements`
3. Verify row count = 97

**Lower section — Monthly Trend (tbl_Monthly):**
1. Leave a blank row gap below `tbl_Movements`
2. Paste `mrr_trend.csv` below that
3. Format as Excel Table, name it `tbl_Monthly`
4. Verify: 26 rows, last running_total = $2,475,630.00

### Step 5 — Confirm and close

Once both RAW tabs are populated and the self-checks pass, save the workbook.
You are ready for the Excel build assignment.

---

## A Note on What Comes Next

The events export you just built has a row for every change that ever
happened to a subscription. In the next assignment, you will open Excel
and classify each row:

- A `created` event with no prior history → **New MRR**
- A `created` event where the customer previously cancelled → **Reactivation**
- A `seats_change` where new_value > old_value → **Expansion**
- A `seats_change` where new_value < old_value → **Contraction**
- A `cancelled` event → **Churned MRR**

That classification logic — and the MRR delta calculation for each row —
will be IF() and XLOOKUP() formulas in Excel. The waterfall chart builds
from there.

The SQL got the data out. Excel tells the story.

---

*Idynamics Finance Analyst Training Program*
*SQL Assignment 03 — Excel Data Pull*
*March 2026*
