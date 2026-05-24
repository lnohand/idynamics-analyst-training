# Excel Assignment 09 — Workbook Redesign: Building for Scale
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Before April — fix the foundation, not the symptom
>
> Michael — you've done three monthly closes. Look at what went wrong in each one.
>
> In February, you pointed GRR and NRR at January's Retention column instead of
> February's. In March you made the same mistake again — wrong column on GRR and
> NRR, and your "vs February" comparisons were pulling from January's column.
> These aren't one-off typos. They're the same error, made the same way, for the
> same reason: you're manually updating formula references that hardcode specific
> column letters and tab names, and every month you're one missed update away from
> a number that's silently wrong.
>
> Real FP&A work is repetitive by design. The monthly close happens twelve times
> a year. A process that requires careful manual updates to thirty formula
> references every single month is not a process — it's a liability. The error
> rate compounds with frequency.
>
> This assignment has no new finance concepts. You already know what every metric
> means and how to calculate it. What you're building is infrastructure that makes
> the rest of Q2, Q3, and Q4 maintainable — a workbook where the class of errors
> you keep making is no longer possible.
>
> — David

---

## What's Wrong with the Current Design

After three closes, your workbook has a consistent failure pattern. Every month:

**You update tab references by hand.** Every formula that reads from the prior
month's tab — Opening MRR, comparison columns in the KPI section, cumulative
calculations — contains a hardcoded tab name like `'Feb 2026 A vs F'`. When you
copy the tab for a new month, you must find and update each of these manually.
Miss one, and a cell is silently reading from the wrong month.

**You update column letters by hand.** GRR and NRR reference a specific column
in the Retention tab. That column shifts one position to the right every month.
You have now gotten this wrong twice — not because you weren't paying attention,
but because the design requires you to remember to do it.

**You type numbers into commentary.** The figures in your commentary — closing
MRR, NRR percentage, EBITDA margin — are typed manually. The moment you correct
a formula elsewhere in the tab, those numbers are stale. You have no way to know.

None of these are finance problems. They are design problems. The fix is not to
be more careful — it is to build a workbook where these errors are no longer
possible.

---

## What You're Building

```
                 ┌──────────────────────────────────────────┐
                 │              Actuals tab                  │
                 │  One row per metric. One column per month.│
                 │  You type here. Everything else reads here.│
                 └────────────────────┬─────────────────────┘
                                      │
              ┌───────────────────────┼────────────────────┐
              │                       │                    │
              ▼                       ▼                    ▼
  ┌─────────────────────┐  ┌──────────────────┐  ┌──────────────────┐
  │  Mar 2026 A vs F    │  │   KPI Tracker    │  │  Waterfall Data  │
  │  (your template)    │  │  (auto-updates)  │  │  (Power BI feed) │
  │                     │  └──────────────────┘  └──────────────────┘
  │  Config cell ───►   │
  │  "prior month tab"  │◄── Retention tab
  │  reads dynamically  │    (dynamic date lookup — no column letters)
  └─────────────────────┘
              │
              │  Copy → rename → change one config cell
              ▼
  ┌─────────────────────┐
  │  Apr 2026 A vs F    │
  │  May 2026 A vs F    │
  │  Jun 2026 A vs F    │
  │       ...           │
  └─────────────────────┘
```

When this is done, the monthly close is four steps:

1. Add one column to `Actuals` — enter the month's numbers
2. Copy the prior monthly tab, rename it, update one config cell
3. Verify outputs
4. Write the qualitative commentary

If you find yourself doing anything beyond those four steps, the redesign
is incomplete.

---

## Part 1 — The `Actuals` Input Tab

**The idea:** Right now your actuals live inside each monthly tab — hardcoded
into cells or pasted from SQL results. That means the same number (say, February
S&M spend) exists in three places: in the Feb tab, referenced by the Mar
tab's comparison column, and typed into your commentary. Change it once and
the other two are wrong. The Actuals tab fixes this by being the one place
where data is entered. Every formula everywhere else reads from here.

**The sketch:**

