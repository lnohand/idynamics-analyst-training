# FP Bridge 3 — NorthStar Consumer Goods: which channel did what
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Open the gross profit number up
>
> Which method you use to explain a variance depends on **what data you are given.** When all you
> have is a P&L, you use the revenue effect and the margin effect — that is what you did at Harlow
> and Westbrook. When you are also given **units and prices**, you use a different method: the
> **price-volume analysis.** This case gives you units and prices, so this is the one where you
> learn it.
>
> That is the one new technique here. The other new thing is the data: this time the actuals come
> as a raw ledger export, typed by people, and you tidy it before you use it. That is what the
> first twenty minutes of most real variance work looks like.
>
> And as promised, **one tab ships empty.** You lay out the P&L yourself.
>
> — David

**Time:** about 100 minutes · **File:** `assignments/excel/NorthStar_Q3_Case.xlsx` (run
`git pull origin main` on `main` first) → save a copy as **NorthStar_Michael.xlsx**

---

## The whole thing in four lines

| Step | Tab | What you produce | Roughly |
|---|---|---|---|
| 1 | `GL`, `Map` | a clean channel name on every ledger row | 20 min |
| 2 | `Summary` | Q3 budget vs actual by channel, down to EBITDA — your layout | 30 min |
| 3 | `Bridge` | gross profit change split into volume, price and unit cost; then the EBITDA walk | 30 min |
| 4 | `Commentary` | five lines for the CFO, plus what you'd do | 20 min |

Do them in order. Read each question twice before you answer it.

## What you're given

| Tab | What's on it |
|---|---|
| `Context` | Priya's email. **Read it before you touch the numbers.** |
| `GL` | 31 ledger rows for July–September: account, channel name as typed, amount, a note. You fill column H. |
| `Map` | The last analyst's list: name as typed → clean name. Three spare green rows. |
| `Budget` | Q3 budget by account and channel. Don't edit. |
| `Units` | Units, price and unit cost per channel, budget and actual, from the order system. Don't edit. |

Everything is in dollars. Every cell you fill is **green**. **Formulas, not typed numbers** — the
only things you type are words, and anything you add to `Map`.

**Tools you already know and will use:** `SUMIFS`, a lookup (`XLOOKUP` or `INDEX`/`MATCH`, your
choice), the F/U flag from Harlow and Westbrook, the residual check.

---

## Step 1 — `GL`: tidy the channel names

Column E is what somebody typed on the journal. The Summary needs one name per channel, so in
column H you look each typed name up in `Map` and bring back the clean one.

**Do it in two moves, and look at the result after the first.**

1. In `H5`, write a lookup that finds `E5` in the `Map` tab's first column and returns the second.
   Fill it down to the last row. Look at what came back. Some rows will show `#N/A`.
2. Click one of those rows' column E cell and press F2. Look at the very end of the text.

**The new function: `TRIM`.** `TRIM(text)` returns the text with the spaces at the start and end
removed.

| Formula | Result |
|---|---|
| `="DTC "="DTC"` | `FALSE` — to Excel these are two different names |
| `=TRIM("DTC ")="DTC"` | `TRUE` |

So look up `TRIM(E5)` instead of `E5`, and fill down again.

*Common mistake:* trimming by hand — retyping the cells in column E. It works today and breaks on
the next export. The ledger stays as it came; the formula does the tidying.

**Done when:** you have checked column H from top to bottom and you can say, for every row, which
channel or department it belongs to. If a row still has no answer, the row itself — its account,
its amount, its note — tells you where it belongs. Decide, fix it in the place where it should be
fixed, and tell me in your email what you did and why.

---

## Step 2 — `Summary`: the Q3 picture, your layout

The tab is empty. Build this on it.

**Columns:** line name · Q3 budget · Q3 actual · Var ($) · Var (%) · F / U

**Rows, in this order:**

- Revenue — one row per channel (DTC, Retail, Wholesale), then Total revenue
- COGS — one row per channel, then Total COGS
- Gross profit — one row per channel, then Total gross profit
- The four opex lines: Marketing, Sales, G&A, Logistics — then Total opex
- EBITDA
- Underneath: gross margin %, budget and actual

