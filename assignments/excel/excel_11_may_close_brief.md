# Excel Assignment 11 — May 2026 Monthly Close
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** May close — a movement type you haven't booked before
>
> Michael — May is another clean monthly close on the rebuilt workbook, with one
> genuinely new thing in the data: a **contraction**. One of our existing
> subscriptions shrank its seat count — it didn't cancel, it got smaller. That is
> a distinct movement in the waterfall, separate from churn and separate from
> expansion, and your workbook has never had to book one before.
>
> When you redesigned the workbook in 09, the Actuals tab carries New, Expansion,
> and Churned — there is no Contraction row. So this month you extend the tab and
> the closing-MRR logic to handle it. Think about where contraction sits in the
> movement chain and what sign it carries before you wire anything up.
>
> One more contrast worth drawing out in your commentary: April's cancellation was
> a revenue churn — the customer stayed. May's cancellation is a logo churn — the
> whole relationship ended. Two cancellations, two different stories. Say which is
> which and why it matters.
>
> Load May first, then close it. Same drill — new movement type.
>
> — David

---

## Before You Start — Load May

Run the **May block** of the database load brief before you touch Excel:
`db_update_apr_may_2026_brief.md`.

- April must already be closed and its block already loaded. Step 0 (the SUB012
  prerequisite) should long since be done.
- Run **Stage 2 — May 2026** now. The two-stage loading discipline matters here too:
  you only load May once April is closed, so May's seat changes never contaminate
  your April 30 snapshot.

Run the load's "confirm the load" queries to prove the data landed — in particular,
confirm the contraction (SUB051 down to 19 seats) and the cancellation (SUB026 →
churned) before you start the close.

---

## What You're Building

A clean monthly close on the redesigned workbook (carried forward from assignment 10),
**plus** a one-time structural change to handle contraction:

1. **Actuals tab** — add the May 2026 column, **add a Contraction row**, and extend the
   Closing MRR logic to include it
2. **May 2026 A vs F tab** — copy the Apr tab, update the config block, add the
   Contraction movement, verify
3. **KPI Tracker tab** — fill in the May 2026 column
4. **WaterfallData tab** — add May's rows (now including a Contraction row)

Plus the May management commentary, a hard gate, which must cover the contraction
signal and the logo-vs-revenue churn contrast.

---

## Part 1 — Pull the May Actuals

Run your MRR snapshot query at `2026-05-31`. Same structure as every prior month.

Before you open Excel, confirm from the data:

- How many active subscriptions and active customers on May 31?
- **New MRR** — query `subscriptions` for May 2026 start dates.
- **Expansion MRR** — query `subscription_events` for May seat increases; derive the
  MRR impact from the seat delta and price per seat.
- **Contraction MRR (new this month)** — query `subscription_events` for a May seat
  *decrease* on an existing, still-active subscription. This is not a cancellation —
  the subscription is smaller, not gone. Derive the MRR impact of the shrink. Think
  about the sign before you record it: contraction reduces MRR.
- **Churn** — check for any May cancellations, and again check the customer behind it.
  This month the cancellation ends the whole relationship, so it is a logo churn —
  confirm that in the data rather than assuming it.

Run your COGS query at `2026-05-31`. Same structure as prior months.

**S&M, R&D, and G&A** come from Lisa's monthly close message in #finance-ops — same
source as always. Do **not** pull OpEx from SQL. Read May's S&M of $29,000 off her
message.

Write down your actuals before going to Excel.

---

## Part 2 — Extend `Actuals`: Add a Contraction Row

This is the one-time structural step for May.

The Actuals tab currently carries the movement inputs New MRR, Expansion MRR, and
Churned MRR, with Closing MRR derived. There is **no Contraction row**. Add one.

- Insert a **Contraction MRR** input row in the movement block, in the position that
  matches where contraction sits in the waterfall (after Expansion, before Churn — the
  standard movement order: Opening → New → Expansion → Contraction → Churn → Closing).
- Enter May's contraction as an input. Decide and apply the sign consistently with how
  you store Churned MRR, so the closing formula treats reductions the same way across
  rows.
- **Extend the Closing MRR formula** so it now includes contraction. Closing MRR is
  Opening plus the positive movements less the negative ones — contraction belongs on
  the reducing side alongside churn. Do not leave it out of the chain; if the row exists
  but Closing MRR doesn't read it, your close will be silently overstated.

