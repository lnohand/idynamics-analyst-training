# FP Bridge 2 — Westbrook Analytics: Feedback

**Status:** Not a pass yet — two rows of the bridge are wrong, and they are the two that carry the
answer. Nothing to resubmit. The next case uses the same technique and you'll get it right there.
**Reviewed by:** David Chen
**Submitted:** 2026-11-14 by email, `Westbrook_Michael.xlsx`

Michael — I recalculated your workbook independently. **50 of 53 figures match.** I'll start with
what you did well, because two of them are things you got wrong last time.

---

## What you did well

**The 5% question — you got it right.** "COGS and Sales & Marketing came in at more than 5% over
budget." Salaries sits at exactly 5.0%, and you left it out. That is the Harlow miss, fixed. You
read the words.

**You found March on your own, and you found why.** Nobody told you which month. You computed the
six margins, saw 47.1% sitting between 59.1% and 57.0%, went to the invoice detail and found the
data-licence tranche booked twice. Then you took out that one item and nothing else. That is exactly
the job, and "tell me about a time you found an error in the numbers" now has a real answer.

**The Summary is clean.** Every line, every variance, and every F/U flag — including Revenue as F,
G&A as F and Software as "-". Last time "U everywhere" was free. This time it wasn't, and your
formulas got all nine right.

**Underlying EBITDA 267 and the (113) variance are right**, and I like that you linked to the invoice
cell instead of typing 60.

---

## The one that matters — the revenue effect

Your cell `Bridge!B6`:

```
=Summary!C5-Summary!B5*Summary!B15          → 1,400
```

What it needed:

```
=(Summary!C5-Summary!B5)*Summary!B15        → 48
```

**The brackets are missing.** Excel multiplies before it subtracts, so yours calculated
3,380 − (3,300 × 60%) = 1,400. With the brackets it is (3,380 − 3,300) × 60% = 80 × 60% = **48**.

You pointed at the right cells — **budget** margin, `B15`, not actual. Your method is right. You had
these same brackets in place at Harlow. This is a slip, not a gap.

But look at what it did next. The margin effect is "whatever is left", so it swallowed the mistake:

| Row | Yours | Correct |
|---|---|---|
| Revenue effect | 1,400 | **+48** |
| Margin effect | (1,500) | **(148)** |
| Residual | 0 | 0 |

**Your residual was 0 and the bridge was still wrong.** That is worth understanding. When one row is
defined as "the remainder", the bridge always closes — the residual can't see an error in the row
above it. So the residual alone is not enough on this kind of bridge. Two other things catch it:

**1. The size check — ten seconds.** Revenue beat budget by 80. An effect that comes from 80 of
extra revenue cannot be 1,400. At a 60% margin it can be worth at most 48. Whenever a bridge row is
bigger than the thing that moved, stop.

**2. The cross-check from the brief.** Margin effect a second way: actual revenue × (actual margin −
budget margin) = 3,380 × (55.62% − 60.00%) = **(148)**. Against your (1,500), that would have shown
the problem immediately. From now on that check gets its own cell.

**Budget or actual — the rule to say every time you build one of these:**

| Effect | The difference | Multiplied by |
|---|---|---|
| Revenue effect | actual revenue − budget revenue | **BUDGET** margin % |
| Margin effect | actual margin % − budget margin % | **ACTUAL** revenue |

First effect at budget. The next one on actual.

---

## Commentary

You wrote all five bullets and an action, so here is my version beside yours. Nothing to rewrite —
read them side by side.

**Row 2 — which of the three groups is biggest.** You wrote "The only cause is repeats", then named
Sales & marketing and Salaries. This is the same answer as at Harlow, and it is the same miss:
"repeats" is Step 3's question. The three groups are three rows of your own bridge.

> *Model:* Revenue effect +48, margin effect (148), cost overspend (73). **Margin is the whole
> problem.** On its own it is bigger than the other two put together, and revenue was actually
> helping.

Part of why you missed it is that your bridge was showing 1,400 and (1,500), which don't say
anything sensible. That is the real cost of the brackets: not two wrong cells, but a wrong
conclusion built on them. Even with the duplicate invoice taken out, margin is still (88) against
cost at (73).

**Row 1 — the headline.** Your number is right: 207 against 380, short by 173. But you wrote that it
was "due to the 2% decrease in Revenue". Revenue went **up** 2.4% — your own Summary says +80, F,
and your row 5 says revenue overachieved. Check each sentence against your own table before it goes
out. And one idea per bullet: yours has four.

> *Model:* H1 EBITDA was 207 against a budget of 380 — short by 173 — even though revenue beat plan
> by 80.

**Rows 3 and 4 — you found both, and then stopped one step short.** Row 3: margin falling about a
point a month. Row 4: enterprise customers down to 490 against a plan of 725, self-serve up to 520
against a plan of 245. Both correct, and you used the June numbers, which is right. Now put the two
rows next to each other. Why would margin fall every month while revenue grows?

> *Model:* We replaced enterprise customers with self-serve customers. Self-serve earns a much lower
> margin, so revenue beat plan and margin fell at the same time. That is still happening at the end
> of June.

That one sentence answers Daniel's whole question. You had every number for it on the page.

**Row 4 was also 130 words.** The finding is in two of your sentences. A CFO reads the first line.

**Row 5.** Revenue grew 22–25 a month against a plan of 20 — true, with numbers, and a fair
comparison to choose. It would have been the right place for the sentence above.

**The action.** "Be more thorough checking cost of sales" is fine. "Invest more into self-serve" is
the opposite of what your own rows 3 and 4 show: self-serve is the growth that is pulling margin
down.

> *Model:* Find out why enterprise renewals failed in Q1, and set a margin floor on self-serve
> before it grows further. Also fix the March close — a duplicated invoice of 60 got through review.

---

## Smaller things

- **The one-off cell.** The reason went into the amount cell and the amount (60) was never written
  down — not on the sheet and not in your reply, which asked for "the month and the amount".
- **`Data!B54`** — an invoice number on the Data tab got blanked. The Data tab is read-only; worth
  checking you haven't typed into it before you send.
- **Your reply** didn't say how long it took. I use that to set the next one.

---

## Where this leaves you

Finding the error, removing only that, the flags, the threshold — those are the hard parts of this
case and you did all of them. What went wrong is one pair of brackets, and then not asking whether
the number it produced made sense.

So the habit for next time is one question, asked of every row you build: **"is this number a
believable size?"** Then say what the bridge shows — which group is the big one — before you write
anything else.

The next case is the same technique again.
