# Checkpoint Quiz 1 — Feedback

**Reviewed by:** David Chen — I ran all of it (Python + every SQL query against the database).

Michael — thanks for the honest notes on the PR. That kind of self-read is exactly what this
checkpoint is for. Here's where you landed, the six things to redo, and a real answer to your
C5 question.

## Headline
The checkpoint did its job — it found the soft spots before we start PY03. **Five landed clean**
(A2, B2, C1, C2, C3), **one concept landed but needs finishing** (A3), and **six need a redo**
(A1, A4, B1, B3, C4, C5). Do those six again on this same branch, paste the new output in the PR,
and we're clear for PY03. Nothing new here — just tightening what's already most of the way there.

## What landed — keep it
- **A2** — count = `4`. Correct, and you used `>=` so Ironwood ($50,000) is correctly counted.
- **A3 — the big one: your parameter concept stuck.** `total_value(SMALL)` → `3000`, not `441500`.
  That's the exact thing that kept biting you in PF4, and it's fixed. Two small finishes below.
- **B2** — sorted table, no index column. Clean.
- **C1 / C2 / C3** — 22 customers / 26·23·6 / **$120,075.00**. C2 especially: you reached for the
  JOIN because `region` lives on `customers`, not `subscriptions`. Exactly right instinct.

## Six to redo (same branch)

**A1 — read the prompt once more.** It asks for three specific prints — the tier of `156000`,
then `50000`, then `47500` — and then **one** `True`/`False` using `and` for whether `61000` is in
the Mid-Market band (`>= 50000 and < 100000`). You looped all nine deals and skipped the band line
entirely. Print the three named amounts, then the one `and` check. (Small: `Enterprise` should be
`>= 100000`, not `>`.)

**A3 — finish it (two small things).** The engine is right. (1) The function should **`return`** the
total, not `print` it inside — you'll want the value *back*, for exactly the reason A4 shows.
(2) Format the print with `$` and commas: `print(f"${total_value(DEALS):,}")` → `$441,500`.

**A4 — return, and watch which variable you print.** Your loop finds `biggest` correctly. But the
print line uses `deal`, not `biggest` — and after a `for deal in deals:` loop ends, `deal` holds the
**last** item it saw (Ironwood, $50,000), which is why you got "Largest: Ironwood Labs." Print
`biggest`. Bigger picture: the brief asks you to **`return`** the deal from the function and build
the line *outside* it, reusing the returned dict — that's the half that hasn't landed yet, same
lesson as A3's return.

**B1 — you skipped the unsorted print.** You sort before the first print, so only the sorted table
shows. B1 wants the table as built (no sort); *then* B2 sorts it. Print the DataFrame once before
you sort.

**B3 — build a list of row-dicts, then a DataFrame.** Right now you loop `.items()` and print
strings — there's no DataFrame at all. Look back at your PY02-a work: start an empty list, append one
`{"Index": name, "Last": last}` dict per pass, then `pd.DataFrame(that_list)` and print with
`index=False`. The classic slip is building one dict instead of a list of them. This is the drilling
you asked for — you're right that it's the weak spot, and it's very learnable.

**C4 — group by the right thing.** This asks for *plans* with more than 9 active subs. Your query is
C2 copy-pasted — it groups by `c.region`, so you got regions back. Group by (and select)
`plan_name`, drop the customers join (`plan_name` is on `subscriptions`), keep the `HAVING`. You
should get **3 plans**.

**C5 — your question, answered.** You asked whether your original instinct — put the status
condition in the `ON`, not the `WHERE` — was right. **Half right, and it's worth getting fully.**
- The question is "customers with **no active** subscription." That's a *find-the-absence* problem:
  LEFT JOIN every customer to their subscriptions, then keep only the customers where **no active**
  match was found.
- The shape:
  ```sql
  SELECT c.company_name
  FROM customers c
  LEFT JOIN subscriptions s
         ON c.customer_id = s.customer_id AND s.status = 'active'
  WHERE s.subscription_id IS NULL;
  ```
- Your instinct that the status condition belongs in **`ON`** is exactly right — and here's *why* it
  matters: if you put `AND s.status = 'active'` in the **`WHERE`** instead, it throws away the NULL
  rows *before* the `IS NULL` test can catch them, and your LEFT JOIN silently collapses to an INNER
  JOIN → **0 rows**. In `ON`, the non-matching customers survive with NULLs, and `IS NULL` keeps
  exactly the ones you want. (That's the ON-vs-WHERE trap from SQL 06.)
- Two corrections to your version: you filter on **`status = 'active'`** (the thing whose *absence*
  you're looking for), not `'cancelled'`; and you need the `IS NULL` line. `WHERE status = 'cancelled'`
  answers a *different* question — "customers who have a cancelled sub" — which is why you got 12 rows
  instead of 1. The correct answer is a single customer: **Atlantic Media Corp**.

## One honest note
You called SQL "incredibly easy, no more drilling needed" — but C4 and C5 were the two that missed.
Nothing wrong with finding it easy; just leave room for the read-it-twice check, because both misses
were about *what the question asked*, not about SQL mechanics you don't know. The mechanics are there.

Redo the six on this branch, paste the new output in the PR description, and we're set for PY03.

— David
