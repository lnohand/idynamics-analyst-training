# Feedback — SQL 05: Aggregates & HAVING (PR #16)
**Reviewer:** David Chen | **Date:** 2026-07-10 | **Verdict: CHANGES REQUESTED — one query fix + one process fix**

Michael — good set overall. Four of your five queries produce exactly the right
numbers, the joins are clean, and you used HAVING correctly the first time you
ever touched it. And you did the right thing flagging Q2 in the PR instead of
forcing it to look done. Now let's fix what's left.

---

## Q2 — there is no hidden character. Let's walk through what actually happened.

Your query:

```sql
SELECT plan_name,
       seats * price_per_seat * (1 - discount_percent / 100.0) AS monthly_mrr
FROM subscriptions
WHERE status = 'active' AND billing_cycle = 'Monthly'
GROUP BY plan_name, monthly_mrr
ORDER BY monthly_mrr DESC;
```

**First, the disproof.** You suspected an invisible character in the plan names.
You already had the evidence against that: your own Q1 groups the *same*
`plan_name` column and returns 6 clean rows. If "Analytics Enterprise" existed
in several invisible variations, Q1 would have split too. You can also test it
directly: `SELECT DISTINCT plan_name, LENGTH(plan_name) FROM subscriptions;`
— six names, six sane lengths, no ghosts. When a result looks impossible, test
your hypothesis against something you already trust before concluding the data
is haunted.

**Now the real cause.** Reconstruct what happened when you wrote it:

1. You started with `GROUP BY plan_name` and Postgres threw an error —
   something like *"column ... must appear in the GROUP BY clause or be used
   in an aggregate function."* It was pointing at your `seats * price_per_seat
   * ...` expression.
2. You made the error go away by adding `monthly_mrr` to the GROUP BY.
3. The query ran — but it was no longer the query you wanted.

Here's the mental model. **GROUP BY defines the buckets. The aggregate function
(SUM, COUNT, AVG) is what collapses each bucket into one row.** Every column in
your SELECT must be one or the other: either it's part of the bucket definition
(in GROUP BY), or it's collapsed by an aggregate. Your `monthly_mrr` expression
was neither — Postgres had 14 different per-subscription MRR values inside the
"Marketing Pro" bucket and no instruction for how to turn them into one number.
That's what the error was telling you.

There were two ways out of that error, and they mean opposite things:

- **Wrap it in the aggregate** → `SUM(seats * price_per_seat * ...)` —
  "collapse each plan's subscriptions into one total." *(what Q2 wanted)*
- **Add it to GROUP BY** → "make every distinct per-subscription MRR its own
  bucket." That's why you got 42 rows: Analytics Enterprise appears once for
  each distinct subscription MRR value under it (6300, 5580, 4680, 3600 —
  those are individual subscriptions, not plan totals).

The fix — note the only changes are SUM(...) and the GROUP BY list:

```sql
SELECT plan_name,
       SUM(seats * price_per_seat * (1 - discount_percent / 100.0)) AS monthly_mrr
FROM subscriptions
WHERE status = 'active' AND billing_cycle = 'Monthly'
GROUP BY plan_name
ORDER BY monthly_mrr DESC;
```

Self-check: 6 rows, Sales Hub on top at **$30,470.00**, the six values summing
to **$120,075.00** — which plus the $36,755.50 annual book is your own April
closing MRR of $156,830.50.

**Why I'm dwelling on this:** it's the same GROUP BY gap as your refresher Q1/Q3,
from the other direction. There you added GROUP BY where nothing needed
collapsing; here you dodged the aggregate where something did. The rule that
covers both: *GROUP BY only exists to serve an aggregate. No aggregate in the
SELECT → no GROUP BY. Aggregate in the SELECT → GROUP BY lists exactly the
label columns, nothing else.* And one habit: when Postgres gives you that
error, don't reach for whatever edit makes it disappear — the error is telling
you which of the two meanings you have to choose.

---

## Process fix — this PR carries your entire April close. New branch, from main.

Your branch history shows you cut `student/05_sql_aggregates_having` from your
April-close branch, not from main. Look at the "Files changed" tab of this PR:
it's not just your `.sql` file — `excel_14_april_close.xlsx` (twice) and your
April commits are in there too.

**Why that's a problem:** a PR is the *entire difference between your branch
and main*. Anything on your branch that main doesn't have yet rides along —
whether you meant it or not. If I merged this PR, your April workbook would
land on main **bypassing the April review that's still open on PR #14**. Every
branch you cut from an unmerged branch inherits all of its unmerged work, and
the two reviews become tangled: neither PR can be judged, approved, or merged
on its own.

**The rule: one assignment = one branch = one PR, always cut from up-to-date
main.** Fix it like this:

```bash
git checkout main
git pull                      # make sure main is current
git checkout -b submission/sql-05-aggregates
# copy your corrected 05_sql_aggregates_having.sql into submissions/sql/
git add submissions/sql/05_sql_aggregates_having.sql my_notes/sql_queries.md
git commit -m "SQL 05 - aggregates and HAVING"
git push -u origin submission/sql-05-aggregates
```

Open a fresh PR from that branch, then **close this one (#16)** — don't merge
it. Your April work is safe: it still lives on your April branch and PR #14,
where I'll review it separately (I saw your "am I on the right track" commit —
answer coming on that PR, not this one).

---

## The rest — small, fix on the new PR

1. **Q5 — right numbers, wrong column.** You grouped by customer correctly
   (that's the hard part — your top-5 values are exact), but returned
   `customer_id`. The brief asks for `company_name` — that's the *only reason*
   the join to `customers` exists; as written, your join fetches nothing you
   use. Nobody presents CUST018 to a board.
2. **Q4/Q5 — LEFT JOIN vs INNER JOIN.** Brief specified INNER. Your results
   happen to match because every subscription has a customer — and in Q5 your
   `WHERE status = 'active'` quietly turns the LEFT JOIN back into an INNER
   join anyway (NULL rows can't pass a WHERE on the right table's columns).
   Use the join the logic calls for; a LEFT JOIN should mean "I want unmatched
   rows kept."
3. **Column aliases:** Q3 `subscription_count` → brief says `active_subs`;
   Q4 `total_mrr` → `monthly_mrr`. Cosmetic, but specs are specs.
4. **PR description is missing the required pieces:** your actual self-check
   numbers for all five queries, and the two one-liners (when does a query
   need GROUP BY; WHERE vs HAVING). After this Q2 experience you're better
   equipped to answer both than you were yesterday — I want them in your own
   words.
5. **Step 0 — confirm it.** Paste the output of
   `SELECT status, COUNT(*) FROM subscriptions GROUP BY status;` in the new PR.
   It must show exactly two rows: active 55 / cancelled 12.

---

**Summary:** concepts are landing — joins solid, first HAVING correct, customer-
level grouping in Q5 correct. Fix Q2 with the aggregate (not the GROUP BY
dodge), rebuild the submission on a clean branch from main, complete the PR
description, and this merges.
