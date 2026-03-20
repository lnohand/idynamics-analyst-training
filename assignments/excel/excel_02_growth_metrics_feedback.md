# Excel 02 — Growth Metrics Feedback
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** RE: Growth tab — review notes
>
> This is good work. The numbers are right, the layout is clean, and
> the written summary reads like something I could paste into a board
> memo. Two numbers in your paragraphs are wrong — I need those fixed
> before I use this. Everything else is solid.

---

## Result: Pass ✅ — two corrections required in written summary

---

## Section 1 — MRR & ARR: Perfect

All six self-checks pass:

| Check | Your Value | Expected | Status |
|---|---|---|---|
| Closing MRR, 2024-01 | $5,800.00 | $5,800.00 | ✅ |
| Closing MRR, 2026-02 | $152,034.50 | $152,034.50 | ✅ |
| ARR, 2025-06 | $1,825,374 | $1,825,374 | ✅ |
| ARR, 2026-02 | $1,824,414 | $1,824,414 | ✅ |
| Net New MRR, 2025-08 | −$2,430.00 | −$2,430.00 | ✅ |
| Cumulative Net New, 2026-02 | $152,034.50 | $152,034.50 | ✅ |

Formula structure is clean. Closing MRR links directly to the
Waterfall tab (`=Waterfall!H3`), ARR is `=B5*12`, cumulative uses
a proper running sum (`=B8+C7`). No hardcoded values anywhere.

---

## Section 2 — Growth Rates: Perfect

| Check | Your Value | Expected | Status |
|---|---|---|---|
| MoM 2024-01 | blank | blank | ✅ |
| MoM 2024-02 | 148.5% | 148.5% | ✅ |
| MoM 2025-07 | −0.7% | −0.7% | ✅ |
| MoM 2026-02 | −0.4% | −0.4% | ✅ |
| YoY 2024-12 | blank | blank | ✅ |
| YoY 2025-06 | 322.7% | 322.7% | ✅ |
| YoY 2026-02 | 40.6% | 40.6% | ✅ |
| CMGR 6-month, 2024-07 | 40.9% | 40.9% | ✅ |
| CMGR 6-month, 2025-06 | 8.9% | 8.9% | ✅ |
| CMGR 6-month, 2025-12 | −0.1% | −0.1% | ✅ |
| CMGR 6-month, 2026-02 | 0.4% | 0.4% | ✅ |
| CMGR 12-month, 2025-01 | 26.9% | 26.9% | ✅ |
| CMGR 12-month, 2025-12 | 4.3% | 4.3% | ✅ |
| CMGR 12-month, 2026-02 | 2.9% | 2.9% | ✅ |

YoY correctly starts at 2025-01, CMGR 6-month starts at 2024-07,
CMGR 12-month starts at 2025-01. Earlier months are blank, not zero.
IFERROR wraps everything cleanly — no `#DIV/0!` visible anywhere.

The CMGR formula is correct: `=(H5/B5)^(1/6)-1`. Cell references
shift properly across all 26 columns.

---

## Section 3 — Growth Quality: Perfect

| Check | Your Value | Expected | Status |
|---|---|---|---|
| Quick Ratio, 2024-08 | 3.6 | 3.6 | ✅ |
| Quick Ratio, 2025-05 | 5.2 | 5.2 | ✅ |
| Quick Ratio, 2025-07 | 0.4 | 0.4 | ✅ |
| Quick Ratio, 2025-08 | 0.5 | 0.5 | ✅ |
| Quick Ratio, 2025-12 | 0.3 | 0.3 | ✅ |
| New as % of gains, 2025-06 | 84% | 84% | ✅ |
| Expansion as % of gains, 2025-08 | 100% | 100% | ✅ |

Gains and Losses formulas correctly pull New + Expansion and
ABS(Contraction) + ABS(Churned) from the Waterfall tab.

Quick Ratio formula handles edge cases well: `=IFERROR(B19/B20,"∞")`
returns "∞" when losses are zero and gains are positive. When both
gains and losses are zero (like Feb 2026 where losses = $594 but
gains = $0), the formula returns 0 — which is correct. A month with
zero gains and positive losses has a Quick Ratio of 0, not ∞.

Composition rows correctly show blank (via IFERROR) in months with
zero gains. Good — `0/0` is undefined, not 0%.

---

## Formatting: Hits every requirement

