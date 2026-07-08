# Feedback — Billing Reconciliation Warm-Up 2

**Reviewed:** 2026-07-08 · **Submission:** `submissions/excel/excel_billing_recon_warmup2.xlsx` (branch `student/excel_billing_recon_warmup2`)

## Verdict: Pass — the reconciliation is correct and ties honestly. One fix, one process note.

You built this cold and got the hard parts right. All four **Difference (must = 0)** cells tie to zero on real, formula-driven numbers — nothing forced. That's the whole point of a reconciliation, and it's a clear step up from the April close.

## Verified against source data

**Total MRR = 8,100** — 6 monthly (3,900) + 6 annual (4,200), pulled live off `Subscriptions`. ✓

**Bridge 1 — MRR → Invoiced (both months tie):**
- **Jan:** 8,100 + annual billing excess 17,600 (A01+A02 renew in Jan → 11 × (600+1,000)) − annual MRR not billed 2,600 (A03–A06) = **23,100** = Total Invoiced. ✓
- **Feb:** 8,100 + excess 6,050 (A06 renews → 11 × 550) − not-billed 3,650 (A01–A05) = **10,500** = Total Invoiced. ✓
- You tracked the renewal-month shift between January and February correctly — that was the trap the brief flagged ("watch what happens to the annual subs").

**Bridge 2 — Invoiced → Collected (both months tie):**
- **Jan:** 23,100 − 650 (M05 payment failure) = 22,450 collected. ✓
- **Feb:** 10,500 + 650 (M05 January invoice retried/collected in Feb) − 300 (M02 credit note) = 10,850 collected. ✓
- Handling the M05 failed-payment-then-retry **across the month boundary** is the subtle one, and you got it.

Nice: using cell references as the SUMIFS criteria (instead of typing "Annual"/"January") was a deliberate way to honor the no-constants rule. Good instinct.

## Fix this

**`B29` (Feb Bridge 2, "Adjustment: M02") = −300 is a typed constant.** The brief says *no typed constants*, and every other cell in the build is live — this is the one holdout. The M02 credit note isn't a number to type; it's a transaction you can derive: it's simply collected minus invoiced for M02 in February.

> `='Invoice Log'!D13-'Invoice Log'!C13`  → 500 − 800 = −300

Same lesson as the SUB050 pad in the April close: never represent an adjustment as a hardcoded figure when the source rows already imply it. You broke that habit everywhere else here — close it out on this cell too.

## Minor
- **No PR opened.** The brief said to open a PR; you pushed the branch but didn't. Also the branch/filename differ slightly from the brief (`student/excel-recon-warmup2` / `recon_warmup2.xlsx`). Cosmetic, but don't skip the PR step — that's how these get reviewed.
- **`B14`** uses a hardcoded row range `=SUM('Invoice Log'!D4:D11)` while the parallel `B30` uses a dynamic `SUMIF` by month. Both give the right answer, but make them consistent — the `SUMIF` form is the one to keep.

— David
