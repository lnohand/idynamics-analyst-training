# SQL 08 — Can You Show Me April Again? — Feedback
**PR #29 · Accepted and merged**

---

## What you got right

- **Step 1:** April re-run is right: $156,815.50 · 55 · 44.
- **Step 3:** you found both seat changes and the amounts: −$440 + $425 = −$15, exactly the
  Step 2 gap.
- **Step 5:** your May list is correct. I checked it row by row against our copy: 56 rows,
  $160,075.50, 45 customers, ordered by `subscription_id`, active decided by dates. Your check
  workbook adds the file up and shows 0 on all three lines. That's the main deliverable of this
  assignment, and it's right.

## Where the files go — my instructions were unclear

The brief gave you two folders: one on your computer and a copy in the repo. That was confusing,
and you can't be faulted for it. Here's what I want from now on: **one folder per month, in the
repo**, at `closes/<YYYY-MM>/`. No separate copy on your computer. In a finance team it would be
a shared drive; here the repo is our shared drive. Step files still go in `submissions/sql/`.

I've moved May's files for you:
- `closes/2026-05/month_end_list.sql`, `subscriptions_2026-05-31.csv`, `check_2026-05-31.xlsx`
- `submissions/sql/08_sql_show_me_april.sql`

Run `git pull` on `main` and you'll see them there. You can delete the `iDynamics Close` folder
on your computer.

## Be more careful next time

None of these changed a number, but each one is something a reviewer would send back.

1. **Answer every part of the step.** Step 2 asked for the difference on each line (your number −
   reported); you wrote "They do not match". Step 3 asked for a query listing every May change,
   and a comment on each one saying whether it moves April. Neither is in the file.
2. **Say the same thing in both places.** Your SQL file says April's list "is in the Engine tab".
   Your PR says you only have May's list because April's was never saved. That's the right answer:
   the Engine is a log of changes, not April's list. When the file and the PR answer the same
   question differently, a reviewer can't tell which one you mean.
3. **Use the precise words.** Step 4: the seat changes didn't change a "billing status". They
   changed `seats`, and that's why MRR moved.

## Step 6 — why you don't re-run the query

You got most of the way: the saved CSV is what you send Sarah. Here's the piece that makes it
the *only* right answer, not just the convenient one.

You already proved it in Steps 1–3. You re-ran April's query and got $156,815.50, not the
$156,830.50 we reported. Nothing was wrong with your query. The `subscriptions` table holds
each subscription as it is **today**. When Toronto Media Group dropped 4 seats in May, their
row was overwritten. The 23-seat version that produced April's number is no longer in the
`subscriptions` table. Only the change log still remembers it.

May will go the same way. Between now and December, customers will add and drop seats, and
prices and discounts will change. Every one of those overwrites a row. Run May's query in
December and you get "May, as the table looks in December": a number that doesn't match what we
reported. You could dig through the change log to explain the gap, as you did for April, but
that's detective work every time someone asks.

The counts hold up better. They come from start and cancellation dates, which don't get
overwritten. That's why April's 55 and 44 still matched in Step 2. MRR doesn't hold up.

So the CSV you saved isn't a shortcut. It's the only copy of May as we reported it. Finance
teams call this **freezing the month**: at month-end you save the list, everyone agrees it's
the record, and from then on every question about May is answered from that file, never from a
re-run. It's also why you couldn't find April's list in Step 3: nobody froze April.

How you'd say it in an interview:

> "I'd send her the list we saved at month-end. Re-running would give a different MRR, because
> the table only keeps today's version of each subscription. Seat, price and discount changes
> overwrite the history. We saw it with April: the re-run came out $15 off."

— David