Budget comes from `Budget`, actual from `GL` using your column H. Derived rows (gross profit,
totals, EBITDA) come from your own rows above, not from the data tabs again.

**Variance is actual minus budget, on every row**, and the F/U flag carries the good-or-bad
meaning — same convention as before.

**Then one check, at the bottom of the tab:**

> Actual revenue + actual COGS + actual opex on your Summary, **minus** the total of every amount
> on the `GL` tab. It must be **0**.

Those are two different routes to the same number: one goes through your clean names, the other
just adds the column. If the answer isn't 0, a ledger row has not reached your P&L. Find it.

**Done when:** the check is 0 from a formula, and your EBITDA variance equals actual EBITDA minus
budget EBITDA.

---

## Step 3 — `Bridge`: volume, price, unit cost

### Which method? Look at the data first

| What you are given | Method | First effect — at **BUDGET** | The rest — on **ACTUAL** |
|---|---|---|---|
| A P&L only (no units, no prices) | Revenue effect and margin effect | Revenue effect = revenue difference × **budget** margin % | Margin effect = margin % difference × **actual** revenue |
| Units and prices as well | **Price-volume** | Volume effect = units difference × **budget** price | Price effect = price difference × **actual** units |

Two methods, one rule to remember them by: **the first effect is valued at budget, everything after
it is measured on actual.** Say it to yourself every time you write one of these formulas. Getting
budget and actual the wrong way round is the most common mistake in this whole topic, and the
numbers still look plausible when you do.

NorthStar gives you units and prices. So: price-volume.

### Learn it on something small first

A coffee cart budgeted **100 cups at $4.00, costing $1.50 each**. It actually sold **120 cups at
$3.50, costing $1.60 each**.

**This is the most common analysis in FP&A, and it is taught here from the start.** It is called
the **price-volume analysis** (or price-volume bridge), and "was that price or volume?" is the
first thing anyone asks about a revenue number.

**Start with revenue.** Revenue is price × units. So when revenue differs from budget, there are
only two possible reasons: we sold a different **number of units**, or we sold them at a different
**price**. Usually both. The analysis gives each reason its own dollar figure:

```
Volume effect = (actual units − budget units) × budget price
Price effect  = (actual price − budget price) × actual units
```

Read them as two questions:

- **Volume:** if the price had stayed at budget, what would the extra (or missing) units have been
  worth? That is why it uses the **budget** price.
- **Price:** on the units we really sold, how much more or less did we collect per unit? That is
  why it uses the **actual** units.

The cart's budget revenue is 100 × 4.00 = **400**, actual is 120 × 3.50 = **420**, so revenue rose
by **20**.

| Effect | In words | Arithmetic | $ |
|---|---|---|---|
| **Volume** | It sold 20 more cups, valued at the price the **budget** assumed. | (120 − 100) × 4.00 | **+80** |
| **Price** | It charged $0.50 less, on every cup it **actually** sold. | (3.50 − 4.00) × 120 | **(60)** |
| | | **Total** | **+20** |

80 − 60 = 20, the whole revenue change, nothing left over. Extra units at the **budget** price;
the price change on the **actual** units. Keep that pairing and the two always add up.

So the cart's story is not "revenue was up 20". It is "selling more was worth 80, and the price cut
gave 60 of it back."

**Now take it down to gross profit.** Revenue is not what Priya is asking about. Two changes:

- An extra cup doesn't earn its price, it earns its **profit**. So the volume effect values the
  extra units at the budget profit per unit: budget price − budget unit cost.
- Cost per cup can move too, so there is a third effect.

```
Volume effect    = (actual units − budget units) × (budget price − budget unit cost)
Price effect     = (actual price − budget price) × actual units          ← unchanged
Unit cost effect = (budget unit cost − actual unit cost) × actual units
```

Budget gross profit: 100 × (4.00 − 1.50) = **250**. Actual: 120 × (3.50 − 1.60) = **228**. Gross
profit fell by **22** even though it sold more cups and revenue went up.

