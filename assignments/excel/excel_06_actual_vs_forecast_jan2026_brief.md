# Excel Assignment 06 — Actual vs Forecast: January 2026
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** January close — need the actuals vs plan before the Monday sync
>
> Michael — January is closed. I need you to compare where we actually
> landed against the plan you built last month.
>
> Add a new tab to your forecast workbook. I want to see the waterfall
> and the P&L side-by-side: actual, forecast, and variance. Dollar
> and percent. Every movement line.
>
> The board has the quarterly plan. When I walk in Monday I need to
> know the January story in one tab — what we hit, what we missed,
> and why. Write me three to five sentences at the bottom.
>
> Pull the actuals from the database. You've done this before.
>
> — David

---

## What You're Building

A new tab called **Jan 2026 A vs F** in your `idynamics_2026_forecast.xlsx`
workbook.

The tab has three sections:

1. **MRR Waterfall** — actual vs forecast vs variance for every movement
2. **P&L Summary** — actual vs forecast vs variance down to EBITDA
3. **Management Commentary** — 3–5 sentences explaining what happened

---

## Part 1 — Pull the January Actuals

Before you open Excel, get the numbers.

Run a query against the database to find:

- All subscriptions **active as of January 31, 2026** and their MRR
- Any **new** subscriptions that started in January
- Any **cancelled** subscriptions in January
- Any **subscription events** in January (seat changes, plan changes,
  price changes)

You know the MRR formula. You know how to filter by date range. Your
`subscription_events` table has everything you need for the waterfall
movements.

Write down the results before you go to Excel. You need:

| Metric | Your Value |
|--------|-----------|
| Opening MRR (Dec 31, 2025) | |
| New MRR | |
| Expansion MRR | |
| Contraction MRR | |
| Churned MRR | |
| Net New MRR | |
| Closing MRR (Jan 31, 2026) | |
| Active subscriptions (Jan 31) | |
| Active customers (Jan 31) | |

**How many new customers signed this month?** That's the single most
important number to understand before you look at the variance.

---

## Part 2 — Derive the Monthly Forecast

Your forecast was built quarterly. January doesn't have its own
forecast line — you need to derive it.

Think about what the Q1 plan assumed. It assumed those movements happen
evenly across the three months of the quarter. How would you convert a
quarterly movement to a monthly one?

Do the same thing for P&L. The Assumptions tab has quarterly OpEx.
Monthly is straightforward.

Write out your monthly forecast numbers before building the tab.

---

## Part 3 — Build the Tab

Layout: **four columns** — Actual | Forecast | $ Variance | % Variance

**MRR Waterfall section:**

| Row | Notes |
|-----|-------|
| Opening MRR | Dec 31 actual — this should be the same in both columns |
| + New MRR | |
| + Expansion MRR | |
| − Contraction MRR | |
| − Churned MRR | |
| = Net New MRR | Calculated row |
| Closing MRR | |
| Closing ARR | Closing × 12 |

**P&L section:**

| Row | Notes |
|-----|-------|
| Revenue | Use the same convention as your forecast tab |
| Cost of Revenue | |
| Gross Profit | |
| Gross Margin % | |
| S&M | |
| R&D | |
| G&A | |
| Total OpEx | |
| EBITDA | |
| EBITDA Margin % | |

**Variance columns:**

- `$ Variance = Actual − Forecast`
- `% Variance = Actual / Forecast − 1`
- For revenue and profit lines, positive variance = favorable
- For cost and churn lines, think about the sign convention before
  you build. A lower-than-forecast churn number is good — make sure
  your formatting communicates that.

**One formula note:** Margin % variance should show percentage points,
not percent-of-percent. `Actual margin % − Forecast margin %` is the
right calculation. Do not divide one margin by the other.

---

## Part 4 — Management Commentary

Three to five sentences at the bottom of the tab. Write it for David,
not for yourself.

A good commentary answers:
1. What was the headline result? (one number, one direction)
2. What drove the miss or beat on each waterfall line?
3. Is this a one-month blip or a signal worth watching?

Do not write "January was slightly below forecast." That tells David
nothing he can act on. Tell him which line missed, by how much, and
what it means for the Q1 run rate.

---

## Self-Check

Before you submit, verify:

| Check | Your Value | Pass? |
|-------|-----------|-------|
| Closing MRR (Actual) | | should match your database query |
| Opening MRR matches Dec 2025 forecast closing | $143,069.50 | |
| Net New MRR = New + Expansion − Contraction − Churned | | |
| Closing = Opening + Net New | | |
| Forecast Closing MRR | | should match Q1 forecast ÷ 3 logic |
| Variance % = Actual/Forecast − 1 | | spot-check one line |

---

## Grading

| Category | Weight |
|----------|--------|
| Actuals correct and sourced from database | 25% |
| Forecast monthly derivation logic is correct | 20% |
| Variance columns sign convention and format | 20% |
| Management commentary — specific, actionable, David's audience | 25% |
| Formatting and PR description | 10% |

---

## Submission

```
submissions/excel/06_actual_vs_forecast_jan2026.xlsx
```

PR description:

```
## What this does
[One sentence]

## January Result
Closing MRR (Actual):   $___________
Closing MRR (Forecast): $___________
$ Variance:             $___________
% Variance:             ___%

## Self-check
Net New MRR ties to waterfall: ✅ / ❌
Closing = Opening + Net New:   ✅ / ❌

## Commentary summary
[One sentence: the headline of your management commentary]

## Questions
[Anything you're unsure about]
```

---

*Module 2 — Actual vs Budget Variance*
*Excel Assignment 06 — April 2026*
