# Excel Assignment 06b — KPIs, Tracker, and WaterfallData
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Three more things before January is really done
>
> Michael — the A vs F tab tells me what happened to revenue and profit.
> But every month I also need to see the unit economics: how much we're
> paying to acquire customers, how well we're retaining them, what each
> customer is worth. These sit right next to the P&L.
>
> You're also going to build two new tabs that will power everything
> going forward. One tracks KPIs across all months so we can see trends.
> The other feeds directly into Power BI. Build them right once — you
> just add rows each month after that.
>
> Same workbook. Three additions.
>
> — David

---

## Before You Start — Answer These in Slack

Post your answers in **#finance** before starting. One sentence each.
David will not share the brief details until you've answered.

> **Q1 — ARPA denominator**
> When calculating ARPA, why do we divide by active *customers* and not
> active *subscriptions*? What would happen to the number if we used
> subscriptions, and why would that mislead us?

> **Q2 — GRR vs NRR**
> What is the difference between GRR and NRR? Give me a concrete example —
> a month where they would be different values. Which is higher in that
> scenario?

> **Q3 — Monthly CAC**
> January had one new customer and $30,000 in S&M spend. Monthly CAC = $30,000.
> Is that a useful number to put in a board slide? Why or why not?

> **Q4 — Why a structured table?**
> I'm asking you to format WaterfallData as an Excel Table (not just a
> range). What does that give you that a plain range doesn't?
> When February closes, what will you do to update it?

---

## What You're Building

Three additions to your existing workbook (`06_actual_vs_forecast.xlsx`):

1. **KPIs section** — added to the bottom of your `Jan 2026 A vs F` tab
2. **KPI Tracker tab** — new tab, all months as columns, accumulates through Q1
3. **WaterfallData tab** — new tab, structured Excel Table, Power BI source

---

## Addition 1 — KPIs Section on Jan 2026 A vs F Tab

Below your management commentary, add a section header:

**January 2026 — SaaS KPIs**

Then build this table. Calculate every metric from the numbers already
in your tab — no new SQL needed for most of them.

| Metric | Value | Notes |
|--------|-------|-------|
| Active Customers | 39 | Unique customer_ids in Jan 31 snapshot — from your SQL |
| Active Subscriptions | 52 | Row count in Jan 31 snapshot — from your SQL |
| ARPA | ? | Closing MRR ÷ Active Customers |
| Gross Margin | 70.0% | (Revenue − COGS) ÷ Revenue — already in your P&L |
| GRR | ? | (Opening MRR − Churned MRR − Contraction MRR) ÷ Opening MRR |
| NRR | ? | (Opening MRR + Expansion − Contraction − Churn) ÷ Opening MRR |
| Quick Ratio | N/A — no losses | (New + Expansion) ÷ (Churn + Contraction) — denominator is $0 |
| S&M (actual) | $30,000 | From Lisa's monthly close message |
| CAC — this month | $30,000 * | S&M ÷ New Customers acquired this month |
| LTV | — † | Quarterly metric — calculated at Q1 close |
| LTV:CAC | — † | Quarterly metric — calculated at Q1 close |
| CAC Payback | — † | Quarterly metric — calculated at Q1 close |

**\* Monthly CAC note** — add a note cell directly below the CAC row:
> "Monthly CAC is noisy with one customer. Q1 CAC will be calculated
> after March closes ($90,000 S&M ÷ 4 customers = $22,500)."

**† Quarterly metrics** — add a note cell below LTV:
> "LTV, LTV:CAC, and CAC Payback are calculated quarterly using the
> trailing 12-month gross churn rate. See Q1 Roll-Up (coming in 06d)."

**Quick Ratio** — January had zero churn and zero contraction. The
denominator is $0. Do not leave the cell blank or show a formula error.
Write the text "N/A — no losses" in the cell. A blank says nothing.
"N/A — no losses" tells me something good happened.

### Self-Check — KPIs

| Metric | Expected |
|--------|---------|
| ARPA | $3,712.29 |
| GRR | 100.0% |
| NRR | 100.0% |
| Quick Ratio | N/A — no losses |
| CAC (monthly) | $30,000 |

