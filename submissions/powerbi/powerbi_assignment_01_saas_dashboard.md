# Power BI Assignment 01 — SaaS Executive Dashboard
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Put the workbook into something the team can actually use
>
> Your Excel workbook is the best analysis we have. The problem is
> that it lives on your laptop. When Sarah asks me "what's our NRR?"
> I can't send her a 10-tab workbook and say "look at row 6 of the
> Retention tab." She needs a dashboard she can open in her browser,
> click around, and get her own answers.
>
> Take the workbook you've already built and turn it into a Power BI
> dashboard. Same data, same numbers — just a different delivery
> format. Don't rebuild anything from scratch. The whole point is
> that the hard work is done. Now make it presentable.
>
> — David

---

## Why Power BI

You've spent the last few weeks building an Excel workbook that
calculates MRR, classifies movements, tracks growth, and measures
retention. Every number is verified. That workbook is the analysis
layer — it's where you think, calculate, and check your work.

Power BI is the presentation layer. It takes the tables you've already
built and turns them into an interactive dashboard that other people
can use without opening Excel. They click a plan name and everything
filters. They hover over a month and see the breakdown. They bookmark
a view and share it with the board.

At iDynamics scale this is a nice-to-have. At 200 customers with a
5-person finance team, it becomes essential — you can't email
workbooks around and expect everyone to see the same numbers.

For this assignment, you're connecting Power BI directly to your
Excel file. No re-importing CSVs. No rewriting formulas. The
workbook is the source of truth and Power BI reads from it.

> **What comes later:** In a production environment, Power BI would
> connect directly to the database (Neon DB in our case) instead of
> an Excel file. That way the dashboard refreshes automatically when
> new data lands. We'll do that in a future assignment. For now,
> Excel-as-source teaches you Power BI itself without adding
> connection string complexity.

---

## What You're Building

A single-page executive dashboard with six sections:

1. **KPI cards** — Current MRR, active subs, NRR, GRR
2. **MRR trend** — closing MRR over 26 months from the Waterfall tab
3. **MRR waterfall bars** — new, expansion, contraction, churned by month
4. **MRR by plan** — donut chart from the Snapshot tab
5. **MRR by region** — bar chart from the Snapshot tab
6. **Retention trend** — GRR and NRR lines over time

Every number on this dashboard already exists in your workbook. You
are not calculating anything new. You are visualizing what's already
there.

---

## Prerequisites

