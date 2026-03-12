# Excel MRR Workbook — Structure & Build Plan
**Idynamics Finance Analyst Training Program | March 2026**

> **Purpose:** This document defines the complete structure of the Excel MRR workbook — every tab, every data input, every formula, and every chart. It is the reference for building the workbook and for verifying the final output. It must be kept up to date as the build progresses.

---

## 1. Overview

The workbook is the primary deliverable for Excel Module 1 (MRR) and Excel Module 2 (Cohort Analysis). It takes SQL query outputs as inputs, builds all analysis in structured tabs, and surfaces a single board-ready Dashboard tab.

### Workbook at a glance

| Tab | Type | Source | Purpose |
|---|---|---|---|
| README | Static | Manual | Documentation, data dictionary, self-check values |
| [RAW] Snapshot | Data | Input A | 49-row active MRR snapshot — do not edit |
| [RAW] Waterfall | Data | Inputs B+C | Movement detail + monthly totals — do not edit |
| [RAW] Cohort | Data | Input D | Customer-month cohort data (future SQL) |
| MRR Waterfall | Analysis | RAW tabs | 5-movement waterfall table and chart |
| MRR Mix | Analysis | RAW Snapshot | Plan / owner / region / billing cycle breakdowns |
| MRR Trend | Analysis | RAW Waterfall | 26-month time series and MoM chart |
| Retention | Analysis | RAW + Waterfall | GRR, NRR, logo churn calculations and charts |
| Cohort — Cust. | Analysis | RAW Cohort | Customer retention % heatmap grid |
| Cohort — Rev. | Analysis | RAW Cohort | Revenue NRR heatmap grid |
| Dashboard | Output | All analysis | Board-ready KPIs, charts, and summary |

### Self-check values

These numbers must reconcile across every tab that references them. If anything does not match, the data or formula is wrong.

| Metric | Value |
|---|---|
| Active MRR (current) | $142,110.50 |
| Active subscriptions | 49 |
| Months in time series | 26 (Jan 2024 – Feb 2026) |
| Total subscription events | 97 |
| Total invoices | 764 |
| Closing MRR (last row of waterfall) | $142,110.50 — must match active MRR |

---

## 2. SQL Inputs

All data enters the workbook through SQL query exports. No manual data entry. The four inputs below are pasted into the RAW tabs as plain values and never modified.

---

### Input A — MRR Snapshot (Deliverable 1)

| | |
|---|---|
| **Query file** | `sql/mrr_snapshot.sql` |
| **Row count** | 49 rows (one per active subscription) |
| **Table name** | `tbl_Snapshot` |
| **Feeds tabs** | MRR Mix, Dashboard |

| Column | Type | Notes |
|---|---|---|
| subscription_id | VARCHAR | Primary identifier |
| customer_id | VARCHAR | Foreign key to customers |
| company_name | VARCHAR | Joined from customers table |
| account_owner | VARCHAR | Joined from customers table |
| region | VARCHAR | Joined from customers table — Eastern, Western, or Central |
| plan_name | VARCHAR | Analytics Starter / Growth / Enterprise, Sales Hub, Marketing Pro, Platform Suite |
| billing_cycle | VARCHAR | Monthly or Annual |
| mrr | NUMERIC | Calculated: `seats x price x (1 - discount/100)` [/12 if Annual]. Rounded to 2 dp. |

> **No date column.** Input A is a point-in-time snapshot representing current active subscriptions. There is no date column because every row is as-of today. The time dimension lives entirely in Input C.

---

### Input B — Waterfall Movements (Step 3 output)

| | |
|---|---|
| **Query file** | `sql/mrr_waterfall.sql` — Step 3 SELECT |
| **Row count** | ~35 rows (long format — multiple rows per month) |
| **Table name** | `tbl_Movements` |
| **Feeds tabs** | MRR Waterfall, Retention |

