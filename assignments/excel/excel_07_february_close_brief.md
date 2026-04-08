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
> You've done this before. Pull the numbers, build the tab, tell me
> the story.
>
> — David

---

## What You're Building

Three additions to your existing workbook (`06_actual_vs_forecast.xlsx`):

1. **Feb 2026 A vs F tab** — new tab with waterfall, P&L, KPIs section, and management commentary
2. **KPI Tracker tab update** — fill in the Feb 2026 column
3. **WaterfallData tab update** — add 7 new rows for February below the existing January rows

---

## Part 1 — Pull the February Actuals

Run your MRR snapshot query at `2026-02-28`. You've done this before.

Before you open Excel, confirm:
- How many active subscriptions and active customers?
- Any new subscriptions this month?
- Any cancellations? Check whether the customer lost a subscription or the full relationship — those are different things and your commentary needs to reflect that.

Run your COGS query. Same formula as the MRR engine — use `cost_per_seat` instead of `price_per_seat`, same point-in-time filter structure. Filter to February 28.

Write down your actuals before going to Excel.

---

## Part 2 — MRR Waterfall (Feb 2026 A vs F Tab)

Add a new tab. Name it exactly: `Feb 2026 A vs F`

**Opening MRR:** February's opening MRR is January's closing MRR. Reference it from the Jan tab — do not type it in twice.

Build the same structure as January — four columns: Actual, Forecast, $ Variance, % Variance — plus an F/U column.

| Movement | Actual | Forecast | $ Variance | % Variance | F/U |
|----------|--------|----------|-----------|-----------|-----|
| Opening MRR | | | | | — |
| New MRR | | | | | |
| Expansion MRR | | | | | |
| Contraction MRR | | | | | |
| Churned MRR | | | | | |
| Net New MRR | | | | | |
| Closing MRR | | | | | |
| Closing ARR | | | | | |

**Forecast:** Same derivation as January — Q1 plan spread across three months.

**Churn variance:** Think carefully about the sign. Less churn than forecast means you kept more revenue than the plan expected. Make sure your F/U column reflects that correctly.

---

## Part 3 — P&L (Feb 2026 A vs F Tab)

Add the P&L section below the waterfall. Same structure as January.

Revenue equals Closing MRR — reference the waterfall, do not retype.

S&M comes from Lisa's message in #finance. The database does not have OpEx — do not try to pull it from SQL.

| Line | Actual | Forecast | $ Variance | % Variance | F/U |
|------|--------|----------|-----------|-----------|-----|
| Revenue | | | | | |
| COGS | | | | | |
| Gross Profit | | | | | |
| Gross Margin % | | | | | |
| S&M | | | | | |
| R&D + G&A | | | | | |
| Total OpEx | | | | | |
| EBITDA | | | | | |
| EBITDA Margin % | | | | | |

---

## Part 4 — KPIs Section (Feb 2026 A vs F Tab)

Add the KPIs section below the P&L. Section header: **February 2026 — SaaS KPIs**

Same metrics as January:

| Metric | Value | Notes |
|--------|-------|-------|
| Active Customers | | |
| Active Subscriptions | | |
| ARPA | | |
| Gross Margin | | |
| GRR | | |
| NRR | | |
| Quick Ratio | | |
| S&M (actual) | | |
| CAC — this month | | |
| CAC — Q1 to date | | Cumulative S&M ÷ cumulative new customers in Q1 so far |
| LTV | — | Quarterly metric — calculated at Q1 close |
| LTV:CAC | — | Quarterly metric — calculated at Q1 close |
| CAC Payback | — | Quarterly metric — calculated at Q1 close |

Compare each February KPI to January using XLOOKUP — do not hardcode January values.

**XLOOKUP [new function]:**

```
=XLOOKUP("Jan 2026", KPITracker[Month], KPITracker[ARPA])
```

Replace `KPITracker[ARPA]` with the column you want to look up. This keeps the formula dynamic when March is added.

---

## Part 5 — Management Commentary

3-4 sentences below the KPIs. This is a hard gate — the PR will not be merged without it.

Cover four things:

1. **Overall result** — headline MRR and EBITDA vs plan
2. **Revenue drivers** — what drove New MRR, and what happened with Expansion
3. **Churn** — name the subscription and explain whether this is subscription churn or customer churn. Why does the distinction matter?
4. **Costs** — which lines ran over and what it did to EBITDA margin

---

## Part 6 — Update KPI Tracker Tab

Fill in the Feb 2026 column. Do not overwrite January — those cells should still reference the `Jan 2026 A vs F` tab.

**Month labels with TEXT and DATE [new functions]:**

Use TEXT and DATE to generate the column header dynamically instead of typing "Feb 2026":

```
=TEXT(DATE(2026,2,1),"mmm yyyy")
```

This gives you `Feb 2026`. Use the same pattern to generate any month label from a date.

---

## Part 7 — Update WaterfallData Tab

Add 7 rows for February directly below the January rows. Columns: Month, Movement, Actual, Forecast, Variance.

The Excel Table expands automatically when you add rows below the existing data.

**Variance sign convention:** Positive variance = favorable impact on revenue vs plan. For Churned MRR: if actual churn was less than forecast, the variance is positive. Do not mechanically apply Actual − Forecast on the churn row.

After saving, refresh Power BI if connected — the Month slicer will pick up February automatically.

---

## Part 8 — Git Workflow

New assignment = new branch:

```
git checkout main
git pull origin main
git checkout -b student/excel_07_february_close
```

When ready to submit:

```
git add submissions/excel/06_actual_vs_forecast.xlsx
git commit -m "Add: 07 — February 2026 close (A vs F tab, KPI Tracker, WaterfallData)"
git push origin student/excel_07_february_close
```

Open a PR from `student/excel_07_february_close` → `main`.

---

## Keep Your Notes Current

Before pushing, update `my-notes/`:

| File | What to add |
|------|------------|
| `my-notes/sql_queries.sql` | February COGS query with date filter |
| `my-notes/kpi_definitions.md` | XLOOKUP prior month pull; when NRR and GRR converge; CAC Q1-to-date formula |
| `my-notes/excel_techniques.md` | TEXT/DATE for month labels; cross-tab formula references |
| `my-notes/git_commands.md` | Nothing new — verify your workflow notes are current |

---

## Submission

File: `submissions/excel/06_actual_vs_forecast.xlsx`

Open a PR from `student/excel_07_february_close` → `main` with this description:

```
## 07 — February 2026 Close

- Feb 2026 A vs F tab added (waterfall, P&L, KPIs, commentary)
- KPI Tracker updated with February column
- WaterfallData updated with 7 new February rows (14 total)
- my-notes/ updated

## Self-check
Closing MRR:              $___________
vs Plan (Net New MRR):    $___________ (F/U)
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

Run through these before you push:

| Check | Expected |
|-------|---------|
| Opening MRR | Referenced from Jan tab — not typed in |
| Closing MRR | $150,305.50 |
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
