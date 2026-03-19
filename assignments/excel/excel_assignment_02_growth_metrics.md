# Excel Assignment 02 — Growth Metrics
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Growth tab — need this before the board call
>
> Michael — the MRR engine looks good. Now I need you to build the
> growth analysis tab in the workbook.
>
> The board doesn't look at raw MRR. They look at growth rates. When
> Daniel says "we grew 5% last month" — where does that number come
> from? When a VC asks "what's your CMGR?" — what do they mean, and
> why don't they just look at month-over-month?
>
> Build the tab. I want to see MRR, ARR, growth rates, and the Quick
> Ratio. And I need you to write a short paragraph at the bottom
> explaining what the numbers say about where the business is headed.
>
> The numbers should speak. If you can't explain what they mean for
> the business, the tab isn't done.
>
> — David

---

## What You're Building

A **Growth** tab in your MRR workbook that transforms the waterfall
numbers into the metrics a board member or investor actually reads.
By the end you will have:

- MRR and ARR for every month (26 months)
- Month-over-month growth rate
- Year-over-year growth rate (where applicable)
- CMGR — compound monthly growth rate (6-month and 12-month)
- Quick Ratio — the growth efficiency metric
- Growth composition — how much comes from new vs. expansion
- A written interpretation of what the numbers say

Everything on this tab references the Waterfall tab. No new data
imports. No hardcoded numbers. Every cell is a formula.

---

## Before You Start — Why These Metrics Exist

**MoM growth is noisy.** One big deal lands in March, nothing in
April — it looks like growth collapsed. In reality, nothing changed.
Monthly numbers are volatile and misleading in isolation.

**CMGR smooths the noise.** It asks: "What constant monthly growth
rate would get us from Point A to Point B over N months?" An investor
doesn't care that March was 17% and April was 5%. They care that the
6-month compounding rate is 8.9%.

**YoY removes seasonality.** Comparing this January to last January
shows the trend without seasonal distortion. It's the simplest way
to show "are we bigger than we were a year ago, and by how much?"

**Quick Ratio tells you if growth is healthy.** A company adding
$10,000 in new MRR sounds great — until you learn it lost $12,000
to churn. Quick Ratio = gains / losses. Below 1 means you're
shrinking even though the sales team is closing deals.

**Growth composition tells you where growth comes from.** A business
growing entirely from new customers is on a treadmill — it must
keep acquiring. A business growing from expansion has strong
product-market fit. The mix shifts as a company matures.

---

## Part 1 — Setup

### Step 1: Create the Growth tab

Add a new tab to your workbook called **Growth**. Position it after
the Waterfall tab.

### Step 2: Build the layout

The layout follows a standard SaaS reporting format: months run
across the top as columns, metrics run down as rows. Each section
has a header row.

Set up the structure:

**Row 1:** Title — "Growth Analysis — January 2024 to February 2026"

**Row 3:** Section header — "1. MRR & ARR" (bold, colored background)

**Rows 4–8:**

| Row | Label | What goes here |
|---|---|---|
| 4 | Month | 2024-01 through 2026-02 (26 columns) |
| 5 | **Closing MRR** | Link to Waterfall closing_mrr for each month |
| 6 | **ARR** | = Closing MRR × 12 |
| 7 | **Net New MRR** | Link to Waterfall net_change for each month |
| 8 | **Cumulative Net New MRR** | Running sum of Net New MRR |

> **Why ARR?** Nobody says "our MRR is $152K." They say "we're at
> $1.8M ARR." ARR is MRR × 12. It's the same number expressed at
> annual scale — which is how businesses, investors, and boards talk.

**Row 10:** Section header — "2. Growth Rates" (bold, colored background)

**Rows 11–16:**

| Row | Label | Formula |
|---|---|---|
| 11 | **MoM Growth %** | = Net New MRR / Prior month Closing MRR |
| 12 | **YoY Growth %** | = (This month's MRR − Same month last year's MRR) / Same month last year's MRR |
| 13 | *(blank spacer)* | |
| 14 | **CMGR (6-month)** | = (Current MRR / MRR 6 months ago) ^ (1/6) − 1 |
| 15 | **CMGR (12-month)** | = (Current MRR / MRR 12 months ago) ^ (1/12) − 1 |
| 16 | **Trailing 3-month avg MoM** | = AVERAGE of the last 3 MoM Growth % values |

> **MoM Growth formula note:** The first month (2024-01) has no prior
> month, so MoM is blank. Use IFERROR to handle it.
>
> **YoY formula note:** YoY only starts at month 13 (2025-01) because
> you need 12 months of history. Leave earlier months blank.
>
> **CMGR formula note:** CMGR (6-month) starts at month 7 (2024-07).
> CMGR (12-month) starts at month 13 (2025-01). The formula is:
>
> ```
> = (current_mrr / mrr_N_months_ago) ^ (1/N) − 1
> ```
>
> In Excel: `=(B5/B_minus_6)^(1/6)-1` where B_minus_6 is the cell
> 6 columns to the left. Make sure you reference the right cell.

