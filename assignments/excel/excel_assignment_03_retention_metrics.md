# Excel Assignment 03 — Retention Metrics
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Retention tab — the other half of the story
>
> Your growth tab answered the first question the board asks: "How
> fast are we growing?" Now we need to answer the second: "Are we
> keeping what we have?"
>
> The growth tab showed that we plateaued in H2 2025. But it didn't
> explain WHY. That's what retention metrics do — they isolate what
> happened to existing customers, separate from new acquisition.
>
> A business can look healthy on a growth chart while quietly bleeding
> out underneath. NRR is how you catch that before it's too late.
>
> Build the Retention tab. Same workbook, same approach — everything
> references the Waterfall and Engine tabs. No new data.
>
> I need three things: GRR, NRR, and logo churn. If you don't know
> what those are, look them up before you start building. Understand
> the concept first, then build.
>
> — David

---

## Why Retention Metrics Exist

Growth metrics tell you the headline: MRR went up or down. Retention
metrics tell you what happened *underneath* — specifically, what
happened to the revenue and customers you already had, ignoring new
acquisition entirely.

This matters because acquisition can mask a retention problem. A
company adding $10K/month in new MRR looks great — until you realize
it's also losing $8K to churn and contraction. The growth tab shows
the net result (+$2K). The retention tab shows the leak ($8K).

There are three retention metrics every SaaS company tracks. Each
one measures something different, and the combination tells you
more than any single number.

---

## The Three Metrics

### Gross Revenue Retention (GRR)

**Question it answers:** Of the revenue we started the month with,
how much did we keep — ignoring any growth from existing customers?

GRR only counts losses. It cannot exceed 100%. It tells you: if you
stopped selling tomorrow and your existing customers never expanded,
how fast would the business shrink?

**Why it matters:** GRR is the floor. If GRR is 95%, you're losing
5% of your base every month, which compounds to roughly 46% annually.
That means you need to replace nearly half your revenue every year
just to stay flat. No amount of expansion fixes a GRR problem — it
only delays it.

### Net Revenue Retention (NRR)

**Question it answers:** Of the revenue we started the month with,
how much do we have now — including expansion from existing customers?

NRR can exceed 100%. When it does, it means existing customers grew
faster than the business lost revenue to churn and contraction. A
company with NRR > 100% would grow even if it never signed another
new customer. This is the single most important metric in a Series A
conversation.

**Why it matters:** NRR is the ceiling of what your existing base
can sustain. If NRR is 103%, your existing revenue compounds at 3%
per month — that's significant. If NRR is 97%, your base is decaying
and you're on a treadmill.

### Logo Churn Rate

**Question it answers:** What percentage of customers left this
month?

Logo churn counts customers (logos), not dollars. One customer = one
logo, regardless of whether they pay $500/month or $8,000/month.

**Why it matters:** Dollar churn and logo churn tell different
stories. You can have low MRR churn but high logo churn — meaning
you're losing lots of small customers but keeping the big ones. Or
low logo churn but high MRR churn — meaning you lost one whale.
The combination reveals *where* the retention problem is.

---

## The Relationship Between GRR, NRR, and Growth

Think of it this way:

- **GRR** tells you if the bucket has holes
- **NRR** tells you if the water level is rising or falling
- **Logo churn** tells you whether you're losing drips or chunks

A healthy business has: GRR > 95%, NRR > 100%, logo churn < 2%/month.

When GRR is low but NRR is high, it means expansion is compensating
for churn. That works short-term but not forever — eventually you
run out of accounts to expand.

When GRR is high and NRR is below 100%, something unusual is
happening — minimal churn but also no expansion. The base is stable
but stagnant.

Your Growth tab already hinted at this dynamic. Now you'll quantify
it.

---

## What to Build

Add a **Retention** tab to the workbook. It needs four sections:

### Section 1 — Monthly Retention Rates

One row per month (same 26-month range). Calculate GRR and NRR for
each month using the waterfall data. Think about which waterfall
columns feed each formula. The opening MRR is your denominator. The
numerator is opening adjusted for the relevant movements.

Handle months where opening MRR is zero (month 1). Handle months
where there are no losses (GRR = 100%, not an error).

### Section 2 — MRR Churn Rates

Two rates, each measuring a different scope of loss:

**MRR churn rate:** Revenue lost to cancellations only, as a
percentage of opening MRR. This is the narrowest definition — just
customers who left entirely.

**Gross MRR churn rate:** Revenue lost to cancellations AND
contraction (downgrades, seat reductions, discounts), as a
percentage of opening MRR. This is the broader definition — all
revenue losses, not just full cancellations.

The difference between these two numbers tells you whether your
churn problem is about customers leaving or customers shrinking.

### Section 3 — Subscription Churn vs. Logo Churn

This section has a trap in it. Read carefully before building.

**Subscription churn rate** counts cancelled subscriptions divided
by active subscriptions at the start of the month. This is
straightforward: COUNTIFS on the Engine tab for cancelled events
in each month, divided by a running count of active subs.

Build the running count: created events add a subscription,
cancelled events remove one. Use COUNTIFS by month and event type.
Prior month's end count = this month's start count.

