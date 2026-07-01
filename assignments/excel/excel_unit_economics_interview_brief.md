# Excel Interview Assignment — Unit Economics

**Audience:** Michael
**Format:** Interview-style. Some parts you answer in words (as you would out loud
in an interview); others you build in the workbook. Show your reasoning — numbers
are never typed as constants where a formula should compute them.
**Time:** ~40–50 min.
**Data:** self-contained — everything you need is in this brief. No database, no
prior workbook.

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Unit economics — the four numbers an investor asks first
>
> Michael — when a board member or a VC opens your model, they don't start with
> MRR. They ask four things: *what does a customer cost to acquire, what are they
> worth, is that worth-it, and how long until we get our money back.* CAC, LTV,
> LTV:CAC, and CAC payback. If you can compute those from a cold dataset and say
> what they mean in one breath, you sound like an analyst who's done this before.
>
> Here's a small company — NorthPeak Analytics. I've given you a snapshot of its
> customer base and a handful of assumptions. Build the unit economics, then tell
> me the story. And watch the gross-margin point — it's the difference between a
> number that's right and a number that just looks right.
>
> — David

---

## The data — NorthPeak Analytics

**Active customers at month-end:**

| Plan    | Customers | MRR per customer |
|---------|-----------|------------------|
| Starter | 25        | $200             |
| Growth  | 10        | $500             |
| Scale   | 5         | $1,200           |

**Assumptions:**

| Input                          | Value    |
|--------------------------------|----------|
| Gross margin                   | 75%      |
| Monthly logo (customer) churn  | 2.0%     |
| S&M spend — last month         | $24,000  |
| New customers acquired — last month | 8   |

---

## Part 1 — Answer in words (no Excel)

Answer as if I asked you in an interview — one or two sentences each.

1. What is **LTV:CAC**, and what's a "good" ratio? If a company's LTV:CAC came in
   at, say, 6–7×, would you call that great — or would it make you ask a question?
   Which question?
2. LTV and CAC payback should be calculated on **gross profit**, not revenue. Why?
   What specifically goes wrong if you compute LTV off revenue and ignore gross
   margin?
3. In plain English, what does **CAC payback** tell a founder that LTV:CAC doesn't
   — and why does an investor watching the bank balance care about it?

## Part 2 — Build it in the workbook

Put NorthPeak's data in a tab and compute the following with **formulas** (nothing
hardcoded that should be derived):

- **ARPA** (average revenue per account, monthly)
- **Gross margin %** (given, but reference it as a cell)
- **Average customer lifetime** (in months)
- **LTV** — gross-margin-adjusted
- **CAC**
- **LTV:CAC** — guard the division with `IFERROR`
- **CAC payback** (in months) — gross-margin-adjusted

Use the gross-margin-adjusted convention throughout (that's the point of Part 1,
Q2). Show ARPA as a real calculation off the customer table, not a typed number.

## Part 3 — Interpretation (2–3 sentences)

Below your build, write what NorthPeak's unit economics say about the business.
Cover: is acquisition efficient, is the payback healthy, and — given the ratio —
is there anything you'd *challenge* management on?

## Part 4 — Stretch: work the levers

NorthPeak's CEO wants to grow faster and proposes **doubling S&M to $48,000 next
month**, which the sales team thinks would bring in **12 new customers** instead of 8.

Recompute **CAC, CAC payback, and LTV:CAC** under that plan (LTV per customer is
unchanged — none of its inputs moved). In one or two sentences: is this a good
trade? What would you want to see before signing off on doubling the budget?

---

## Submission

- The workbook with Parts 2–4 built (formula-driven).
- A short note with your Part 1 and Part 3 answers.

---

## Self-Check

Run through these before you submit. If any value doesn't match, find the
discrepancy before you call it done.

| Check | Expected |
|-------|----------|
| Total active customers | 40 |
| Total MRR | $16,000 |
| ARPA (monthly) | $400 |
| Average customer lifetime | 50 months |
| LTV (gross-margin-adjusted) | $15,000 |
| CAC | $3,000 |
| LTV:CAC | 5.0× |
| CAC payback (gross-margin-adjusted) | 10 months |
| Stretch — CAC / payback / LTV:CAC | $4,000 / 13.3 months / 3.75× |

---

*Excel Interview Assignment — Unit Economics*
*iDynamics Finance Analyst Training Program*