| Effect | In words | Arithmetic | $ |
|---|---|---|---|
| **Volume** | 20 more cups, at the profit per cup the **budget** assumed. | (120 − 100) × (4.00 − 1.50) | **+50** |
| **Price** | $0.50 less, on every cup it **actually** sold. | (3.50 − 4.00) × 120 | **(60)** |
| **Unit cost** | Each cup cost $0.10 more, on every cup it **actually** sold. | (1.50 − 1.60) × 120 | **(12)** |
| | | **Total** | **(22)** |

50 − 60 − 12 = −22, the whole change, nothing left over.

**Budget or actual? Check each one before you move on.**

| Effect | The difference | Multiplied by |
|---|---|---|
| Volume | actual units − budget units | **BUDGET** price − **BUDGET** unit cost |
| Price | actual price − budget price | **ACTUAL** units |
| Unit cost | budget unit cost − actual unit cost | **ACTUAL** units |

The volume effect uses budget numbers because the price and cost changes are the next two rows'
job — use actual there and you count them twice. And the unit cost effect is written **budget minus
actual**, so that a cost going up comes out negative, like everything else that hurts profit.

**Where product mix goes.** With more than one product, total profit also moves when the *mix*
changes — more of what you sell is the high-profit product, or less. In this method each product's
extra units are valued at **that product's own** budget profit per unit, so the mix change is
**inside the volume effect**. There is no separate mix row and you don't need one here. If someone
asks "where is mix?", that is the answer.

*Common mistake:* valuing the extra units at the actual price or actual margin. It double-counts
the price cut, and the three effects stop adding up.

### Now NorthStar

On `Bridge`, fill the three effects for each channel from `Units`, then the Total column and the
Total row. Before each formula, say which it needs: **volume → budget price and budget unit cost;
price and unit cost → actual units.** The same reminder is printed above the table on the tab.

The sixth column pulls each channel's **gross profit variance from your Summary**, and the seventh
is the difference. **It must be 0 on every row.** This is a real check: the bridge comes from the
order system, your Summary comes from the ledger, and they have never met until this cell.

**Then answer the question under the table:**

> Which channels sold **5% or more** above their budgeted units?

**Then the EBITDA walk**, underneath. You have built this twice. Budget EBITDA, your three effects
(the totals), the four opex lines, actual EBITDA, and a residual that subtracts your total from the
Summary figure. In `What it means`, one plain sentence per row — two are filled in as examples.

**Done when:** every difference is 0, the residual is 0, and no green is left on `Bridge`.

---

## Step 4 — `Commentary`: five lines for Priya

One bullet per row. **Write all of them before you ask me for my version.**

| Row | What you get |
|---|---|
| 1, 2 | the comparison, in full |
| 3, 4 | **a hint only.** I tell you where to look. You work out what the comparison is. |
| 5 | **nothing.** You decide what's worth saying, write the comparison in the left cell, then the bullet. |

Row 5 is the one that matters. Go back to Priya's email before you write it.

**How to word one:**

- Lead with the number, not the adjective.
- Give the comparison, not just the value. A number on its own isn't a finding.
- Say what it means for next quarter.
- One idea per bullet.

Then the last row: **what you would do.** An action, not an observation. Name the thing, and say
what you'd stop, start or change.

**Done when:** five bullets and an action, every one with a number in it.

---

## Hand in

Save as **NorthStar_Michael.xlsx** and email it to me, attached, subject **NorthStar**, the
same way you sent Harlow and Westbrook.

In the email, five short things:

1. **Step 1** — what you found in column H that the lookup couldn't answer, what you did, and why.
2. **Your two checks** — the Summary check and the walk residual. Two numbers.
3. **Row 5** — what comparison you chose, and why that one.
4. **Why a bridge?** Priya already had the variance table. What does she know after your bridge
   that the table couldn't tell her?
5. **How it went.** How long, and where you got stuck.

Ask for my version of the commentary once yours is written, and I'll send it to compare against.
