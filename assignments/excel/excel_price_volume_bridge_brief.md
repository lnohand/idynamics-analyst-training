# Excel Warm-Up — The Price vs. Volume Bridge
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** When revenue moves, I need to know *why*
>
> Michael — you've done the budget-vs-actual work, so you can already
> tell me *that* revenue came in above or below plan. The next question
> a CFO always asks is *why*: did we grow because we sold more, or
> because we charged more? Those are completely different stories.
> Growth from selling more units is share gains; growth from price is
> pricing power. One is repeatable, one might not be — and they don't
> carry the same risk.
>
> This is a short warm-up, not a graded close. Work through the concept
> section first, then run the bridge on the three benchmark companies
> and on our own subscription book. Keep it small and clean — the point
> is the method, not the formatting.
>
> When you're done, go flip through the **Profitability & Margins**
> deck in the finance training tool. The "price versus volume" card
> will push you on how to say this in an interview.
>
> — David

---

## The Concept

### What problem does it solve?

Revenue is just **price × quantity**. So when revenue changes between
two periods, it can only be because price changed, quantity changed, or
both. The price-volume bridge splits a single revenue change into those
two drivers so you can explain it instead of just reporting it.

It matters because the two drivers tell very different stories:

- **Volume-led growth** — you sold more units (more customers, more
  seats). It's usually a sign of healthy demand and market-share gains,
  but each extra unit carries its variable cost.
- **Price-led growth** — you charged more per unit (higher ACV, a price
  increase). It flows almost entirely to margin and signals pricing
  power, but it can be a one-time lift and may eventually soften demand.

A company can even **grow revenue while losing volume** if a price
increase more than offsets the units lost — and you'd never see that
risk without breaking the change apart.

### The formula

For a single product, with prior period 0 and current period 1:

```
ΔRevenue   = Revenue₁ − Revenue₀ = (P₁ × Q₁) − (P₀ × Q₀)

Volume effect = (Q₁ − Q₀) × P₀      ← change in quantity, at the OLD price
Price effect  = (P₁ − P₀) × Q₁      ← change in price, at the NEW quantity

Volume effect + Price effect = ΔRevenue   (it ties out exactly)
```

The reason it ties out exactly: there's a small "combined" term —
the bit of the change that comes from price *and* quantity moving
together. Using the **new** quantity (Q₁) in the price effect tucks that
combined term into price, so the two buckets always add back to the
total. (Some teams put it in volume instead by using Q₀ for price and
Q₁ for volume — either is fine, as long as you're consistent. We'll use
the version above.)

### Worked example

A product sold **100 units at $10** last period, and **110 units at
$11** this period.

| | Quantity | Price | Revenue |
|---|---|---|---|
| Prior (0) | 100 | $10 | $1,000 |
| Current (1) | 110 | $11 | $1,210 |

Revenue rose **$210 (+21%)**. Break it apart:

- **Volume effect** = (110 − 100) × $10 = **+$100**
- **Price effect** = ($11 − $10) × 110 = **+$110**
- Check: $100 + $110 = **$210** ✓

So of the $210 increase, $100 came from selling more units and $110 from
charging more — a roughly balanced story you could now defend in a room.

### In our world

For a subscription business, "quantity" is the **number of customers (or
subscriptions)** and "price" is **ARPA / ACV** — average revenue per
account. So the same bridge tells you how much of an ARR change came from
*adding logos* versus *each logo paying more*.

---

## Part 1 — Benchmark Scenarios

Build a small table in a new Excel tab named `Price-Volume Bridge`. For
each company below, compute Δ Revenue, the volume effect, and the price
effect using the formulas above. Use real formulas (not typed numbers),
and add a check column that confirms volume effect + price effect = Δ
Revenue.

**Company A — Northwind Retail**

| | Quantity | Price |
|---|---|---|
| Prior | 500 | $20 |
| Current | 540 | $21 |

**Company B — Cascade Tools**

| | Quantity | Price |
|---|---|---|
| Prior | 1,000 | $50 |
| Current | 950 | $55 |

**Company C — Riverstone Supply**

