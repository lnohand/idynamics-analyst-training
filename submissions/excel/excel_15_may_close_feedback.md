# Feedback — Excel 15: May 2026 Close

**PR #27 · branch `student/excel_15_may_close`**

Strong mechanical work, Michael — the hard part of this one is right. You added
the **Contraction row to `Actuals` in the correct waterfall slot** (Opening → New
→ Expansion → **Contraction** → Churn → Closing) and extended Closing MRR to
`F7 = =F2+F3+F4-F5-F6`, so contraction actually flows through. And you dodged the
trap the brief laid: on the May A vs F tab **both** derived rows pick up
contraction — `Net New B8 = =B4+B5-B6-B7` and `Closing B9 = =B3+B4+B5-B6-B7` — not
just Closing. The whole close ties end to end:

| Self-check | Expected | Yours |
|---|---|---|
| May Net New MRR | $3,245.00 | **3,245.00** ✅ |
| May Closing MRR | $160,075.50 | **160,075.50** ✅ |
| Active Subscriptions | 56 | **56** ✅ |
| GRR / NRR resolve | values, not #N/A | **98.75% / 99.02%** ✅ |

Opening chain intact (`F2 = =E7`), closed months Jan–Apr untouched, GRR/NRR are
dynamic `INDEX/MATCH` on the config month with no hardcoded columns, and the
KPI Tracker May column ties. Nice.

But this assignment was built around one idea — **contraction vs. churn** — and
that's exactly where it comes apart. Two substantive fixes before this can merge,
plus some hygiene.

---

## A — Substantive close issues (fix before resubmit)

### A1 — The commentary swaps contraction and logo churn (the headline)
This is the one that matters. Your own `Engine` table is the ground truth, and it
disagrees with your story:

- **Toronto Media Group** (SUB051, Sales Hub, 23→19 seats): `movement = Contraction`,
  `mrr_delta = -440`, `is_logo_churn = 0`. They **shrank but stayed** — this is the
  contraction.
- **Ontario Education Connect** (SUB026, Analytics Growth): `movement = Churned`,
  `mrr_delta = -1520`, `is_logo_churn = 1`. They **cancelled outright** — this is
  the logo churn.

Your commentary says the opposite of both:

- **A64:** *"We also lost 4 seats from Toronto Media Group. This is a logo churn
  meaning that we lost both the revenue and the logo."* — No. A 4-seat reduction
  on a still-active subscription **is the contraction**. Losing seats is not
  losing the logo.
- **A65:** *"...the situation with Ontario Education Connect is only a contraction
  since they still have seats in the plan."* — No. Ontario Education Connect
  cancelled; they have **no** seats left. This is the logo churn — and this
  sentence directly contradicts your own A64, which correctly calls their
  Analytics Growth plan "the cancelled subscription this month."

You had the raw facts right (4 seats off Toronto Media Group; Ontario Education
Connect's Analytics Growth cancelled) — you just pinned the wrong **label** on
each. Rewrite so the contraction paragraph names **Toronto Media Group** (existing
customer reducing usage, still active — watch their seat trend on that account),
and the churn paragraph names **Ontario Education Connect** as the **logo churn**
(whole relationship ended, active-customer count takes the hit), contrasted with
April's **revenue** churn where the customer stayed. Your A64 opening already draws
that April contrast correctly — keep it, and fix everything after it.

### A2 — Contraction's Favorable/Unfavorable sign is backwards
You handled the churn row correctly but left contraction on the wrong convention.

- **Churn (row 7):** `D7 = =C7-B7` (Forecast − Actual) = −444.9 → `F7` = **"U"**.
  Correct — more churn than plan is unfavorable.
- **Contraction (row 6):** `D6 = =B6-C6` (Actual − Forecast) = 440 − 0 = **+440**
  → `F6` = **"F" (Favorable)**.

May's actual contraction ($440) is **worse** than the $0 plan, so it must read
**Unfavorable**, not Favorable. Contraction reduces revenue exactly like churn —
give its variance the same flipped treatment you already gave churn (compute it
as Forecast − Actual, or flip the F/U test on that row). The brief called this out
specifically: *"apply your sign convention consistently so a worse-than-plan
contraction reads as unfavorable."* This error also rode into **Waterfall Data
`E33` = +440** (favorable) sitting next to churn `E34` = −444.9 (unfavorable) —
same inconsistency, fix both.

### A3 — `Waterfall` grid summary still points at April
On the Engine-driven `Waterfall` tab you added May's row (row 32, Contraction
−440, Closing 160,075.5 — good), but the summary cell beneath it,
**`B35` "Waterfall Closing MRR" = `=H31`**, still reads the **April** row
(156,830.5). It should point at the May row `H32` (160,075.5). This is precisely
the "check whether the summary rows beneath the table still point at the last
month" note in Part 4. (The reconciliation gap in that block doesn't tie to $0
even once you repoint it, and that pre-dates May, so leave the rest of that block
alone — just fix the stale reference.)

---

## B — Process / hygiene

### B1 — Wrong file location
The workbook is committed at the **repo root** as `excel_15_may_close.xlsx`. It
needs to live at **`submissions/excel/excel_15_may_close.xlsx`**, where every prior
submission sits — otherwise it's outside where the assignment expects it. Move it
(`git mv`) and re-push.

### B2 — `my_notes/` not updated
Only the `.xlsx` changed on the branch. The brief asks for three note updates, and
you know all three cold — write them down:
- `sql_queries.md` — the `subscription_events` query that isolates a seat
  *decrease* (contraction) from an expansion and from a cancellation.
- `kpi_definitions.md` — **contraction** as a movement type: what it is, where it
  sits in the waterfall, what sign it carries, how it pulls on NRR; plus the
  logo-vs-revenue churn recap with the April/May examples (the exact thing A1 is
  about).
- `excel_techniques.md` — how you added a movement row without disturbing closed
  months.

### B3 — Empty PR description
The PR body is blank. Fill in the description from the brief's template and paste
your completed Self-Check table — that's how I see what you verified before
pushing.

### B4 — Tab name has a trailing space
Your new tab is `'May 2026 A vs F '` — with a trailing space. The brief asked for
**no** trailing space (the space is the fragile convention we're trying to retire,
not copy forward). Nothing breaks today because your references are internally
consistent, but rename it to `'May 2026 A vs F'` and update the handful of
references that point at it (KPI Tracker, Waterfall Data).

---

## What to fix before resubmitting
Focus on the two that matter — **A1 (rewrite the commentary so the two customers
are on the right movement)** and **A2 (contraction F/U → Unfavorable, both tabs)**.
Then the quick ones: **A3** stale summary reference, **B1** file location,
**B2** notes, **B3** PR description, **B4** tab name. The math underneath is solid —
this is a revise-and-resubmit on the analysis and the housekeeping, not the close
itself.

— David
