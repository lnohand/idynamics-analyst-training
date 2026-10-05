# SQL Assignment 09: Freeze June
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** June close: freeze today
>
> June is over and its data is loaded. Take June's subscription list and freeze it
> today. From this month, June's figures in every report come from that list,
> starting with the board pack Sarah is putting together.
>
> We now keep the close on the shared drive, the way finance teams do. May is
> already in there.
>
> — David

Expect about 2 hours.

---

## The close folder

The close lives in **iDynamics Close** on Google Drive (link in David's Slack message):

```
iDynamics Close/
  Close log              ← one line per frozen month
  2026-05 May/           ← frozen: you can view it, not change it
  2026-06 Jun/           ← open: you work here
```

Everything that supports a month's numbers goes in that month's folder. Anyone
(a reviewer, an auditor, you next year) should be able to open the folder and follow
the number without asking you.

**Upload files exactly as they are.** Don't open the CSV in Google Sheets and don't
let Drive convert it. The extract stays exactly as it came out of the database.

---

## The exercises

### Step 1 — Take June's list

Same as May: run your month-end list query for **30 June 2026**, export the CSV,
and check the file against your query's totals (all three differences 0). Put the
three files in **2026-06 Jun**:

- `month_end_list.sql`
- `subscriptions_2026-06-30.csv`
- `check_2026-06-30.xlsx`

Write down the three totals: total MRR, number of subscriptions, number of
different customers.

### Step 2 — Sarah's question

Sarah, putting the board pack together:

> *"Sales says they closed **three** new subscriptions in June. How many new ones
> are in your June list?"*

1. Find the subscriptions that are in your June list but **not** in May's list
   (`2026-05 May/subscriptions_2026-05-31.csv`). How many are there?
2. Find the ones Sales is counting. Their report counts subscriptions **entered
   into the system** in June (`created_at`).
3. Explain the difference to Sarah in 2–3 sentences: which number belongs in
   June's board pack, and why.

### Step 3 — Freeze June

**Freezing.** You saw why in SQL 08: re-running April didn't give you April back.
Once June is frozen, its list is the record. If a June mistake turns up later, the
correction goes into the next open month, with a note.

David announces the freeze. You freeze. David locks the folder.

1. **Close log:** add June's line, the same way May's line is filled in.
2. **Hand over the files:** for each of your three June files, right-click →
   **Share** → next to David's name choose **Transfer ownership**. While a file is
   yours, you can always change it, whatever the folder allows.
3. **Tell David:** send him your hand-in email (see Submission), headed
   "June frozen". He accepts the files and sets your access to view-only. From then on, nobody
   can change June's files without David.

### Step 4 — The interview question

What you did in Step 2 has a name: **cut-off**, deciding which month each item
belongs to. Auditors test it at every year-end.

"What is cut-off, and why do auditors test it?" Answer in **at most 100 words**,
the way you'd say it to an interviewer, using your June close as the example.

---

## Submission

No branch or pull request this time. Your files are on the drive. Send David
one email, headed "June frozen", with:

- **Step 1:** your three totals
- **Step 2:** the count from your list, the subscriptions Sales is counting, and
  your answer to Sarah
- **Step 4:** your answer

If something doesn't add up and you couldn't find out why, say so. That's a good
answer. Hiding it isn't.
