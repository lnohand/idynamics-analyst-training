# Excel Assignment 07 — February 2026 Monthly Close
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** February close — same process, more interesting data
>
> Michael — January was clean. No churn, one new customer, everything
> in line. February has more moving pieces: two new customers, one
> subscription that churned, and an S&M line that ran over plan.
>
> Same structure as January. New tab, same sections: waterfall, P&L,
> KPIs, commentary. Then update the KPI Tracker and WaterfallData tabs
> so everything stays current.
>
> Before I send the data, I need to know you understand what you're
> looking at. Answer the questions below in #finance first.
>
> — David

---

## What You're Building

Four additions to your existing workbook (`06_actual_vs_forecast.xlsx`):

1. **Feb 2026 A vs F tab** — new tab with waterfall, P&L, KPIs section, and management commentary
2. **KPI Tracker tab update** — fill in the Feb 2026 column (headers already exist)
3. **WaterfallData tab update** — add 7 new rows for February below the existing Jan rows

This is the same monthly workflow you ran in January. The process is the
same — what changes is the data, and what changes in the data tells the story.

---

## Part 1 — SQL: Pull February Actuals

Before you touch Excel, pull the numbers from the database.

### MRR Snapshot Query

Run your standard MRR snapshot query with the date filter set to
`'2026-02-28'`. This gives you every active subscription as of February
month-end.

What to look for in the results:

- **Active subscriptions:** 53 rows
- **Active customers:** 41 unique `customer_id` values
- **New subscriptions signed this month:**
  - SUB063 — Dynamic Retail Solutions (CUST041), Sales Hub, 28 seats × $110 = $3,080.00. Signed Feb 10.
  - SUB064 — Pacific Coast Analytics (CUST042), Analytics Growth, 32 seats × $95 = $3,040.00. Signed Feb 20.
- **Churned subscription:**
  - SUB050 — BC Media Group (CUST007), Analytics Starter, 15 seats × $45 × (1 − 12%) = $594.00. Cancelled Feb 20.

### Subscription Churn vs. Customer Churn — Read This Carefully

CUST007 (BC Media Group) cancelled SUB050 this month. That is subscription
churn — one subscription ended.

**CUST007 is not a lost customer.** They still have SUB007 (Marketing Pro)
active. You will see CUST007 in your February snapshot. Active customers
stays at 41, not 40.

This distinction matters. Subscription churn reduces MRR. Customer churn
means you lost the relationship entirely. They are not the same thing. Note
it in your commentary — David will ask about it.

### COGS Query

Run this query exactly as written:

```sql
SELECT ROUND(SUM(
    s.seats * s.cost_per_seat * (1 - s.discount_percent / 100.0)
    * CASE WHEN s.billing_cycle = 'Annual' THEN 1.0/12 ELSE 1 END
), 2) AS actual_cogs
FROM subscriptions s
WHERE s.start_date     <= '2026-02-28'
  AND (s.cancelled_date IS NULL OR s.cancelled_date > '2026-02-28');
```

This pulls every active subscription as of Feb 28 and applies the same
cost-per-seat logic you've seen in the engine. Annual subscriptions are
divided by 12 to get the monthly COGS allocation.

### Self-Check — Part 1

| Check | Expected |
|-------|---------|
| Active subscriptions (Feb 28 snapshot) | 53 |
| Active customers (unique customer_ids) | 41 |
| Actual COGS from query | $45,091.65 |
| New subscription count this month | 2 |
| Churned subscription | SUB050 (CUST007 / BC Media Group) |
| Is CUST007 a lost customer? | No — SUB007 still active |

---

## Part 2 — MRR Waterfall (Feb 2026 A vs F Tab)

### Create the Tab

Add a new tab to your workbook. Name it exactly: `Feb 2026 A vs F`

### Opening MRR

February's opening MRR is January's actual closing MRR: **$144,779.50**.

This is not the plan's original opening. It is the number your January tab
produced. Reference it with a formula from your January tab — do not type the
number in twice.

### Build the Waterfall

Build the same structure as January: Actual, Forecast, $ Variance,
% Variance, F/U columns. Use these exact values:

| Movement | Actual | Forecast | $ Variance | % Variance | F/U |
|----------|--------|----------|-----------|-----------|-----|
| Opening MRR | $144,779.50 | $144,779.50 | $0 | 0.0% | — |
| New MRR | $6,120.00 | $4,000.00 | $2,120.00 | 53.0% | F |
| Expansion MRR | $0.00 | $715.35 | ($715.35) | (100.0%) | U |
| Contraction MRR | $0.00 | $0.00 | $0 | n/a | — |
| Churned MRR | $594.00 | $953.80 | $359.80 | 37.7% | F |
| Net New MRR | $5,526.00 | $3,761.55 | $1,764.45 | 46.9% | F |
| Closing MRR | $150,305.50 | $148,541.05 | $1,764.45 | 1.2% | F |
| Closing ARR | $1,803,666.00 | $1,782,492.60 | $21,173.40 | 1.2% | F |

**Churn variance note:** Churned MRR is $359.80 favorable. Less churn than
forecast is favorable — you kept more revenue than the plan expected. Do not
mark it unfavorable just because churn happened. Less churn than plan = F.

**Expansion variance note:** Expansion MRR is ($715.35) unfavorable. Plan
expected $715.35 in expansion from existing customers. None materialized.

### Self-Check — Part 2

| Movement | Actual | $ Variance | F/U |
|----------|--------|-----------|-----|
| New MRR | $6,120.00 | $2,120.00 | F |
| Expansion MRR | $0.00 | ($715.35) | U |
| Churned MRR | $594.00 | $359.80 | F |
| Net New MRR | $5,526.00 | $1,764.45 | F |
| Closing MRR | $150,305.50 | $1,764.45 | F |
| Closing ARR | $1,803,666.00 | $21,173.40 | F |

---

## Part 3 — P&L (Feb 2026 A vs F Tab)

Add the P&L section below the waterfall on the same tab.

Revenue equals Closing MRR — reference the waterfall row, do not
re-type the number.

COGS comes from your SQL query result: **$45,091.65**.

| Line | Actual | Forecast | $ Variance | % Variance | F/U |
|------|--------|----------|-----------|-----------|-----|
| Revenue | $150,305.50 | $148,541.05 | $1,764.45 | 1.2% | F |
| COGS | ($45,091.65) | ($44,562.32) | ($529.33) | (1.2%) | U |
| Gross Profit | $105,213.85 | $103,978.74 | $1,235.12 | 1.2% | F |
| Gross Margin % | 70.0% | 70.0% | 0.0 pp | — | — |
| S&M | ($31,000.00) | ($30,000.00) | ($1,000.00) | (3.3%) | U |
| R&D + G&A | ($44,000.00) | ($44,000.00) | $0 | 0.0% | — |
| Total OpEx | ($75,000.00) | ($74,000.00) | ($1,000.00) | (1.4%) | U |
| EBITDA | $30,213.85 | $29,978.74 | $235.12 | 0.8% | F |
| EBITDA Margin % | 20.1% | 20.2% | (0.1 pp) | — | U |

**Important — read the variance signs carefully:**

Revenue beat plan by $1,764.45. That's favorable. But both COGS and S&M
ran over plan. COGS was $529.33 over (unfavorable). S&M was $1,000.00 over —
Lisa flagged this: contract events support ran $1,000 above budget.

EBITDA is favorable by only $235.12. The revenue beat almost entirely offset
the COGS and S&M overruns. Gross margin % held at 70.0%, so the COGS
overage was proportional to revenue — no margin degradation. But EBITDA
margin ticked down 0.1 pp because S&M ran hot.

Don't hide this. A $235 EBITDA beat sounds good until you explain the
components. Your commentary should say that.

**Forecast source:** COGS forecast = $44,562.32. This comes from the
plan's assumption of 30% COGS as a percent of forecast revenue
($148,541.05 × 30% = $44,562.32).

### Self-Check — Part 3

| Line | Actual | $ Variance | F/U |
|------|--------|-----------|-----|
| Revenue | $150,305.50 | $1,764.45 | F |
| COGS | ($45,091.65) | ($529.33) | U |
| Gross Profit | $105,213.85 | $1,235.12 | F |
| Gross Margin % | 70.0% | 0.0 pp | — |
| S&M | ($31,000.00) | ($1,000.00) | U |
| Total OpEx | ($75,000.00) | ($1,000.00) | U |
| EBITDA | $30,213.85 | $235.12 | F |
| EBITDA Margin % | 20.1% | (0.1 pp) | U |

---

## Part 4 — KPIs Section (Feb 2026 A vs F Tab)

Add the KPIs section below the P&L on the same tab.

Section header: **February 2026 — SaaS KPIs**

Build the following table. Wire cells to this tab wherever possible —
do not type numbers in twice.

