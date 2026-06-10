# Excel Assignment — Rule of 40
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Board prep — they're going to ask about Rule of 40
>
> Michael — we have a board check-in coming up and the deck includes
> our Q1 summary. One of our investors is going to ask about our
> Rule of 40 score. I've heard this question at every board meeting
> since Series A.
>
> You've now built the full picture of this business: growth, retention,
> unit economics, and the monthly close. Rule of 40 is how you compress
> all of that into a single number investors use to compare companies.
> You need to know it cold.
>
> Before you look at our numbers, work through the concept section
> below. Then calculate it for the benchmark companies I've included,
> and finally apply it to Idynamics using our Q1 actuals.
>
> After this assignment, go work through the Rule of 40 flashcard deck
> in the finance training tool. The cards will push you on the harder
> interview questions.
>
> — David

---

## The Concept

### What problem does it solve?

Growth and profitability pull in opposite directions for SaaS companies.
A company that grows 80% year-over-year is probably burning heavily —
high S&M spend, aggressive hiring, negative margins. A company that
shows 30% EBITDA margins is probably growing slowly, because it isn't
reinvesting in customer acquisition.

Investors need a way to compare a fast-burning grower against a
capital-efficient slow grower. The Rule of 40 puts both on the same
scale.

### The formula

**Rule of 40 score = ARR growth rate (%) + profit margin (%)**

If the score is 40 or above, the company passes. Below 40, the growth
and profitability combination is considered insufficient.

A company growing at 60% with negative 20% EBITDA margin scores 40 —
right at the line. A company growing at 20% with 25% EBITDA margin
scores 45 — it passes even though growth is slow. The framework lets
investors trade one for the other.

### Which metrics to use

**Growth component:** Year-over-year ARR growth rate is the standard.
Some practitioners use revenue growth; others use QoQ growth annualized.
Always clarify which is being used when comparing companies — the
choice moves the number.

**Profitability component:** Three options are used in practice:

| Metric | When used | Limitation |
|--------|-----------|------------|
| EBITDA margin | Most common, especially for comparisons | Can be inflated by high stock-based compensation |
| FCF margin | Preferred at scale ($100M+ ARR) | Sensitive to working capital timing |
| Operating income margin | Used in some public company analysis | Least common for private SaaS |

For the calculations in this assignment, you'll work with both EBITDA
and FCF margin so you see how the choice affects the result.

### Who popularized it and when

The Rule of 40 was popularized by Brad Feld (Foundry Group) and has
been widely cited since around 2015. It became the dominant benchmark
for SaaS health because it's simple, comparable across companies, and
captures the core tension of the business model in a single number.

### When does it apply?

The Rule of 40 is most meaningful above $50M ARR. Below that
threshold — especially in the $0–$10M range — companies are still
finding product-market fit, building GTM, and investing heavily. The
score is often very high (because early growth rates are extreme) or
very low (because burn is deep and growth is still fitful). Either
way, it's not the primary lens investors use at this stage.

Early-stage investors focus on growth rate, NRR, and unit economics
in isolation. Rule of 40 becomes a primary benchmark in growth-stage
and late-stage fundraising conversations.

---

## Part 1 — Benchmark Company Calculations

David has pulled Q1 2026 data for three SaaS companies that are public
comparables in our investor deck. Calculate the Rule of 40 score for
each and determine whether it passes.

Build a small table in a new Excel tab named `Rule of 40`. Use clean
formatting — section headers, values right-aligned, pass/fail clearly
marked with a formula (not typed text).

**Company A — Accel Software** ($75M ARR, Series D)

| Metric | Value |
|--------|-------|
| Q1 2025 ending ARR | $53,000,000 |
| Q1 2026 ending ARR | $75,000,000 |
| Q1 2026 EBITDA margin | -3% |
| Q1 2026 FCF margin | -8% |

**Company B — Meridian Cloud** ($220M ARR)

| Metric | Value |
|--------|-------|
| Q1 2025 ending ARR | $176,000,000 |
| Q1 2026 ending ARR | $220,000,000 |
| Q1 2026 EBITDA margin | +18% |
| Q1 2026 FCF margin | +12% |

**Company C — Flux Analytics** ($140M ARR)

| Metric | Value |
|--------|-------|
| Q1 2025 ending ARR | $88,000,000 |
| Q1 2026 ending ARR | $140,000,000 |
| Q1 2026 EBITDA margin | -8% |
| Q1 2026 FCF margin | -14% |

