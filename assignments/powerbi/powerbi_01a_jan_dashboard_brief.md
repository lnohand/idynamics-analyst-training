# Power BI Assignment 01a — January SaaS Dashboard
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Let's get the January dashboard live
>
> Michael — the Excel workbook is solid, but spreadsheets don't scale for an
> audience. When I'm in a leadership meeting I need to pull up one screen and
> see MRR movement and unit economics at a glance — not scroll through tabs.
> That's what Power BI is for. You built the WaterfallData table in 06b
> specifically so we could connect it here. Now connect it. I want to see the
> January waterfall and KPI cards in a Power BI dashboard by end of week.
> This is the first version — one month, clean, no clutter.
>
> — David

---

## What You're Building

Four additions in a new Power BI file:

1. **Data connection** — Power BI linked to your Excel workbook, loading `WaterfallData` and `KPI Tracker` as live tables
2. **Waterfall chart** — MRR waterfall for January 2026, pulled from `WaterfallData`
3. **KPI cards** — four cards showing Closing MRR, ARPA, GRR, and NRR for January
4. **Month slicer** — a filter control that works now with one month and auto-expands as you add data

The file you'll submit: `submissions/powerbi/powerbi_01a_jan_dashboard.pbix`

---

## Part 1 — Connect Power BI to Your Excel Workbook

**What Power BI Desktop is**

Power BI Desktop is a free Microsoft application for building interactive dashboards. It does not store your data — it connects to a source file (your Excel workbook) and reads from it. When the source data changes, you click Refresh and the dashboard updates. That's the whole point of the structured Excel Table format you built in 06b.

If you don't have Power BI Desktop installed, download it free from microsoft.com/en-us/power-bi. Install it, then open it.

**Connecting to your workbook**

1. Open Power BI Desktop. Dismiss the splash screen if one appears.
2. In the top ribbon, click **Home → Get Data → Excel workbook**.
3. A file picker dialog opens. Navigate to your repo and select:
   ```
   submissions/excel/06_actual_vs_forecast.xlsx
   ```
4. Click **Open**.

**The Navigator pane**

After selecting the file, a Navigator pane opens on the right side of the screen. This pane lists every sheet and every named Table that Power BI found in the workbook. You should see entries including:

- `WaterfallData` — this is the named Excel Table you created in 06b
- `KPI Tracker` — this is the sheet (Power BI can read sheets too)

If you see a sheet called `Waterfall Data` (with a space) but not `WaterfallData` (no space) in the Table list, the Excel Table may not be named correctly. Go back to your workbook, check the Table Design tab, and confirm the table name is `WaterfallData` with no space.

**Loading the tables**

5. In the Navigator, tick the checkbox next to `WaterfallData`.
6. Tick the checkbox next to `KPI Tracker`.
7. Click **Load** (not "Transform Data" — the tables are already clean from your Excel work).

Power BI will load both tables into its data model. You'll see them listed in the **Fields** pane on the right side of the screen. The Fields pane is where you find your columns when building visuals.

### Self-Check — Connection

Before moving on, verify:

| Check | What to look for |
|-------|-----------------|
| WaterfallData in Fields pane | Expand it — you should see: Month, Movement, Actual, Forecast, Variance |
| KPI Tracker in Fields pane | Expand it — you should see your metric names and month columns |
| Row count | Click on the WaterfallData table name in the Fields pane — the status bar at the bottom shows row count. You should see 7 rows. |

---

## Part 2 — Build the Waterfall Chart

**What a waterfall chart is**

A waterfall chart shows how a starting value changes through a series of increases and decreases to reach an ending value. In SaaS finance, this is the MRR waterfall: start with Opening MRR, add New MRR and Expansion MRR, subtract Contraction MRR and Churned MRR, and arrive at Closing MRR. Power BI has a built-in waterfall chart type that handles the increase/decrease coloring automatically — you don't need to configure that logic yourself.

**Adding the visual**

1. In the **Visualizations** pane (right side of screen), click the **Waterfall chart** icon. It looks like a stepped bar chart. If you hover over the icons, the tooltip will say "Waterfall chart."
2. A blank chart placeholder appears on the canvas.

**Placing the fields**

