# PD1b — Read a pandas line: Feedback

**Status:** Approved ✅
**Reviewed by:** David Chen

Michael, nothing to fix on this one. I pulled your branch and ran `pd1b_read_pandas.py` on
the June list. Every line of output matches mine: 50 monthly subscriptions (steps and one
line agree), 4 plans at 30,000+ (Analytics Enterprise, Marketing Pro, Platform Suite,
Sales Hub), and the fixed lines print 57 and 162,830.50.

## How I know it's your code doing the work

In a copy of the file I switched one Annual subscription to Monthly and added 1 to its MRR,
then ran your script again. Monthly went to **51** in both the step version and the
one-line version, and the total went to **162,831.50**. The numbers come from the file.

## Step 3: the two errors

You found both and fixed them in the right order. One thing for next time: the brief
asked for the error's **last line**, and you described the bug in your own words instead. The message is
worth keeping because it tells you which bracket to use before you even look at the code:

1. `TypeError: 'builtin_function_or_method' object is not subscriptable` → you need `( )`
2. `TypeError: 'DataFrame' object is not callable` → you need `[ ]`

"not callable" means use `[ ]`; "not subscriptable" means use `( )`.

Your own descriptions were right. To make them stronger, name the error and then the fix in
one line: *"`len[june]` → 'not subscriptable': len is an action, so it needs `( )`: `len(june)`."*

## Step 4: the four readings

You said your writing is probably meh. It's better than that: 1, 3 and 4 are right, and
2 has one slip. Below is each of your sentences next to a model one, with the one thing
to change. Nothing to rewrite. Use these as the pattern next time.

**The pattern:** name what you're creating, then read the right side in the order pandas
does it, one short phrase per bracket or dot: *"X is: from june, keep… / group… / pick…
/ add up…"*. Then, if it helps, one plain sentence saying what it means for the business.

**1.** `annual = june[june["billing_cycle"] == "Annual"]`
- Yours: *"…sets the annual variable as the values in the June dataframe that have a billing cycle of annual."*
- Model: *"annual is: from june, keep the rows where june's billing_cycle is "Annual"."*
- Improve: say **rows**, not "values". The True/False inside `[ ]` keeps whole rows,
  and naming that is the point of the exercise.

**2.** `share = big["mrr"].sum() / june["mrr"].sum() * 100`
- Yours: *"…the sum of the biggest mrr's in the june dataframe divided by the sum of all the biggest mrr's in the june dataframe multiplied by 100."*
- Model: *"share is: pick big's mrr and add it up, divide by june's mrr added up, times 100,
  so it's the percentage of June's MRR that comes from the big subscriptions."*
- Improve: the bottom half is `june["mrr"].sum()`, which is **all** of June's MRR, not the big ones
  again. Read each name exactly as written (`big` on top, `june` underneath). When you're
  not sure what a piece is, print it on its own, as in Example 2. Here that's 48,150.00 on top,
  162,830.50 underneath, and 29.6%, the same share as in PD1.

**3.** `by_seats = june.groupby("customer_id", as_index=False)["seats"].sum()`
- Yours: *"…sets by_seats to be the total seats of each customer_id in the june dataframe."*
- Model: *"by_seats is: group june by customer_id, pick seats, add them up in each group, so one row per customer with their total seats."*
- Improve: yours gives the result correctly. Add the steps (group → pick → add up) so the
  sentence follows the line left to right. That's what lets you spot the wrong step when
  a line breaks.

**4.** `print(f"Total MRR: {june['mrr'].sum():,.2f}")`
- Yours: *"…prints the total mrr of the june dataframe and has a 2 decimal format with commas."*
- Model: *"print the text "Total MRR: " and, in the { } slot, june's mrr added up, with commas and 2 decimals."*
- Improve: just mention the text label `Total MRR: ` that prints first. Otherwise this is right.

**Shorter is fine.** "This line sets the X variable as" can just be "X is:". That saves
words and puts the name up front.

## "Too easy"

Thanks, that's good to hear. PD2 has no blanks at all: you get James's four questions and
a blank file, and you write the whole script yourself. Go ahead.

— David
