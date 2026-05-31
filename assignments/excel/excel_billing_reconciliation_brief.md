# Excel Assignment — Billing Reconciliation (Jan & Feb 2026)
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** The numbers don't add up — find out why
>
> Michael — I pulled our January bank statement last week and the
> deposits don't match what I expected from our MRR. Before you
> say "close enough" — it is never close enough in finance.
>
> Every dollar that comes into this company passes through three
> systems: the billing platform, the bank, and the revenue model.
> Those three systems will almost never show the same number for
> the same period. Your job as a finance analyst is to understand
> exactly why they differ — and to be able to explain it to an
> auditor, an investor, or me on a Tuesday morning.
>
> I've dropped the January and February billing exports and bank
> statements into the data folder. Your workbook already has the
> MRR. Put all three side by side and reconcile them. Show your
> work — not just the final numbers, but the bridge from one to
> the next. If something doesn't tie, don't adjust a number to
> make it fit. Find the reason.
>
> — David

---

## What You're Building

A new tab in your workbook: **`Billing Reconciliation`**

Two months covered: January 2026 and February 2026.

Two reconciliation bridges per month:
1. **MRR → Total billed** — why doesn't what you earned equal what you invoiced?
2. **Total billed → Total collected** — why doesn't every invoice become cash?

For this business, MRR equals revenue recognized. The third bridge
(collected → revenue recognized) collapses to zero because we invoice
on a subscription basis and recognize revenue as it is earned. Your
job is to explain the first two gaps.

---

## Before You Start — Read This

You are about to work with three different representations of
the same business activity. They measure different things, at
different points in time, on different bases. Understanding the
difference is the entire point of this assignment.

**MRR (your workbook)**
What revenue the business has earned this month based on active
subscriptions. This is an accrual concept — it recognizes revenue
as it is earned, regardless of when cash changes hands.

**Billing export (billing_jan_2026.csv / billing_feb_2026.csv)**
What invoices were sent to customers this month. A customer could
be invoiced for twelve months at once, or for one month, depending
on their plan. Billing is not the same as earning.

**Bank statement (bank_statement_jan_2026.csv / bank_statement_feb_2026.csv)**
What cash actually arrived in the company's account. An invoice
sent does not guarantee payment. Cash in the bank is the only
number that does not lie.

**Critical rule:** Use the billing file for the period you are
reconciling, not a current database export. The DB reflects what
is true *now* — subscription details change over time. The billing
file captures what was invoiced at a point in time, which is the
historical record you need for this exercise.

These three numbers will not match. Your job is to explain every
gap between them.

---

## Part 1 — Get the Data

The four files are in the `data/` folder of the repo:
- `billing_jan_2026.csv`
- `billing_feb_2026.csv`
- `bank_statement_jan_2026.csv`
- `bank_statement_feb_2026.csv`

Open each file and spend five minutes understanding its structure
before you build anything. Ask yourself:

- What does one row represent?
- What does the `status` column tell you in the billing file?
- What does the `type` column tell you in the bank statement?
- Is every invoice in the billing file also in the bank statement?
  If not, why not?
- Is every bank deposit traceable to an invoice? If not, what is it?

Do not start building until you can answer all five questions.

**Orientation check — confirm before continuing:**

| Check | Your answer |
|-------|------------|
| What does one row in the billing file represent? | |
| What does one row in the bank statement represent? | |
| How many invoices are in the January billing file? | |
| How many transactions are in the January bank statement? | |
| Are those two numbers the same? If not, why not? | |

---

## Part 2 — Build the Summary Table

On the `Billing Reconciliation` tab, build this table for both
January and February side by side:

| Metric | January 2026 | February 2026 |
|--------|-------------|--------------|
| MRR (from your workbook) | | |
| Total invoiced (from billing file) | | |
| Total collected (from bank statement) | | |
| MRR vs Invoiced — gap | | |
| Invoiced vs Collected — gap | | |

**How to compute each row:**

- **MRR**: Reference your existing A vs F tabs — do not re-type.
- **Total invoiced**: Sum the `amount_due_usd` column in the billing
  file. Decide how to handle each status value before summing —
  not all rows are the same.
- **Total collected**: Sum only the cash that actually arrived.
  Read the bank statement carefully — not all rows move in the same
  direction.

When you have all six numbers, look at the gaps. Before moving to
Part 3, write down your hypothesis for why each gap exists. You will
test those hypotheses in the bridges.

---

## Part 3 — Bridge 1: MRR to Invoiced

MRR and total invoiced will not match. This is not an error. It is
a structural feature of how SaaS billing works.

**The key question:** Are all your customers on monthly billing?

Look at the `billing_cycle` column in the billing file. Sort or
filter by it. What do you notice?

For customers on **monthly** billing, the invoice amount for one
month should approximately equal their monthly MRR contribution.
Verify this for a few rows.

For customers on **annual** billing, the invoice tells a
completely different story. An annual customer pays for twelve
months upfront. On the day they pay, you collect twelve months
of cash — but you have only earned one month of revenue.

Find every annual subscription in the billing file. For each one:
1. What was the invoice amount?
2. What is their monthly MRR contribution?
3. What is the difference between what was invoiced and what
   was earned this month?

That difference is called **deferred revenue**. It is a
liability on the balance sheet — cash you have collected but
not yet earned. It unwinds month by month as the subscription
period runs.

Now look at the active subscriptions in your MRR model.
How many subscriptions are active in January? How many invoices
are in the January billing file? Are those numbers the same?

If they are not, the missing subscriptions are annual subscribers
whose billing date falls in a different month. Their cash arrived
in a prior period. Revenue is being recognized each month, but
no invoice goes out in January. This works in the opposite
direction from the annual renewals above: revenue recognized,
cash already collected.

