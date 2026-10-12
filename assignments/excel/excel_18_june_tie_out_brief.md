# Excel Assignment 18: Does June Tie?
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** June: tie it out before it goes to Sarah
>
> June's list is frozen. Now put June's MRR in your workbook. Before any of it goes
> into Sarah's board pack, show me it ties to the frozen list.
>
> Your workbook builds MRR from events. The frozen list is what we actually had on
> 30 June. If the two disagree, I want to know by how much, and why.
>
> — David

Expect about 3 hours.

---

## Your files

| Name in this brief | File | Where |
|---|---|---|
| **May list** | `subscriptions_2026-05-31.csv` | `iDynamics Close/2026-05 May` |
| **June list** | `subscriptions_2026-06-30.csv` | `iDynamics Close/2026-06 Jun` |
| **May workbook** | `excel_15_may_close.xlsx` (the fixed one, on `main`) | repo |
| **Events query** | `mrr_events.sql` | repo, `submissions/sql` |

Both lists are frozen. **Use them as they are. Don't run the list query
(`month_end_list.sql`) again** to make new ones. The June list is June's closing:
your workbook has to agree with it, not the other way round.

Everything you hand in goes in **`iDynamics Close/2026-06 Jun/Reporting`**.

---

## Step 1: Put June in the workbook

1. Save a copy of the May workbook as **`workbook_2026-06.xlsx`** in `Reporting`.
2. Run the events query for June only: add a filter so it returns only events dated
   1 to 30 June 2026.
3. Paste those rows into the **Engine** table, below the last May row. The query
   returns `month` as text (`2026-06`): change it to a date (1 Jun 2026), like the
   rows above. Then copy the formula columns (`movement` to `is_logo_reactivation`)
   down from the last May row to your new rows.
4. On the **Actuals** tab, add a June column next to May, and fill in only these
   rows:
   - **Opening MRR** and **Closing MRR**: copy May's formulas across.
   - **New MRR, Expansion MRR, Contraction MRR, Churned MRR**: add up June's Engine
     rows for each movement. Actuals keeps Contraction and Churned as positive
     amounts.
   - **Active Subscriptions**: how many subscriptions are active at the end of June.
   - **Active Customers**: how many different customers have at least one active
     subscription at the end of June.

   Work out both counts from the Engine.

Leave June's other cells on Actuals empty, and leave every other tab as it is. They
wait until June ties.

**Never use the June list to fill in the workbook.** A number copied from the list
can't be tied to the list.

Save the query exactly as you ran it, June filter included, as
**`june_workbook_query.sql`** in `Reporting`. Anyone checking your June numbers needs
to see where they came from.

This month only the **totals** are tied: opening MRR, closing MRR, subscriptions and
customers. The four movements are tied from July.

---

## Step 2: Before you compare, look at each source's key

You will compare three sources:

- the **May list**
- the **June list**
- the workbook's **June Engine rows** (the rows you added in Step 1)

They aren't the same kind of list. For each source, answer:

1. What is its primary key: the field that is different on every row?
2. Can the same `subscription_id` appear on more than one row?
3. So how do you bring its amounts into Recon, and which of the Assignment 17 checks
   still apply to it?

Write one line per source. When you build the Recon tab in Step 3, put the three
lines in a note on it. They also go in your email.

---

## Step 3: Build the tie-out file

The check must not live inside the thing it checks, so make a separate file:
**`tieout_2026-06.xlsx`** in `Reporting`. It has these tabs:

```
tieout_2026-06.xlsx
  Summary         ← the only tab a reviewer needs to read
  Recon           ← one row per subscription
  src_List_Jun    ← the June list, imported, untouched
  src_List_May    ← the May list, imported, untouched
  src_Workbook    ← from workbook_2026-06.xlsx: the June Engine rows and the June
                    Actuals column, pasted as values
  (src_Workbook_corrected ← only if you have to fix the workbook: Step 4)
```

