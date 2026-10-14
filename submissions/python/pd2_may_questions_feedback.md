# PD2 — On your own: James's May questions: Feedback

**Status:** Approved ✅
**Reviewed by:** David Chen

Michael, every figure is right, and this time you wrote the whole script yourself from a blank
file. I ran `pd2_may_questions.py` on the May list: 56 subscriptions and 160,075.50; the same 6
subscriptions under 1,000 (4,040.00, 2.5% of MRR); seats by plan in the right order with 1,398 in
total; and the same 6 customers at 8,000+ (55,375.00, 34.6%). Nothing to fix.

## How I know it's your code doing the work

In a copy of the May list I added 1 to SUB017 and 1 to SUB025, then ran your script again. Total
MRR went to 160,077.50, the small-subscriptions MRR to 4,041.00, and CUST025 to 10,801.0. The
numbers come from the file.

## Step 2: you don't need `groupby` here

Your Step 2 works, but it takes a detour:

```python
grouped = may.groupby(["subscription_id", "customer_id", "plan_name"], as_index=False)["mrr"].sum()
small = grouped[grouped["mrr"] < 1000]
```

Every subscription is already one row in the May list, so grouping by `subscription_id` gives
back the same 56 rows you started with. James asked about subscriptions, so filter the list
directly:

```python
small = may[may["mrr"] < 1000]
```

Same 6 rows. Here's the rule to take into PD3:

- **Filter** when the question is about the rows you already have ("which subscriptions…").
- **Group** only when rows need adding up first ("seats per plan", "MRR per customer"). That's
  your Steps 3 and 4, and you did both of them right, including grouping before filtering in Step 4.

You said Step 2 is where you got stuck. This is probably why: it looked like a groupby question,
and it isn't one.

## "How do I know each answer is right?"

That section is missing from your PR. Here are the checks I'd have written, one per step. Each
one compares against something you didn't calculate in that step:

1. 56 and 160,075.50 are the May close figures.
2. Every `mrr` in the list is under 1,000, and they go up from top to bottom.
3. The seat total equals `may["seats"].sum()` from the whole list: 1,398.
4. Every customer total is 8,000 or more, and CUST025's 10,800 equals its two subscriptions added up.

From PD3 on, every step ends with a "Check it worked" line. Run that check each time before you
move on.

## One question

Right idea. Back it with the rows, because that's what makes the answer checkable:
*"CUST025 has two subscriptions in May, SUB025 at 6,840 and SUB048 at 3,960. Neither is above
7,000, but together they make 10,800. Customer MRR is the sum of the customer's subscriptions,
which is why Step 4 groups by customer before filtering."*

## Small thing: number formats

The brief's summary lines have formats: share as `2.5%` (`:.1f` then `%`), MRR with commas
(`:,.2f`). Not marked down, just worth matching next time. One tip of my own: seats are a count,
not money, so `1,398` (`:,`) reads better than `1,398.00`.

Taking longer than you expected is normal for the first blank-file assignment. Going back to
PD1b to work it out is exactly the right move. Next up is PD3: comparing two months with
`pd.merge`.

— David