Then enter the rest of May's inputs in the May 2026 column: New MRR, Expansion MRR,
Contraction MRR, Churned MRR, S&M, R&D, G&A, New Customers, Active Customers, Active
Subscriptions. Leave the blue formula rows (Opening MRR, Closing MRR, Total OpEx, COGS,
Gross Profit, EBITDA) to derive.

**Verify the chain:** May Opening MRR equals April Closing MRR, and May Closing MRR
recalculates from all four movements — confirm that changing the contraction input
moves Closing MRR.

> Because earlier months (Jan–Apr) had no contraction, their Contraction cells should be
> zero/blank inputs. Adding the row must not disturb closed months — confirm their
> closing MRRs are unchanged after you insert the row.

---

## Part 3 — Build the May A vs F Tab

The same template close, with the contraction movement now flowing through:

1. **Copy** the `Apr 2026 A vs F` tab. Rename the copy exactly: `May 2026 A vs F`.
2. **Update the config block** — set the current-month date to May and the prior-month
   tab name to `Apr 2026 A vs F`.
3. **Add the Contraction movement to the waterfall section** on this tab if your monthly
   template doesn't already surface it. The waterfall needs a Contraction row that reads
   May's contraction from the `Actuals` May column (via the config month label, the same
   way every other actual is pulled), and the Closing MRR on the tab must include it.
   Everything else should self-configure off the two config cells — comparison column off
   the prior tab, GRR/NRR off May's Retention column, month-end date deriving to May 31.

Keep the existing waterfall/P&L/KPIs/commentary layout and the
Actual / Forecast / $ Variance / % Variance / F/U structure. Carry the Forecast column
treatment the redesigned tab already established — the Forecast column holds the original
plan; the comparison column reads the prior month via the config cell. Don't invent a new
forecast structure for the contraction row; give it a forecast consistent with how the
other movement rows on the tab are forecast (the plan didn't anticipate this specific
contraction, so think about what the right forecast comparison is and keep your variance
sign convention consistent).

**Churn variance sign:** unchanged — less churn than plan is favorable; don't mechanically
apply Actual − Forecast on the churn row. Apply the same care to the contraction row's
F/U.

**Test:** set the config date back to April — the tab should show April values (and the
contraction row should read April's contraction, which is zero). Set it to May again. Any
cell still showing a hardcoded number hasn't been converted.

---

## Part 4 — KPIs Section (May 2026 A vs F Tab)

The KPIs section carries over from the copied tab. Confirm each reads May:

| Metric | Source |
|--------|--------|
| Active Customers | from `Actuals` May column |
| Active Subscriptions | from `Actuals` May column |
| ARPA | derived |
| Gross Margin | derived |
| GRR | dynamic Retention lookup at May month-end |
| NRR | dynamic Retention lookup at May month-end |
| Quick Ratio | derived |
| S&M (actual) | from `Actuals` May column — originally Lisa's #finance-ops message |
| CAC — this month | monthly S&M ÷ May new customers |
| LTV / LTV:CAC / CAC Payback | — quarterly metrics, calculated at quarter close, not this month |

Note that contraction pulls **down** on NRR even while expansion pushes it up — make sure
your NRR reflects both, and that your commentary reads the net.

---

## Part 5 — Management Commentary (May)

3–4 sentences below the KPIs section. **This is a hard gate — the PR will not be merged
without it.**

Same commentary discipline: the **key-metrics line is formula-driven** (month, closing
MRR, NRR, EBITDA margin pull from cells — never typed); the **qualitative analysis** below
is written by hand; numbers are never typed into commentary.

Cover these points:

1. **Overall result** — how May closed (MRR, EBITDA) versus plan, in words.
2. **The contraction signal (headline this month):** name the subscription that shrank and
   explain what a contraction signals — an existing customer reducing usage, not leaving.
   Why is a contraction a different (and in some ways more diagnostic) signal than a new
   logo or a churn? What would you watch next on that account?
3. **Churn — logo vs revenue, contrasted with April:** name May's cancelled subscription
   and state that this is a **logo churn** — the entire customer relationship ended.
   Contrast it explicitly with April's cancellation, which was a **revenue churn** (that
   customer stayed on another subscription). Explain why the two are read differently:
   what each does to the active-customer count and to your view of retention.
