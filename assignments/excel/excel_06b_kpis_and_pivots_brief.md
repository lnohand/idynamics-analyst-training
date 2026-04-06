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

## What You're Building

Three additions to your existing workbook (`06_actual_vs_forecast.xlsx`):

1. **KPIs section** — added to the bottom of your `Jan 2026 A vs F` tab
2. **KPI Tracker tab** — new tab, all months as columns, accumulates through Q1
3. **WaterfallData tab** — new tab, structured Excel Table, Power BI source

---

## Addition 1 — KPIs Section on Jan 2026 A vs F Tab

Below your management commentary, add a section header:

**January 2026 — SaaS KPIs**

Then build this table. You've calculated all of these before — look up
the formulas in your `my-notes/kpi_definitions.md` or the assignments
where you first built them (Excel 03 for retention, Excel 04 for unit economics).

| Metric | Value | Notes |
|--------|-------|-------|
| Active Customers | 39 | From your Jan 31 SQL snapshot |
| Active Subscriptions | 52 | From your Jan 31 SQL snapshot |
| ARPA | calculate | Excel 04 |
| Gross Margin | calculate | Already in your P&L |
| GRR | calculate | Excel 03 |
| NRR | calculate | Excel 03 |
| Quick Ratio | N/A — no losses | Excel 02 — see note below |
| S&M (actual) | $30,000 | From Lisa's monthly close message |
| CAC — this month | calculate * | Excel 04 |
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

Calculate each metric and fill in the PR description before submitting.
Do not skip this step — if a number looks off, find the bug before opening the PR.

| Metric | Your value |
|--------|-----------|
| ARPA | |
| GRR | |
| NRR | |
| Quick Ratio | |
| CAC (monthly) | |

---

## Addition 2 — KPI Tracker Tab

Create a new tab called `KPI Tracker`.

This tab shows all months as columns. Right now it has one column (January).
When February closes, you add a February column. When March closes, you add
March. A Q1 column appears after March with the quarterly metrics.

Build this structure:

| Metric | Jan 2026 | Feb 2026 | Mar 2026 | Q1 2026 |
|--------|---------|---------|---------|---------|
| Closing MRR | | | | |
| Active Customers | | | | |
| ARPA | | | | |
| Gross Margin | | | | |
| GRR | | | | |
| NRR | | | | |
| Quick Ratio | | | | |
| S&M (actual) | | | | |
| CAC — monthly | | | | |
| CAC — trailing Q | — | — | — | |
| LTV | — | — | — | (calc at Q1) |
| LTV:CAC | — | — | — | (calc at Q1) |
| CAC Payback | — | — | — | (calc at Q1) |

**Rules for this tab:**
- Jan column values must reference your `Jan 2026 A vs F` tab — do not
  type the numbers in twice. Use formulas to pull them across.
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

Populate 7 rows for January 2026 — one per waterfall movement, in order:
Opening MRR, New MRR, Expansion MRR, Contraction MRR, Churned MRR, Net New MRR, Closing MRR.

All numbers come directly from your `Jan 2026 A vs F` tab. Do not retype them —
reference the cells or copy the values across. Variance = Actual − Forecast.

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
| Closing MRR row, Actual column | matches your Jan 2026 A vs F tab |
| Closing MRR row, Variance column | matches your Jan 2026 A vs F tab |

---

## Git Workflow for This Assignment

### New assignment = new branch. Always.

The branch from Excel 06 (`student/excel_06_actual_vs_forecast_jan2026`) is merged
and done. Do not push new work to it. Start fresh:

```
git checkout main
git pull origin main
git checkout -b student/excel_06b_kpis_tracker
```

Work on this branch. When you're ready to submit, push and open a PR:

```
git add submissions/excel/06_actual_vs_forecast.xlsx
git commit -m "Add: 06b — KPIs section, KPI Tracker tab, WaterfallData tab"
git push origin student/excel_06b_kpis_tracker
```

**One branch per assignment. One PR per assignment. Never reuse a merged branch.**

---

### Keep your personal reference files current

Every time you learn a new SQL query, a new Git command, or a new Excel
technique — write it down in your own reference files and push them.

You should have (or create) these files on your branch, in a folder called
`my-notes/`:

| File | What goes in it |
|------|----------------|
| `my-notes/sql_queries.sql` | Every query you've written, with a comment explaining what it does |
| `my-notes/git_commands.md` | Every Git command you've used, with an example |
| `my-notes/excel_techniques.md` | Formulas and techniques — XLOOKUP, named ranges, Excel Tables, pivot refresh, etc. |
| `my-notes/kpi_definitions.md` | Every metric you've calculated: formula, what it means, when to use it |

These are your notes, not a submission. No one is grading them. But they will
save you hours — instead of Googling the same thing twice, you'll have it
written in your own words from the last time you used it.

Update them before you commit each assignment. If you learned three new things
this week, they should be in the file before the PR goes up.

---

## Submission

Same workbook, same file:
```
submissions/excel/06_actual_vs_forecast.xlsx
```

Open a PR from `student/excel_06b_kpis_tracker` → `main` with this description:

```
## 06b additions
- KPIs section added to Jan 2026 A vs F tab
- KPI Tracker tab created (Jan column, structure for Feb/Mar/Q1)
- WaterfallData tab created (Excel Table, 7 Jan rows)
- my-notes/ updated with new KPI definitions and Excel techniques

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