---

## Addition 2 — KPI Tracker Tab

Create a new tab called `KPI Tracker`.

This tab shows all months as columns. Right now it has one column (January).
When February closes, you add a February column. When March closes, you add
March. A Q1 column appears after March with the quarterly metrics.

Build this structure:

| Metric | Jan 2026 | Feb 2026 | Mar 2026 | Q1 2026 |
|--------|---------|---------|---------|---------|
| Closing MRR | $144,779.50 | | | |
| Active Customers | 39 | | | |
| ARPA | $3,712.29 | | | |
| Gross Margin | 70.0% | | | |
| GRR | 100.0% | | | |
| NRR | 100.0% | | | |
| Quick Ratio | N/A — no losses | | | |
| S&M (actual) | $30,000 | | | |
| CAC — monthly | $30,000 * | | | |
| CAC — trailing Q | — | — | — | $22,500 |
| LTV | — | — | — | (calc at Q1) |
| LTV:CAC | — | — | — | (calc at Q1) |
| CAC Payback | — | — | — | (calc at Q1) |

**Rules for this tab:**
- Jan column values must reference your `Jan 2026 A vs F` tab — do not
  type the numbers in twice. Use formulas: `='Jan 2026 A vs F'!B8`
- Feb and Mar columns: leave the cells empty for now. Build the column
  headers and row labels — just no values yet.
- Q1 column: quarterly metrics only. Leave monthly metrics blank in Q1.
- Add a small note below the table:
  > "LTV, LTV:CAC, and CAC Payback appear in the Q1 column only.
  > Monthly figures are too sensitive to single-month churn swings
  > to be meaningful."

---

## Addition 3 — WaterfallData Tab

Create a new tab called `Waterfall Data` (two words — this is the sheet name).

On this tab, build a table with exactly these columns:

| Month | Movement | Actual | Forecast | Variance |
|-------|----------|--------|----------|---------|
| Jan 2026 | Opening MRR | 143069.50 | 143069.50 | 0 |
| Jan 2026 | New MRR | 1710.00 | 4000.00 | -2290.00 |
| Jan 2026 | Expansion MRR | 0.00 | 715.35 | -715.35 |
| Jan 2026 | Contraction MRR | 0.00 | 0.00 | 0.00 |
| Jan 2026 | Churned MRR | 0.00 | 953.80 | -953.80 |
| Jan 2026 | Net New MRR | 1710.00 | 3761.55 | -2051.55 |
| Jan 2026 | Closing MRR | 144779.50 | 146831.05 | -2051.55 |

Then format this range as an **Excel Table**:
- Select the data including headers
- Insert → Table (or Ctrl+T)
- Tick "My table has headers"
- In the Table Design tab, rename it to `WaterfallData` — one word, no space

The sheet is called `Waterfall Data`. The table inside it is called
`WaterfallData`. Power BI will connect to the table name.

When February closes, you will add 7 more rows (same structure, Month = "Feb 2026").
The table expands automatically — no reformatting needed.

### Self-Check — WaterfallData

| Check | Expected |
|-------|---------|
| Row count (Jan only) | 7 rows |
| Table name | WaterfallData |
| Closing MRR row, Actual column | 144779.50 |
| Closing MRR row, Variance column | -2051.55 |

---

## Submission

Same workbook, same file:
```
submissions/excel/06_actual_vs_forecast.xlsx
```

Same branch — push to `student/excel_06_actual_vs_forecast_jan2026` or open
a new branch `student/excel_06b_kpis_tracker`. Open a PR with:

```
## 06b additions
- KPIs section added to Jan 2026 A vs F tab
- KPI Tracker tab created (Jan column, structure for Feb/Mar/Q1)
- WaterfallData tab created (Excel Table, 7 Jan rows)

## KPI self-check
ARPA:            $___________
GRR:             ___%
NRR:             ___%
Quick Ratio:     ___________
CAC (monthly):   $___________
WaterfallData row count: ___
```

---

*Excel Assignment 06b — KPIs, Tracker, and WaterfallData*
*Idynamics Finance Analyst Training Program*
*April 2026*