The Visualizations pane has a section called **field wells** — these are the drop zones that control what data goes where in the chart. For the waterfall chart you will see wells labeled **Category**, **Breakdown**, **Y-axis**, and possibly others.

3. From the Fields pane, drag the **Movement** column (from WaterfallData) into the **Category** field well. This puts the waterfall rows (Opening MRR, New MRR, etc.) on the X-axis.
4. Drag the **Actual** column (from WaterfallData) into the **Y-axis** field well. This sets the bar heights.

**Why "Closing MRR" needs special handling**

Power BI waterfall charts always auto-generate a final "Total" bar. It computes this by summing every bar in the chart — increases add, decreases subtract. This is exactly right for the middle movement rows. But your WaterfallData also includes a "Closing MRR" row, which is already the ending balance. If that row is included in the chart, Power BI counts it twice: once as a data bar, and again when it sums everything for the auto-Total. The Total bar ends up inflated and wrong.

The fix is to exclude the "Closing MRR" row from the chart and then rename the auto-Total bar to "Closing MRR."

**Step 5 — Exclude Closing MRR from the chart visual**

5. With the waterfall chart selected, look at the **Filters** pane (to the right of the Visualizations pane — click the funnel icon if it is not visible).
6. Under **Filters on this visual**, find the **Movement** filter field. If it is not there yet, drag the **Movement** column from the Fields pane into the "Add data fields here" drop zone under "Filters on this visual."
7. In the Movement filter, set the filter type to **Basic filtering**.
8. You will see a list of all Movement values with checkboxes. **Uncheck "Closing MRR"** so it is excluded from the chart. Leave all other values checked.
9. The chart now feeds from 6 rows: Opening MRR + five movements. The auto-Total bar correctly computes Opening MRR + movements = Closing MRR.

**Step 6 — Rename "Total" to "Closing MRR"**

The auto-Total bar label reads "Total" by default. Rename it:

10. With the chart selected, click the **Format visual** tab in the Visualizations pane (the paint roller icon).
11. Under the **Visual** tab, scroll down to find the **Total labels** section (it may appear inside a **Bars** section).
12. Look for a **Label** or **Title** text field. Clear it and type `Closing MRR`.

The final bar now reads "Closing MRR" and shows the correct ending MRR balance.

13. Resize the chart to fill roughly the left two-thirds of the canvas.

### Self-Check — Waterfall Chart

| Check | Expected |
|-------|---------|
| Bars on X-axis | Opening MRR, Net New MRR, New MRR, Churned MRR, Contraction MRR, Expansion MRR, Closing MRR |
| "Closing MRR" not in Movement filter | Unchecked — it is excluded from the chart data |
| Final bar label | "Closing MRR" (not "Total") |
| Bars colored correctly | Increases green, decreases red (or blue/orange — Power BI defaults vary) |
| Closing MRR bar height | Matches your Jan 2026 A vs F tab value ($144,779.50) |

---

## Part 3 — Build the KPI Cards

**What KPI cards are**

A KPI card is the simplest visual in Power BI — it shows a single number with a label. You'll build four: one each for Closing MRR, ARPA, GRR, and NRR. These pull from the `KPI Tracker` table you loaded in Part 1.

**The filtering challenge**

Your KPI Tracker table has metrics as rows and months as columns. Power BI works best with data that has months as rows (one row per month-metric combination). For this assignment, the KPI Tracker is structured the way you built it in Excel — which means you need to tell Power BI which column to pull from.

For each card, you will write a **Measure**. A Measure is a Power BI formula that calculates a value. You write it in a language called DAX (Data Analysis Expressions). DAX looks similar to Excel formulas.

**Creating a Measure for Closing MRR**

1. Right-click on `KPI Tracker` in the Fields pane → **New measure**.
2. A formula bar appears at the top. You'll write a DAX expression that:
   - Looks in the `KPI Tracker` table
   - Finds the row where the metric name equals "Closing MRR"
   - Returns the value in the "Jan 2026" column

   The structure uses `CALCULATE` and `FILTER`. Here is the pattern — fill in the exact column and row names from your table:

   ```
   Closing MRR Jan = CALCULATE(
       SUM('KPI Tracker'[Jan 2026]),
       FILTER('KPI Tracker', 'KPI Tracker'[Metric] = "Closing MRR")
   )
   ```

   Note: your metric column may be named differently depending on what you called it in 06b. Check the Fields pane for the exact column name. If your metrics column is called "Metric" this formula works as written. Adjust the column name and the metric label text to match your actual table.