- **Power BI Desktop** installed (free, Windows only — download from
  https://powerbi.microsoft.com/desktop/)
- Your completed workbook: `03_retention_metrics.xlsx`
- The workbook saved in a stable location (not a temp folder — Power BI
  will remember the file path)

---

## Part 1 — Connect to Your Workbook

### Step 1: Create a new Power BI file

Open Power BI Desktop. File → Save As → `idynamics_dashboard.pbix`.
Save it in the same folder as your workbook.

### Step 2: Import from Excel

Go to **Home → Get Data → Excel Workbook**. Browse to
`03_retention_metrics.xlsx`.

Power BI will show a Navigator with all your sheet names. Select
these three tabs:

- **Raw Snapshot**
- **Waterfall**
- **Engine**

Do NOT select Growth or Retention yet — those tabs have a horizontal
layout (months as columns) that Power BI can't chart directly. We'll
come back to those.

Click **Transform Data** to open Power Query Editor.

> **Why only three tabs?**
> Power BI works best with vertical tables — one row per record,
> columns as attributes. Your Raw Snapshot (one row per subscription)
> and Engine (one row per event) are already in that shape. The
> Waterfall tab is close — one row per month. But Growth and
> Retention have months running left-to-right, which is great for
> Excel reading but needs reshaping for Power BI.

### Step 3: Clean each table in Power Query

**Raw Snapshot:**
1. Click the Raw Snapshot query in the left panel
2. Verify column types: `mrr` should be Decimal Number, `subscription_id`
   should be Text (not number)
3. If Power BI imported the header row as data, click **Use First Row
   as Headers**
4. Check row count in the bottom status bar: should be **51 rows**

**Waterfall:**
1. Click the Waterfall query
2. The first row is a title ("MRR Waterfall — January 2024 to February
   2026"). Remove it: click **Remove Top Rows** → 1 row
3. Click **Use First Row as Headers** — you should now see: Month,
   Opening, New, Expansion, Contraction, Churned, Net, Closing
4. Below the data rows there's a blank row and three summary rows
   (Waterfall Closing MRR, Snapshot MRR, Reconciliation Gap). Remove
   them: click **Remove Bottom Rows** → 4 rows
5. Set the Month column to Date type
6. Set all MRR columns (Opening through Closing) to Decimal Number
7. You should have **26 data rows** (Jan 2024 through Feb 2026)

**Engine:**
1. Click the Engine query
2. Use First Row as Headers if needed
3. Verify `mrr_delta` is Decimal Number, `month` is Date, `event_date`
   is Date
4. Should be **97 data rows**

When all three are clean, click **Close & Apply**.

### Self-check — Part 1

In **Data** view, click each table and verify:

| Table | Rows | Key columns |
|-------|------|-------------|
| Raw Snapshot | 51 | subscription_id, plan_name, region, mrr |
| Waterfall | 26 | Month, Opening, New, Expansion, Contraction, Churned, Closing |
| Engine | 97 | event_id, movement, mrr_delta, month |

---

## Part 2 — Build the Data Model

### Step 4: Check relationships

Go to **Model** view. Power BI may have auto-detected a relationship
between Engine and Raw Snapshot on `subscription_id`. If it did,
verify it's Many-to-One (Engine → Snapshot). If it didn't, create it
by dragging `subscription_id` from Engine onto `subscription_id` in
Raw Snapshot.

The Waterfall table stands alone — it has no join key to the other
tables. That's fine. It's a pre-aggregated monthly summary that
feeds its own visuals independently.

Your model should have:
- 2 tables connected by subscription_id (Engine → Raw Snapshot)
- 1 standalone table (Waterfall)

> **Why so simple?**
> Because the heavy lifting already happened in Excel. You didn't
> import raw CSVs that need joining — you imported finished tables.
> The Snapshot already has region and plan baked in. The Waterfall
> already has monthly totals calculated. The Engine already has
> movement types classified. Power BI just displays what you built.

---

## Part 3 — Build Measures

### Step 5: Create a Measures table

**Home → Enter Data** → name the table `_Measures` → click Load.

### Step 6: Add measures

Click `_Measures`, then **Home → New Measure** for each:

**Current MRR** — sums the mrr column from the snapshot:

```dax
Current MRR = SUM('Raw Snapshot'[mrr])
```

**Active Subscriptions:**

```dax
Active Subscriptions = COUNTROWS('Raw Snapshot')
```

**Avg MRR per Sub:**

```dax
Avg MRR per Sub = DIVIDE([Current MRR], [Active Subscriptions], 0)
```

**Latest Closing MRR** — pulls the last month's closing from the
Waterfall. This is different from Current MRR because the Waterfall
includes the reconciliation gap:

```dax
Latest Closing MRR = 
CALCULATE(
    MAX(Waterfall[Closing]),
    Waterfall[Month] = MAX(Waterfall[Month])
)
```

**Net Change** — latest month's net MRR change:

```dax
Latest Net Change = 
CALCULATE(
    MAX(Waterfall[Net]),
    Waterfall[Month] = MAX(Waterfall[Month])
)
```

Format all currency measures as Currency (2 decimals). Format Active
Subscriptions as Whole Number.

### Self-check — Part 3

Create temporary card visuals to verify:

| Measure | Expected |
|---------|----------|
| Current MRR | $144,185.50 |
| Active Subscriptions | 51 |
| Avg MRR per Sub | $2,827.17 |
| Latest Closing MRR | $152,034.50 |
| Latest Net Change | -$594.00 |

**Two different MRR numbers — this is correct.** $144,185.50 is the
snapshot (current state of active subscriptions). $152,034.50 is the
waterfall closing (sum of all historical movements). The $7,849 gap
is the reconciliation difference you already documented in Excel.
Use the snapshot number ($144,185.50) on the KPI card — it's more
accurate for current state.

Delete temporary cards after verifying.

---

## Part 4 — Design the Dashboard

### Step 7: Set up the page

In **Report** view:
- Rename the page tab to "Executive Dashboard"
- Format page → Canvas background: White
- Page size: 16:9

### Step 8: Header

Add a **Text Box** across the top:

```
iDynamics — SaaS Executive Dashboard
Data through February 2026
```

Title at 18pt bold, subtitle at 10pt, dark gray (#333333).

### Step 9: KPI cards (top row)

Create **four Card visuals** in a row:

| Card | Measure | Expected Value |
|------|---------|----------------|
| 1 | Current MRR | $144,185.50 |
| 2 | Active Subscriptions | 51 |
| 3 | Avg MRR per Sub | $2,827.17 |
| 4 | Latest Net Change | -$594.00 |

Format each card:
- Callout value: 24pt
- Category label: 9pt
- Background: light gray (#F5F5F5)
- Left border: thick, colored (#1565C0 blue)

### Step 10: MRR trend line (middle row, left)

Create a **Line Chart**:

- **X-Axis:** Waterfall[Month]
- **Y-Axis:** Waterfall[Closing]

This shows the 26-month MRR trajectory from $5,800 to $152,034.

Format:
- Title: "MRR Over Time"
- Line color: #1565C0
- Line thickness: 2px
- Data markers: on
- Y-axis: start at 0
- X-axis: if labels overlap, angle them

### Step 11: MRR movements (middle row, right)

Create a **Clustered Column Chart**:

- **X-Axis:** Waterfall[Month]
- **Y-Axis:** Add these as separate values:
  - Waterfall[New]
  - Waterfall[Expansion]
  - Waterfall[Contraction]
  - Waterfall[Churned]

This shows the composition of change each month — the same
information as your Waterfall tab but as a visual.

Format with the color system from your Excel workbook:
- New: #2E7D32 (green)
- Expansion: #81C784 (light green)
- Contraction: #F4892F (orange)
- Churned: #C62828 (red)
- Title: "Monthly MRR Movements"

> **Note:** Contraction and Churned are already stored as negative
> numbers in your Waterfall tab. The chart will show them below
> the axis automatically. This is correct — losses go down,
> gains go up.

### Step 12: MRR by Plan (bottom row, left)

Create a **Donut Chart**:

- **Legend:** Raw Snapshot[plan_name]
- **Values:** Raw Snapshot[mrr]

Format:
- Title: "Current MRR by Plan"
- Data labels: show category name + value
- Inner radius: ~50%

Verify: Platform Suite should be the largest slice ($36,750),
followed by Analytics Enterprise ($32,580).

### Step 13: MRR by Region (bottom row, right)

Create a **Horizontal Bar Chart**:

- **Y-Axis:** Raw Snapshot[region]
- **X-Axis:** Raw Snapshot[mrr]

Format:
- Title: "Current MRR by Region"
- Bar color: #2E7D32
- Sort descending by value

Verify: Eastern Canada ($69,785) and Western Canada ($68,421)
should be roughly equal. Central Canada ($5,980) is much smaller.

### Step 14: Add slicers

Add two **Slicer** visuals:

1. **Plan:** Raw Snapshot[plan_name] — Dropdown style
2. **Region:** Raw Snapshot[region] — Dropdown style

Place them along the top-right or as a sidebar.

When you click a plan in the slicer, the donut, bar chart, and KPI
cards (Current MRR, Active Subs, Avg MRR) will all filter. The
Waterfall visuals (trend line and movements chart) will NOT filter
because the Waterfall table isn't related to the Snapshot table.
That's expected — the waterfall is company-level, not plan-level.

> **Teaching moment:** This is a real limitation. If David asks
> "show me the MRR trend for Platform Suite only," this dashboard
> can't do it because the Waterfall tab is pre-aggregated. To get
> plan-level trends, you'd need to go back to the Engine table and
> build a different visual. That's a stretch goal below.

### Self-check — Part 4

With no slicers selected:

| Visual | Expected |
|--------|----------|
| Current MRR card | $144,185.50 |
| Active Subs card | 51 |
| Trend line last point | $152,034.50 (Feb 2026) |
| Donut largest slice | Platform Suite |
| Bar chart top bar | Eastern Canada |

Click "Analytics Starter" in the plan slicer:
- Current MRR card should drop to $3,105.00
- Active Subs should show 5
- Donut should show only one slice
- Bar chart should show only regions with Starter customers
- Trend line should NOT change (Waterfall is independent)

Clear the slicer and confirm everything returns to baseline.

---

## Part 5 — Polish and Present

### Step 15: Formatting pass

Apply these rules across all visuals:

- Font: Segoe UI everywhere (Power BI default)
- Visual titles: 11pt bold
- Card backgrounds: light gray; chart backgrounds: white
- Remove gridlines on bar/column charts
- Legend position: bottom on all charts
- No borders on chart objects

### Step 16: Data freshness label

Small text box, bottom-right:

```
Source: 03_retention_metrics.xlsx | Data through Feb 2026
```

Font: 8pt, gray (#999999).

### Step 17: Test interactivity

Walk through this checklist:

- [ ] Click a bar in the region chart → donut and cards filter
- [ ] Click a donut slice → bar chart and cards filter
- [ ] Use the plan slicer → snapshot visuals update, waterfall stays
- [ ] Use the region slicer → snapshot visuals update, waterfall stays
- [ ] Click a column in the movements chart → nothing else should filter (waterfall is standalone)
- [ ] Clear all filters → all values return to baseline

### Step 18: Practice the walkthrough

The dashboard tells a story in this order:

1. **Cards** — "Current MRR is $144K across 51 active subscriptions"
2. **Trend line** — "We grew from zero to $152K over 26 months, but
   the curve flattened in H2 2025"
3. **Movements chart** — "You can see why — green bars (new MRR)
   disappeared after June 2025, and red bars (churn) kept going"
4. **Donut** — "Platform Suite is our biggest plan at $37K, but no
   single plan dominates"
5. **Region bar** — "Revenue is split almost evenly between East
   and West, with Central at 4%"
6. **Slicer demo** — click Platform Suite → "Here's what it looks
   like filtered to just one plan"

Practice this out loud. The audience doesn't care how you built
it. They care what it tells them.

---

## Deliverables

Save and commit:

```
submissions/powerbi/01_saas_dashboard.pbix
```

Branch: `student/powerbi-01-saas-dashboard`

PR description:

```
## What this does
Power BI executive dashboard sourced from 03_retention_metrics.xlsx.
4 KPI cards, MRR trend line, monthly movement bars, plan donut,
region bar chart, two slicers with cross-filtering.

## Self-check
Current MRR (Snapshot): $144,185.50 ✅
Active Subscriptions: 51 ✅
Waterfall Closing (Feb 2026): $152,034.50 ✅
Cross-filtering: snapshot visuals filter, waterfall stays independent ✅
Data model: 3 tables, 1 relationship ✅

## Questions for reviewer
[Anything you're unsure about]
```

---

## Stretch Goals

**Stretch 1 — Add the Retention trend.**
This requires reshaping data. In Power Query, import the Retention
tab. Use **Unpivot Columns** to turn the month columns into rows,
giving you a vertical table with columns: Metric, Month, Value.
Filter to just GRR and NRR rows. Then build a dual-line chart
showing both over time. This is harder than anything in the core
assignment — it teaches Power Query transformation.

**Stretch 2 — Plan-level trend from Engine.**
Create a measure that sums `mrr_delta` cumulatively by plan. This
lets you build a trend line that DOES respond to the plan slicer.
Use:

```dax
Cumulative MRR = 
CALCULATE(
    SUM(Engine[mrr_delta]),
    FILTER(
        ALL(Engine[month]),
        Engine[month] <= MAX(Engine[month])
    )
)
```

Then build a line chart with Engine[month] on x-axis and this measure
on y-axis. Add Raw Snapshot[plan_name] to the Legend. Now the plan
slicer filters the trend.

**Stretch 3 — Bookmarks for presentation.**
Create bookmarks (View → Bookmarks) that save specific slicer states:
"All Plans," "Platform Suite Only," "Eastern Canada Only." Add
bookmark buttons to the page. During KT, click through them instead
of manually adjusting slicers.

---

## Common Mistakes

**"Current MRR doesn't match the trend line endpoint."**
Correct — they shouldn't match. Current MRR ($144,185.50) comes
from the Snapshot. The trend line endpoint ($152,034.50) comes from
the Waterfall. The $7,849 gap is the reconciliation difference you
already documented. This is not a bug.

**"The slicer doesn't affect the waterfall chart."**
Correct — this is expected. The Waterfall table has no relationship
to the Snapshot table. It's pre-aggregated monthly data at the
company level. Plan-level filtering only works on Snapshot-connected
visuals. See Stretch 2 for a workaround.

**"Contraction and Churned bars point down."**
Correct — they're stored as negative numbers in your Waterfall tab.
Negative bars below the axis is the standard visual convention for
MRR losses.

**"Power BI shows (Blank) in my donut chart."**
Check if Power Query dropped any rows or if the plan_name column
has nulls. Add a visual-level filter: plan_name "is not blank."

**"The Month column sorts wrong (Apr before Feb)."**
Power BI is sorting alphabetically instead of chronologically.
Select the Month column in Data view → Column tools → Sort by
Column → sort by the Month column itself (if it's a Date type,
this should work automatically). If it's text, you need to create
a month-number column and sort by that.

---

## What This Teaches

This assignment covers four things that matter in every analyst role:

1. **Connecting Power BI to an existing data source** — the real
   skill is knowing what to import, not how to click buttons
2. **Data modeling** — understanding which tables relate and which
   stand alone, and why that affects filtering
3. **The gap between analysis and presentation** — your Excel
   workbook has 8 tabs of detail. The dashboard has 6 visuals.
   Deciding what to show and what to leave out is the job.
4. **Interactive storytelling** — slicers and cross-filtering let
   the audience explore, which builds more trust than a static chart

---

## Reference: Color System

Consistent with your Excel workbook:

| Element | Hex | Usage |
|---------|-----|-------|
| New MRR | #2E7D32 | Green — growth |
| Expansion | #81C784 | Light green — upsell |
| Contraction | #F4892F | Orange — warning |
| Churned | #C62828 | Red — loss |
| Trend / Neutral | #1565C0 | Blue — trend lines, cards |

Enter custom colors: click any color picker → Custom color → paste hex.

---

*Idynamics Finance Analyst Training Program*
*Power BI Assignment 01 — SaaS Executive Dashboard*
*March 2026*