| Column | Type | Notes |
|---|---|---|
| month | VARCHAR | YYYY-MM format |
| movement_type | VARCHAR | New \| Expansion \| Contraction \| Churned \| Reactivation |
| mrr | NUMERIC | Positive for gains, negative for Contraction and Churned |

---

### Input C — Monthly Totals (Step 4 output)

| | |
|---|---|
| **Query file** | `sql/mrr_waterfall.sql` — Step 4 SELECT |
| **Row count** | 26 rows (one per month) |
| **Table name** | `tbl_Monthly` |
| **Feeds tabs** | MRR Waterfall (opening/closing), MRR Trend, Retention |

| Column | Type | Notes |
|---|---|---|
| month | VARCHAR | YYYY-MM format |
| net_mrr_change | NUMERIC | Sum of all movements in that month |
| total_mrr | NUMERIC | Running total — closing MRR after all movements applied |

---

### Input D — Cohort Data (separate SQL — future)

| | |
|---|---|
| **Query file** | `sql/mrr_cohort.sql` (not yet assigned) |
| **Row count** | ~500+ rows (one per customer per active month) |
| **Table name** | `tbl_Cohort` |
| **Feeds tabs** | Cohort — Customers, Cohort — Revenue |

| Column | Type | Notes |
|---|---|---|
| cohort_month | VARCHAR | Month the customer first subscribed |
| customer_id | VARCHAR | Customer identifier |
| months_since_signup | INTEGER | 0 = signup month, 1 = one month later, etc. |
| active | BOOLEAN | TRUE if customer had an active subscription that month |
| mrr | NUMERIC | Customer MRR for that month (0 if churned) |

---

## 3. Tab Details

---

### Tab 1 — README

**Static documentation tab. No formulas. Written reference that lives inside the workbook.**

Contains the following sections, each in a clearly labeled block:

- **Tab index:** One-line description of every tab and what it is used for.
- **Data dictionary:** Definition of every column in every RAW table, units, and the MRR formula.
- **Self-check values:** Active MRR $142,110.50, 49 active subs, 26 months, 97 events. These are the reconciliation anchors.
- **Color legend:** The five movement colors used consistently across all charts (see Section 4).
- **How to refresh:** Steps for pasting a new SQL export when the data updates — which cells to select, how to paste as values only.

---

### Tab 2 — [RAW] Snapshot

**Paste of Input A. Named `tbl_Snapshot`. Source of truth for all MRR mix analysis.**

- **Format as Excel Table:** Ctrl+T on paste. Name it `tbl_Snapshot`. This enables structured references in the Mix pivots.
- **Freeze row 1.** Column headers must always be visible.
- **No edits ever:** This tab is a landing zone. Any correction goes back to the SQL query, not here.
- **Self-check on paste:** Add a check cell below the table: `=SUM(tbl_Snapshot[mrr])` — must equal **$142,110.50**. Format it with a green/red conditional rule.

---

### Tab 3 — [RAW] Waterfall

**Two paste tables on one tab: movement detail (Input B) and monthly totals (Input C).**

Two separate tables, clearly labeled with bold headers above each:

- **Table 1 — Movements (Input B):** Named `tbl_Movements`. Columns: month | movement_type | mrr. Approximately 35 rows in long format.
- **Table 2 — Monthly totals (Input C):** Named `tbl_Monthly`. Columns: month | net_mrr_change | total_mrr. Exactly 26 rows.

Keep them on the same tab because they share a time axis — useful to scan side by side when debugging the waterfall.

- **Self-check:** Last row of `tbl_Monthly[total_mrr]` must equal **$142,110.50**.

---

### Tab 4 — [RAW] Cohort

**Future paste of cohort SQL output. Tab exists now so Cohort tabs can reference it without broken links.**

Leave empty until the cohort SQL assignment is complete. Named `tbl_Cohort`. Expected ~500+ rows.

---

### Tab 5 — MRR Waterfall

**The hardest tab to build and the most important for board presentations.**

