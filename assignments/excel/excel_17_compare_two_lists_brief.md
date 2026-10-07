# Excel Assignment 17: Compare Two Lists
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** One technique before June
>
> Before you tie out June, I want you to have one technique down properly:
> comparing two lists. You'll use it every month and in every reconciliation you
> ever do: billing against the bank, Sales' report against our list, this month
> against last month.
>
> Sorting two lists side by side and scanning them works until it doesn't: a row
> that's in one list and not the other shifts everything below it, and nothing
> tells you that you missed it. With the method below, a lost row makes a check
> fail.
>
> We show it once. After this, whenever two lists need comparing, I expect you to
> do it this way by yourself, and I'll check that you do.
>
> — David

Expect about 1.5 hours.

---

## What you're comparing

- **April's list:** `subscriptions_2026-04-30.csv` (attached to David's email).
  April was closed before we started freezing months, so finance rebuilt its list
  from the April close. It matches what we reported for April.
- **May's list:** `subscriptions_2026-05-31.csv` in `iDynamics Close/2026-05 May`.

**Your goal:** from these two lists alone, rebuild May's MRR movements (New,
Expansion, Contraction, Churn) and check them against the May figures in your
workbook (`Actuals`, May column). For May, they should agree.

Work in a new file: **`compare_2026-04_2026-05.xlsx`**.

---

## The method

The lists stay exactly as they came, each on its own tab. All the comparing
happens on a **separate tab** that reads from them.

```
src_List_Apr   src_List_May          Compare
 (untouched)    (untouched)    ← one row per ID; all formulas live here
```

1. **Load each list onto its own tab.** Data → From Text/CSV → Load. Don't edit
   these tabs.
2. **Check each list has each ID only once.** Count the rows and count the
   different IDs. If they differ, a subscription is listed twice and its number
   will come out wrong.
3. **On the Compare tab, list every ID from *both* lists, once.** Copy the IDs
   from each list into one column, one under the other, then Data → Remove
   Duplicates. Leave a few empty rows at the top for step 6. Never start from one
   list only: the IDs that are in just one list (new, cancelled) matter most.
4. **Bring in each list's MRR**, one column per list, with SUMIFS. It gives **0**
   when the ID isn't in that list. Add a **Yes/No** column per list (COUNTIF): a 0
   in the MRR column can mean "not in the list" or "in it with MRR 0".
5. **Difference** = May − April, on every row.

   With made-up IDs:

   ```
   ID       In Apr?  In May?  Apr MRR   May MRR   Difference
   SUB901   Yes      Yes      1,000     1,000          0
   SUB902   Yes      No         800         0       −800
   SUB903   Yes      Yes        500       650       +150
   SUB904   No       Yes          0     1,200     +1,200
   ```

6. **Prove nothing was lost.** At the top, a small check table. Each row: the
   figure from your Compare table, the same figure from the list's own tab, and
   the difference, which must be **0**.

   ```
   CHECKS                     Compare   List tab   Diff
   April MRR total               …          …        0
   May MRR total                 …          …        0
   IDs in April (Yes count)      …          …        0
   IDs in May (Yes count)        …          …        0
   ```

7. **Explain every row where Difference isn't 0.** Here, the explanation is the
   movement (Your task, 2).

### What to watch for

- **IDs in only one list.** These are your new and cancelled items, so they
  usually matter most.
- **The same ID listed twice in one list.** Step 2 catches it.
- **IDs that look the same but don't match**, e.g. `SUB002 ` with a trailing space.
  The sign: hardly any IDs come out "Yes" in both lists. Two lists a month apart should share almost all their IDs.

### What changes your approach next time

- **Size and how often.** For a one-off, copy, paste and Remove Duplicates is fine,
  even for thousands of rows: Ctrl+Shift+↓ selects down to the last filled cell. For a
  comparison you'll repeat every month, build the ID column with a formula instead
  (UNIQUE over both lists stacked with VSTACK), so it updates when you replace the
  lists.
- **One row per ID, or many.** A month-end list has one row per subscription.
  Invoices or events can have many rows per customer. SUMIFS adds them up, which is
  what you want there, but then step 2 doesn't apply.
- **What you're matching on.** Here both lists share `subscription_id`. When they
  don't (the bank doesn't know our subscription IDs), first decide what identifies
  the same item on both sides.

---

## Your task

1. Build the Compare tab with the method above, checks included.
2. Add a **Movement** column that labels every row New, Expansion, Contraction,
   Churn or No change, from the Yes/No and Difference columns. Work out the rule
   yourself: what does each label mean in terms of the two lists?
3. Below the Compare table, a small table: total Difference per movement. Next to
   it, the same movements from your workbook's May column, and the difference. **All must be 0.**
   Compare like with like: your workbook stores Contraction and Churn as positive
   amounts that get subtracted, while your Difference column has them as negatives.
   Pick one convention, and say in a note on the sheet which one. If a difference
   still isn't 0, find out why before you write anything.
4. In **at most 60 words**: why is this method safer than sorting the two lists
   side by side? Use what happened in your table as the example.

---

## Submission

Reply to David's email with `compare_2026-04_2026-05.xlsx` attached and your
60-word answer in the email.
