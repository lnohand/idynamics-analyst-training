# Excel Assignment 08 — March 2026 Close + Q1 Roll-Up
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** March close + Q1 — first quarter-end, board wants the full picture
>
> Michael — March is Q1 close. That means two things land at the same time:
> the monthly close and the first full-quarter summary we'll present to the board.
>
> The monthly close is the same process you've run twice. What's new this month
> is expansion MRR — one of our existing customers grew their seat count. That's
> the first time NRR has moved above 100%. Make sure your waterfall and commentary
> capture that signal clearly.
>
> Below the March tab, add a Q1 Roll-Up section. The board wants one place to see
> Q1 totals: revenue, EBITDA, net new MRR, and the quarterly unit economics we
> haven't been able to calculate from a single month. LTV, LTV:CAC, CAC Payback —
> those land here for the first time.
>
> You know the process. Pull the data, build the tab, write the story.
>
> — David

---

## What You're Building

Four additions to your existing workbook (`06_actual_vs_forecast.xlsx`):

1. **Mar 2026 A vs F tab** — MRR waterfall, P&L, KPIs section, and March management commentary
2. **Q1 Roll-Up section** — added below the March KPIs on the same tab, with quarterly aggregations and quarterly KPIs (LTV, LTV:CAC, CAC Payback)
3. **KPI Tracker tab update** — fill in the Mar 2026 column; add Q1 quarterly metrics to the Q1 column
4. **WaterfallData tab update** — add 7 more rows for March (21 total)

This assignment has **two commentary sections**, both hard gates. The March commentary covers the monthly close. The Q1 Roll-Up commentary covers the full quarter. Both are required before the PR can be merged.

---

## Part 1 — Pull March Actuals

**Before running any queries:** Confirm the Feb/Mar INSERT script has been applied to your database. Run the March closing verification query from the bottom of the script and check that the result matches the expected closing MRR in the self-check table below. If it doesn't, the seat update for SUB012 (23→27 seats) may not have been applied — re-run the INSERT script before continuing.

Run your MRR snapshot query at `2026-03-31`. You've done this twice — same structure, new date.

Check for all March revenue events before opening Excel:

- **New MRR:** Query the `subscriptions` table for any subscriptions with a March 2026 start date.
- **Expansion MRR:** Query the `subscription_events` table for March seat changes. This is the first month expansion events may appear in your data — check carefully and do not assume the result.
- **Churn:** Check for any cancellations in March.

Before opening Excel, write down:
- How many active subscriptions and active customers on March 31?
- What expansion events occurred, and what is the MRR impact of each?
- What churn events occurred, and what is the MRR impact of each?

Run your COGS query at `2026-03-31`. Same structure as January and February.

**S&M, R&D + G&A, and total OpEx** come from Lisa's monthly close message in #finance-ops — same as January and February. Do not pull OpEx from SQL.

Write down your actuals before going to Excel.

---

## Part 2 — March A vs F Tab

Add a new tab. Name it exactly: `Mar 2026 A vs F`

**Opening MRR — two columns, two different sources:**

- **Actual column (B3):** Reference `'Feb 2026 A vs F'!B9` — February's actual closing MRR. Do not type it in.
- **Forecast column (C3):** Use `$150,592.60` — this is February's forecast closing MRR, derived from the quarterly plan: opening ($143,069.50) + 2 × (Q1 Net New MRR / 3). Hardcode this value for now. We will build a proper monthly forecast for Q2.

The forecast opening is not the same as the actual opening. If February came in above or below plan, that difference will show up in D3 as an opening variance — and that is correct. The forecast column holds the original plan, not a rolling reset.

Build the same waterfall and P&L structure you built for January and February. You know the layout.

**One difference this month:** Expansion MRR is non-zero. Make sure the Expansion MRR row has actual values and a correct variance — do not leave it at zero or N/A.

**Churn variance sign:** If actual churn is less than forecast (favorable), the $ variance in D7 should be **positive**. Use `=C7-B7` (Forecast − Actual) on the churn row, and invert your F/U logic: `IFS(D7>0, "F", D7<0, "U", D7=0, "-")`.

Below the waterfall and P&L, add the KPIs section:

**March 2026 — SaaS KPIs**

Same metrics as January and February:

| Metric | Value | Notes |
|--------|-------|-------|
| Active Customers | | |
| Active Subscriptions | | |
| ARPA | | |
| Gross Margin | | |
| GRR | | |
| NRR | | |
| Quick Ratio | | |
| S&M (actual) | | From Lisa's message in #finance-ops |
| CAC — this month | | |
| CAC — Q1 to date | | (Jan S&M + Feb S&M + Mar S&M) ÷ (Jan new customers + Feb new customers + Mar new customers) |
| LTV | see Q1 Roll-Up | Calculated below in Q1 section |
| LTV:CAC | see Q1 Roll-Up | Calculated below in Q1 section |
| CAC Payback | see Q1 Roll-Up | Calculated below in Q1 section |

---

## Part 3 — Management Commentary (March)

3-4 sentences below the KPIs section. **This is a hard gate — the PR will not be merged without it.**

Cover these four points:

1. **Q1 headline result** — how did March close and what does it mean for the quarter overall?
2. **Expansion MRR signal** — this is the first month NRR exceeded 100%. What drove it and what does it indicate about customer health?
3. **EBITDA trend** — is the EBITDA margin improving, flat, or deteriorating across the three months of Q1? Is that directionally good or concerning?
4. **One thing to watch in Q2** — one specific risk or opportunity that the Q1 data raises.

---

## Part 4 — Q1 Roll-Up Section

Below the March management commentary, add a new section header:

**Q1 2026 Roll-Up**

This section sits on the same tab as the March close, below the commentary. It aggregates across all three months of Q1. This is the first time you are building this structure — a short explanation of what goes where:

**Q1 MRR Summary** — one table aggregating the waterfall movements:

| Movement | Q1 Total |
|----------|---------|
| Q1 Total New MRR | |
| Q1 Total Expansion MRR | |
| Q1 Total Churned MRR | |
| Q1 Net New MRR | |
| Q1 Closing MRR | |

**Q1 P&L Summary** — one table aggregating across all three months:

| Line | Q1 Total |
|------|---------|
| Q1 Revenue | sum of Jan + Feb + Mar closing MRR |
| Q1 COGS | sum across three months |
| Q1 Gross Profit | |
| Q1 Gross Margin % | |
| Q1 S&M | |
| Q1 R&D + G&A | |
| Q1 Total OpEx | |
| Q1 EBITDA | |
| Q1 EBITDA Margin % | |

Aggregate each line from your three monthly tabs. Be consistent in your approach across all rows.

---

## Part 5 — Quarterly KPIs

Below the Q1 P&L Summary, add a section:

**Q1 2026 — Quarterly KPIs**

These three metrics are calculated here for the first time. Monthly figures are too volatile to be meaningful — they are valid only at the quarterly level.

| Metric | Value |
|--------|-------|
| Q1 New Customers | total new customers acquired in Q1 |
| Quarterly CAC | Q1 total S&M ÷ Q1 new customers |
| LTV | |
| LTV:CAC | |
| CAC Payback (months) | |

**Formula structure for the three new metrics — these are introduced here for the first time:**

**Quarterly CAC:**
```
= Q1 Total S&M / Q1 New Customers
```

**LTV** (customer lifetime value using gross margin and trailing gross churn):
```
= (Gross Margin % / (Monthly Gross Churn Rate × 12)) × ARPA
```
- Use Q1 Gross Margin % from the Q1 P&L Summary above
- Monthly Gross Churn Rate = Q1 Churned MRR ÷ Q1 Opening MRR (i.e., January opening MRR)
- ARPA = Q1 Closing MRR ÷ Q1 Active Customers (March 31 count)
- If Q1 Churned MRR is zero, your LTV will be very large — that is mathematically correct; note it in commentary

**LTV:CAC:**
```
= LTV / Quarterly CAC
```

**CAC Payback (months to recover CAC):**
```
= Quarterly CAC / (ARPA × Gross Margin %)
```
- This answers: how many months of revenue at current margin does it take to recover the cost of acquiring one customer?

---

## Part 6 — Q1 Roll-Up Commentary

3-4 sentences below the Quarterly KPIs table. **Also a hard gate.**

Cover:
1. **Q1 overall result** — one sentence on the quarter-level headline (revenue, EBITDA)
2. **Unit economics** — are the LTV:CAC and CAC Payback ratios at a healthy level? What benchmark tells you whether they are?
3. **Trend across the quarter** — did metrics improve, hold, or deteriorate from January through March?
4. **Q2 recommendation** — one actionable thing the data suggests the business should focus on in Q2

---

## Part 7 — Update KPI Tracker Tab