**But subscription churn is not logo churn.**

A "logo" in SaaS means a customer — a company. Logo churn means the
customer left entirely. If Montreal Finance Hub cancels one of their
two subscriptions, that's a subscription cancellation but NOT a
churned logo — they're still a customer.

**Your task:** After building the subscription churn rate, investigate
the 11 cancelled subscriptions in the Engine tab. For each one, check
whether that customer had other active subscriptions at the time of
the cancellation. You can do this by looking at the Raw Snapshot and
Engine tabs together.

Add a row called **True Logo Churns** that counts only the
cancellations where the customer had no remaining active subs.
Add a row called **Logo Churn Rate** that divides true logo churns
by the count of active customers (not subscriptions) at the start
of the month.

**Why this matters:** A company can report "11 subscription
cancellations" and "3 lost customers" from the same data. The
first number sounds alarming. The second tells the real story.
Confusing the two is one of the most common mistakes junior analysts
make — and one of the first things a VP Finance will catch.

### Section 4 — Trailing Averages and Written Interpretation

Calculate trailing 3-month and trailing 12-month averages for NRR,
GRR, and logo churn. These are what go on the Dashboard — single
months are noisy, trailing averages show the trend.

Write **two paragraphs** below the data:

**Paragraph 1 — The retention story.** What do GRR and NRR say about
this business? Is the existing base healthy or decaying? When was
retention strongest and weakest? Use trailing averages, not individual
months.

**Paragraph 2 — Subscription churn vs. logo churn.** What did you
find when you investigated the 11 cancellations? How many were true
logo exits vs. customers dropping a product but keeping another?
What does this tell you about the nature of churn at Idynamics — is
the company losing customers or losing products within customers?

---

## Formatting

Follow the same conventions as the Growth tab:

- Section headers: bold white on dark blue
- Rates: percentage format, 1 decimal place
- Negatives: red parentheses via number format
- Blank/error cells: IFERROR, never show formula errors
- Freeze column A and the header row
- Add a horizontal reference line concept: in the NRR row, any month
  below 100% is a month the existing base shrank. Consider conditional
  formatting to highlight these.

---

## Self-Check Values

| Check | Expected |
|---|---|
| GRR, 2024-08 | 95.8% |
| GRR, 2025-08 | 96.4% |
| GRR, 2026-02 | 99.6% |
| NRR, 2025-04 | 100.6% |
| NRR, 2025-09 | 101.2% |
| NRR, 2026-02 | 99.6% |
| MRR churn rate, 2024-08 | 4.19% |
| MRR churn rate, 2025-08 | 3.10% |
| Gross MRR churn rate, 2025-08 | 3.57% |
| Gross MRR churn rate, 2025-03 | 0.93% |
| Active subs start of 2024-08 | 20 |
| Active subs start of 2025-01 | 34 |
| Active subs start of 2026-02 | 52 |
| Sub cancellations, 2024-08 | 1 |
| Sub cancellations, 2025-06 | 2 |
| Subscription churn rate, 2024-08 | 5.0% (1 of 20) |
| Subscription churn rate, 2025-06 | 3.8% (2 of 52) |
| Total sub cancellations (all time) | 11 |
| True logo churns (all time) | 3 |
| Trailing 12-month avg NRR (Feb 2026) | 99.7% |

> **If your GRR exceeds 100% in any month**, you have a formula error.
> GRR is capped at 100% by definition — it excludes expansion.
>
> **If your sub count doesn't end at 51–52**, recount your created
> and cancelled events. The Engine tab has 62 created events and 11
> cancelled events. 62 − 11 = 51 active at the end. The start count
> for Feb 2026 is 52 (before the Feb cancellation).
>
> **If you find more than 3 true logo churns**, you're not checking
> whether the customer had other active subscriptions at the time of
> cancellation. Most of the 11 cancellations are customers dropping
> one product while keeping another.

---

## Submission

Save the workbook. Commit to your repo:

```
submissions/excel/03_retention_metrics.xlsx
```

Branch: `student/excel-03-retention-metrics`

PR description:

```
## What this does
Retention tab: monthly GRR, NRR, MRR churn rate, gross churn rate,
subscription churn with running active count, true logo churn
analysis, trailing averages, and written interpretation.

## Self-check
GRR 2024-08: 95.8% ✅
NRR 2025-09: 101.2% ✅
Sub churn 2025-06: 3.8% (2 of 52) ✅
True logo churns (all time): 3 ✅
Trailing 12-month NRR (Feb 2026): 99.7% ✅

## Interpretation
[One sentence: what does the retention data say about this business?]

## Questions for reviewer
[Anything you're unsure about]
```

---

## What Comes Next

After Retention, two tabs remain before the Dashboard:

- **Unit Economics** — ARPA, gross margin, LTV, and the CAC data
  from Accounting. This is where you find out whether each customer
  is worth more than it costs to acquire.
- **Dashboard** — pulls the key numbers from Growth, Retention, and
  Unit Economics into a single board-ready view.

The board reads the Dashboard. But every number on it traces back to
the tabs you're building now.

---

*Idynamics Finance Analyst Training Program*
*Excel Assignment 03 — Retention Metrics*
*March 2026*
