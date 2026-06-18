# Excel Assignment 10 — April 2026 Monthly Close
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** April close — first close on the rebuilt workbook
>
> Michael — April is the first real close on the workbook you rebuilt in
> assignment 09. No quarter roll-up this month, no new structure to invent.
> This is the payoff: add one column to Actuals, copy the prior monthly tab,
> change two config cells, verify, write the story. If you find yourself doing
> anything beyond those four steps, the redesign isn't finished — go fix it
> rather than working around it.
>
> The data has one wrinkle worth your attention. We had a cancellation this
> month, but the customer behind it is still active on another subscription.
> Sarah flagged it: that is a revenue churn, not a logo churn, and your
> commentary needs to say which it is and why the distinction matters. We have
> expansion again this month, but don't assume it carries NRR back over 100% —
> work the number and let the data tell you where it lands.
>
> Load April first, then close it. Pull the numbers, build the tab, tell me the
> story.
>
> — David

---

## Before You Start — Load April

Run the **April block** of the database load brief before you touch Excel:
`db_update_apr_may_2026_brief.md`.

- First complete **Step 0** (the SUB012 prerequisite) if you haven't already —
  it brings your database current with the March close. Your March 31 snapshot
  must read 54 subscriptions before you load April.
- Then run **Stage 1 — April 2026** only. Do **not** load the May block yet;
  loading May early changes seat counts that will throw off your April 30
  snapshot. Two-stage loading discipline: one month at a time.

Run the load's "confirm the load" queries to prove the data landed before you
start querying for the close.

---

## What You're Building

This is a clean monthly close on the redesigned workbook
(`submissions/excel/excel_09_workbook_redesign.xlsx`, carried forward). The four-step
close you built the template for:

1. **Actuals tab** — add the Apr 2026 column and enter April's input numbers
2. **Apr 2026 A vs F tab** — copy the Mar tab, update the config block, verify
3. **KPI Tracker tab** — fill in the Apr 2026 column (auto-pulls from your tab)
4. **WaterfallData tab** — add the April rows for Power BI

Plus the April management commentary, which is a hard gate.

---

## Part 1 — Pull the April Actuals

Run your MRR snapshot query at `2026-04-30`. Same structure you've run four times
now — new date.

Before you open Excel, confirm from the data:

- How many active subscriptions and active customers on April 30?
- **New MRR** — query `subscriptions` for any April 2026 start dates.
- **Expansion MRR** — query `subscription_events` for April seat changes. There is
  expansion this month; check the seat delta and price per seat and derive the
  MRR impact yourself.
- **Churn** — check for any April cancellations. When you find one, look at the
  customer behind it: do they still hold another active subscription, or did the
  whole relationship end? That answer decides whether you call this a revenue
  churn or a logo churn, and it changes both your active-customer count and your
  commentary. Do not assume — verify it in the data.

Run your COGS query at `2026-04-30`. Same structure as prior months — `cost_per_seat`
in place of `price_per_seat`, same point-in-time filter.

**S&M, R&D, and G&A** come from Lisa's monthly close message in #finance-ops — the
same source as every prior month. Do **not** pull OpEx from SQL. Read April's S&M
of $32,000 off her message and enter it from there.

Write down your actuals before going to Excel.

---

## Part 2 — Enter April into the `Actuals` Tab

Add an `Apr 2026` column to the `Actuals` tab and enter April's input cells only —
the yellow INPUT rows: New MRR, Expansion MRR, Churned MRR, S&M, R&D, G&A, New
Customers, Active Customers, Active Subscriptions.

Do **not** type into the blue formula rows:

- **Opening MRR** must derive by formula from March's Closing MRR. You built that
  chain in assignment 09 — let it carry over. If April's Opening MRR doesn't equal
  March's Closing MRR automatically, a formula is missing.
- **Closing MRR, Total OpEx, COGS, Gross Profit, EBITDA** all derive from the inputs
  above them. Never type into them.

**Verify the chain:** after entering April's inputs, confirm April Opening MRR equals
March Closing MRR and April Closing MRR recalculates on its own.

---

## Part 3 — Build the April A vs F Tab

This is the four-step template close you designed in 09. Do it the designed way:

1. **Copy** the `Mar 2026 A vs F` tab. Rename the copy exactly: `Apr 2026 A vs F`.
2. **Update the config block** — the two cells you built for exactly this: set the
   current-month date to April, and set the prior-month tab name to `Mar 2026 A vs F`.
3. **Change nothing else.** Every actual on the tab should now read from the Apr 2026
   column of `Actuals`; the comparison column should point at the March tab via the
   config cell; GRR and NRR should resolve to April's Retention column with no column
   letters; the month-end date should derive to April 30.

The waterfall and P&L structure stay exactly as they are — you are supplying April
data through the plumbing you built, not rebuilding the output. The redesign kept the
Actual / Forecast / $ Variance / % Variance / F/U layout; use it as-is.

**Forecast column:** follow whatever the redesigned tab established for A-vs-F — the
Forecast column holds the original quarterly plan, not a rolling reset, and the
comparison column reads the prior month via the config cell. Do not invent a new
forecast structure for April; carry the one already on the tab.

**Churn variance sign:** the same convention you've used since February — less churn
than plan is favorable, so don't mechanically apply Actual − Forecast on the churn
row. Confirm the F/U column reads correctly for April.

**Test before moving on:** temporarily set the config date back to March — every actual
should show March values. Set it to April again. Any cell still showing a hardcoded
number hasn't been converted, and that is a redesign gap to fix, not to patch.

---

## Part 4 — KPIs Section (Apr 2026 A vs F Tab)