#### Step 1: Pivot the long-format data

Insert a PivotTable from `tbl_Movements`. Configure as follows:

| Pivot field | Zone |
|---|---|
| month | Rows |
| movement_type | Columns |
| mrr | Values (Sum) |

Result: one row per month, five movement-type columns. Contraction and Churned will show negative values. Missing combinations show as blank — leave them blank, do not zero-fill.

#### Step 2: Build the wide calculation table

To the right of the pivot, in a regular range (not inside the pivot), build this table. One row per month:

| Column | Formula logic |
|---|---|
| Opening MRR | `=XLOOKUP(prior month, tbl_Monthly[month], tbl_Monthly[total_mrr], 0)`. First month = 0. |
| New MRR | Reference from pivot column |
| Expansion MRR | Reference from pivot column |
| Contraction MRR | Reference from pivot column (negative value) |
| Churned MRR | Reference from pivot column (negative value) |
| Reactivation MRR | Reference from pivot column |
| Net MRR | `=SUM(New + Expansion + Contraction + Churned + Reactivation)` |
| Closing MRR | `=Opening MRR + Net MRR` |

> **Critical self-check:** Closing MRR in the last row (February 2026) must equal **$142,110.50**. If it does not, there is a missing event type or a formula error in the waterfall SQL.

#### Step 3: Waterfall chart

Chart type: Clustered Stacked Column. One series per movement type. X-axis = month.

- Positive movements (New, Expansion, Reactivation) stack upward from zero.
- Negative movements (Contraction, Churned) stack downward from zero.
- Apply the standard color coding defined in Section 4.
- Remove chart border. Remove gridlines. Add data labels on each segment.

#### Step 4: Running total line

Add a secondary series using Closing MRR as a line on a secondary axis. This places the running MRR curve on top of the waterfall bars — the standard format for investor and board presentations.

---

### Tab 6 — MRR Mix

**Four PivotTables from `tbl_Snapshot`. Each with its own chart. Answers: where does our MRR come from?**

#### Pivot 1 — By Plan

| PivotTable setting | Value |
|---|---|
| Source | tbl_Snapshot |
| Rows | plan_name |
| Values | Count of subscription_id (rename: Subs), Sum of mrr (rename: Total MRR) |
| Sort | Total MRR descending |
| Add | Calculated field: % of grand total for MRR column |

Chart: Horizontal bar chart sorted by MRR descending. Data labels showing dollar amount and percentage.

#### Pivot 2 — By Account Owner

Same structure as Pivot 1. Rows = `account_owner`. Chart = horizontal bar chart.

#### Pivot 3 — By Region

Same structure as Pivot 1. Rows = `region`. Three values: Eastern, Western, Central. Chart = horizontal bar chart. This cut identifies geographic concentration risk — if one region drives the majority of MRR, churn events there disproportionately impact the business.

#### Pivot 4 — By Billing Cycle

Rows = `billing_cycle`. Two segments only: Monthly and Annual. Chart = donut chart with data labels inside each segment showing sub count, total MRR, and percentage.

---

### Tab 7 — MRR Trend

**26-month time series. Two charts: total MRR trajectory and net monthly change.**

Source: `tbl_Monthly`. Extend the table with two calculated columns:

| Column | Formula | Notes |
|---|---|---|
| MoM % change | `=(C3-C2)/C2` wrapped in IFERROR | First row = blank. Format as percentage. |
| Reference line | `=$142,110.50` hard-coded in every row | Used for a flat 'current MRR' marker on Chart 1. |

#### Chart 1 — Total MRR over time

- Line chart. X-axis = month, Y-axis = total_mrr.
- Add a second flat line series from the reference column. Format as dashed gray. Label the right end `$142,110`.
- This chart shows trajectory and scale — the big picture.

#### Chart 2 — Net MRR change by month

