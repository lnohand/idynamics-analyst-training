# Excel Assignment 01 — MRR Engine
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** MRR workbook — need the engine built before Thursday
>
> Michael — the SQL exports look good. Now I need you to build the
> actual MRR engine in Excel.
>
> The events export has every change that ever happened to a subscription.
> Your job is to classify each event, calculate the dollar impact, and
> roll it all up into a monthly waterfall. That waterfall is what goes
> in front of the board.
>
> I want to see the logic, not just the answer. Build it step by step
> so I can audit every formula. If something doesn't tie, I need to
> be able to trace it back to the source row.
>
> — David

---

## What You're Building

An MRR engine that turns 97 raw events into a monthly waterfall showing
how MRR grew from $0 to ~$144K over 26 months. By the end you will
have:

- Every event classified as New, Expansion, Contraction, or Churned
- A dollar amount calculated for every event
- A monthly waterfall: Opening → + New → + Expansion → − Contraction
  → − Churned → Closing
- A reconciliation check against the snapshot MRR

---

## Part 1 — Setup

### Step 1: Create the workbook

Create a new workbook called `idynamics_mrr_workbook.xlsx`.

Create these tabs:

| Tab name | Purpose |
|---|---|
| [RAW] Events | Paste of mrr_events.csv — do not edit this tab |
| [RAW] Snapshot | Paste of mrr_snapshot.csv — do not edit this tab |
| [RAW] Cash | Paste of mrr_cash_trend.csv — do not edit this tab |
| Ref | Reference tables (plan pricing, movement rules) |
| Engine | Where you classify events and calculate deltas |
| Waterfall | Monthly summary — the deliverable |

### Step 2: Import the SQL exports

For each CSV:
1. Open the CSV in Excel (separate window)
2. Select all (Ctrl+A), copy (Ctrl+C)
3. Go to the matching RAW tab, click cell A1
4. Paste Special → Values only (Ctrl+Shift+V)
5. Format as Table (Ctrl+T), confirm the range

Name each table:

| Tab | Table name |
|---|---|
| [RAW] Events | `tbl_Events` |
| [RAW] Snapshot | `tbl_Snapshot` |
| [RAW] Cash | `tbl_Cash` |

**Self-check after paste:**

| Check | Expected |
|---|---|
| tbl_Events row count | 97 |
| tbl_Snapshot row count | 51 |
| tbl_Cash row count | 26 |
| `=SUM(tbl_Snapshot[mrr])` | **$144,185.50** |

> Put each check formula below its table. If the snapshot SUM doesn't
> match, stop. The data import is wrong.

### Step 3: Build the plan pricing reference table

Go to the **Ref** tab. Create a small table with the standard monthly
price per seat for each plan. Format it as a table named `tbl_Plans`.

| plan_name | monthly_price |
|---|---|
| Analytics Starter | 45 |
| Analytics Growth | 95 |
| Analytics Enterprise | 180 |
| Marketing Pro | 85 |
| Sales Hub | 110 |
| Platform Suite | 150 |

> **Why you need this:** When a subscription upgrades from Analytics
> Starter to Analytics Growth, the events table tells you the old and
> new plan *names* — not the prices. You need this lookup table to
> turn plan names into dollar amounts.
>
> **Annual plans:** The annual price_per_seat in the database is 12×
> the monthly rate. You don't need to store annual prices here —
> the ÷12 billing adjustment handles it. This table stores monthly
> rates only.

---

## Part 2 — Build the Engine Tab

### Step 4: Copy events data to the Engine tab

Copy the entire tbl_Events table to the Engine tab. This is your
working copy — the RAW tab stays untouched.

> **Tip:** Select the full table in [RAW] Events, copy, then Paste
> Special → Values into the Engine tab starting at A1. Format as a
> new table named `tbl_Engine`.

You now have 97 rows with all the event data. You'll add new columns
to the right of the existing data.

### Step 5: Add the Movement column

Add a new column to tbl_Engine called **movement**.

This column classifies every event into one of four categories:

| movement | When to use it |
|---|---|
| New | Event type is `created` |
| Expansion | A change that *increases* MRR |
| Contraction | A change that *decreases* MRR |
| Churned | Event type is `cancelled` |

