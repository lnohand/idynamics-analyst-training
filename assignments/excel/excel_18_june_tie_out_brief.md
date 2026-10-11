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

## The rule for June

**The frozen list is June's closing.** Don't re-query it. Your workbook has to agree
with it, not the other way round.

---

## Step 1: Put June in your workbook

Save a copy of your fixed May workbook as **`workbook_2026-06.xlsx`** in
`2026-06 Jun/Reporting` and build June in it, the way you built May. You only need
the **Engine** and June's **Actuals** column: opening, the four movements, closing,
subscriptions, customers. The rest of the pack (A vs F, KPIs, P&L) waits until June
ties.

This month you tie **totals**: opening, closing MRR, subscriptions and customers.
The split between the four movements is tied from next month.

Build every June figure from the workbook's own sources. **A number copied from the
list can't be tied to the list.**

**Save the SQL you ran** to get June into the workbook, exactly as you ran it, as
**`june_workbook_query.sql`** in `2026-06 Jun/Reporting`. Anyone checking your June
numbers needs to see where they came from.

---

## Step 2: Compare, using the method

You'll compare June with the lists the way you learned in Assignment 17 (Compare
Two Lists): sources untouched on their own tabs, one row per ID from every source,
0 when missing, and the checks that prove nothing was lost or doubled. No reminder
of the steps this time. Using the method is part of what's checked.

**One thing is new: look at each source's key before you compare.** This time you
have three sources, and they aren't the same kind of list. For each one, answer:

1. What is the list's primary key, the field that is different on every row?
2. Can the same `subscription_id` appear more than once in it?
3. So how do you bring that source's values into Recon, and which of the Assignment
   17 checks still apply to it?

Answer in one line per source, in a note on the Recon tab and in your email.

---

## Step 3: The tie-out file

A check doesn't live inside the thing it checks. Make a separate file,
**`tieout_2026-06.xlsx`**, in **`2026-06 Jun/Reporting`** on the drive. Build it so
July takes ten minutes: copy, replace the sources, change the month, update the source names.

```
tieout_2026-06.xlsx
  Summary         ← the only tab a reviewer needs to read
  Recon           ← one row per subscription (Assignment 17's method)
  src_List_Jun    ← frozen June list, untouched
  src_List_May    ← frozen May list, untouched
  src_Workbook    ← your workbook's June Engine rows + June Actuals column, as values
  (src_Workbook_corrected ← only if you had to fix something: Step 4)
```

**Summary:**
- Header: the month (one cell; everything else refers to it), what this file
  checks (one line), each source with its file name and the date and time you took it, prepared by + date.
- **Tie table:** workbook | list | difference for **opening MRR** (your May closing
  against the May list) and for **closing MRR, subscriptions and customers** (against
  the June list). Opening first: if May doesn't tie, nothing in June can.
- **Reconciling items:** one line per explained difference: amount, explanation,
  Corrected or Open.
- **Unexplained** = the closing MRR difference − reconciling items. It must be **0**. A number
  that forces it to 0 without an explanation is a plug, and we never plug.

**Recon:** the Assignment 17 method with three sources. Columns: subscription ID · in May?
· in June? · May MRR · June MRR · list change (June − May) · workbook's June change
(its Engine rows for that subscription, added up) · Difference (workbook − list
change). The Difference total must equal the closing MRR difference minus the
opening difference, before any correction.

**Rules:** every amount traces to a source tab; the only thing you type that isn't
text, a date or a time is the month (reconciling amounts come from Recon); checks show a number, not "looks fine". Paste workbook figures **as values** and
note the file name and the date and time you copied them: the tie-out records what
the workbook said when you checked it.

---

## Step 4: Fix it and write it up

1. If June doesn't tie, find out why. Then **correct the workbook at the source of
   the error**, never in the tie-out file. Don't overwrite what you checked: paste
   the corrected figures as a second source tab, `src_Workbook_corrected`. The
   Summary then shows both: **before** (the difference, the reconciling items,
   Unexplained 0) and an **after** tie table that reads `src_Workbook_corrected`:
   difference 0. Recon stays on the figures you checked.
2. **Write the finding for David and Sarah.** This is the main deliverable. Use the
   **Finding template** in `iDynamics Close/Docs`: Answer · Why · Evidence · So
   what, **at most 120 words**. The standard is **How we write findings** in the
   same folder, and you'll be marked against it. Read its three examples before you
   write: yours should have the same shape, answer first with the number.
3. **Sign-off**, in the template's format: Status · Numbers · Ties to · Corrected ·
   Open.

If June ties first time, say so, and say how you know your check could have failed.

---

## Submission

Files on the drive in **`2026-06 Jun/Reporting`**: `tieout_2026-06.xlsx`,
`june_workbook_query.sql` and `workbook_2026-06.xlsx`. Then one email to David,
headed **"June tied out"**, with your key answers (Step 2), your finding and your
sign-off pasted in.

Sarah will read it, and she'll have a question for you on Slack.