Build it so that July takes ten minutes: copy the file, replace the src tabs, change
the month cell, update the file names in the header.

### Recon

Use Assignment 17's method: untouched src tabs, every ID from every source listed
once, 0 when an ID is missing from a source, and the check table that proves nothing
was lost or counted twice. No reminder of the steps this time. Using the method is
part of what's checked.

Columns, in this order:

1. subscription ID
2. in May list? (Yes/No)
3. in June list? (Yes/No)
4. May MRR
5. June MRR
6. list change = June MRR − May MRR
7. workbook change = `mrr_delta` of that subscription's June Engine rows, added up
8. Difference = workbook change − list change

The total of column 8 must equal the closing MRR difference minus the opening MRR
difference, both from the Summary's first (**before**) tie table.

### Summary

**Header:**
- the month, in one cell (every other mention of the month refers to this cell)
- one line saying what this file checks
- each source: its file name, and the date and time you copied it into this file
- prepared by, and the date

**Tie table**, with three columns: workbook · list · difference (workbook − list).

| Row | Workbook figure | List figure |
|---|---|---|
| Opening MRR | June's opening MRR in `src_Workbook` | May list, total MRR |
| Closing MRR | June's closing MRR in `src_Workbook` | June list, total MRR |
| Subscriptions | June's Active Subscriptions in `src_Workbook` | June list, number of subscriptions |
| Customers | June's Active Customers in `src_Workbook` | June list, number of different customers |

Opening goes first. If the opening difference isn't 0, find out why before you look
at June: if May doesn't tie, nothing in June can.

**Reconciling items:** one line per explained difference, with its amount (from
Recon), the explanation, and its status:
- **Corrected**: you fixed it in the workbook (Step 4)
- **Open**: not fixed yet, and you say what still has to happen

**Unexplained** = closing MRR difference − the reconciling items. It must be **0**.
A number that forces it to 0 without an explanation is a plug, and we never plug.

### Rules for the whole file

- Apart from text, dates and times, the month is the only thing you type. Never
  type an amount or a count.
- Every amount comes by formula from a src tab or from Recon.
- Checks show a number (the difference), not "looks fine".
- Workbook figures go in **as values**, with the file name and the date and time
  you copied them. The tie-out records what the workbook said when you checked it.

---

## Step 4: Fix it and write it up

1. **If June doesn't tie, find out why. Fix it in `workbook_2026-06.xlsx`**, where
   the wrong number is made. Never fix it in the tie-out file.
   - Leave `src_Workbook` exactly as it is: it is what you checked.
   - Paste the corrected June Engine rows and June Actuals column, as values, into a
     new tab, `src_Workbook_corrected`.
   - On Summary, keep the first tie table (**before**: the difference, the
     reconciling items, Unexplained 0). Under it, add a second tie table (**after**)
     that reads `src_Workbook_corrected`. Its differences must all be 0.
   - Recon keeps reading `src_Workbook`.
2. **Write the finding for David and Sarah.** This is the main deliverable. Use the
   **Finding template** in `iDynamics Close/Docs`: Answer · Why · Evidence · So
   what, **at most 120 words**. You'll be marked against **How we write findings**,
   in the same folder. Read its three examples before you write: yours should have
   the same shape, with the answer first and the number in it.
3. **Sign-off**, in the template's format: Status · Numbers · Ties to · Corrected ·
   Open.

If June ties on the first try (every difference 0), say so, and say how you know your
check could have failed.

---

## Submission

1. In `iDynamics Close/2026-06 Jun/Reporting`: `workbook_2026-06.xlsx`,
   `june_workbook_query.sql` and `tieout_2026-06.xlsx`.
2. A new email to David with the subject **"June tied out"**, with these pasted in:
   your three lines from Step 2 (one per source), your finding and your sign-off.

Sarah will read it, and she'll have a question for you on Slack.