The logic for `created` and `cancelled` is straightforward — those
event types always map to the same movement.

The challenge is the middle four event types. For each one, you need
to look at old_value and new_value to decide direction:

| event_type | Expansion when... | Contraction when... |
|---|---|---|
| seats_change | new_value > old_value | new_value < old_value |
| price_change | new_value > old_value | new_value < old_value |
| plan_upgrade | always | — |
| plan_downgrade | — | always |
| discount_added | — | always (adding a discount reduces MRR) |

**Formula hint:** Look at `IFS()`. It evaluates conditions top to
bottom and returns the result for the first match. You can nest
multiple conditions to cover all seven event types.

**Self-check:**

| movement | Count |
|---|---|
| New | 62 |
| Expansion | 15 |
| Contraction | 9 |
| Churned | 11 |
| **Total** | **97** |

> Use `COUNTIF` on your movement column to verify. If any row is blank
> or says something unexpected, your IFS logic missed a case.

### Step 6: Add the MRR Delta column

Add a new column called **mrr_delta**.

This is the dollar impact of each event. Positive for New and Expansion.
Negative for Contraction and Churned.

Every delta formula follows the same pattern:

```
[quantity change] × [price component] × (1 − discount/100) × [billing adjustment]
```

The billing adjustment is: if billing_cycle = "Annual", divide by 12.
If "Monthly", multiply by 1 (no change).

But what goes into [quantity change] and [price component] depends on
the event type. Think through each one:

**created:** The subscription just started. What is its full MRR?
You have seats, price_per_seat, discount_percent, and billing_cycle
in the row.

**cancelled:** The subscription ended. How much MRR was lost? Same
fields, but the result should be negative.

**seats_change:** The seat count changed. The price stayed the same.
What is the dollar impact of the seat delta? You have old_value and
new_value (which are seat counts), plus price_per_seat, discount,
and billing_cycle.

**price_change:** The price changed. The seat count stayed the same.
What is the dollar impact? old_value and new_value are prices. You
need seats from the export.

**plan_upgrade / plan_downgrade:** The plan changed. old_value and
new_value are plan *names*, not prices. You need to look up the
monthly price for the old plan and the new plan from your tbl_Plans
reference table. Then calculate: seats × (new_price − old_price) ×
(1 − discount/100) × billing adjustment. Upgrades are positive,
downgrades are negative.

> **Lookup hint:** `XLOOKUP(old_value, tbl_Plans[plan_name],
> tbl_Plans[monthly_price])` returns the monthly price for the
> old plan name. Same pattern for the new plan.
>
> **Annual plan wrinkle:** The plans table stores monthly prices.
> The subscriptions table stores annual price_per_seat as the full
> year amount (monthly × 12). When you look up a plan price from
> tbl_Plans for an annual subscription, you're getting the monthly
> rate — but then the ÷12 billing adjustment would wrongly divide
> it again. Think about when to apply the ÷12 and when not to.
> For plan changes, the lookup already gives you the monthly rate,
> so you do NOT divide by 12 again.

**discount_added:** A discount was applied. old_value and new_value
are discount percentages. The MRR reduction is: seats × price ×
(new_discount − old_discount) / 100 × billing adjustment. This
should be negative (contraction).

**Formula hint:** Build this as a nested IFS like the movement column.
Each branch handles one event_type with its own formula. Start with
the easiest case (`created`) and work your way through.

> **Build and check one event type at a time.** Don't try to write
> the full formula in one go. Get `created` working first, verify a
> few rows by hand, then add `cancelled`, and so on.

**Self-checks (verify specific rows):**

| Event | Type | Expected mrr_delta |
|---|---|---|
| EVT001 | created | $1,900.00 |
| EVT003 | created | $1,955.00 |
| EVT023 | cancelled | −$1,900.00 |
| EVT042 | price_change (80→85) | $140.00 |
| EVT057 | seats_change (22→19) | −$255.00 |
| EVT074 | plan_upgrade (Starter→Growth) | $800.00 |
| EVT053 | plan_downgrade (Growth→Starter) | −$650.00 |
| EVT081 | plan_upgrade (Growth→Enterprise) | $2,210.00 |
| EVT055 | discount_added (0→5%, Annual) | −$104.50 |

