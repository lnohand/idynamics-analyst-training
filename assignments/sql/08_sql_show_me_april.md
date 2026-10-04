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
1. the three **closes/2026-05/** files, alone (Step 5)
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

**What this step is for.** May is closed, and we've reported $160,075.50 of MRR.
Sooner or later someone will ask *which subscriptions make up that number?* In this
step you save that list, and prove the saved file adds up to it.

Nothing has been loaded into the database since 31 May; June data goes in after
you've done this step.

**How analysts organize a close.** Finance teams don't use git. They keep **one
folder per month** on a shared drive, and everything that supports that month's
numbers goes in it:

- the query that produced the data
- the data extract itself
- the check that shows the extract agrees with what was reported

Once the month is closed, nothing in that folder changes. If something turns out
to be wrong later, the correction goes into the next month, with a note. A reviewer,
an auditor, or you six months from now should be able to open the folder and
follow May's number without asking anyone.

**Set this up on your own computer:**

```
Documents/
  iDynamics Close/
    2026-05 May/
      month_end_list.sql
      subscriptions_2026-05-31.csv
      check_2026-05-31.xlsx
```

Start each month's folder name with the year and month as numbers (`2026-05`), so
the folders sort in date order. June
will get its own folder next to this one.

**1. Write the query.** One row per subscription active on 31 May, with these
columns, in this order, named exactly:

`subscription_id, customer_id, plan_name, billing_cycle, seats, price_per_seat, discount_percent, mrr`

Order by `subscription_id`. Same rules as SQL 07: active is decided by the dates,
and MRR is rounded to 2 decimals per subscription. Save it in the May folder as
**month_end_list.sql**.

**2. Export the result** to the May folder as **subscriptions_2026-05-31.csv**:

- right-click the result grid → **Export data** → **CSV**
- keep the header row and the comma delimiter
- on the Output page, choose the folder and type the file name

DBeaver adds a timestamp to the name by default. Delete it.

**3. Prove the file is right.** Your query was right in SQL 07. What you haven't
checked is the **file**, and the file is what people will rely on. Exports go wrong
in quiet ways:

- you exported the result of an earlier version of the query
- the grid had a filter on
- an old file with the right name is the one you're looking at

None of these give an error. The only way to know the file is right is to add it up
and compare it with what was reported.

Open a **new blank workbook** in Excel → **Data → From Text/CSV** → select the CSV
→ **Load**. This copies the data into the workbook and leaves the CSV untouched.
Next to the data, work out:

- total MRR
- number of subscriptions
- number of different customers (*hint:* `=COUNTA(UNIQUE(range))`)

Type your SQL 07 Step 6 totals beside them, with a difference column. All three
differences must be 0. Save the workbook in the May folder as
**check_2026-05-31.xlsx**.

**Never open the CSV itself in Excel and save it.** Excel rewrites the file when it
saves: 1985.50 becomes 1985.5, and formatting changes. The extract has to stay
exactly as it came out of the database.

**4. Hand it in.** Git is how you send your work to me; it isn't part of the
analyst's process. Copy the three files from your May folder into a new
**closes/2026-05/** folder at the top level of the repo, next to `docs/` and
`assignments/`. Commit those three files on their own, as the first commit on your
branch, with the message `Save May 2026 month-end list`.

### Step 6 — Sarah, in December

It's December. Sarah asks you to show her the subscriptions behind May's MRR.
In 2–3 sentences in your PR description: what do you send her, and why don't you
re-run the query?

---

## Submission

- Branch `student/sql_08_show_me_april`, four files:
  **closes/2026-05/month_end_list.sql**, **closes/2026-05/subscriptions_2026-05-31.csv**,
  **closes/2026-05/check_2026-05-31.xlsx**, **submissions/sql/08_sql_show_me_april.sql**.
- PR description:
  - **Step 1–2:** your three April numbers, the three reported ones, the differences
  - **Step 3:** where the April list is; then each change that moved April, its
    amount, and the total
  - **Step 4:** your answer
  - **Step 5:** the three totals from your check workbook
  - **Step 6:** your answer
- If something doesn't add up and you couldn't find out why, say so in the PR.
  That's a good answer. Hiding it isn't.
