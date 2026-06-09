# Billing Reconciliation — Feedback

Good attempt at the structure. The two-bridge framework is right and you correctly identified Pacific Analytics as the annual billing customer. But several formulas are wrong and three sections are missing. Here's what to fix.

---

**Bridge 1 — Annual billing excess (Row 11)**

Your formula is `=B4-B2`, which is Total Collected minus MRR. That's not what this item is supposed to represent.

Annual billing excess is the gap between what you invoiced Pacific Analytics and what you earned from them in January. They paid for twelve months upfront — $46,800 and $23,826, totalling $70,626. But January MRR only recognizes one month of that. The excess is the other eleven months: cash collected but not yet earned. That number needs to come from the billing file, not from Total Collected.

Use SUMIF to pull annual rows from the billing file, then multiply by 11/12:
```
= SUMIF(billing_jan_2026!H:H, "Annual", billing_jan_2026!P:P) * (11/12)
```
For February, do the same against the Feb billing file — there were no annual renewals that month, so it'll come out zero, which is correct.

---

**Bridge 1, February — Annual MRR with no billing (Row 12)**

Your formula: `=((billing_jan_2026!M34 + billing_jan_2026!M37) / 12) * 2`

Two problems. First, you're using column M (subtotal, before discounts). Row 37 has a 5% discount applied — the subtotal is $25,080 but the actual invoice was $23,826. Always use column P (`amount_due_usd`) for any cash or revenue figure.

Second, you're multiplying by 2. February has one month of MRR from these customers, not two. Remove it.

Correct formula:
```
= (billing_jan_2026!P34 + billing_jan_2026!P37) / 12
```

---

**Bridge 2, January — Total Collected (Row 19)**

`B19 = B18`. You've set January's collected amount equal to invoiced, which makes the Bridge 2 difference zero no matter what. Change `B19` to `=B4`.

---

**Total Invoiced — failed and refunded rows**

In January, you're skipping row 31 (Prairie SaaS Innovations — status: failed, $675, reason: insufficient funds). That invoice was issued. It belongs in Total Invoiced. Bridge 2 is where you explain it wasn't collected. If you leave it out of Total Invoiced, Bridge 2 can't tie.

In February, you're skipping row 36 (Ontario Manufacturing Tech / SUB050 — status: refunded, −$169.71). That's a credit note for a subscription cancelled on Feb 20. A credit note is a billing document — include it. The negative amount will reduce your Total Invoiced, which is correct.

Update both formulas to sum the full range and let the values flow through.

---

**Total Collected, February — the refund**

You're skipping bank statement row 41: a debit of −$169.71, the cash refund corresponding to the credit note above. If the credit note reduces Total Invoiced, the refund needs to reduce Total Collected. Include row 41 — the negative will pull the total down automatically.

---

**Missing: SUB012 data integrity check**

You didn't do Part 5. Go to the billing file, find SUB012 (Maritime E-commerce), and note the seat count and invoice amount. Then check what the database shows for that subscription today. The numbers are different. Work out which one is correct for January and why — and what that means for how you should approach historical analysis.

---

**Missing: The credit note analysis**

You identified the row in the Feb billing file (your formula skips it) but never analyzed it. Trace the full story: what was the credit note for, why was it issued, did cash already move before it was issued, and how does it affect the reconciliation?

---

**Missing: Commentary**

Nothing written. This is a hard gate — the PR won't merge without it. Four things to cover, in plain prose at a level a CFO could read: why MRR doesn't equal cash collected (name the subscriptions and amounts), whether all January revenue was collected in January, what the deferred revenue balance was at January 31, and what you found with SUB012 and why it matters.