```
     A                    B           C           D           E
     ──────────────────── ─────────── ─────────── ─────────── ───────────
 1   Metric               Jan 2026    Feb 2026    Mar 2026    Apr 2026 →
     ════════════════════════════════════════════════════════════════════
 2   Opening MRR          [formula]   [formula]   [formula]   [formula]
 3   New MRR              [INPUT]     [INPUT]     [INPUT]     [INPUT]
 4   Expansion MRR        [INPUT]     [INPUT]     [INPUT]     [INPUT]
 5   Churned MRR          [INPUT]     [INPUT]     [INPUT]     [INPUT]
 6   Closing MRR          [formula]   [formula]   [formula]   [formula]
     ────────────────────────────────────────────────────────────────────
 7   S&M                  [INPUT]     [INPUT]     [INPUT]     [INPUT]
 8   R&D                  [INPUT]     [INPUT]     [INPUT]     [INPUT]
 9   G&A                  [INPUT]     [INPUT]     [INPUT]     [INPUT]
10   Total OpEx           [formula]   [formula]   [formula]   [formula]
11   COGS                 [formula]   [formula]   [formula]   [formula]
12   Gross Profit         [formula]   [formula]   [formula]   [formula]
13   EBITDA               [formula]   [formula]   [formula]   [formula]
     ────────────────────────────────────────────────────────────────────
14   New Customers        [INPUT]     [INPUT]     [INPUT]     [INPUT]
15   Active Customers     [INPUT]     [INPUT]     [INPUT]     [INPUT]
16   Active Subscriptions [INPUT]     [INPUT]     [INPUT]     [INPUT]

     Legend:  [INPUT] = yellow cell, you type this
              [formula] = blue cell, derived — never type here
```

**Build rules:**

- Opening MRR is always the prior month's Closing MRR — derive it by formula,
  never type it. January's Opening MRR is a one-time historical anchor.
- Closing MRR derives from Opening + New + Expansion − Churned.
- COGS, Gross Profit, Total OpEx, EBITDA all derive from the inputs above them.
- Every cell that requires human input must be visually distinct from every
  formula cell — background colour, font colour, or border. No exceptions.

**Backfill:** Enter January, February, and March actuals into this tab now. Before entering March, also fix the Q1 New Customers formula on the March tab — see the correction note in the "What You Are Not Changing" section below.

> **Data correction — March Expansion MRR:** Your current March tab shows $180.
> That is wrong. Before you enter March actuals into `Actuals`, re-run your
> `subscription_events` query and verify the correct figure. The correct value
> is $380 — SUB012 expanded from 23 to 27 seats at $95/seat. This is the
> number that goes into the Actuals tab.

**Verify:** Change New MRR for February to any number. Confirm that Closing MRR
for February updates, Opening MRR for March updates, and Closing MRR for March
updates. If any step in the chain breaks, a formula is missing.

---

## Part 2 — Monthly Tabs That Self-Configure

**The idea:** Right now, copying the March tab to create April requires hunting
down ~30 formula references and updating each one. You miss one — and you did,
twice — and a cell silently reads from the wrong month. The fix is to put all
month-specific information in a single config block. Every formula on the tab
reads from that block. To create a new month, you update two cells in the config block.

**The sketch — config block (top-right of the monthly tab):**

```
     H                    I                           J
     ──────────────────── ─────────────────────────── ───────────────────────────────
 1   MONTHLY CONFIG
 2   Current month:       [date → 01-Mar-26         ]  ← change these two cells
 3   Prior month tab:     [text → Feb 2026 A vs F  ]     when creating a new month
 4   Month-end date:      [formula → 31-Mar-26     ]  ← derived from row 2, never type this
```

**The sketch — how the waterfall section changes:**

```
     BEFORE                                AFTER
     ─────────────────────────────         ─────────────────────────────────────────
     Opening MRR  ='Feb 2026 A vs F'!B9   Opening MRR  = reads from Actuals[Opening MRR, Mar 2026]
     New MRR       3,000  ← hardcoded     New MRR      = reads from Actuals[New MRR, Mar 2026]
     Expansion     380    ← hardcoded     Expansion    = reads from Actuals[Expansion MRR, Mar 2026]
     Churned       0      ← hardcoded     Churned      = reads from Actuals[Churned MRR, Mar 2026]
     S&M           29,000 ← hardcoded     S&M          = reads from Actuals[S&M, Mar 2026]
```

The month label used to find the right column in Actuals comes from your config
cell — not hardcoded. Change the config cell date to April, and every lookup
automatically finds April's column.

**The sketch — comparison column:**

```
     BEFORE                                AFTER
     ──────────────────────────────────    ──────────────────────────────────────────
     vs Feb  ='Feb 2026 A vs F'!B9        vs Prior  = reads via config["Feb 2026 A vs F"]!B9
             ='Feb 2026 A vs F'!B32                 = reads via config["Feb 2026 A vs F"]!B32
             ...30+ cells to update                 ...update one config cell, all follow
```

