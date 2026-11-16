# PD6b — Who moved in June?: Feedback

**Status:** Pass on the analysis. One fix before I merge: commit the CSV.
**Reviewed by:** David Chen

Michael, I rebuilt the June bridge from the three close files on my own and checked it against your
output. **Every number you printed is right.**

---

## What you did well

- **Step 1.** May is 160,075.5, June is 162,830.5, and the total change is **2,755** across 46 customers. You grouped
  on `customer_id`, used `how="outer"` and filled the blanks with zero. That's all from memory, and all correct.
- **New and churn are the right way round.** CUST048 shows `right_only` with May MRR at 0, so
  it's new. CUST028 shows `left_only` with June at 0, so it's churn. That's the direction Check 3 is
  about, and you have it right. (Next time, print the two tables in Step 2 like the check says.)
- **The signs.** You used `> 0` for "went up" and `< 0` for "went down", and only on customers in both
  months. That gives five movers: 1 new, 2 expansion, 1 contraction, 1 churn. The total still comes to 2,755.
- **Step 3.** You labelled each table first and stacked them after, which is the order the lesson was about.
- **Your finding is real.** SaaS is our biggest industry (8 customers), and it's the only one that went
  backwards in June, at −855. Two lines of that were already in the tables, but the third line, "look into
  SaaS", is a recommendation, and that's the part I asked for.

**Your Step 3 question, "how did you want me to do this?":** the lesson used `new["movement"] = "New"`.
Your `new = new.assign(movement="New")` does the same thing, and it's a perfectly good way to do it.
Looking it up and finding `.assign` was the right thing to do. Keep it.

---

## The fix: commit the CSV, five columns

Your branch has only the `.py` file. That's probably not your fault: the repo's `.gitignore` skips
every `.csv`, so git quietly left it out. The brief asks for `pd6_june_movers.csv` too, so the board has a
file to open.

When you add it, change one line first, the `to_csv` in Step 4. Right now it saves the whole merged
table, which includes `mrr_may`, `mrr_june`, `city`, `region` and `_merge`. Save just the board's five columns:

```python
pizdi[["customer_id", "company_name", "industry", "movement", "change"]].to_csv(...)
```

Then add it with `-f` (force), because a plain `git add` will refuse an ignored file:

```
git add -f submissions/python/pd6_june_movers.csv
```

Commit, push, and I'll merge.

---

## Two things for next time (nothing to change now)

**1. Step 4 merge: say `how="left"`.** You left `how=` out, so pandas ran an **inner** merge.
It came out right only because all five movers are in the customer file. If one ever isn't, an inner
merge drops that customer without telling you, and the board's list is short. The brief's line
"your movers list is the one that must survive intact" means start from movers and keep all of
it, which is `how="left"`.

**2. Print the checks, not just the answers.** These were missing:

- **Step 2:** the zero-change count. It's 41.
- **Step 4:** the row count and "Not found: 0".
- **Step 5:** the Total line.

- **Step 1b:** each month's total before the groupby, next to its total after. That's the check that
  catches grouping on the wrong column.

The answers were right this
time, and the checks are how you'll know when they aren't.

---

## Smaller things

- **The PR description:** the `[paste the whole thing…]` placeholder is still there, and your output
  sits under it instead of inside the code block.
- **Variable names:** `nahoy` and `pizdi`. This repo is a work sample, and anyone reviewing your code
  can look those up. Use names that say what's in the table, like `both_months`
  and `movers_named`. They're easier to follow, and when you come back in a month you'll know what each one held.
- **`_merge`:** your answer explains the error correctly. The fix that goes with it is to drop the column
  once you're finished with it: `.drop(columns="_merge")`.

2.5 hours against my 90 minutes, from memory, is a fair trade. The rebuild was the point, and you did it.
