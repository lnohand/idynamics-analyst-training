# Feedback — Price-Volume Bridge Warm-Up

**PR #13 · branch `student/excel_price_volume_bridge`**

Good news first: the bridge itself is clean. Every row is built on real
formulas, the check column (`=E+F`) ties to Δ Revenue on all four rows, and
every number matches the self-check exactly — Northwind +800/+540, Cascade
−2,500/+4,750, Riverstone +3,200/−1,200, iDynamics +18,000/+11,200. The
dominant-driver column is formula-driven too. The mechanics are not the
problem. The interpretation is.

---

## Fix 1 — Cascade paragraph: the elasticity ratio is inverted

You wrote:

> "Based on the revenue delta, we can infer that a 1% price increase will
> create roughly a 2% decrease in customer base which is healthy."

Work the actual numbers. Cascade raised price ~10% (50 → 55) and lost ~5% of
units (1,000 → 950). That is roughly **0.5% of volume lost per 1% of price** —
demand is *inelastic*, which is exactly why the price increase grew revenue.
You've stated the ratio upside down (2% instead of ~0.5%), and an inverted
ratio tells the opposite story: 2%-lost-per-1%-of-price would mean demand is
*elastic* and the price hike would have destroyed revenue, not grown it.

Also drop "which is healthy" as the verdict. The whole point of the Cascade
case (see the call-out in the brief) is that it's *real pricing power but worth
watching* — push price far enough and the units you lose eventually flip the
math negative. That tension is the insight; don't resolve it away.

## Fix 2 — Cascade paragraph: an invented fact

> "Their strategy is to increase the price and lower the cost per unit."

There is no cost data anywhere in this exercise — only price and quantity. You
can't infer anything about their unit costs from a price-volume bridge. Cut
this sentence. Say what the data actually supports: they traded a small number
of price-sensitive customers for higher revenue per remaining customer.

The iDynamics paragraph (Paragraph 1) is fine — volume-led growth, correctly
called the healthier kind at this stage.

## Fix 3 — Update your notes

The brief asks for a short `my-notes/` entry capturing the bridge formula in
your own words plus the one insight that stuck (Cascade is the obvious
candidate). Your branch only changed the workbook — no notes were touched.
Add the entry.

## Fix 4 — File location

The brief specifies `submissions/excel/price_volume_bridge.xlsx`. Your file
landed at the repo root as `excel_price_volume_bridge.xlsx`. Move it to the
specified path so the submission folder stays organized.

---

## What's Good

| | |
|---|---|
| All four rows use real formulas | ✅ |
| Check column ties out (volume + price = Δ Revenue) | ✅ |
| All values match the self-check exactly | ✅ |
| Dominant-driver column formula-driven | ✅ |
| Paragraph 1 (iDynamics) — correct read | ✅ |

Four fixes, all in the Cascade paragraph plus notes/placement. The numbers are
right; tighten the story. Push to the same branch when done.
