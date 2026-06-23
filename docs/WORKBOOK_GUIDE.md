# How Your Finance Workbook Works

A map of your monthly close workbook (Google Sheets) — what each sheet/tab is for, what you
touch, and how often. Read this before a close, and any time a tab confuses you. Keep it
open in another window while you work.

## The one rule that holds the whole thing together

**Each month, you only ever *type* into two places:**

1. the new month's column on the **`Actuals`** tab, and
2. the **two config cells** on a freshly-copied month tab.

Everything else is formulas that recalculate themselves. If you catch yourself typing a
number anywhere else, stop — either you're about to overwrite a formula, or a formula is
missing and needs fixing instead of patching. That instinct is the whole point of the
redesign.

## How the data flows

```
DB snapshot (your SQL)  ─►  Actuals  ─►  "MMM 2026 A vs F"  ─►  KPI Tracker
   (you type the inputs)      │              (the close)      └►  Waterfall Data ─► BI dashboard
                              │
Engine (event log)  ─►  Waterfall  ─►  Retention  ─►  GRR / NRR on every month tab
                        └► Unit Economics

Forecast Assumptions  ─►  2026 Forecast  ─►  Forecast columns on the A vs F tabs

billing_/bank_ tabs  ─►  Billing Reconciliation
```

Read it as: **you type actuals into `Actuals`; the Engine event log drives retention; the
annual plan drives the forecast columns; the billing/bank files drive reconciliation.**
The close tabs just wire those together.

## The tabs, by job

### Tabs you touch every month

| Tab | What it's for | What you do | When |
|---|---|---|---|
| **Actuals** | The single source of truth. One column per month. You type the yellow INPUT rows; the blue rows (Opening/Closing MRR, OpEx, COGS, Gross Profit, EBITDA) derive on their own. | Add the new month's column, enter the inputs only | Every close |
| **`MMM 2026 A vs F`** (e.g. `Apr 2026 A vs F`) | The actual close: MRR waterfall, P&L, KPIs, commentary — Actual vs Forecast. Everything reads `Actuals` by the config date. | **Copy** last month's tab, rename it, change the **two config cells** (current-month date + prior-month tab name), then write the commentary | Every close (a new tab) |
| **KPI Tracker** | Every month side by side, one metric per row. Pulls from the A vs F tabs. | Add the new month's column; leave prior columns alone | Every close |
| **Waterfall Data** | The structured table your BI dashboard reads (Power BI / Looker Studio). | Add the month's movement rows below the last | Every close |

### Tabs that update themselves (don't hand-edit)

| Tab | What it's for | Your job |
|---|---|---|
| **Waterfall** | Turns the raw `Engine` event log into a monthly MRR waterfall. **Load-bearing** — `Retention` reads it heavily, and your GRR/NRR depend on it. | Leave it. It extends as the Engine grows. |
| **Retention** | GRR, NRR, churn rates by month. Your A vs F tabs pull GRR/NRR from here. | Leave it — it derives from `Waterfall`. |
| **Unit Economics** | ARPA, ARPS, LTV/CAC analysis. | Refresh when you do the quarterly metrics. |

### Source data you paste/append from the database

| Tab | What it's for | When |
|---|---|---|
| **Engine** | Your subscription **event log** — every created / cancelled / seats-change / discount event. This is the spine that feeds retention. | Append the month's new events from the DB |
| **billing_MMM_2026** | Raw monthly invoice export — the "invoiced" side of reconciliation. | Paste the month's file when you reconcile |
| **bank_statement_MMM_2026** | Raw monthly bank export — the "collected" side. | Same |
| **Ref** | Static lookup: plan → price / cost / margin. | Rarely — only if pricing changes |

### Set once a year — then read-only

| Tab | What it's for |
|---|---|
| **Forecast Assumptions** | The 2026 plan inputs (starting position, growth, churn). Set when the annual plan is built. |
| **2026 Forecast** | The forecast model, derived from Assumptions. It supplies the Forecast columns on your A vs F tabs. |
| **Historical Baseline** | The pre-2026 quarterly waterfall the model anchors to. Foundation — don't touch. |

### Standalone — not part of the monthly close

| Tab | What it's for |
|---|---|
| **Billing Reconciliation** | The MRR → Invoiced → Collected bridges. Add a column per month you reconcile, pointed at that month's billing/bank tabs. |
| **Price-Volume Bridge** | A separate warm-up exercise — unrelated to the close. |

## Your monthly close checklist

Each month, in order, you touch exactly these:

1. **Engine** — paste the month's new events from the DB.
2. **Actuals** — add the month's column; type the inputs only.
3. **New `MMM 2026 A vs F`** — copy the prior month, change the two config cells, write the commentary.
4. **KPI Tracker** — add the month's column.
5. **Waterfall Data** — add the month's movement rows.
6. *(only if you're reconciling)* paste **billing_** / **bank_** for the month and add a **Billing Reconciliation** column.

Everything else — Forecast, Assumptions, Historical Baseline, Ref, Waterfall, Retention,
Unit Economics — you leave alone. It's annual, static, or self-deriving.

## Two tabs people mix up

- **`Waterfall`** (no space) is an internal **engine** — Engine → Waterfall → Retention →
  your GRR/NRR. Delete it and retention breaks across the whole workbook. Never remove it.
- **`Waterfall Data`** (with a space) is an **export** for your BI dashboard. Nothing inside
  the workbook reads it, and that's correct — it's a feed for the dashboard, not a formula
  source.

## If a formula breaks when you change something

Before you delete or move anything, **find what depends on it first.** Google Sheets has no
"trace dependents" button, so use **Edit → Find and replace**, type the sheet/cell name, and
set *Search: all sheets* to see everywhere it's referenced. Most `#REF!` surprises come from
removing a cell another tab was quietly reading. Check first, then change — same discipline
as the reconciliation cleanup.

## Submitting your work

You work in Google Sheets, but the submission is still the `.xlsx` in GitHub:

1. **File → Download → Microsoft Excel (.xlsx)** — get the file back out of Sheets.
2. Save it over `submissions/excel/excel_<assignment>.xlsx` in your local repo.
3. `git add` it on your assignment branch, commit, and `git push`. The PR updates itself.

**Don't attach the file to a PR comment** — attachments aren't a submission; they don't
update the PR and can't be reviewed or merged. The file lives in the branch; only words
(what you changed, that the self-check ties) go in the comment.

> One Sheets gotcha when you download back to `.xlsx`: re-check that nothing turned into a
> `#REF!` or lost a tab reference in the round-trip, and that the `Waterfall Data` table
> still reads cleanly for the dashboard. Open the file once after download and confirm the
> close still ties before you commit.
