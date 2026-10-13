# PD1 — Meet pandas: Feedback

**Status:** Merged ✅
**Reviewed by:** David Chen

Michael, this one's done. Nothing to fix. I pulled your branch and ran
`pd1_june_list.py` on the June list, and every figure matches mine: 57 subscriptions,
162,830.50 total, 8 subscriptions at 5,000+ (29.6% of MRR), Annual 7 / 36,755.50,
Monthly 50 / 126,075.00, all six plans, and all 8 customers with 50+ seats.

## How I know it's your code doing the work

I added 1 to SUB002's MRR in a copy of the file and ran your script again. The total
went to **162,831.50** and Annual went to **36,756.50**. So the numbers come from the file,
not from something you typed in. That's the check that matters.

## Step 5: the one with no code

You grouped first, then filtered, then sorted. That's the right order, and your answer
says why: 50 seats is a per-customer question, and no single subscription has 50 seats
(the largest has 45). If you filter first, you get nothing back. You worked out
yourself that the filter goes on `by_seats` and not on `june`, and that's the main
thing to take away from this assignment: **filtering works on any DataFrame, including
one you just built with groupby.**

## Your answers

1. **July:** right. Change the file name and you're done. Renaming `june` to `month` is
   a nice touch, so the script doesn't read as June-only.
2. **Why pandas over Excel:** speed is part of it. The bigger part is this: the frozen
   list is never edited by hand, and anyone who runs the script gets the same numbers.
   Here's a model answer:
   *"The same questions come up every month, so I re-run one script instead of redoing
   filters and pivots by hand. The frozen file is never touched, and anyone who runs it
   gets the same numbers, so the work is reproducible."*
3. **Group before filter:** exactly right.

Thanks for the honest "how it went". Having to review the basics before starting is
useful for me to know. The next one uses exactly these tools, so the review you did
pays off right away.

— David