**Row 18:** Section header — "3. Growth Quality" (bold, colored background)

**Rows 19–24:**

| Row | Label | Formula |
|---|---|---|
| 19 | Gains (New + Expansion) | = New MRR + Expansion MRR from Waterfall |
| 20 | Losses (Contraction + Churned) | = ABS(Contraction) + ABS(Churned) from Waterfall |
| 21 | **Quick Ratio** | = Gains / Losses |
| 22 | *(blank spacer)* | |
| 23 | **New as % of gains** | = New MRR / Gains |
| 24 | **Expansion as % of gains** | = Expansion MRR / Gains |

> **Quick Ratio formula note:** In months with zero losses, the
> result would be a division-by-zero error. Wrap in IFERROR and
> display "∞" (or leave blank — your choice). Months with losses = 0
> and gains > 0 are infinitely efficient — all growth, no leakage.
>
> **Composition formula note:** In months with zero gains (no new
> and no expansion), both percentages are undefined. Use IFERROR.
> These months are significant — they mean the business added nothing.

---

## Part 2 — Build It

### Step 3: Fill in every formula

Work left to right, one section at a time. Start with Section 1
(MRR & ARR), confirm the numbers, then move to Section 2, then
Section 3.

**Self-checks after Section 1:**

| Check | Expected |
|---|---|
| Closing MRR, 2024-01 | $5,800.00 |
| Closing MRR, 2026-02 | $152,034.50 |
| ARR, 2025-06 | $1,825,374.00 |
| ARR, 2026-02 | $1,824,414.00 |
| Net New MRR, 2025-08 | −$2,430.00 |
| Cumulative Net New MRR, 2026-02 | $152,034.50 |

> Cumulative net new MRR at the end should equal closing MRR —
> because the business started at $0.

**Self-checks after Section 2:**

| Check | Expected |
|---|---|
| MoM Growth, 2024-02 | 148.5% |
| MoM Growth, 2025-07 | −0.7% |
| MoM Growth, 2026-02 | −0.4% |
| YoY Growth, 2025-06 | 322.7% |
| YoY Growth, 2026-02 | 40.6% |
| CMGR 6-month, 2024-07 | 40.9% |
| CMGR 6-month, 2025-06 | 8.9% |
| CMGR 6-month, 2025-12 | −0.1% |
| CMGR 6-month, 2026-02 | 0.4% |
| CMGR 12-month, 2025-01 | 26.9% |
| CMGR 12-month, 2025-12 | 4.3% |
| CMGR 12-month, 2026-02 | 2.9% |

> **Spot-check the CMGR by hand.** Pick 2025-06 CMGR (6-month).
> MRR 6 months ago (2024-12) was $91,123.50. MRR now is $152,114.50.
> (152,114.50 / 91,123.50) ^ (1/6) − 1 = 8.9%. If you don't get
> this, your cell references are off by a column.

**Self-checks after Section 3:**

| Check | Expected |
|---|---|
| Quick Ratio, 2024-08 | 3.6 |
| Quick Ratio, 2025-05 | 5.2 |
| Quick Ratio, 2025-07 | 0.4 |
| Quick Ratio, 2025-08 | 0.5 |
| Quick Ratio, 2025-12 | 0.3 |
| New as % of gains, 2025-06 | 84% |
| Expansion as % of gains, 2025-08 | 100% |

---

## Part 3 — Read the Numbers

This is the most important part of the assignment. The tab isn't
done until you can explain what it says.

### Step 4: Add a summary section below the data

Starting around Row 27, add a section header:
"4. What the Numbers Say" (bold, colored background)

Write **three short paragraphs** (3–5 sentences each) in merged cells
below the header. Use your own words. Reference specific numbers from
the tab. The paragraphs should answer:

**Paragraph 1 — The growth story.**
How did MRR grow from $0 to $152K? Was growth steady or lumpy? When
was the fastest growth? When did it slow down? Use the CMGR numbers,
not MoM — CMGR tells the real story.

**Paragraph 2 — The H2 2025 problem.**
Something changed in July 2025. What do the numbers show? Look at
net new MRR, Quick Ratio, and growth composition. What happened to
new customer acquisition? How did expansion and churn interact during
this period?

**Paragraph 3 — Where the business is headed.**
Based on the trailing CMGR and current Quick Ratio, is the business
growing, flat, or shrinking? What would you tell the board? What's
the one metric they should worry about most?

> **Why this matters:** A junior analyst who builds a perfect tab but
> can't explain what it means has done half the job. David doesn't
> read 26 columns of numbers. He reads your paragraph and then asks
> questions about specific months. The paragraph is the deliverable.
> The numbers are the evidence.

