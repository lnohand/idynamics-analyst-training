# PD3 — Where did June's MRR change come from?: Feedback

**Status:** Approved ✅
**Reviewed by:** David Chen

Michael, the bridge is right, and you did it in about an hour without getting stuck. I ran
`pd3_june_movements.py` on the May and June lists. Steps 1–3 give the same numbers as mine: 45
customers each month, the five customers who changed, and New 2,420 · Expansion 1,340 · Contraction
−330 · Churn −675. Your difference is 0.00, so the bridge ties. Nothing to resubmit.

## How I know it's your code doing the work

In a copy of the June list I added 1 to SUB071, then ran your script again. June's total went to
162,831.50, Expansion to 1,341.00, and the difference stayed 0.00. The numbers come from the file,
and your tie-out keeps working when they change.

## Your Step 4 question: what "Rebuilt closing" means

Good question, and you were right to ask. **Rebuilt closing = opening + the four movements.**
It's June's closing MRR built from May's, and it should equal June's actual closing:

```
Opening (May):    160,075.50
Rebuilt closing:  162,830.50     ← 160,075.50 + 2,420 + 1,340 − 330 − 675
Closing (June):   162,830.50
Difference:       0.00
```

The 2,755.00 you printed is the four movements added up. That number has its own name: **net new
MRR**. It's useful too, but it isn't the rebuilt closing. Your `Difference` line already adds the
opening in, which is why it still comes out 0.00.

One small thing on the same step: the brief said to take opening and closing from the original
lists (`may["mrr"].sum()`, `june["mrr"].sum()`), not from `may_cust` and `june_cust`. Here they give
the same totals. The reason is that a check should come from a different source than the thing it
checks. If a groupby ever dropped a row, the original list would still have the true total.

You'll use this exact idea in PD4. There, the `check` column is opening + movements − closing, for
every month at once.

## One question

You found the right customer, pasted the right row and gave the right reason. One correction:
`stayed` is the group of customers who were in both months, not a movement. SUB071's 1,190 shows up
in **Expansion**. Model answer:

*"No. New includes only SUB070 (CUST048, 2,420). SUB071 belongs to CUST040, who already paid 1,710
in May: `CUST040 1710.0 2900.0 both 1190.0`. A second subscription from an existing customer means
they pay us more, so its 1,190 is Expansion, not New."*

## Why pandas?

Right idea. The strongest version is about next month:
*"The merge lines up every ID from both months in one step, so there's no building a combined
list and removing duplicates by hand. Next month I change two file names and rerun it, and the
tie-out tells me straight away whether it's right."*

Next up is PD4: the same bridge for every month from January to June.

— David
