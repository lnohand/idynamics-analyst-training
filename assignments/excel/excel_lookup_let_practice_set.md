# Practice Set — XLOOKUP · INDEX/MATCH · LET

**For:** Michael
**Why:** reps to cement the three lookup tools. **Build these in Excel** — set up the two
tables below in a sheet, then write each formula in a cell and confirm the result. Note the
formula you used alongside each answer.
**Self-check answers are at the bottom** — try each before you peek.

Work off these two small tables.

**Table 1 — Plans** (`A1:D5`)
```
        A            B            C          D
1     Plan       Price/seat     Seats      MRR
2     Starter        20          100        2000
3     Growth         45          220        9900
4     Scale          90          140       12600
5     Enterprise    150           80       12000
```

**Table 2 — Monthly KPIs** (`A1:F4`)  — months run left→right
```
        A               B         C         D         E         F
1     Metric          Jan       Feb       Mar       Apr       May
2     MRR           144780    150306    153686    156831    160308
3     NRR            100.0%     99.6%    100.3%     99.6%     99.7%
4     Active Cust.      39        41        42        44        46
```

---

## A — XLOOKUP

**A1.** Return **Scale's** Price/seat from Table 1.

**A2.** Which **plan** charges **45** per seat? (You're looking *up* by price and returning
the name to its **left** — the thing VLOOKUP can't do.)

**A3.** Look up plan **"Team"** (it doesn't exist) and return **"no plan"** instead of an
error.

**A4.** From Table 2, return **MRR** for whatever month is typed in cell **H1**. Write it so
that changing `H1` from `"Apr"` to `"May"` updates the answer with no edit to the formula.
Give both results.

## B — INDEX/MATCH

**B1.** Same as A1 (Scale's Price/seat), but with **INDEX/MATCH** instead of XLOOKUP.

**B2 — two-way lookup, built up in three steps** (goal: **NRR in Apr** from Table 2):

- **B2a — find the row.** Use `MATCH` to find which **row** `"NRR"` is on within the metric
  labels `A2:A4`. What number does it return?
- **B2b — find the column.** Use `MATCH` to find which **column** `"Apr"` is on within the
  month header `B1:F1`. What number?
- **B2c — combine.** Feed both into one `INDEX` over the data block `B2:F4`:
  `INDEX(B2:F4, ⟨your B2a⟩, ⟨your B2b⟩)`. What value comes back?

*(This is the same `MATCH` you already use to pick a month — now on **both** axes. The only
new part: `INDEX` takes a second argument, `INDEX(block, row, column)`.)*

**B3.** Find the **plan** whose Price/seat is **90**, using INDEX/MATCH (a left-lookup).

## C — LET

**C1.** Here's a formula that discounts a plan's MRR by 10% if it's over $10,000 — notice
`INDEX(D2:D5, MATCH("Scale",A2:A5,0))` is written **three times**:
```
=IF(INDEX(D2:D5,MATCH("Scale",A2:A5,0))>10000,
    INDEX(D2:D5,MATCH("Scale",A2:A5,0))*0.9,
    INDEX(D2:D5,MATCH("Scale",A2:A5,0)))
```
Rewrite it with **LET** so the lookup runs once. Give the number it returns.

**C2.** Write **one LET** that computes **Growth's MRR** as Price/seat × Seats — find
Growth's row once, pull both values, multiply. Give the number (it should match `D3`).

---

## Self-Check (numbers only — the formulas are the point)

| | Answer |
|---|---|
| A1 | 90 |
| A2 | Growth |
| A3 | no plan |
| A4 | Apr → 156,831 · May → 160,308 |
| B1 | 90 |
| B2a | 2 (NRR is the 2nd metric) |
| B2b | 4 (Apr is the 4th month) |
| B2c | 99.6% |
| B3 | Scale |
| C1 | 11,340 (12,600 × 0.9) |
| C2 | 9,900 (45 × 220) |

*If a number's off, it's almost always the range or the match column — check those first.*