- Column chart. Positive months in green, negative months in red.
- **Implementation:** Two series. Series A = `IF(net_mrr_change > 0, net_mrr_change, 0)` colored green. Series B = `IF(net_mrr_change < 0, net_mrr_change, 0)` colored red. Both as clustered columns on the same axis.
- This chart shows month-by-month volatility — which months were bad and by how much.

---

### Tab 8 — Retention

**GRR, NRR, and logo churn. The three metrics every SaaS investor deck includes.**

#### The three metrics

```
GRR = (Opening MRR - Churned MRR - Contraction MRR) / Opening MRR
```

GRR is capped at 100%. It measures how well the business holds existing revenue, ignoring any growth from existing customers. If GRR is unhealthy, expansion cannot save the business.

```
NRR = (Opening MRR - Churned MRR - Contraction MRR + Expansion MRR + Reactivation MRR) / Opening MRR
```

NRR can exceed 100%. A value above 100% means surviving customers grew faster than the business lost revenue to churn and contraction. This is the single number VCs focus on most in a Series A conversation.

```
Logo Churn Rate = Customers lost this month / Customers active at start of month
```

Dollar churn and logo churn tell different stories. Losing one $8,000/month customer (1 logo, high dollar impact) is very different from losing five $200/month customers (5 logos, lower dollar impact).

#### Additional SQL required

GRR and NRR pull directly from the waterfall pivot — no new SQL needed. Logo churn requires one additional SQL query:

```sql
-- sql/mrr_logo_churn.sql
SELECT
    TO_CHAR(DATE_TRUNC('month', event_date), 'YYYY-MM') AS month,
    COUNT(*) AS logos_churned
FROM subscription_events
WHERE event_type = 'cancelled'
GROUP BY DATE_TRUNC('month', event_date)
ORDER BY month;
```

Logos Added per month is derived from `tbl_Movements` — no extra SQL needed. New and Reactivation movements each add one logo. The COUNTIFS formula handles both:

```
=COUNTIFS(tbl_Movements[movement_type],"New",tbl_Movements[month],[this month])
 +COUNTIFS(tbl_Movements[movement_type],"Reactivation",tbl_Movements[month],[this month])
```

#### Main table — one row per month

| Column | Source | Formula |
|---|---|---|
| Month | tbl_Monthly | Reference |
| Opening MRR | Prior row closing | `=prior row Closing MRR` |
| Churned MRR | Waterfall pivot | Reference (absolute value) |
| Contraction MRR | Waterfall pivot | Reference (absolute value) |
| Expansion MRR | Waterfall pivot | Reference |
| Reactivation MRR | Waterfall pivot | Reference |
| Closing MRR | tbl_Monthly | Reference (verify = Opening + Net) |
| GRR | Calculated | `=(Opening - Churned - Contraction) / Opening` |
| NRR | Calculated | `=(Opening - Churned - Contraction + Expansion + Reactivation) / Opening` |
| Logos Added | tbl_Movements | `=COUNTIFS(New, month) + COUNTIFS(Reactivation, month)` |
| Logos Churned | Logo churn SQL paste | Reference from paste table |
| Active Logos (start) | Derived running count | `=prior row Active Logos (start) + prior row Logos Added - prior row Logos Churned`. First row: count of New events in month 1. |
| Logo Churn Rate | Calculated | `=Logos Churned / Active Logos (start)` |

#### Conditional formatting rules

| Column | Green | Amber | Red |
|---|---|---|---|
| GRR | >= 90% | 85% – 90% | < 85% |
| NRR | >= 100% | 90% – 100% | < 90% |
| Logo Churn Rate | < 0.5% | 0.5% – 1% | > 1% |

#### Charts on this tab

- **Chart 1 — NRR vs GRR over time:** Two lines on the same axis. Add a horizontal reference line at 100% labeled 'breakeven'. Months where NRR > 100% should be visually obvious at a glance.
- **Chart 2 — Logo churn rate by month:** Column chart. Add a horizontal benchmark line at 1% monthly labeled 'SMB benchmark'.
- **Chart 3 — Expansion vs Churned MRR:** Grouped column chart showing expansion and churned as two bars per month. Visualizes whether expansion is trending toward offsetting churn.