3. Press Enter to confirm.
4. Repeat for ARPA, GRR, and NRR — create one measure each with the same pattern, changing the metric name string.

**Adding the cards to the canvas**

5. In the Visualizations pane, click the **Card** visual icon (it looks like a rectangle with a number in it).
6. Drag your `Closing MRR Jan` measure into the **Fields** well for the card.
7. The card now shows the January Closing MRR value.
8. Repeat for ARPA, GRR, and NRR — add a separate card for each measure.
9. Arrange the four cards in a row across the top or right side of the canvas.

**Formatting the cards**

For each card, click on it to select it, then use the **Format** pane (the paint roller icon in Visualizations) to:
- Set the **Data label** font size to something readable (18–24pt)
- Change the **Category label** to match the metric name (it defaults to the measure name — you can rename the measure itself by right-clicking it in the Fields pane)

### Self-Check — KPI Cards

| Metric | Your value |
|--------|-----------|
| Closing MRR | |
| ARPA | |
| GRR | |
| NRR | |

If a card shows a different value, check that the metric name string in your measure exactly matches what's in the Metric column of your KPI Tracker table. Capitalization and spacing matter.

---

## Part 4 — Add the Month Slicer

**What a slicer is**

A slicer is a filter control on the canvas. When you click a value in the slicer, it filters every other visual on the page to show only data for that selection. Right now you have one month (Jan 2026), so the slicer shows one option. When you add February rows to WaterfallData, the slicer will automatically show both options — and clicking February will update the waterfall chart and KPI cards to show February data.

**Adding the slicer**

1. In the Visualizations pane, click the **Slicer** icon (it looks like a funnel).
2. A blank slicer placeholder appears on the canvas.
3. From the Fields pane, drag the **Month** column from `WaterfallData` into the slicer's **Field** well.
4. The slicer now shows "Jan 2026."

**Positioning and testing**

5. Resize and position the slicer somewhere visible — top of the canvas or left side works well.
6. Click "Jan 2026" in the slicer. Confirm that the waterfall chart and KPI cards are still showing January data (they should be — this is also a test that the slicer is connected to the visuals).
7. Click the slicer value again or use the eraser icon on the slicer to deselect — confirm visuals still show data.

### Self-Check — Slicer

| Check | Expected |
|-------|---------|
| Slicer shows | "Jan 2026" |
| Clicking Jan 2026 | Waterfall chart and KPI cards remain populated |
| Slicer type | List or dropdown — either works |

---

## Part 5 — Refresh Workflow

This is the most important thing you will learn in this assignment.

**Why the refresh workflow matters**

Every month you close, you add 7 new rows to WaterfallData in Excel (one per waterfall movement for that month). Because WaterfallData is a named Excel Table — and because you connected Power BI to that table by name — Power BI can pull in the new rows automatically. You don't rebuild the dashboard. You click one button.

**Testing the refresh**

1. Open `06_actual_vs_forecast.xlsx` in Excel.
2. Go to the `WaterfallData` tab.
3. Scroll to the bottom of the WaterfallData table. Add one dummy row:
   - Month: `Test Month`
   - Movement: `Test Row`
   - Actual: `999`
   - Forecast: `999`
   - Variance: `0`
4. Save the Excel file. Close it.
5. Go back to Power BI Desktop.
6. Click **Home → Refresh** in the top ribbon.
7. Power BI re-reads the Excel file. After the refresh completes, check the WaterfallData row count in the status bar — it should now show 8 rows.
8. Confirm the slicer now shows "Test Month" as an option.
9. Go back to Excel. Delete the dummy row. Save. Close.
10. Refresh in Power BI again. Row count returns to 7. "Test Month" disappears from the slicer.

The dashboard is live-connected to the Excel file. Every month close, add rows, save, refresh. That's the workflow.

### Self-Check — Refresh

| Check | Expected |
|-------|---------|
| Row count after adding dummy row | 8 |
| Row count after deleting dummy row | 7 |
| Slicer updates after refresh | Yes — shows and then hides "Test Month" |