> If EVT055 doesn't match, check your billing cycle logic for
> discount events on annual subscriptions.

**Column totals self-check:**

| movement | SUM of mrr_delta |
|---|---|
| New | $161,459.00 |
| Expansion | $10,210.00 |
| Contraction | −$2,361.00 |
| Churned | −$17,273.50 |
| **Grand total** | **$152,034.50** |

> Use `SUMIF(movement_column, "New", delta_column)` to check each
> category.

---

## Part 3 — Monthly Waterfall

### Step 7: Build the Waterfall tab

Go to the **Waterfall** tab. Create a table with one row per month
and these columns:

| Column | What goes here |
|---|---|
| month | Each month from 2024-01 through 2026-02 (26 rows) |
| opening_mrr | Prior month's closing_mrr. First month = 0. |
| new_mrr | Sum of all mrr_delta where movement = "New" for this month |
| expansion_mrr | Sum of all mrr_delta where movement = "Expansion" for this month |
| contraction_mrr | Sum of all mrr_delta where movement = "Contraction" for this month |
| churned_mrr | Sum of all mrr_delta where movement = "Churned" for this month |
| net_change | new + expansion + contraction + churned |
| closing_mrr | opening_mrr + net_change |

**For the movement columns:** You need to sum mrr_delta from
tbl_Engine, filtered by two conditions — the month AND the movement
type.

> **Formula hint:** `SUMIFS` takes a sum range and one or more
> criteria pairs. You need to match both the month column and the
> movement column from tbl_Engine.

**For opening_mrr:** Each row's opening equals the prior row's
closing. The first row (2024-01) starts at $0 — there was no MRR
before the first subscription.

**For closing_mrr:** `= opening_mrr + net_change`. This is pure
arithmetic — no lookup needed.

**Self-checks:**

| Month | Opening | New | Expansion | Contraction | Churned | Net | Closing |
|---|---|---|---|---|---|---|---|
| 2024-01 | $0.00 | $5,800.00 | $0.00 | $0.00 | $0.00 | $5,800.00 | $5,800.00 |
| 2024-08 | $45,353.50 | $6,840.00 | $0.00 | $0.00 | −$1,900.00 | $4,940.00 | $50,293.50 |
| 2025-03 | $108,159.00 | $19,390.00 | $0.00 | −$1,009.50 | $0.00 | $18,380.50 | $126,539.50 |
| 2025-08 | $151,014.50 | $0.00 | $2,960.00 | −$710.00 | −$4,680.00 | −$2,430.00 | $148,584.50 |
| 2026-02 | $152,628.50 | $0.00 | $0.00 | $0.00 | −$594.00 | −$594.00 | **$152,034.50** |

> If your 2024-01 closing doesn't match $5,800, check your SUMIFS —
> you may be matching the wrong month format. The month column in
> tbl_Engine must match exactly what you typed in the Waterfall tab.

---

## Part 4 — Reconciliation

### Step 8: Check the waterfall against the snapshot

Your waterfall closing MRR in the last row (2026-02) should be
**$152,034.50**. Your snapshot SUM is **$144,185.50**.

These don't match. The gap is **$7,849.00**.

**This is expected.** Do not go back and change your formulas to force
a match. The gap is real, and understanding why it exists is part of
the exercise.

**Why the gap exists:**

The events export joins to the subscriptions table, which stores each
subscription's **current** state — not what it looked like at the time
of each event. Twenty-four subscriptions changed after they were created
(seat increases, price changes, plan upgrades, discounts). For those
subscriptions, the `created` event row uses today's seats and price,
which are higher or lower than what they were at signup.

That means the "New MRR" column in the waterfall is overstated for
subscriptions that later expanded and understated for those that
contracted. The change events then add or subtract their deltas on
top, resulting in double-counting.

Example: SUB012 started with 18 seats in June 2024 but later grew
to 23 seats. The export shows 23 seats on the `created` row. So the
waterfall counts 23 × $95 = $2,185 as New MRR, then also counts
(23 − 18) × $95 = $475 as Expansion. The real New MRR should have
been 18 × $95 = $1,710. The difference ($475) is counted twice.

**What to do about it:**

On the Waterfall tab, below the table, add three cells:

```
Waterfall Closing MRR:   [formula referencing last row closing]
Snapshot MRR:            $144,185.50
Reconciliation Gap:      [formula: waterfall - snapshot]
```

The gap should show **$7,849.00**. If it doesn't, you have a formula
error somewhere.

> **Why this matters in real life:** Every finance team that builds
> an MRR waterfall from current-state data hits this problem. The
> solution is to reconstruct the historical state of each subscription
> at the time of each event — which requires more advanced SQL
> (window functions with PARTITION BY). We'll revisit that in a later
> module. For now, the gap is documented and understood.

---

## Part 5 — Format and Review

### Step 9: Format the Waterfall tab for readability

- All dollar columns: Accounting format, 2 decimal places
- Negative values: show in red or in parentheses
- Contraction and Churned columns should always be negative or zero
- Add a header row above the table: **MRR Waterfall — January 2024
  to February 2026**
- Freeze the header row so month labels stay visible when scrolling

### Step 10: Final review

Walk through these checks before submitting:

- [ ] tbl_Events: 97 rows
- [ ] tbl_Snapshot: 51 rows, SUM(mrr) = $144,185.50
- [ ] Movement column: 62 New + 15 Expansion + 9 Contraction + 11 Churned = 97
- [ ] mrr_delta spot checks: at least 3 events match the values in Step 6
- [ ] Waterfall 2024-01 closing = $5,800.00
- [ ] Waterfall 2026-02 closing = $152,034.50
- [ ] Reconciliation gap = $7,849.00
- [ ] No blank cells in the movement or mrr_delta columns

---

## Hints — Only Read If You're Stuck

These are not instructions. They are nudges. Try to build each step
on your own first.

<details>
<summary>Stuck on the movement IFS formula?</summary>

Think about the order of your conditions. Handle the simple cases
first (created → "New", cancelled → "Churned"), then plan_upgrade
and plan_downgrade (always one direction), then discount_added
(always Contraction), then seats_change and price_change (which
depend on comparing old_value to new_value).

Remember: old_value and new_value are stored as text. You may need
to convert them to numbers before comparing. `VALUE()` turns text
into a number in Excel.
</details>

<details>
<summary>Stuck on the mrr_delta formula?</summary>

Break it into cases. If you have 7 event types and each needs a
different formula, that's 7 branches in your IFS. Start with
`created` — it's the simplest because you just multiply:
seats × price_per_seat × (1 − discount_percent/100) and adjust
for billing cycle.

For plan changes, the tricky part is the lookup. You need two
lookups per event — one for the old plan price and one for the
new plan price. The delta is seats × (new_price − old_price).
</details>

<details>
<summary>Stuck on SUMIFS?</summary>

SUMIFS takes this shape:
`SUMIFS(what_to_sum, range1, criteria1, range2, criteria2)`

You want to sum mrr_delta from tbl_Engine where the month column
equals a specific month AND the movement column equals a specific
movement type.
</details>

---

## Submission

Save the workbook. Commit to your repo:

```
submissions/excel/01_mrr_engine.xlsx
```

Branch: `student/excel-01-mrr-engine`

PR description:

```
## What this does
MRR engine workbook: 97 events classified into 4 movement types,
dollar deltas calculated, monthly waterfall from Jan 2024 to Feb 2026.

## Self-check
Snapshot MRR: $144,185.50 ✅
Movement counts: 62 New / 15 Expansion / 9 Contraction / 11 Churned ✅
Waterfall closing: $152,034.50 ✅
Reconciliation gap: $7,849.00 (documented — current-state data limitation)

## Questions for reviewer
[Anything you're unsure about]
```

---

## What Comes Next

The waterfall you just built has the right structure but an imperfect
data source. In the next assignment, you'll:

- Build the **MRR Mix** tab from the snapshot (pivot tables by plan,
  region, billing cycle, account owner)
- Add a **waterfall chart** that visualizes the monthly movements
- Calculate **retention metrics** (GRR and NRR) from the waterfall
- Assemble a **Dashboard** tab for board presentation

The engine is the foundation. Everything else references it.

---

*Idynamics Finance Analyst Training Program*
*Excel Assignment 01 — MRR Engine*
*March 2026*