---

## Part 4 — Format

### Step 5: Apply professional formatting

- **Section headers:** Bold white text on dark blue background
  (match the template style from the other tabs)
- **Growth rates:** Percentage format, 1 decimal place (e.g., 8.9%)
- **Dollar values:** Accounting format, no decimals for ARR
  (it's a big number — $1,825,374, not $1,825,374.00)
- **MRR and Net New MRR:** Accounting format, 2 decimal places
- **Quick Ratio:** Number format, 1 decimal place
- **Negative values:** Red with parentheses — use number format,
  not manual coloring
- **CMGR cells:** Light yellow background to highlight them as
  the key investor metrics (matches the template convention)
- **Blank/error cells:** Display as blank (IFERROR), never show
  `#DIV/0!` or `#VALUE!`
- **Freeze:** Freeze column A and row 4 so labels and month headers
  stay visible when scrolling

### Step 6: Conditional formatting

Add conditional formatting to the Quick Ratio row:

| Value | Fill color | Meaning |
|---|---|---|
| ≥ 4.0 | Green | Excellent |
| 2.0 – 3.99 | Light green | Healthy |
| 1.0 – 1.99 | Yellow | Fragile |
| < 1.0 | Red | Shrinking — losses exceed gains |

This makes the H2 2025 problem jump off the screen.

---

## Benchmarks (add to your Ref tab)

Add these benchmarks to the Ref tab so they're documented in the
workbook. You'll reference them in your written summary.

| Metric | Threshold | Label |
|---|---|---|
| MoM Growth | > 10% | Exceptional (early stage) |
| MoM Growth | 5 – 10% | Strong |
| MoM Growth | 2 – 5% | Good (post-PMF) |
| MoM Growth | 0 – 2% | Stalling |
| MoM Growth | < 0% | Declining |
| CMGR 6-month | > 15% | Exceptional |
| CMGR 6-month | 10 – 15% | Strong |
| CMGR 6-month | 5 – 10% | Good |
| CMGR 6-month | 2 – 5% | Moderate |
| CMGR 6-month | < 2% | Stalling |
| Quick Ratio | > 4.0 | Excellent |
| Quick Ratio | 2.0 – 4.0 | Healthy |
| Quick Ratio | 1.0 – 2.0 | Fragile |
| Quick Ratio | < 1.0 | Shrinking |

---

## Final Self-Check Checklist

Walk through these before submitting:

- [ ] Section 1: Closing MRR row matches Waterfall exactly (all 26 months)
- [ ] Section 1: ARR for 2026-02 = $1,824,414.00
- [ ] Section 1: Cumulative Net New MRR at end = $152,034.50
- [ ] Section 2: MoM 2024-01 is blank (not an error, not 0%)
- [ ] Section 2: YoY starts at 2025-01, earlier months blank
- [ ] Section 2: CMGR 6-month for 2025-06 = 8.9%
- [ ] Section 2: CMGR 12-month for 2026-02 = 2.9%
- [ ] Section 3: Quick Ratio for 2025-07 = 0.4
- [ ] Section 3: No #DIV/0! errors anywhere on the tab
- [ ] Section 3: Conditional formatting shows red in Jul–Aug 2025,
  Nov–Dec 2025, Feb 2026
- [ ] Section 4: Three paragraphs written, referencing specific numbers
- [ ] Formatting: section headers styled, CMGR rows highlighted,
  negatives in red parentheses
- [ ] Ref tab: benchmarks added

---

## Submission

Save the workbook. Commit to your repo:

```
submissions/excel/02_growth_metrics.xlsx
```

Branch: `student/excel-02-growth-metrics`

PR description:

```
## What this does
Growth analysis tab: MRR/ARR time series, MoM/YoY/CMGR growth rates,
Quick Ratio, growth composition, and written business interpretation.

## Self-check
ARR (Feb 2026): $1,824,414 ✅
CMGR 6-month (Jun 2025): 8.9% ✅
CMGR 12-month (Feb 2026): 2.9% ✅
Quick Ratio (Jul 2025): 0.4 ✅
No formula errors ✅

## Interpretation
[One sentence summary of your paragraph 3 — what you'd tell the board]

## Questions for reviewer
[Anything you're unsure about]
```

---

## What Comes Next

The Growth tab shows the trajectory. The next tabs show *why* the
trajectory looks the way it does:

- **Retention** — GRR and NRR explain the churn that dragged growth
  down in H2 2025
- **Unit Economics** — ARPA, gross margin, and LTV show whether each
  customer is profitable
- **Dashboard** — pulls the key numbers from Growth, Retention, and
  Unit Economics into a single board-ready view

The Growth tab is the headline. Everything else is the footnotes.

---

*Idynamics Finance Analyst Training Program*
*Excel Assignment 02 — Growth Metrics*
*March 2026*