For each company, calculate:
1. YoY ARR growth rate
2. Rule of 40 score using EBITDA margin
3. Rule of 40 score using FCF margin
4. Pass / Fail (40 or above = pass)

Note where the EBITDA and FCF versions give different results and why.

---

## Part 2 — Idynamics Q1 2026

David has pulled the Q1 2026 summary data from the board deck. Apply
the same calculation to Idynamics.

**Idynamics Q1 2026 snapshot**

| Metric | Value |
|--------|-------|
| Q1 2025 ending ARR | $840,000 |
| Q1 2026 ending ARR | $1,730,000 |
| Q1 2026 EBITDA margin | 18% |
| Q1 2026 FCF margin | 12% |

Calculate the same four metrics you calculated for the benchmark
companies. Add Idynamics as a fourth row in the same table, with a
consistent format.

---

## Part 3 — Written Interpretation

Below the table, write two short paragraphs directly in the Excel tab.

**Paragraph 1 — What does the score mean?**

Idynamics' Rule of 40 score is well above 40. Does that mean the
business is healthy? Explain what the score actually signals and what
its limitation is given our current ARR. Which benchmark company would
be a more meaningful Rule of 40 comparison for a board conversation,
and why?

**Paragraph 2 — The growth component**

At our current stage, the growth rate is the more important of the two
components. Why? What would need to change for the Rule of 40 score to
become the primary benchmark — rather than a secondary one — in a
future fundraising conversation?

Each paragraph: 3–5 sentences. No filler. Answer the question directly.

---

## Self-Check Values

| Company | ARR Growth | R40 (EBITDA) | R40 (FCF) | Pass (EBITDA) |
|---------|-----------|--------------|-----------|---------------|
| Accel Software | 41.5% | 38.5 | 33.5 | Fail |
| Meridian Cloud | 25.0% | 43.0 | 37.0 | Pass |
| Flux Analytics | 59.1% | 51.1 | 45.1 | Pass |
| Idynamics | 106.0% | 124.0 | 118.0 | Pass (early-stage caveat) |

> **Accel Software note:** A score of 38.5 on an EBITDA basis is a miss.
> The FCF score of 33.5 is worse — the gap between EBITDA and FCF tells
> you there's cash pressure beyond what the P&L shows. A company at
> $75M ARR is expected to be at or approaching 40. This one needs either
> a growth acceleration or a tighter cost structure before the next round.

> **Idynamics note:** A score of 124 looks exceptional but is misleading
> as a standalone benchmark. At $1.73M ARR, we're in the range where
> early growth rates are naturally extreme. The number to watch is
> whether we maintain EBITDA margin as we scale OpEx in 2026. If growth
> slows to 60% next year and margin holds at 18%, the score is 78 —
> still excellent. If margins compress to -5% as we invest in GTM, the
> score is 55 — healthy but the trend matters.

---

## Submission

Branch: `student/excel-rule-of-40`

Tab name in workbook: `Rule of 40`
Add the tab to your existing workbook (`06_actual_vs_forecast.xlsx` or
the redesigned version from Excel 09).

```
submissions/excel/rule_of_40.xlsx
```

PR description:

```
## What this does
Rule of 40 tab: YoY ARR growth, EBITDA and FCF Rule of 40 scores for
three benchmark companies and Idynamics Q1 2026. Written interpretation
below the table.

## Self-check
Accel Software R40 (EBITDA): 38.5 — Fail ✅
Meridian Cloud R40 (EBITDA): 43.0 — Pass ✅
Flux Analytics R40 (EBITDA): 51.1 — Pass ✅
Idynamics R40 (EBITDA): 124.0 — Pass (early-stage caveat noted) ✅

## Interpretation summary
[One sentence: what does Idynamics' score actually tell us at this stage?]
```

---

## After Submission

Open the finance training tool and work through the **Rule of 40**
flashcard deck (13 cards). The cards cover the harder interview questions:
metric choice, blind spots, valuation correlation, NRR's effect on the
score, and how to use it in a budget conversation. The calculation is
the foundation — the flashcards build the fluency you need to discuss
it in a room.

---

*Idynamics Finance Analyst Training Program*
*Rule of 40 — Concept + Application*
*June 2026*