Build the reconciliation bridge:

| Item | January | February |
|------|---------|---------|
| MRR | | |
| + Annual billing excess (cash collected > MRR earned this month) | | |
| − Annual MRR with no billing this month (MRR earned, cash in prior period) | | |
| = Total invoiced | | |
| Difference (must be zero) | | |

If your bridge does not tie to zero, something is missing or
misclassified. Find it before moving on.

---

## Part 4 — Bridge 2: Invoiced to Collected

Look at the bank statement deposits for January. Now look at
the billing file. Are they the same?

Filter the billing file for January. Are there any invoices where
`status` is not `paid`? What happened to those invoices? Did the
cash show up in January's bank statement?

Now look at the February bank statement carefully. Are all deposits
for invoices from February? Or is something else in there?

Build the bridge:

| Item | January | February |
|------|---------|---------|
| Total invoiced | | |
| + / − Adjustments (label each one explicitly) | | |
| = Total collected | | |
| Difference (must be zero) | | |

Every adjustment line must say what it is and why it exists.
"Misc" or "adjustment" are not acceptable labels. Real reconciliations
get audited — every item needs a name, a reason, and a reference to
the source document.

---

## Part 5 — Data Integrity Check

Before you write your commentary, do one more check.

Go back to the billing file. Pick any subscription you recognize
from your workbook. Confirm the invoice amount matches what you
would expect based on the subscription's seat count and price.

Now do the same for **SUB012**. Look at the billing file. Look at
what the DB currently shows for that subscription. Do they agree?

If there is a discrepancy:
- What does the billing file show for January?
- What does the DB show today?
- Why might these be different?
- Which is the correct number for January?

This is one of the most common and dangerous errors in SaaS finance:
using the current state of the database to represent a historical
period. The billing file is the point-in-time record. Write down
what you find — it belongs in your commentary.

---

## Part 6 — February: The Credit Note

Look at the February billing file. One row has a negative amount.

- What is it?
- Which customer and subscription does it relate to?
- Why was it issued?
- How does it affect total billed vs total collected?

A credit note reduces the amount the customer owes. It is the
billing system's record that an invoice was partially or fully
reversed. How you treat it in the reconciliation depends on
whether cash already moved.

Think through the timing: was the invoice paid before the credit
note was issued? If yes, what happens to the cash?

---

## Management Commentary

Below the reconciliation tables, write your commentary.

**This is a hard gate — the PR will not be merged without it.**

Write this as a coherent explanation a CFO could read — not as
answers to numbered questions. Your commentary must cover:

1. **Why MRR does not equal cash collected.** Name the specific
   structural reasons — not just "billing cycles differ" but the
   actual subscriptions and amounts involved.

2. **Whether all January revenue was collected in January.** If
   not, what was outstanding, and was it subsequently resolved?

3. **The deferred revenue balance at January 31.** Name which
   subscriptions created it and why it matters.

4. **The data integrity issue you found.** Explain what it means
   for how analysts should use the DB when working with historical
   periods.

Minimum: 4-6 sentences. Vague language ("some invoices were unpaid",
"there were differences") will not pass. Name the subscriptions,
name the amounts, name the reasons.

---

## Git Workflow

```
git checkout main
git pull origin main
git checkout -b student/excel_billing_reconciliation
```

When ready to submit:

```
git add submissions/excel/excel_09_workbook_redesign.xlsx
git commit -m "Add: Billing Reconciliation tab — Jan and Feb 2026"
git push origin student/excel_billing_reconciliation
```

---

## Keep Your Notes Current

Before pushing, update `my-notes/`:

| File | What to add |
|------|------------|
| `my-notes/kpi_definitions.md` | Deferred revenue definition; MRR vs billed vs collected; point-in-time DB integrity rule |
| `my-notes/excel_techniques.md` | Reconciliation bridge structure; how to tie across three data sources; labeling reconciling items |

---

## Submission

File: `submissions/excel/excel_09_workbook_redesign.xlsx`

PR description:

```
## Billing Reconciliation — Jan and Feb 2026

- Billing Reconciliation tab added
- Bridge 1: MRR → Invoiced (Jan and Feb) — ties to zero
- Bridge 2: Invoiced → Collected (Jan and Feb) — ties to zero
- Deferred revenue identified and quantified
- Data integrity finding documented
- Commentary included

## Self-Check

January invoices in billing file:        ___
February invoices in billing file:       ___
Jan MRR → Invoiced bridge ties to zero:  ✅ / gap of $___
Jan Invoiced → Collected bridge ties:    ✅ / gap of $___
Feb MRR → Invoiced bridge ties to zero:  ✅ / gap of $___
Feb Invoiced → Collected bridge ties:    ✅ / gap of $___
Deferred revenue at Jan 31:              $___________
Data integrity issue found:              ✅ yes / ❌ no
Commentary included:                     ✅ / not done
```

---

## Final Self-Check

You are not given expected totals for this assignment. That is
deliberate.

Your reconciliation is correct when:

- Every gap between MRR, billed, and collected is explained by
  a specific, named item (a subscription, a payment, a credit
  note, a timing difference)
- Both bridges tie to zero — no unexplained residual
- All reconciling items are labeled with what they are and why
  they exist
- The data integrity issue is identified, the correct historical
  value is stated, and the implication is explained
- Commentary covers all four required topics in coherent prose

If you cannot explain a gap, you have not finished. Do not open
a PR with unexplained differences.

---

*Excel Assignment — Billing Reconciliation*
*Idynamics Finance Analyst Training Program*
*April 2026*
