# Excel Assignment 09 — Workbook Redesign: Building for Scale
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Before we start Q2 — fix the foundation
>
> Michael — before you open a new tab for April, I want you to step back and look
> at what you've built.
>
> Over the last three months, every close has required you to update dozens of
> formula references, increment column letters by hand, and type numbers into
> commentary that you'd already calculated. That's not a process — that's a
> liability. Each manual step is a chance to miss something, copy a stale value,
> or introduce a subtle error that doesn't surface until the board asks a question
> you can't answer cleanly.
>
> Real FP&A work is repetitive by design. The monthly close happens every month.
> The job isn't just to get the right number once — it's to build something that
> produces the right number every time, with less effort and fewer decisions, not more.
>
> This assignment has no new finance concepts. You already know what every metric
> means and how to calculate it. What you're building here is the infrastructure
> that makes the rest of Q2, Q3, and Q4 maintainable.
>
> — David

---

## What's Wrong with the Current Design

You've done three monthly closes. Each one required:

- Copying a tab and manually updating every cross-tab formula reference
  (`'Jan 2026 A vs F'` → `'Feb 2026 A vs F'` → scattered across 30+ cells)
- Incrementing a column letter by hand to point GRR and NRR at the right month
  in the Retention tab — a step you got wrong in Round 1 of your March submission
- Writing commentary and hardcoding the numbers into the text — numbers that
  became stale the moment a formula above them changed

None of these are finance problems. They're design problems. And the fix is not
to be more careful — it's to build a workbook where the mistakes are no longer possible.

---

## What You're Building

Three structural changes to the workbook:

1. **An `Actuals` input tab** — a single table where all monthly actuals live.
   Every monthly close tab and the WaterfallData tab read from here.
   Data entry happens in one place. Formulas live everywhere else.

2. **A monthly tab that configures itself** — one cell on each monthly tab
   stores the prior month's tab name. Every formula that references the prior
   month points to that one cell. When you copy the tab for a new month,
   you change one cell — not thirty.

3. **Dynamic retention lookups** — GRR and NRR formulas that find the right
   column in the Retention tab automatically, using the current month's date,
   not a hardcoded column letter. This formula never needs to change.

After this redesign, the monthly close workflow becomes:
1. Add a column to `Actuals` and enter the month's numbers
2. Copy the monthly tab template, rename it, update the config cell
3. Verify outputs
4. Write the qualitative commentary

That's it.

---

## Part 1 — The `Actuals` Input Tab

Create a new tab called `Actuals`.

Design it as a clean table:
- **Rows:** one per metric (New MRR, Expansion MRR, Churned MRR, S&M, R&D, G&A,
  New Customers this month, Active Customers at close, Active Subscriptions at close)
- **Columns:** one per month, starting with January 2026. The header row holds
  the month label.

**Rules for this tab:**
- Every cell that requires a human to enter a value should be visually distinct
  from formula cells. Pick a convention — background colour, border, font — and
  use it consistently. Someone looking at this tab for the first time should
  immediately know what they need to fill in.
- Opening MRR for each month must derive from the prior month's closing MRR by
  formula. It is never typed in.
- Closing MRR derives from Opening + Net New by formula.
- COGS, Gross Profit, Total OpEx, EBITDA derive by formula from the inputs above.

When you are done, the `Actuals` tab should contain everything needed to
reconstruct any month's close without opening the monthly tab at all.

**Verify:** Delete the value in one of your input cells. Confirm that every
downstream calculation — on this tab and on the monthly tab — updates or shows
an error. Then restore the value.

---

## Part 2 — A Monthly Tab That Configures Itself

Take the `Mar 2026 A vs F` tab. You are going to restructure how it gets data.

**Step 1 — Add a config cell.**

In an unused area of the tab (top-right corner works), create a labelled cell
that holds the name of the prior month's tab as plain text. This is the only
cell you will change when you copy the template for a new month.

**Step 2 — Remove all hardcoded tab references from formulas.**

Every formula that currently contains `'Feb 2026 A vs F'` needs to be rewritten
to reference that config cell instead. Excel has a function that converts a text
string into a live cell reference — look it up, understand what it does and what
its limitations are before using it.

Your target: every formula on this tab that currently hardcodes a tab name
should reference the config cell. Changing the config cell should be the only
action required to re-point the entire tab at a different prior month.

**Step 3 — Pull actuals from `Actuals`, not from formulas on this tab.**

The waterfall rows (New MRR, Expansion MRR, Churned MRR) currently have their
actual values hardcoded or sourced from SQL queries you ran manually. Rework them
to pull from the `Actuals` tab using the current month's column. If the month
label in `Actuals` matches the label for this tab, the formula should find and
return the right value automatically.

**Verify:** After completing Steps 1–3, copy the tab, rename it `Apr 2026 A vs F`,
change the config cell to point at March, and enter a dummy set of April actuals
in the `Actuals` tab. Every figure on the April tab should update correctly
without any other changes. If anything still references `Mar 2026 A vs F` directly,
you have more to fix.