**Build steps:**

1. Add the config block in an unused corner of the tab. Label it clearly.
   The config block is documentation as much as it is mechanics — it tells
   anyone opening the tab exactly what month they're in and which month
   precedes it.

2. Rewrite every cell that currently holds a hardcoded actual (New MRR,
   Expansion MRR, Churned MRR, S&M, R&D, G&A, Active Customers, Active
   Subscriptions, New Customers, Opening MRR) to look up its value from
   the `Actuals` tab using the current month label from your config cell.

3. Rewrite the comparison column so that the prior month tab name comes from
   your config cell, not from a hardcoded string in each formula. Excel has
   a function that converts a text string into a live cell reference —
   research it, understand what it does and what its cost is, and use it
   for this purpose.

**Test:** Set the config cell date to February. Every actual on the tab should
show February values. Set it back to March. Everything returns to March. Any
cell still showing a hardcoded number has not been converted.

---

## Part 3 — Dynamic Retention Lookups

**The idea:** GRR and NRR currently reference a specific column letter in the
Retention tab. That letter must be incremented every month — and you have gotten
this wrong twice. The fix is to stop using column letters entirely and instead
let a formula find the right column by matching the month-end date.

**The sketch:**

```
  Retention tab structure:

       ...    Y          Z          AA         AB         AC    ...
  ─────────────────────────────────────────────────────────────────────
  Row 4: ...  30-Nov-25  31-Dec-25  31-Jan-26  28-Feb-26  31-Mar-26 ...
                                       ↑           ↑          ↑
  Row 6: ...   [GRR%]     [GRR%]    [GRR%]      [GRR%]    [GRR%]  ...  ← GRR
  Row 7: ...   [NRR%]     [NRR%]    [NRR%]      [NRR%]    [NRR%]  ...  ← NRR


  BEFORE:  GRR = Retention!AB6    ← column AB = Feb. You typed this manually.
                                    March needs AC. April needs AD. You keep
                                    forgetting.

  AFTER:   GRR = find 31-Mar-26 in row 4 → return value from row 6 at that position
                    ↑
                    month-end date comes from your config cell (EOMONTH formula)
                    no column letters anywhere
```

**Build steps:**

Your config block already holds the current month's first day as a date. Derive
the month-end date from it using the Excel function that returns the last day of
a given month.

Then rewrite GRR and NRR to:
1. Use that month-end date
2. Search row 4 of the Retention tab for a match
3. Return the value in row 6 (or row 7 for NRR) at the matched position

Excel has lookup functions that search a range for a value and return either its
position or a corresponding value from another range. Research your options.
The resulting formula should contain no column letters and no numbers that
you would ever need to change.

**Verify:** Confirm the formula returns the correct GRR for March. Temporarily
set your config cell date to February — the formula should return February's GRR.
Return to March.

---

## Part 4 — Formula-Driven Commentary

**The idea:** The figures in your commentary are typed by hand. Change an
underlying number and your commentary is wrong — silently. The fix is to
generate the key metrics line by formula so it always reflects the current
calculated values.

**The sketch:**

```
  BEFORE:
  ┌────────────────────────────────────────────────────────────────────┐
  │  "March 2026 — Closing MRR: $153,685 | NRR: 100.2% |              │
  │  EBITDA margin: -6.1%. Expansion drove NRR above 100%..."          │
  └────────────────────────────────────────────────────────────────────┘
       ↑ these numbers are typed. Change Expansion MRR above and
         $153,685 is now wrong. You have no warning.


  AFTER:
  ┌────────────────────────────────────────────────────────────────────┐
  │  [formula cell]                                                    │
  │  "March 2026 — Closing MRR: $XXX,XXX | NRR: XX.X% |               │  ← auto-updates
  │  EBITDA margin: -X.X%"                                             │
  ├────────────────────────────────────────────────────────────────────┤
  │  [you write this]                                                  │
  │  "Expansion MRR turned positive for the first time — SUB012 added  │  ← your analysis
  │  4 seats. S&M of $29K came in below the $31K plan. Despite the     │
  │  strong revenue result, EBITDA remains negative as R&D ramp        │
  │  continues. Watch retention closely in April — SUB012 expansion    │
  │  is driving NRR but a single customer concentration risk remains." │
  └────────────────────────────────────────────────────────────────────┘
```

**Build steps:**

