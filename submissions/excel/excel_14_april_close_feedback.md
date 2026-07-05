# Feedback — Excel 14: April 2026 Close

**PR #14 · branch `student/excel_14_april_close`**

*(Second-pass review — supersedes the prior version. You cleared the close fixes
from last time; this pass covers two new items on the April tab plus the
reconciliation cleanup that's still outstanding.)*

Good turnaround on the last round. Confirmed fixed: **Active Subscriptions now
reads 55** (and the month-over-month change shows +1), the **April waterfall rows
are in** (all seven movements, `Apr-26` label), **OpEx is sourced** from Lisa's
April numbers ($32k / $23k / $20k), and the **cost and retention commentary were
rewritten** correctly. The close ties end to end and the churn hard gate is solid.

Two things surfaced on this pass, and the Billing Reconciliation cleanup from last
time is still open.

---

## A — New close issues (Apr 2026 A vs F tab)

### A1 — Two "vs prior month" cells use a hardcoded column — fix these first
This is the teachable one, and it's the source of the bad number in your
commentary (A2 below).

- **C30 (Active Customers — vs Mar)** uses
  `XLOOKUP(..., 'KPI Tracker'!$C$4:$C$16)`. Column C of the KPI Tracker is
  **February**, so it computes 44 − 41 = **+3** when the real change vs March is
  44 − 42 = **+2**. The cell directly below it — **C31, Active Subscriptions** —
  already does this the right way, with a dynamic prior-month lookup
  (`MATCH(DATE(YEAR($I$2),MONTH($I$2)-1,1), …)`). Make C30 match C31.
- **C36 (Quick Ratio — vs)** has the same defect, pointed at column B
  (**January**).

Why it happened: when you copied the March tab, those cells were *correct for
March* — column C was February, which was March's prior month. A hardcoded column
doesn't move when the tab moves. This is exactly the redesign gap the brief
warned about: "Any cell still showing a hardcoded number hasn't been converted —
fix it, don't patch it." These don't throw an error and don't cascade into
Closing MRR, which is what makes them dangerous: they quietly show a
plausible-but-wrong delta. Convert both to the dynamic prior-month pattern, then
re-run your "set the config back to March, everything reconciles" test and watch
C30 and C36 specifically.

### A2 — New-customer count in the commentary: it should be 2
Your data says **2** (Actuals `New Customers` = 2; "New customers acquired" = 2).
The commentary says two different wrong things:
- A63: "...only bringing in **1**..."
- A65: "...acquiring **3 new customers**."

The "3" came straight off the buggy C30 delta — you read +3 from the tab and
wrote it into the story. Fix C30 first, then set both sentences to **2**. This is
the lesson behind A1: a wrong number on the tab doesn't stay on the tab, it ends
up in what you tell David.

### A3 — Move the deferred-revenue sentence off the April commentary
A64 ends with the January deferred-revenue line ($64,740.50, SUB002/SUB054).
That's correct content — and you already state it properly on the Billing
Reconciliation tab (A42, see below). But it has no business in the April close
narrative; it breaks an otherwise clean churn paragraph, and the as-of-January
framing is out of place in an April story. Delete it from the April A vs F
commentary and keep the one on the reconciliation tab.

### A4 — Notes still only partly updated
Only `my_notes/sql_queries.md` changed. The brief asks for two more, and you
clearly know both cold — get them written down:
- `kpi_definitions.md` — revenue churn vs logo churn, and how each affects the
  active-customer count and the retention read.
- `excel_techniques.md` — the four-step close in practice (one Actuals column +
  two config cells).

---

## B — Billing Reconciliation: still open from last review

You haven't come back to this tab yet. From the prior review, these still stand:

### B1 — February Total Invoiced still adds the credit note back
`C3 = SUM(billing_feb_2026!P2:P49) + 169.71`. The Feb billing file already sums to
**$113,974.29** with the −$169.71 SUB050 credit note in it. Adding $169.71 back to
report $114,144 contradicts both the billing file and your own Part 6 note ("Total
billed will also be reduced"). Leave the credit note *in* Total Invoiced
(= $113,974.29) and drop the add-back; then Bridge 2 needs only the +$675 SUB028
line.

### B2 — The annual-MRR line is still hardcoded
`B13`/`C13` type seats and prices as literals
(`-(31*180) + -(36*150) + …`). The values are right, but it's the same trap as a
stale comparison cell — the day a seat count changes, this silently goes wrong and
no one notices. Reference the subscription cells so the line recomputes itself.

### B3 — Credit: deferred revenue is now stated
You did quantify the deferred-revenue balance on the recon tab (A42:
**$64,740.50 at January 31**, the two Pacific Analytics annuals). That closes the
old open item — just remove the duplicate from the April commentary (A3 above).

---

## What's good (this pass)

| | |
|---|---|
| Active Subscriptions corrected to 55; MoM change reads +1 | ✅ |
| April waterfall rows in — all 7 movements, `Apr-26` label, favorable churn sign | ✅ |
| OpEx sourced from Lisa's numbers; cost commentary rewritten to "OpEx $1k over plan" | ✅ |
| Retention wording fixed — revenue churn lowers NRR/GRR, logo retained | ✅ |
| Closing MRR = $156,830.50; Opening derives from March | ✅ |
| GRR/NRR dynamic, no hardcoded column letters; NRR 99.6% (just under 100%) | ✅ |
| Engine / Waterfall / Retention formula updates resolve clean — zero errors | ✅ |
| Churn correctly identified as revenue, not logo (hard gate) | ✅ |
| Deferred-revenue balance now quantified on the recon tab | ✅ |

---

**Bottom line:** Fix C30 and C36, set the new-customer count to 2, move the
deferred-revenue sentence off the April tab, and finish the two notes files —
then the April close is done. The reconciliation tab (B1/B2) is the remaining real
work and is still where it was last review. Push to the same branch when done.

*(Minor: stray duplicate workbook at repo root differs from the `submissions/excel/`
copy — remove the root one so there's no ambiguity about which file is graded. Tab
name `Apr 2026 A vs F ` carries a trailing space; KPI Tracker April header is a raw
date serial rather than the "Apr 2026" text label — both cosmetic.)*