4. **Costs** — what OpEx did to the EBITDA margin this month.

---

## Part 6 — Update KPI Tracker Tab

Fill in the `May 2026` column, pulling from `May 2026 A vs F` the same way the tracker
references the other monthly tabs. Do not overwrite prior months. LTV / LTV:CAC / CAC
Payback stay as dashes in the May column — quarterly metrics.

---

## Part 7 — Update WaterfallData Tab

Add May's rows directly below the existing April rows, same columns: Month, Movement,
Actual, Forecast, Variance.

- **Contraction adds a row that now carries a real value.** The Contraction row has been
  present (at zero) since the waterfall began for consistency; this month it holds an
  actual contraction figure. Make sure it's populated for May and that the sign matches
  how you stored it in `Actuals`.
- Keep the full movement set per month: Opening, New, Expansion, Contraction, Churned, Net
  New, Closing.
- Generate the Month label with the same `TEXT`/`DATE` pattern so it reads `May-26`.
- The Excel Table expands automatically when you add rows below the existing data.

**Variance sign convention:** positive variance = favorable to revenue vs plan. Churn and
contraction both reduce revenue — apply your sign convention consistently so a worse-than-
plan contraction reads as unfavorable.

After saving, refresh Power BI if connected — the Month slicer will pick up May
automatically.

---

## Part 8 — Git Workflow

New assignment = new branch:

```
git checkout main
git pull origin main
git checkout -b student/excel_11_may_close
```

When ready to submit:

```
git add submissions/excel/excel_11_may_close.xlsx
git commit -m "Add: 11 — May 2026 close (Contraction movement, May A vs F tab, KPI Tracker, WaterfallData)"
git push origin student/excel_11_may_close
```

Open a PR from `student/excel_11_may_close` → `main`.

---

## Keep Your Notes Current

Before pushing, update `my-notes/`:

| File | What to add |
|------|------------|
| `my-notes/sql_queries.sql` | May snapshot query; the `subscription_events` query that isolates a seat *decrease* (contraction) from an expansion and from a cancellation |
| `my-notes/kpi_definitions.md` | **Contraction** as a movement type — what it is, how it differs from churn and from expansion, where it sits in the waterfall and what sign it carries; how contraction affects NRR; logo churn vs revenue churn recap with the April/May examples |
| `my-notes/excel_techniques.md` | How you extended the Actuals tab and the Closing MRR logic to add a movement row without disturbing closed months |
| `my-notes/git_commands.md` | Nothing new — verify your workflow notes are current |

---

## Submission

File: `submissions/excel/excel_11_may_close.xlsx`

Open a PR from `student/excel_11_may_close` → `main` with this description:

```
## 11 — May 2026 Close

- Actuals tab: Contraction row added; Closing MRR logic extended; May 2026 column entered
- May 2026 A vs F tab added by copying Apr tab + updating config block, with Contraction movement
- KPI Tracker updated with May column
- WaterfallData updated with May rows (Contraction row now populated)
- May commentary present (contraction signal + logo vs revenue churn contrast)
- Closed months unchanged after adding the Contraction row
- my-notes/ updated

[paste completed Self-Check table here]
```

---

## Self-Check

Run through these before you push. If any value does not match, find the discrepancy
before opening the PR.

| Check | Expected |
|-------|---------|
| May block loaded (after April closed) | ✅ |
| May Opening MRR | Derived from April Closing — not typed |
| Contraction row added to Actuals and included in Closing MRR logic | ✅ |
| Closed months (Jan–Apr) unchanged after adding the Contraction row | ✅ |
| May Closing MRR | $160,075.50 |
| Active Subscriptions | 56 |
| Config block: only the two config cells changed vs the Apr tab | ✅ |
| GRR / NRR formulas: no hardcoded column letters | ✅ |
| WaterfallData: May rows added below April, Contraction row populated | ✅ |
| KPI Tracker May column filled | ✅ |
| Commentary present, covering the contraction signal and logo-vs-revenue churn | ✅ (hard gate) |

---

*Excel Assignment 11 — May 2026 Monthly Close*
*Idynamics Finance Analyst Training Program*
*June 2026*