Excel has a function that converts a number into formatted text — the same
formats used in cell number formatting (currency, percentage, etc.). Use it
to build a single formula cell that produces the key metrics line: month name,
closing MRR, NRR, EBITDA margin. All values come from formula cells above —
none are typed.

Your qualitative commentary — the analysis, the context, the judgment — sits
in a separate cell or section beneath it. That part is always written by hand.
The rule is: numbers never are.

**Verify:** Change Expansion MRR in `Actuals` for March by $500. The closing
MRR, NRR, and EBITDA margin in your formula line should all update. No text
should require manual editing.

---

## Part 5 — Prove It Works: The April Dry Run

Once all four parts are complete, test the template by running a dry close
for April.

1. Add an `Apr 2026` column to `Actuals` — enter realistic dummy numbers
2. Copy `Mar 2026 A vs F`, rename it `Apr 2026 A vs F`
3. In the config block: update the current month date to April, update
   the prior month tab name to `Mar 2026 A vs F`
4. Do not change anything else

Verify:
- Every actual on the tab reads from the Apr 2026 column in `Actuals`
- GRR and NRR show April's values — no column letters in those formulas
- The commentary formula line shows "April 2026" with correct figures
- No errors anywhere in the workbook

If you need to change anything beyond the two config cells, the redesign
is incomplete. Find what still requires a manual update and fix it.

Delete the April test tab when you're done. It was a dry run, not a real close.

---

## Part 6 — Update Your Notes

After completing the redesign, update `excel_techniques.md` with:

- How the `Actuals` tab works and why centralising data entry matters
- How the config cell approach works and what its limitations are
- How you built the dynamic Retention lookup and why it is better than
  a column letter reference
- What function you used to convert a text string into a live cell reference,
  and when you would and would not use it
- How `TEXT()` concatenation works for formula-driven commentary
- The four-step monthly close workflow going forward

These notes are for the version of you who picks this workbook up in October
and needs to understand why things were built the way they were.

---

## What You Are Not Changing

- The Retention tab — do not modify it. Your formulas must work with it as-is.
- The Engine, Waterfall, and Unit Economics tabs — leave entirely alone.
- The tab layout and visual structure of your monthly tabs — waterfall, P&L,
  KPIs, commentary sections all stay the same. You are changing the plumbing
  that supplies data, not the output.
- January and February tabs — closed months. Do not modify them. Your redesign
  applies to March and forward.

> **Formula correction — Q1 New Customers:** The Q1 Roll-Up section of your
> March tab has a logic error in the New Customers formula. It is computing a
> net delta (end count minus start count) instead of summing the new logos
> acquired each month. The correct approach: add up new customers from each
> monthly tab separately — January (1) + February (2) + March (2) = 5 total
> Q1 new customers. Fix this formula while you have the tab open. It cascades
> into Quarterly CAC — the correct Q1 CAC is $18,000, not $30,000.

---

## Submission

File: `submissions/excel/excel_09_workbook_redesign.xlsx`

Branch: `student/excel_09_workbook_redesign` → open a PR to `main`

PR description:

```
## 09 — Workbook Redesign

- Actuals tab created; Jan/Feb/Mar data backfilled; March Expansion MRR corrected to $380
- Q1 New Customers formula corrected on March tab: 1+2+2=5, CAC = $18K
- Monthly tab config block added; all actuals pull from Actuals tab
- GRR/NRR: dynamic Retention lookup — no column letters in formulas
- Comparison column: prior month references via config cell
- Commentary: formula-driven key metrics line implemented
- April dry run: changed two config cells only, all outputs correct, no errors
- excel_techniques.md updated

[self-check table]
```

---

## Self-Check

| Check | Expected |
|-------|---------|
| March Expansion MRR in `Actuals` is $380 (not $180) | ✅ |
| Q1 New Customers = 5 (1+2+2), Quarterly CAC = $18,000 | ✅ |
| Changing any input in `Actuals` updates all downstream monthly tabs | ✅ |
| Changing the month date in the config block re-points all actuals | ✅ |
| GRR and NRR formulas contain no hardcoded column letters or numbers | ✅ |
| Comparison column: no hardcoded tab name in any formula | ✅ |
| April dry run: correct outputs with only the config block changed | ✅ |
| April dry run: no errors anywhere in the workbook | ✅ |
| Commentary key metrics line updates when actuals change | ✅ |
| Jan and Feb tabs unchanged | ✅ |
| `excel_techniques.md` updated | ✅ |

---

*Excel Assignment 09 — Workbook Redesign: Building for Scale*
*Idynamics Finance Analyst Training Program*
*May 2026*
