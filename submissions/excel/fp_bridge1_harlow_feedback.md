# FP Bridge 1 — Harlow Payments: Feedback

**Status:** Pass. Two things to fix in your head, not in the file.
**Reviewed by:** David Chen
**Submitted:** 2026-11-12 by email, `Harlow_Michael.xlsx`

Michael — I recalculated your whole workbook independently rather than reading the numbers you'd
saved, and **every single figure matched: 25 out of 25.** Summary, the bridge, the underlying block.
The residual is zero because you computed it, not because you typed it.

**This is your strongest submission so far**, and the reason isn't the arithmetic. It's that the
three places where this case is designed to catch people, it didn't catch you.

---

## What you did well

**You fixed the F/U convention, and you fixed it in the hard place.**

You filled the cost logic down `F8:F13` — fine. But you then *overrode* it on both derived rows:
`F7` (gross profit) reads `IF(C7>B7,"F","U")` and `F13` (EBITDA) reads `IF(C13<B13,"U","F")`. Those
are the two rows where the rule inverts, and they're the exact thing you had backwards in your May
workbook. You didn't just get it right; you noticed that two rows needed a different rule from the
nine around them.

**The revenue effect used the budget margin.** `=(Summary!C5-Summary!B5)*Summary!B15`. `B15` is the
*budget* gross margin. Reaching for the actual margin there is the single most common way this
bridge goes wrong — it double-counts, because the margin change is the next row's job. You went to
the right cell.

**The margin effect as the residual.** `=Summary!D7-Bridge!B6` — the gross profit gap less the
revenue effect. That's the method, and it's why your bridge closes.

**The residual is a real formula.** `=B12-Summary!C13`. Forcing that cell to zero with a plug is an
automatic fail on this step and it's a thing people do. You subtracted your total from the Summary
figure and let it tell you the truth.

**Step 3 — you took out the settlement and nothing else.** "The only thing that needs to be removed
is the lawsuit settlement because it is a one time fee. The remainder of the revenues and expenses
are repeats." That is the correct answer and the discipline the step exists to test. Adjusting the
marketing or the salaries is the error I was watching for.

**And one I want to single out.** In bullet 3 you wrote that G&A "will remain consistent around 30."
I thought that was wrong when I read it, because the H1 G&A overspend is 52. Then I went and looked:
your monthly G&A runs 31, 30, 78, 32, 31, 30 — about 30 a month every month except March. You weren't
quoting the H1 number at all; you'd gone into the monthly data and read the run rate. Nobody asked
you to do that. **That is the instinct this whole programme is trying to build**, and it's the thing
I'd want you to talk about in an interview.

Your bullet 6 is the other one: the monthly revenue gap at −2, −6, −12, −23, −35, −49, exact, with
the right conclusion that the gap is widening rather than levelling off.

---

## Two things to fix

### 1. The 25% question — Software was exactly 25.0%

You answered "Software and General & admin came in at more than 25% over budget."

Software came in at **exactly 25.0%**. 150 against a budget of 120 is 1.25, precisely. Your own
sheet says so — cell `E10` holds 0.25 exactly, not 0.2501. **"More than 25%" excludes it.** The
answer was General & admin alone.

This is the same thing as `>` versus `>=` in the Python work, and it's now happened in both places,
so I'm going to stop calling it carelessness and call it a habit worth building: **when a question
gives you a threshold in words, read the words again before you type the sign.** "More than",
"at least", "under", "or more" — they are four different comparisons and only one of them is yours.

There's a second reason this one matters. The one line that *did* clear the bar is General & admin,
and G&A only clears it **because of the settlement** — the one cost in the whole case that doesn't
repeat. So the honest answer to "which lines are more than 25% over" is "one, and it's the one that
won't happen again." That's a much better sentence for a CFO than a list of two.

### 2. Commentary bullet 2 answered a different question

The prompt was: *your three groups of causes against each other — which is biggest.* Your three
groups are the ones you built in the bridge: revenue effect, margin effect, cost overspend.

You wrote: "The biggest cause is repeats." That's Step 3's axis — what recurs versus what doesn't —
not the three groups.

The answer was **cost overspend: 299.0 of the 443.6 miss, more than revenue (88.9) and margin (55.7)
put together.** You had all three numbers in your own bridge, two rows apart.

I'm not marking this because the number was hard. I'm marking it because **you built the bridge
correctly and then didn't say what it showed.** The bridge exists to produce exactly that sentence.
When you've finished one, the next question is always "so which of these is the big one?" — and the
answer goes in the write-up.

---

## Smaller things

- **Bullet 1 reports −1,529%.** It's arithmetically right and it's meaningless — it's a percentage
  off a budget of 29. Saying "the variance percentage isn't informative at this base" is worth more
  than quoting it. A number that can't be interpreted shouldn't be in a board pack.
- **"Roughly 50% of the OpEx"** in your action. Marketing's 135 is 45% of the *overspend* (299) and
  30% of the total miss (443.6). As written it reads as a share of total opex, which would be 6%.
  Say which denominator you mean — it's the difference between a sharp line and a vague one.
- **Bullet 5 has no numbers in it.** Bullet 4 does, and it's much stronger for it. Headcount closed
  at 50 against a plan of 46. Put the figures in.

---

## Where this leaves you

You've now built an EBITDA bridge that ties, on a case you'd never seen, with the two classic errors
avoided. The technique is yours.

What the two misses have in common is that they're both **the last step** — reading the words of the
question before answering it, and saying what your own analysis showed once you'd done it. The
numbers were never the problem. Worth remembering that the write-up is the part the CFO actually
reads.

You've seen my version of the commentary. Compare bullet 2 against yours specifically.

---

*Harlow was a scaffolded case — every row label and header was given to you. The next one builds on
the same technique with friendlier numbers and a harder question, and after that you get an empty
tab and build the shape yourself.*
