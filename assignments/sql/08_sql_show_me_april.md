# SQL Assignment 08: Can You Show Me April Again?
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Sarah needs April's list
>
> Sarah is putting together the quarter review and wants to see the subscriptions
> behind April's MRR — the number we reported when we closed April. You built the
> query for exactly this in SQL 07: point it at 30 April and send her the list.
>
> Before you send it, check it against what we reported. She will.
>
> — David

Expect about 2–3 hours.

---

## Before you start — git

SQL 07 is merged, so you're clear to start. Start a new branch `student/sql_08_show_me_april` the way
`docs/git_workflow_reference.md` describes ("Every Time You Start a New
Assignment") — fetch, then **Create new branch from…** → `origin/main`.
Do not start it from your SQL 07 branch. Do all of this assignment on the new branch.

Commit order:
1. the two **closes/2026-05/** files, alone (Step 5)
2. your step file, **submissions/sql/08_sql_show_me_april.sql**

---

## The exercises

Write every step's queries in **one file**, with a comment line above each step
(`-- Step 1`, `-- Step 2`, …), the same way as SQL 07. Every count comes
from a query that counts.

### Step 1 — Run April again

Take your SQL 07 Step 6 query (total MRR, number of subscriptions, number of
different customers) and run it for **30 April 2026** instead of 31 May.

Write the three numbers down.

### Step 2 — Compare with what we reported

April's reported numbers are in your own close: the `Actuals` tab of your May
workbook, **April column** — Closing MRR, Active Subscriptions, Active Customers.
(If you can't open your local copy, the workbook in PR #27 on GitHub has the same
April column.)

Put your three Step 1 numbers next to the three reported ones and write down the
difference for each, as **your Step 1 number − reported number**. Do they match?

April was closed and reported. Nothing about April should have changed.

### Step 3 — Find out why

To find the subscriptions that differ, the obvious move is to compare your Step 1
list with the list behind April's reported number, row by row.

**Where is that list?** Write down your answer before you go on.

Then find the cause another way. Whatever changed, it changed **after** 30 April.
You know a table that records changes to subscriptions, with a date for each.
List every change between 1 May and 31 May 2026.

For **each** change, decide: does it change your Step 1 result for 30 April, or
not? Say why in a comment next to it. (SQL 07 Step 7 will help with one of
them.)

For each change that does, work out by hand how much it moved April's MRR.

**Check your own work:** those amounts must add up **exactly** to your Step 2
differences. If they don't, you've missed something — keep looking.

### Step 4 — Why those, and not the others?

Look again at which of your Step 2 numbers matched and which didn't. In 1–2
sentences in your PR description: why did the changes you found in Step 3 affect
some of the three numbers but not the others?

### Step 5 — Save May's list

May is closed too. Nothing has been loaded into the database since 31 May; June
data goes in after you've done this step.

Write the 31 May list query, one row per subscription active on 31 May, with these
columns in this order, named exactly:

`subscription_id, customer_id, plan_name, billing_cycle, seats, price_per_seat, discount_percent, mrr`

ordered by `subscription_id`. Same rules as SQL 07: active is decided by
dates, MRR rounded to 2 decimals per subscription.

Then save two files into a new **closes/2026-05/** folder at the top level of the
repo, next to `docs/` and `assignments/` (in VS Code: right-click → New Folder):

- the query itself, as **month_end_list.sql**
- its result, exported from DBeaver as **subscriptions_2026-05-31.csv**

*DBeaver export:* right-click the result grid → **Export data** → **CSV** → keep the
header row and the comma delimiter → on the Output page choose the folder and type
the file name. DBeaver adds a timestamp to the name by default — make sure the file
is named exactly as above.

**Check the file, not the database — before you commit it.** Open the CSV in Excel.
From the file alone, work out total MRR, the number of subscriptions and the number
of different customers. They must equal your SQL 07 Step 6 totals. Close the file
**without saving** — Excel would change it.

*Hint for the distinct count:* `=COUNTA(UNIQUE(range))` counts the different values
in a range. Select only the customer IDs themselves — not the header, and no empty
cells; either one counts as an extra value.

Then **commit these two files on their own, as the first commit on your branch**,
with the message `Save May 2026 month-end list`. Write down that commit's hash
(VS Code: Source Control → the commit in the graph, or `git log --oneline`).

### Step 6 — Sarah, in December

It's December. Sarah asks you to show her the subscriptions behind May's MRR.
In 2–3 sentences in your PR description: what do you send her, and why don't you
re-run the query?

---

## Submission

- Branch `student/sql_08_show_me_april`, three files:
  **closes/2026-05/month_end_list.sql**, **closes/2026-05/subscriptions_2026-05-31.csv**,
  **submissions/sql/08_sql_show_me_april.sql**.
- PR description:
  - **Step 1–2:** your three April numbers, the three reported ones, the differences
  - **Step 3:** where the April list is; then each change that moved April, its
    amount, and the total
  - **Step 4:** your answer
  - **Step 5:** the three totals you got from the CSV, and the hash of the commit
    that saved it
  - **Step 6:** your answer
- If something doesn't add up and you couldn't find out why, say so in the PR.
  That's a good answer. Hiding it isn't.