| Metric | Value | Notes |
|--------|-------|-------|
| Active Customers | 41 | From SQL snapshot — CUST007 cancelled SUB050 but retains SUB007 (Marketing Pro). Customer count is 41, not 40. This is subscription churn, not customer churn. |
| Active Subscriptions | 53 | From SQL snapshot |
| ARPA | $3,665.99 | Reference closing MRR and active customers from this tab |
| Gross Margin | 70.0% | Reference P&L cells |
| GRR | 99.6% | Use the same formula you built in January |
| NRR | 99.6% | Use the same formula you built in January |
| Quick Ratio | 10.3x | Use the same formula you built in January |
| S&M (actual) | $31,000 | From Lisa's monthly close message — $1,000 over plan |
| CAC — this month | $15,500 | Use the same formula you built in January |
| CAC — Q1 to date | $20,333 | Cumulative S&M ÷ cumulative new customers acquired in Q1 to date |
| LTV | — | Quarterly metric — calculated at Q1 close |
| LTV:CAC | — | Quarterly metric — calculated at Q1 close |
| CAC Payback | — | Quarterly metric — calculated at Q1 close |

**NRR = GRR this month.** NRR and GRR are both 99.6%. That is not a typo.
When there is zero expansion MRR and zero contraction MRR, the only
difference between GRR and NRR is expansion — and there was none. The two
metrics converge. This is normal for months with no upsells.

**CAC Q1 to date:** $61,000 total S&M (Jan $30,000 + Feb $31,000) divided
by 3 new customers acquired in Q1 so far (1 in January + 2 in February).

Add a note below LTV:
> "LTV, LTV:CAC, and CAC Payback are calculated quarterly using the
> trailing 12-month gross churn rate. See Q1 Roll-Up (coming in Excel 08)."

### Self-Check — Part 4

| Metric | Expected |
|--------|---------|
| Active Customers | 41 |
| Active Subscriptions | 53 |
| ARPA | $3,665.99 |
| GRR | 99.6% |
| NRR | 99.6% |
| Quick Ratio | 10.3x |
| CAC (monthly) | $15,500 |
| CAC (Q1 to date) | $20,333 |

---

## Part 5 — Management Commentary (Feb 2026 A vs F Tab)

Add a commentary section below the KPIs. This is the paragraph (or bullet
list) David reads first. Write it as if you are reporting to him — because
you are.

Cover four things in this order:

1. **Overall result** — headline MRR and EBITDA vs plan, one sentence each.
2. **Revenue drivers** — what drove New MRR, and why Expansion was zero.
3. **Churn** — name the customer and subscription. Explain why Churned MRR
   is favorable vs plan. Make clear whether this is subscription churn or
   customer churn and why it matters.
4. **Costs** — which lines ran over, by how much, and what that did to
   EBITDA margin.

**Tone guidance:** Don't bury the bad news. Revenue beat is real, but two
cost lines ran over. A reader who only sees "$235 favorable EBITDA" is
missing the story. Lead with the beat, explain the offsets, and name the
S&M line specifically. David already knows the numbers — your commentary
should tell him what they mean.

---

## Part 6 — Update KPI Tracker Tab

Go to the `KPI Tracker` tab. The Feb 2026 column has headers but no values.
Fill in the February column now.

**Rule: do not overwrite the January column.** Those cells should still
reference the `Jan 2026 A vs F` tab. Do not touch them.

For February, you can type the values directly or reference cells on the
`Feb 2026 A vs F` tab — either works, but formula references are preferred.

Fill in these values:

| Metric | Feb 2026 Value |
|--------|---------------|
| Closing MRR | $150,305.50 |
| Active Customers | 41 |
| ARPA | $3,665.99 |
| Gross Margin | 70.0% |
| GRR | 99.6% |
| NRR | 99.6% |
| Quick Ratio | 10.3x |
| S&M (actual) | $31,000 |
| CAC — monthly | $15,500 |
| CAC — trailing Q (Q1 to date) | $20,333 |

The Mar 2026 and Q1 2026 columns remain empty. Don't fill them in —
March hasn't closed yet.

### Self-Check — Part 6

| Check | Expected |
|-------|---------|
| Feb 2026 Closing MRR in tracker | $150,305.50 |
| Feb 2026 Active Customers | 41 |
| Feb 2026 ARPA | $3,665.99 |
| Feb 2026 Quick Ratio | 10.3x |
| Jan 2026 column still formula-referenced | ✅ |

---

## Part 7 — Update WaterfallData Tab

Go to the `WaterfallData` tab. You have 7 rows for January. Add 7 more
rows directly below them for February.

Add these rows exactly:

| Month | Movement | Actual | Forecast | Variance |
|-------|----------|--------|----------|---------|
| Feb 2026 | Opening MRR | 144779.50 | 144779.50 | 0 |
| Feb 2026 | New MRR | 6120.00 | 4000.00 | 2120.00 |
| Feb 2026 | Expansion MRR | 0.00 | 715.35 | -715.35 |
| Feb 2026 | Contraction MRR | 0.00 | 0.00 | 0.00 |
| Feb 2026 | Churned MRR | 594.00 | 953.80 | 359.80 |
| Feb 2026 | Net New MRR | 5526.00 | 3761.55 | 1764.45 |
| Feb 2026 | Closing MRR | 150305.50 | 148541.05 | 1764.45 |

**Sign convention for the Variance column:** The variance always represents
impact on revenue vs plan — positive means favorable, negative means
unfavorable. For churn rows, less churn than forecast is favorable, so the
variance is positive even though actual < forecast. If you calculate
Actual − Forecast for Churned MRR you get −359.80 — that is wrong here.
Enter 359.80.

The Excel Table (`WaterfallData`) expands automatically when you add rows
below the existing data. No reformatting needed — just type in the next row
and the table picks it up.

After saving, refresh Power BI (if connected) to pull in the February data.
The Month slicer will now show both Jan 2026 and Feb 2026.

### Self-Check — Part 7

| Check | Expected |
|-------|---------|
| Total rows in WaterfallData table | 14 (7 Jan + 7 Feb) |
| Feb Closing MRR row — Actual | 150305.50 |
| Feb Closing MRR row — Variance | 1764.45 |
| Feb New MRR row — Variance | 2120.00 |
| Feb Expansion MRR row — Variance | -715.35 |

---

## Part 8 — Git Workflow

### New assignment = new branch. Always.

The branch from Excel 06b (`student/excel_06b_kpis_tracker`) is merged
and done. Do not push new work to it. Start fresh:

```
git checkout main
git pull origin main
git checkout -b student/excel_07_february_close
```

Work on this branch. When you're ready to submit:

```
git add submissions/excel/06_actual_vs_forecast.xlsx
git commit -m "Add: 07 — February 2026 close (A vs F tab, KPI Tracker, WaterfallData)"
git push origin student/excel_07_february_close
```

Open a PR from `student/excel_07_february_close` → `main`.

**One branch per assignment. One PR per assignment. Never reuse a merged branch.**

---

### Keep your personal reference files current

Before you push, update your `my-notes/` files with anything new from this assignment:

| File | What to add |
|------|------------|
| `my-notes/sql_queries.sql` | February COGS query with date filter and comment |
| `my-notes/kpi_definitions.md` | GRR vs NRR — when they converge and why; Quick Ratio formula; CAC Q1-to-date calculation |
| `my-notes/excel_techniques.md` | Cross-tab formula references; adding rows to an Excel Table |
| `my-notes/git_commands.md` | Nothing new this cycle — but verify your workflow notes are current |

---

## Submission

Same workbook, same file:
```
submissions/excel/06_actual_vs_forecast.xlsx
```

Open a PR from `student/excel_07_february_close` → `main` with this description:

```
## 07 — February 2026 Close

- Feb 2026 A vs F tab added (waterfall, P&L, KPIs, commentary)
- KPI Tracker updated with February column
- WaterfallData updated with 7 new February rows (14 total)
- my-notes/ updated with new KPI definitions and COGS query

## Self-check

Closing MRR:              $___________
vs Plan (Net New MRR):    $___________ ___
Active Customers:         ___
ARPA:                     $___________
GRR:                      ___%
NRR:                      ___%
Quick Ratio:              ___x
CAC (monthly):            $___________
CAC (Q1 to date):         $___________
WaterfallData total rows: ___
KPI Tracker Feb col:      ✅ / not done
```

---

## Final Self-Check

Before you push, confirm every number:

| Check | Expected |
|-------|---------|
| Closing MRR | $150,305.50 |
| vs Plan (Net New MRR) | $1,764.45 F |
| Active Customers | 41 |
| ARPA | $3,665.99 |
| GRR | 99.6% |
| NRR | 99.6% |
| Quick Ratio | 10.3x |
| CAC (monthly) | $15,500 |
| WaterfallData total rows | 14 (7 Jan + 7 Feb) |
| KPI Tracker Feb col filled | ✅ |

---

*Excel Assignment 07 — February 2026 Monthly Close*
*Idynamics Finance Analyst Training Program*
*April 2026*
