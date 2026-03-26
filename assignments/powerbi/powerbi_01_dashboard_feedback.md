# Power BI 01 — SaaS Executive Dashboard: Feedback

### Reviewer Notes — March 2026

---

## Overall

Good first Power BI file, Michael. The structure is solid — you got the right tables imported, built a _Measures table, created the correct DAX measures, and laid out a single-page dashboard with all the major visual types. The data model is clean. Two issues need fixing before this ships, and there are several polish items worth addressing.

---

## What's Working

**Data model — correct.** Four tables: Engine, Raw Snapshot, Waterfall, _Measures. Engine relates to Raw Snapshot on subscription_id. Waterfall stands alone. That's exactly the model the assignment describes.

**KPI cards — correct measures, correct layout.** Current MRR, Active Subscriptions, Avg MRR per Sub, Latest Net Change. All four pull from _Measures. All have #F5F5F5 backgrounds. Category labels are set to 9pt. Currency formatting is applied.

**MRR trend line — correct field and color.** Waterfall[Closing] on Y-axis, #1565C0 blue, gridlines removed. That's right.

**Movements column chart — correct fields.** New, Expansion, Contraction, Churned from the Waterfall table. Titled "Monthly MRR Movements."

**Slicers — both present.** Plan slicer and Region slicer, both sourced from Raw Snapshot. Positioned in the top-right corner alongside the cards.

**Header textbox — correct content.** "iDynamics — SaaS Executive Dashboard" and "Data through February 2026" in #333333.

---

## Must Fix (2 issues)

### 1. Donut chart uses COUNT instead of SUM

**This is the biggest problem in the file.** The "Current MRR by Plan" donut chart is using `Count of mrr` (CountNonNull) instead of `Sum of mrr`. That means it's showing how many subscriptions each plan has — not how much MRR each plan generates. Those are very different stories.

For example, if Analytics Pro has 3 subs at $5,000 each and Starter has 15 subs at $100 each, COUNT shows Starter as the biggest slice. SUM shows Analytics Pro at $15K vs Starter at $1.5K. The whole point of this chart is MRR distribution by plan, not subscription count.

**Fix:** Click the donut chart → in the Values well, click the dropdown arrow on the mrr field → change from "Count" to "Sum." Verify the largest slice is Platform Suite and the total across all slices equals $144,185.50.

### 2. Date Hierarchy on trend line and movements chart

Both the line chart and the column chart are using Power BI's automatic Date Hierarchy with Year as the active drill level. That means the trend line is probably showing 3 data points (2024, 2025, 2026) instead of the 26 monthly data points the assignment requires. Same problem on the movements chart — it's aggregating New/Expansion/Contraction/Churned by year instead of showing each month individually.

This is the most common Power BI gotcha with date columns. When you drag a Date field onto an axis, Power BI auto-expands it into Year → Quarter → Month → Day. You need to either:

**Option A (recommended):** Right-click the Month field in the Fields pane → uncheck "Date Hierarchy" → drag the raw Month field onto the X-axis. This gives you one point per month.

**Option B:** In the visual, drill down from Year to Month level. But this is fragile — viewers would need to know to drill down every time they open the file.

After fixing, the trend line should show 26 data points from Jan 2024 to Feb 2026, starting near $5,800 and ending at $152,034.50. The movements chart should show 26 columns of stacked bars.

---

## Should Fix (Polish)

### 3. Page name is still "Page 1"

Step 7 says rename the tab to "Executive Dashboard." Right-click the page tab at the bottom → Rename.

### 4. Subtitle formatting matches title

Both lines in the header textbox are 18pt bold. The assignment says the title ("iDynamics — SaaS Executive Dashboard") should be 18pt bold, but the subtitle ("Data through February 2026") should be 10pt, not bold. Select the subtitle text → change font size to 10pt and remove bold.

### 5. No source label

Step 16 asks for a small text box in the bottom-right:

> Source: 03_retention_metrics.xlsx | Data through Feb 2026

Font: 8pt, gray (#999999). This is a professional habit — every dashboard should cite its data source and freshness date.

### 6. No custom colors on the movements chart

The assignment provides a specific color system for the waterfall bars: green (#2E7D32) for New, light green (#81C784) for Expansion, orange (#F4892F) for Contraction, red (#C62828) for Churned. The column chart is currently using Power BI's default palette.

**Fix:** Click the column chart → Format pane → Data colors → set each series to its assigned hex code. This is how you'd do it in a real board deck — the colors carry meaning (green = growth, red = loss), and they should match the Excel workbook you already built.

### 7. No left accent border on KPI cards

The assignment specifies a thick left border in #1565C0 blue on each card. Cards 2–4 have a basic border enabled but no color or left-side accent. Card 1 has no border at all. This is a small visual detail, but it's the kind of thing that separates a draft from a finished product.

---

## Not Required But Worth Noting

**Retention trend (Stretch 1) is not present.** The overview mentions 6 sections including "Retention trend — GRR and NRR lines over time," but the detailed steps put this in Stretch Goals since it requires Power Query unpivoting. Not a ding — just flagging it as the next thing to try if you want to push the dashboard further.

**Cross-filtering behavior** — make sure you've tested the checklist from Step 17. The key test: click a plan in the slicer → snapshot visuals (cards, donut, bar chart) should update, but the waterfall visuals (trend line, movements) should NOT change. That's the expected behavior because the Waterfall table is standalone.

---

## Self-Check Scorecard

| Check | Expected | Status |
|-------|----------|--------|
| Current MRR card | $144,185.50 | ✅ Correct measure |
| Active Subs card | 51 | ✅ Correct measure |
| Trend line last point | $152,034.50 (Feb 2026) | ⚠️ Fix date hierarchy first, then verify |
| Donut largest slice | Platform Suite (by MRR) | ❌ Currently showing count, not MRR |
| Bar chart top bar | Eastern Canada | ✅ Correct (SUM confirmed) |
| Cross-filtering | Snapshot visuals filter, waterfall independent | ✅ Model supports this |
| Data model | 3 data tables + 1 measures table, 1 relationship | ✅ Correct |
| Movement chart | 26 monthly bars with 4 series | ⚠️ Fix date hierarchy first |
| Page name | "Executive Dashboard" | ❌ Still "Page 1" |
| Source label | Bottom-right, 8pt gray | ❌ Missing |

---

## What to Do

1. Fix the donut aggregation (COUNT → SUM) — this takes 10 seconds
2. Fix the date hierarchy on both waterfall charts — this takes 2 minutes
3. Rename the page
4. Fix the subtitle font size
5. Add the source label
6. Set custom colors on the movements chart
7. Re-run the Step 17 interactivity checklist
8. Resubmit

The bones are good. The two must-fix items are common Power BI mistakes that every analyst makes exactly once. After this round, the dashboard is presentable.

---

*iDynamics Finance Analyst Training Program*
*Power BI Assignment 01 — Feedback*
*March 2026*