---

## Management Commentary

In a text box on the dashboard (Insert → Text box), write 3-4 sentences addressing both of the following:

1. **What does this dashboard show at a glance that the Excel tab does not?** Think about the difference between reading a table of numbers and seeing a chart — what insight is faster to reach?

2. **Why did the Excel Table format in 06b make this Power BI connection possible?** What would have broken if you had used a plain range instead of a named Excel Table?

**Minimum: 3-4 sentences. This is a hard gate — the PR will not be merged without it.**

Note: this commentary is different from your monthly close commentaries. Instead of narrating a business result (what happened, why, so what), you are reflecting on the tool and the workflow. Explain what the dashboard adds and why the data structure made it work.

---

## Git Workflow

This is a new assignment and a new file type — start a new branch.

```
git checkout main
git pull origin main
git checkout -b student/powerbi_01a_jan_dashboard
```

Save your Power BI file to the submissions folder:

```
submissions/powerbi/powerbi_01a_jan_dashboard.pbix
```

If the `submissions/powerbi/` folder doesn't exist yet, create it.

When ready to submit:

```
git add submissions/powerbi/powerbi_01a_jan_dashboard.pbix
git add my-notes/power_bi_notes.md
git commit -m "Add: Power BI 01a — January SaaS dashboard"
git push origin student/powerbi_01a_jan_dashboard
```

Open a PR from `student/powerbi_01a_jan_dashboard` → `main`.

---

## Keep Your Notes Current

This is your first Power BI assignment. Create a new notes file:

```
my-notes/power_bi_notes.md
```

Before you submit, make sure it includes:

| Topic | What to write |
|-------|--------------|
| Get Data workflow | The steps to connect Power BI to an Excel workbook |
| Navigator pane | What it shows, how to select tables vs sheets |
| Field wells | What they are and how you used them (Category, Y-axis, Fields) |
| Measures and DAX | What a measure is, the CALCULATE + FILTER pattern you used |
| Slicer | What it does, how to add one |
| Refresh workflow | The exact steps to refresh after updating the Excel source |
| Waterfall chart Totals | Why Closing MRR must be excluded from the chart visual (double-counting), how to filter it out, and how to rename the auto-"Total" bar to "Closing MRR" in Format → Total labels |

These notes will save you time in every Power BI assignment that follows. Write them in your own words.

---

## Submission

File:
```
submissions/powerbi/powerbi_01a_jan_dashboard.pbix
```

Open a PR from `student/powerbi_01a_jan_dashboard` → `main` with this description:

```
## Power BI 01a — January SaaS Dashboard

- WaterfallData and KPI Tracker connected from 06_actual_vs_forecast.xlsx
- Waterfall chart built (Movement on X-axis, Actual on Y-axis)
- KPI cards: Closing MRR, ARPA, GRR, NRR
- Month slicer added (Jan 2026)
- Refresh workflow tested (dummy row added, refreshed, removed, refreshed again)
- Management commentary added as text box on dashboard
- my-notes/power_bi_notes.md created

## Self-Check

WaterfallData row count:         ___
Closing MRR (card):              $___________
ARPA (card):                     $___________
GRR (card):                      ___%
NRR (card):                      ___%
Slicer shows:                    ___________
Refresh row count (dummy added): ___
Refresh row count (dummy removed): ___
```

---

## Final Self-Check

These are the expected values. Check every one before opening your PR. If anything doesn't match, find the issue before submitting — not after.

| Check | Expected value |
|-------|---------------|
| WaterfallData row count | 7 |
| Closing MRR card | $144,779.50 |
| ARPA card | $3,712.29 |
| GRR card | 100.0% |
| NRR card | 100.0% |
| Quick Ratio | N/A — no losses (January had zero churn; the denominator is $0. Do not show a formula error or a blank card. If you add a Quick Ratio card, display the text "N/A — no losses" or omit the card and note it in your PR.) |
| Month slicer value | Jan 2026 |
| Waterfall chart: Closing MRR bar | Matches $144,779.50 |
| Row count after dummy row + refresh | 8 |
| Row count after deleting dummy + refresh | 7 |

---

*Power BI Assignment 01a — January SaaS Dashboard*
*Idynamics Finance Analyst Training Program*
*April 2026*