---

## Part 3 — Dynamic Retention Lookups

The Retention tab grows one column per month. Row 4 of that tab holds a date
for each column — the last day of the month that column represents.

Currently, GRR and NRR reference a hardcoded column letter (`AB6`, `AB7`).
You will replace this with a formula that works as follows:

1. It looks at the current month's close date
2. It searches row 4 of the Retention tab for that date
3. It retrieves the GRR (or NRR) value from the matching column

Excel has functions that search a range for a value and return either its
contents or its position, and functions that retrieve a value from a range
given a row and column position. You will need to combine at least two of
these to build the lookup.

The close date for the current month should be derived from a formula — not
hardcoded. If the tab is for March 2026, the formula should produce March 31, 2026.

**Requirement:** After building this, the GRR and NRR formulas must not contain
any column letter or column number that would need to change next month.
Test by verifying the formula returns the correct value for March, then confirm
it would return the correct value for February if you changed the month.

---

## Part 4 — WaterfallData

Currently, WaterfallData references each monthly tab directly:
`='Jan 2026 A vs F'!B4`, `='Feb 2026 A vs F'!B4`, and so on.

Rework it to read from `Actuals` instead. For each row in WaterfallData, the
formula should find the correct month column in `Actuals` and pull the corresponding
metric. When you add April actuals to the `Actuals` tab, WaterfallData should
pick up the April rows without any manual changes to the WaterfallData tab itself.

You'll need to decide how to structure this. One approach is to keep the same
row-per-movement format and write formulas that find the right month and metric
by looking them up in `Actuals`. Another is to change the structure so that
WaterfallData becomes a pure output of `Actuals` with no manual rows to add.

Think through which approach you'd rather maintain for the next nine months of
closes. Document your reasoning in `excel_techniques.md`.

---

## Part 5 — Commentary

This part is about reducing risk, not automating writing. The qualitative judgment
in your commentary — the "what does this mean" — must be written by a person.
But the numbers embedded in the text should never be typed by hand.

For each commentary section, restructure it so that:

- All figures (closing MRR, NRR %, EBITDA margin, LTV:CAC, CAC Payback) are
  generated by formula and displayed as formatted text
- The qualitative sentences you write sit in a separate cell or clearly separated
  section beneath the numbers

Excel has a function that converts a number into formatted text — look it up.
You'll use it to produce outputs like `$153,685` or `100.2%` from a formula cell,
so that if the underlying number changes, the displayed text updates automatically.

After implementing this, test it: change Expansion MRR in `Actuals` by $500.
Every number in the commentary should update. No text should require manual editing.

---

## Part 6 — Update your notes

After completing the redesign, update `excel_techniques.md` with:

- How the config-cell approach works and what its limitations are
- How the dynamic retention lookup works and why it's better than a column letter
- How the WaterfallData restructure works and what you chose and why
- How TEXT() concatenation works for formula-driven commentary

These notes are for the version of you who picks this workbook up in October
and needs to understand why it was built this way.

---

## What You Are Not Changing

- The monthly tab layout and structure — waterfall, P&L, KPIs, commentary —
  stays the same. This is a redesign of the plumbing, not the output.
- The Retention tab — do not modify it. Your formulas must work with it as-is.
- Historical data — January and February actuals are already in your monthly tabs.
  Backfill them into `Actuals` as part of this assignment.

---

## Submission

File: same workbook — `submissions/excel/excel_09_workbook_redesign.xlsx`

Save a copy of the workbook under the new filename. The restructured workbook
should contain all prior months' data and produce identical outputs to the
current workbook for January, February, and March.

Open a PR from `student/excel_09_workbook_redesign` → `main` with this description:

```
## 09 — Workbook Redesign

- Actuals input tab created; Jan/Feb/Mar data backfilled
- Monthly tab config-cell approach implemented; verified by copying to Apr test tab
- GRR/NRR: dynamic Retention lookup — no column letters
- WaterfallData: [describe your approach and why]
- Commentary: formula-driven numbers implemented
- excel_techniques.md updated

[self-check table]
```

---

## Self-Check

| Check | Expected |
|-------|---------|
| Changing one config cell re-points entire monthly tab at prior month | ✅ |
| April test tab produces correct outputs without additional formula edits | ✅ |
| GRR/NRR formulas contain no hardcoded column letters or numbers | ✅ |
| Changing any value in `Actuals` updates all downstream tabs | ✅ |
| Commentary numbers update when actuals change | ✅ |
| WaterfallData picks up a new month when `Actuals` is extended | ✅ |
| Jan, Feb, Mar outputs match the current workbook exactly | ✅ |
| `excel_techniques.md` updated | ✅ |

---

*Excel Assignment 09 — Workbook Redesign: Building for Scale*
*Idynamics Finance Analyst Training Program*
*May 2026*