| Item | Status |
|---|---|
| Section headers: bold white on dark blue | ✅ |
| CMGR rows: light yellow highlight | ✅ |
| Percentages: 1 decimal place | ✅ |
| ARR: no decimals | ✅ |
| MRR: 2 decimal places, accounting format | ✅ |
| Quick Ratio: 1 decimal place | ✅ |
| Negatives: red parentheses via number format | ✅ |
| No `#DIV/0!` or `#VALUE!` errors | ✅ |
| Freeze panes at A5 | ✅ |
| Conditional formatting on QR row (4 tiers) | ✅ |
| Benchmarks added to Ref tab | ✅ |

[Note] You applied the negative-in-red-parentheses number format
here from the start — you learned from the Assignment 01 feedback
about not using manual font coloring. That's the behavior I want to
see. Learn it once, apply it everywhere.

---

## Section 4 — Written Summary: Strong, Two Fixes Required

The writing is genuinely good. You structured a narrative — early
explosion, plateau, crisis, stagnation — and backed every claim with
a specific number from your spreadsheet. The H2 2025 diagnosis
("new logo acquisition has essentially stopped") is the right
conclusion. The board takeaway ("ARR has stalled at ~$1.82M and the
growth engine that built it has gone quiet") is exactly the kind of
sentence that belongs on a slide.

Two factual errors need correction:

### [Must fix] Paragraph 1 — Wrong CMGR month

You wrote:

> "the 6-month CMGR collapsed from **10.6% in Jun 2025** to 0.4%
> by Feb 2026"

The CMGR (6-month) for June 2025 is **8.9%**, not 10.6%. You cited
May 2025's value (10.6%) and labeled it as June. Check cell S14
(Jun 2025) vs. R14 (May 2025) in your own tab.

The fix: change "10.6% in Jun 2025" to either "8.9% in Jun 2025" or
"10.6% in May 2025" — pick whichever reads better in the sentence.
The story doesn't change, but the number has to match the month.

### [Must fix] Paragraph 2 — Contradicts your own data

You wrote:

> "Quick Ratio swung from 15.2x (Sep) to 0.0x (Nov), back to ∞ in
> Jan 2026 (**zero losses but also zero gains**)"

Your spreadsheet shows Jan 2026 had **$1,710 in New MRR** and $0 in
losses. That's why the Quick Ratio is ∞ — there were gains with zero
losses, which is the definition of infinite efficiency. "Zero gains"
is wrong. You contradicted cell Z19 in your own tab.

The fix: change "zero losses but also zero gains" to "gains of
$1,710 against zero losses" or simply remove the parenthetical.

### [Note] Paragraph 3 — Minor count

You wrote expansion "appeared in only 10 of 26 months." Counting
months where Expansion MRR > $0 in your data, I get 9. The
difference doesn't change your argument — expansion is sporadic
either way — but precision matters when you're putting numbers in
front of a board.

---

## What I Liked

Three things stood out:

**1. You used CMGR, not MoM, to tell the story.** Your paragraph
doesn't say "growth was 17% in March and 5% in April." It says
"the 6-month CMGR collapsed from X to Y." That's the right instinct.
MoM is noise. CMGR is signal. Board members and investors think in
compounding rates, not monthly snapshots.

**2. You diagnosed the root cause, not just the symptom.** You
didn't stop at "growth slowed down." You traced it to the specific
mechanism: new logo acquisition stopped, expansion alone can't
compensate, and the business is coasting on its installed base. That's
analysis, not reporting.

**3. You gave a forward-looking takeaway.** "Until new logo MRR
returns to the $5K–$10K/month range, the business is coasting and
vulnerable to any churn spike." That's actionable. A board member
reads that and knows what question to ask next: "What's the plan to
restart acquisition?"

---

## What to Fix

1. **Paragraph 1:** Change the CMGR figure — 8.9% for Jun 2025,
   not 10.6%
2. **Paragraph 2:** Jan 2026 had $1,710 in gains, not zero
3. **Paragraph 3:** Expansion appeared in 9 months, not 10

After these three edits, push an updated commit. No other changes
needed — the formulas and formatting are clean.

---

## Assignment 01 Cleanup — Still Pending

The Engine tab still uses `$M:$M` and `$P:$P` for the plan change
XLOOKUP instead of the Ref table. The formula structure (duplicated
IFS blocks for Monthly/Annual) is also unchanged. I told you to
skip these for the board deadline and that was the right call. But
circle back to them after the board call — the five items from the
Assignment 01 feedback still apply.

---

*Excel 02 Growth Metrics Feedback | Idynamics Finance Analyst Training*
*March 2026*