#### KPI summary row at top

Three summary cells formatted as KPI cards at the top of the tab:

- Trailing 12-month average NRR
- Trailing 12-month average GRR
- Trailing 12-month average logo churn rate

These three numbers are what goes in the board deck summary.

---

### Tab 9 — Cohort — Customers

**Customer retention % heatmap. Rows = cohort months. Columns = M0 through M25.**

Grid structure: 20 cohort rows (January 2024 through January 2026) x up to 26 month columns (M0–M25). Not every cohort reaches M25 — recent cohorts have only a few columns.

#### Cell formula (example: Cohort = Jan-2024, M = 3)

```
=IFERROR(
  COUNTIFS(tbl_Cohort[cohort_month], [this cohort],
           tbl_Cohort[months_since_signup], [M],
           tbl_Cohort[active], TRUE)
  /
  COUNTIFS(tbl_Cohort[cohort_month], [this cohort],
           tbl_Cohort[months_since_signup], 0)
, "")
```

- **M0 = 100% always:** Every cohort retains 100% of itself at month zero.
- **Blank for future periods:** IFERROR returns empty string for months that have not happened yet.
- **Cohort size column:** Add a column to the left of M0 showing the count of customers in that cohort. Useful for weighting — a cohort of 2 looks different from a cohort of 8.
- **Average row at bottom:** Average retention % at each M across all cohorts. This is the number that goes in board presentations.

#### Heatmap formatting

Apply a 3-color conditional format scale across all value cells:

- 100% = dark green
- 50% = yellow
- 0% = red
- Blanks (future periods) = no color applied

The heatmap makes cohort dropout patterns instantly readable without scanning individual numbers.

---

### Tab 10 — Cohort — Revenue

**Revenue NRR heatmap. Same structure as customer cohort but values are MRR-based.**

Same grid as Tab 9. Values are MRR-retention percentages, not customer-count percentages.

#### Cell formula

```
=IFERROR(
  SUMIFS(tbl_Cohort[mrr], tbl_Cohort[cohort_month], [this cohort],
         tbl_Cohort[months_since_signup], [M])
  /
  SUMIFS(tbl_Cohort[mrr], tbl_Cohort[cohort_month], [this cohort],
         tbl_Cohort[months_since_signup], 0)
, "")
```

> **Why this tab matters more than Tab 9:** Revenue cohorts can show values above 100% — that happens when expansion MRR from surviving customers more than offsets churn. A cohort with 80% customer retention but 110% revenue retention means the customers who stayed grew significantly. This is NRR at the cohort level. Add a highlight rule: any cell > 100% gets a blue fill. These are the data points for the investor narrative.

- Add an average NRR row at the bottom. If any month's average exceeds 100%, note it — that is a key positive for fundraising conversations.

---

### Tab 11 — Dashboard

**One-screen board-ready summary. No calculations. All values linked from analysis tabs.**

#### Layout (top to bottom)

**Section 1 — Six KPI cards in a row:**

| Card | Value | Source |
|---|---|---|
| Current MRR | $142,110.50 | `=Last row of tbl_Monthly[total_mrr]` |
| MoM Change | $X,XXX | `=tbl_Monthly[net_mrr_change]` last row |
| Active Subscriptions | 49 | `=COUNTA(tbl_Snapshot[subscription_id])` |
| Avg MRR per Sub | ~$2,900 | `=SUM(tbl_Snapshot[mrr]) / COUNTA(tbl_Snapshot[subscription_id])` |
| NRR (trailing 12-mo.) | X% | `=AVERAGE` of last 12 NRR rows from Retention tab |
| Logo Churn (trailing) | X% | `=AVERAGE` of last 12 logo churn rate rows from Retention tab |