The KPIs section is part of the tab you copied, so it carries the same metric rows.
Confirm each reads April:

| Metric | Source |
|--------|--------|
| Active Customers | from `Actuals` Apr column |
| Active Subscriptions | from `Actuals` Apr column |
| ARPA | derived |
| Gross Margin | derived |
| GRR | dynamic Retention lookup at April month-end |
| NRR | dynamic Retention lookup at April month-end |
| Quick Ratio | derived |
| S&M (actual) | from `Actuals` Apr column — originally Lisa's #finance-ops message |
| CAC — this month | monthly S&M ÷ April new customers |
| LTV / LTV:CAC / CAC Payback | — quarterly metrics, calculated at quarter close, not this month |

Pay attention to NRR this month. Expansion is present, but churn happened too — so
don't assume NRR is back above 100%. Compute it from your retention table and let the
result drive your commentary, whichever side of 100% it lands on.

---

## Part 5 — Management Commentary (April)

3–4 sentences below the KPIs section. **This is a hard gate — the PR will not be
merged without it.**

Remember the commentary discipline from the redesign: the **key-metrics line is
formula-driven** (month, closing MRR, NRR, EBITDA margin all pull from cells — never
typed), and the **qualitative analysis** below it is what you write by hand. Numbers
are never typed into commentary.

Cover these points:

1. **Overall result** — how April closed (MRR, EBITDA) versus plan, in words.
2. **Revenue drivers** — what drove New MRR, and what Expansion did to NRR.
3. **Churn — revenue vs logo (Sarah's follow-up):** name the cancelled subscription
   and state plainly whether this is a **revenue churn or a logo churn**. The customer
   behind April's cancellation still holds another active subscription, so the company
   lost revenue but did not lose the logo. Explain why that distinction matters — what
   it means for the active-customer count, for retention, and for how you'd read the
   churn signal differently than a full logo loss.
4. **Costs** — what OpEx did to the EBITDA margin this month.

---

## Part 6 — Update KPI Tracker Tab

Fill in the `Apr 2026` column. If you built the tracker to reference the monthly tabs
the way the redesign intended, most of this should populate by pulling from
`Apr 2026 A vs F`. Do not overwrite prior months — those cells should still reference
their own tabs. LTV / LTV:CAC / CAC Payback stay as dashes in the April column —
they're quarterly metrics.

---

## Part 7 — Update WaterfallData Tab

Add April's rows directly below the existing March rows, same columns: Month,
Movement, Actual, Forecast, Variance.

- Use the same movement rows you've used since the waterfall began (Opening, New,
  Expansion, Contraction, Churned, Net New, Closing). April has no contraction, so the
  Contraction row carries zero — but keep the row so the table stays consistent across
  months.
- Generate the Month label with the same `TEXT`/`DATE` pattern you used for prior
  months so it reads `Apr-26`.
- The Excel Table expands automatically when you add rows below the existing data.

**Variance sign convention:** positive variance = favorable to revenue vs plan. On the
Churned row, less churn than forecast is positive — don't mechanically apply
Actual − Forecast there.

After saving, refresh Power BI if connected — the Month slicer will pick up April
automatically.

---

## Part 8 — Git Workflow

New assignment = new branch:

```
git checkout main
git pull origin main
git checkout -b student/excel_10_april_close
```

When ready to submit:

```
git add submissions/excel/excel_10_april_close.xlsx
git commit -m "Add: 10 — April 2026 close (Actuals, Apr A vs F tab, KPI Tracker, WaterfallData)"
git push origin student/excel_10_april_close
```

Open a PR from `student/excel_10_april_close` → `main`.

---

## Keep Your Notes Current

Before pushing, update `my-notes/`:

| File | What to add |
|------|------------|
| `my-notes/sql_queries.sql` | April snapshot query; how you identified the April cancellation and checked whether the customer kept another active subscription |
| `my-notes/kpi_definitions.md` | Revenue churn vs logo churn — the distinction, and how each one affects the active-customer count and the retention read |
| `my-notes/excel_techniques.md` | The four-step close on the redesigned workbook in practice — what you actually changed for April (one Actuals column + two config cells) |
| `my-notes/git_commands.md` | Nothing new — verify your workflow notes are current |

---

## Submission

File: `submissions/excel/excel_10_april_close.xlsx`

Open a PR from `student/excel_10_april_close` → `main` with this description:

```
## 10 — April 2026 Close

- Actuals tab: Apr 2026 column added, inputs entered, formula rows derive
- Apr 2026 A vs F tab added by copying Mar tab + updating config block only
- KPI Tracker updated with April column
- WaterfallData updated with April rows
- April commentary present (revenue churn vs logo churn addressed)
- my-notes/ updated

[paste completed Self-Check table here]
```

---

## Self-Check

Run through these before you push. If any value does not match, find the discrepancy
before opening the PR.

| Check | Expected |
|-------|---------|
| April block loaded (Step 0 done, May NOT loaded) | ✅ |
| April Opening MRR | Derived from March Closing — not typed |
| April Closing MRR | $156,830.50 |
| Active Subscriptions | 55 |
| April NRR | just under 100% — expansion is present but churn outweighs it |
| Config block: only the two config cells changed vs the Mar tab | ✅ |
| GRR / NRR formulas: no hardcoded column letters | ✅ |
| WaterfallData: April rows added below March | ✅ |
| KPI Tracker Apr column filled | ✅ |
| Commentary present, and churn correctly identified as revenue (not logo) churn | ✅ (hard gate) |

---

*Excel Assignment 10 — April 2026 Monthly Close*
*Idynamics Finance Analyst Training Program*
*June 2026*
