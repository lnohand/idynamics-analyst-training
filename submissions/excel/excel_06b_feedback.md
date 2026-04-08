# Excel 06b Feedback — KPIs, Tracker, WaterfallData
**PR:** #8 | **Reviewed by:** David Chen

---

## Round 2 Review

Good progress. Four of the six fixes from last round are resolved. Here's
where things stand.

---

## Fixed — Good Work

**ARPA source:** Correct. Now using `Closing MRR ÷ Active Customers` from
your Jan 31 snapshot = $3,712.29. This is the right pattern for every
monthly KPI going forward.

**Contraction MRR row:** Present in Jan A vs F (row 6, value = $0 actual and
forecast). Row exists in the architecture. Good.

**WaterfallData sourcing:** Contraction and Churned rows now reference
`Jan 2026 A vs F` directly. No more Waterfall tab references.

**PR description self-check:** Filled in. Numbers match.

---

## Still Open

### Fix 1 — PR description missing WaterfallData row count

The brief template explicitly included:

```
WaterfallData row count: ___
```

It's missing from your PR description. This is a small thing but the rule is
the whole template, not just the KPI numbers. Add it.

---

### Fix 2 — KPI Tracker month headers still not text labels

You applied a date format (`mmm-yy`) to the column header cells — so they
now display as `Jan-26`, `Feb-26`, `Mar-26` rather than raw serial numbers.
That's better, but it's still not what was asked for.

The brief specifies: `Jan 2026`, `Feb 2026`, `Mar 2026`, `Q1 2026`.

The difference matters for Power BI. When you connect a table to Power BI
and it reads a formatted date cell, it may interpret it as a date type and
apply its own formatting — which could break your axis labels or filter
panels. A plain text cell is unambiguous. Type the text directly, or use a
`TEXT()` formula: `=TEXT(B3,"mmm yyyy")`.

Change all three column headers to static text: `Jan 2026`, `Feb 2026`,
`Mar 2026`. `Q1 2026` is already text — leave it.

---

### Fix 3 — kpi_definitions.md has wrong content

This file should contain your KPI definitions — formula, what it means,
when to use it. It currently contains a copy of the Git workflow from
`git_commands.md`. This is not a minor overlap — the file has zero KPI
content.

You defined five KPIs in this assignment: ARPA, GRR, NRR, Quick Ratio, CAC.
You also now understand why LTV and LTV:CAC are quarterly metrics and not
monthly ones. Write those definitions in your own words.

---

### Fix 4 — excel_techniques.md is empty

The file was created but has no content. In this assignment you used Excel
Tables for the first time and applied them with a specific naming convention
(`WaterfallData`). You also used `IFS()` for conditional F/U flags and
`IFERROR()` for safe division. Document what you did and why — this tab is
your future reference sheet, not a submission artifact.

---

## One More Thing — Open Cell Comment

Your cell comment on WaterfallData D5 still reads:
*"The Jan 2026 A vs F file does not include Contraction MRR."*

This was accurate when you wrote it. It's no longer accurate — you fixed it.
Delete the comment before the next push so the workbook doesn't contradict
itself.

---

## Summary

| # | Issue | Status | Action |
|---|-------|--------|--------|
| 1 | PR description empty | ✅ Fixed | — |
| 2 | ARPA wrong source | ✅ Fixed | — |
| 3 | Contraction row missing | ✅ Fixed | — |
| 4 | WaterfallData wrong sources | ✅ Fixed | — |
| 5 | KPI Tracker date format | ⚠️ Partial | Change to text: `Jan 2026` format |
| 6 | my-notes not updated | ❌ Open | Fix kpi_definitions.md, fill excel_techniques.md |
| 7 | PR description missing WaterfallData row count | ❌ Open | Add to PR description |
| 8 | Stale cell comment | ❌ Open | Delete WaterfallData D5 comment |

Four fixes remaining. Push them and reply here. This is close.