Each card: large number at 24pt, label below at 10pt, colored thick left border using the workbook accent color. No shapes — format cells only.

- **Section 2 — Waterfall chart:** Copied from MRR Waterfall tab. Full width.
- **Section 3 — Two charts side by side:** MRR trend line (from MRR Trend tab) and MRR by plan donut (from MRR Mix tab).
- **Section 4 — NRR vs GRR line chart:** Copied from Retention tab. Replaces the cohort strip — cleaner for board audiences.

#### Dashboard formatting rules

- No gridlines visible: View > Show > uncheck Gridlines.
- White background on all cells.
- No borders on chart objects (Format Chart Area > No border).
- Consistent fonts: section titles 12pt bold, KPI values 24pt, labels 9pt.
- No pivot tables visible on this tab — only clean chart objects and formatted cells.

---

## 4. Color System

These five colors are used consistently across every chart in the workbook. Define them once in the README tab and apply them everywhere.

| Movement | Color | Hex | Notes |
|---|---|---|---|
| New MRR | Solid green | #2E7D32 | Strong — this is the main growth driver |
| Expansion MRR | Light green | #81C784 | Lighter to distinguish from New |
| Contraction MRR | Orange | #F4892F | Warning — not yet churn, but moving that way |
| Churned MRR | Red | #C62828 | Loss — strongest negative signal |
| Reactivation MRR | Blue | #1565C0 | Recovery — positive, distinct from New |

---

## 5. Build Order

Each step unblocks the next. Do not skip ahead.

| Step | Task | Depends on | Self-check |
|---|---|---|---|
| 1 | Paste Inputs A, B, C into RAW tabs. Format as Excel Tables. | SQL queries complete | `SUM(tbl_Snapshot[mrr])` = $142,110.50. `tbl_Monthly` last row = $142,110.50. |
| 2 | MRR Waterfall — PivotTable from tbl_Movements + wide calculation table. | Step 1 | Closing MRR last row = $142,110.50. |
| 3 | MRR Waterfall — stacked column chart + running total line. | Step 2 | 5 colored series visible. Line sits on top of bars. |
| 4 | MRR Mix — four PivotTables + four charts. | Step 1 | Grand total of each pivot = $142,110.50. |
| 5 | MRR Trend — extend tbl_Monthly, two charts. | Step 1 | Last data point on Chart 1 = $142,110.50. |
| 6 | Retention — build GRR/NRR/logo churn table + three charts + KPI row. | Steps 2, 5 | Last closing MRR row matches Step 2. |
| 7 | Dashboard — six KPI cards, link charts from Steps 3–6. | Steps 3–6 | Current MRR card = $142,110.50. |
| 8 | Paste Input D into [RAW] Cohort. Build Cohort — Customers tab. | Cohort SQL assignment | M0 column = 100% for all cohorts. |
| 9 | Build Cohort — Revenue tab. | Step 8 | Check for any cell > 100% — highlight blue. |
| 10 | Final review — README, color consistency, no visible gridlines on Dashboard. | All steps | All self-check values pass. |

---

## 6. File Management

| File | Location | Purpose |
|---|---|---|
| `idynamics_mrr_workbook.xlsx` | `repo/excel/` | The workbook — committed without data in RAW tabs |
| `sql/mrr_snapshot.sql` | `repo/sql/` | Deliverable 1 query |
| `sql/mrr_waterfall.sql` | `repo/sql/` | Deliverables 2 Steps 2–4 |
| `sql/mrr_logo_churn.sql` | `repo/sql/` | Logo churn count by month |
| `sql/mrr_cohort.sql` | `repo/sql/` | Cohort data (future assignment) |

> **Data in Git:** RAW tab data should not be committed to the repository — it may contain customer information. The workbook file committed to Git should have empty RAW tabs. SQL query files are committed. Exported CSV files from SQL outputs are not committed.

---

*Idynamics Finance Analyst Training Program | Last updated March 2026*