| | Quantity | Price |
|---|---|---|
| Prior | 2,000 | $8.00 |
| Current | 2,400 | $7.50 |

For each: compute the **volume effect**, the **price effect**, and which
of the two is the **dominant driver**. Notice that B and C both grow
revenue — but for opposite reasons.

---

## Part 2 — Idynamics Subscriptions

Apply the same bridge to our own book. Treat **customers** as quantity
and **ACV** as price.

| | Customers | ACV |
|---|---|---|
| Q1 2025 | 50 | $3,000 |
| Q1 2026 | 56 | $3,200 |

Add Idynamics as a fourth row in the same table, same format. Compute the
volume effect, the price effect, and the dominant driver.

---

## Part 3 — Written Interpretation

Below the table, write two short paragraphs directly in the Excel tab.

**Paragraph 1 — Idynamics.** Of our Q1-over-Q1 revenue change, how much
came from adding customers versus raising ACV? What does that mix signal
about how the business is growing, and is it the healthier kind of growth
for us at this stage?

**Paragraph 2 — Cascade Tools.** Cascade grew revenue even though it sold
*fewer* units. Explain how, what it says about their strategy, and the
one thing you'd watch going forward.

Each paragraph: 3–5 sentences. Answer the question directly, no filler.

---

## Self-Check Values

Your bridge should tie to these. The volume and price effects must sum to
Δ Revenue on every row.

| Scenario | Δ Revenue | Volume effect | Price effect | Dominant driver |
|---|---|---|---|---|
| Northwind Retail | +$1,340 | +$800 | +$540 | Volume |
| Cascade Tools | +$2,250 | −$2,500 | +$4,750 | Price (volume fell) |
| Riverstone Supply | +$2,000 | +$3,200 | −$1,200 | Volume (price fell) |
| Idynamics | +$29,200 | +$18,000 | +$11,200 | Volume (slightly ahead of price) |

> **Cascade Tools is the one to study.** Revenue went up $2,250, but the
> volume effect is **negative** — they lost 50 units. The whole gain came
> from a price increase large enough to more than offset the units lost.
> That's real pricing power, but it's worth watching: keep pushing price
> and you can eventually lose enough customers that the math flips.

---

## Understanding Checks

Post your answers to these in your check-in thread before you consider the
warm-up done (a sentence or two each):

1. Cascade Tools grew revenue while selling fewer units. In your own
   words, how is that possible, and is it a good or a risky kind of
   growth?
2. Riverstone's price effect is negative but revenue still rose. What
   does that say about their pricing strategy, and what's the trade-off?
3. If you'd put the combined term in *volume* instead of price (using the
   old quantity for the price effect), would the two effects still add
   back to Δ Revenue? Which bucket's number would change?
4. Idynamics grew ARR on a roughly 60/40 split of volume vs. price. For a
   SaaS business, is volume-led or price-led ARR growth generally
   healthier — and why?

---

## Git Workflow

Branch from main, work on this branch, open a PR when done:

```
git checkout main
git pull origin main
git checkout -b student/excel_price_volume_bridge
```

When ready to submit:
```
git add submissions/excel/price_volume_bridge.xlsx
git commit -m "Add: price-volume bridge warm-up"
git push origin student/excel_price_volume_bridge
```

Open a PR from `student/excel_price_volume_bridge` → `main`.

---

## Keep Your Notes Current

Before submitting, add a short entry to `my-notes/` capturing the
price-volume bridge formula in your own words and the one insight that
stuck with you (the Cascade case is a good candidate).

---

## Submission

File: `submissions/excel/price_volume_bridge.xlsx`

Open a PR with this description:

```
## Price-volume bridge warm-up
- Price-Volume Bridge tab: 3 benchmarks + Idynamics, effects tie to Δ Revenue
- Part 3 interpretation paragraphs written in the tab
- Understanding-check answers posted in my check-in thread
- my-notes/ updated

## Self-Check
Northwind volume / price effect: +$800 / +$540
Cascade volume / price effect: −$2,500 / +$4,750
Riverstone volume / price effect: +$3,200 / −$1,200
Idynamics volume / price effect: +$18,000 / +$11,200
```