Fill in the Mar 2026 column. Same approach as February — reference cells from the `Mar 2026 A vs F` tab.

Then fill in the Q1 2026 column with the quarterly metrics from the Q1 Roll-Up section:

| Metric | Q1 2026 column |
|--------|---------------|
| Closing MRR | March closing MRR |
| Active Customers | March 31 count |
| ARPA | Q1 ARPA (from Q1 Roll-Up) |
| Gross Margin % | Q1 Gross Margin % |
| GRR | Q1 GRR |
| NRR | Q1 NRR |
| S&M | Q1 total S&M |
| CAC — trailing Q | Quarterly CAC (from Q1 Roll-Up) |
| LTV | from Q1 Roll-Up |
| LTV:CAC | from Q1 Roll-Up |
| CAC Payback | from Q1 Roll-Up |

Monthly metrics (ARPA, GRR, NRR, Quick Ratio, monthly CAC) in the Q1 column should show quarterly equivalents or be left blank per the note already in the tracker. LTV, LTV:CAC, and CAC Payback appear in the Q1 column only — those cells in the Jan and Feb columns should remain dashes as you built them.

---

## Part 8 — Update WaterfallData Tab

Add 7 rows for March directly below the February rows. Same columns: Month, Movement, Actual, Forecast, Variance.

Seven rows in order: Opening MRR, New MRR, Expansion MRR, Contraction MRR, Churned MRR, Net New MRR, Closing MRR.

Month column formula: `=TEXT(DATE(2026,3,1),"mmm-yy")` — same pattern as your February rows, giving `Mar-26`

After saving, the table will have 21 rows total (7 Jan + 7 Feb + 7 Mar). If Power BI is connected, refresh it — March will appear in the Month slicer automatically.

---

## Git Workflow

New assignment = new branch:

```
git checkout main
git pull origin main
git checkout -b student/excel_08_march_close_q1
```

When ready to submit:

```
git add submissions/excel/excel_08_march_close_q1.xlsx
git commit -m "Add: 08 — March 2026 close + Q1 Roll-Up"
git push origin student/excel_08_march_close_q1
```

Open a PR from `student/excel_08_march_close_q1` → `main`.

---

## Keep Your Notes Current

Before pushing, update `my-notes/`:

| File | What to add |
|------|------------|
| `my-notes/sql_queries.sql` | March snapshot query; `subscription_events` query for expansion MRR |
| `my-notes/kpi_definitions.md` | LTV formula with inputs; LTV:CAC; CAC Payback; quarterly CAC; note on why these are quarterly-only |
| `my-notes/excel_techniques.md` | Cross-tab aggregation for Q1 Roll-Up; quarterly vs monthly metric structure |
| `my-notes/git_commands.md` | No new commands — verify notes are current |

---

## Submission

File: `submissions/excel/excel_08_march_close_q1.xlsx`

Open a PR from `student/excel_08_march_close_q1` → `main` with this description:

```
## 08 — March 2026 Close + Q1 Roll-Up

- Mar 2026 A vs F tab added (waterfall, P&L, KPIs, March commentary)
- Q1 Roll-Up section added to Mar tab (Q1 waterfall, P&L, quarterly KPIs, Q1 commentary)
- KPI Tracker updated with March column and Q1 quarterly metrics
- WaterfallData updated with 7 new March rows
- my-notes/ updated

[paste completed Self-Check table here]
```

---

## Self-Check

Run through these before you push. If any value does not match, find the discrepancy before opening the PR.

| Check | Expected |
|-------|---------|
| March Opening MRR | Referenced from Feb tab — not typed in |
| March Closing MRR | $153,685.50 |
| Q1 Closing MRR | $153,685.50 (same as March closing — it is the quarter-end balance) |
| Q1 New Customers | ___ (you derive this) |
| Q1 CAC (trailing quarter) | $__________ (you derive this) |
| March NRR | > 100% — expansion exists for the first time this month |
| WaterfallData total rows | 21 |
| KPI Tracker Mar column filled | ✅ |
| KPI Tracker Q1 quarterly metrics (LTV, LTV:CAC, CAC Payback) | ✅ |
| March commentary present | ✅ (hard gate) |
| Q1 Roll-Up commentary present | ✅ (hard gate) |

---

*Excel Assignment 08 — March 2026 Close + Q1 Roll-Up*
*Idynamics Finance Analyst Training Program*
*April 2026*
