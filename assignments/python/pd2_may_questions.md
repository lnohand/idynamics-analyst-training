# PD2 — On your own: James's May questions
### Idynamics Finance Analyst Training Program

> **From:** David Chen, VP Finance · **To:** Michael · **Subject:** James needs four facts about May
>
> James is planning the renewals team's outreach and asked for four facts about May's
> subscriptions: how many and how much, the small ones, seats by plan, and our biggest customers.
>
> You answered Sarah's June questions in PD1. Same tool, new questions, and this time you write
> the script yourself. No code in this brief.
>
> — David

Expect about 1 hour.

---

## Why this

In PD1 you typed code we gave you. This is the real test: a blank file, a business question, and
you decide which tool answers it. Everything you need is in PD1: `read_csv`, filters, picking
columns, `sort_values`, `groupby`, `len`, `.sum()` and the f-string format codes. If you're stuck,
open PD1 and find the example that does something similar; that's how analysts work.

---

## Step 0 — Set up

In VS Code, open the repo, then **Terminal → New Terminal**:

```
git status
```

It must say `nothing to commit, working tree clean`. If it lists files, message me before going on.

Then:

```
git checkout main
git pull origin main
git checkout -b student/pd2_may_questions
git log origin/main..HEAD --oneline
```

The last command must print nothing.

The data is the frozen May list: `closes/2026-05/subscriptions_2026-05-31.csv`. It has the same
columns as June's, including `seats`.

---

## Your turn

In Explorer, right-click `submissions/python` → **New File** → `pd2_may_questions.py`. Run ▶
after each step. Print each step's heading exactly as given, with a blank line before each heading
after the first, so the output reads as one report.

### Step 1 — Load and check
Heading: `1. LOAD AND CHECK`

How many subscriptions were there at the end of May, and how much MRR? Print both, MRR with commas
and 2 decimals.

### Step 2 — The small subscriptions
Heading: `2. SUBSCRIPTIONS WITH MRR UNDER 1,000`

James wants the subscriptions paying **less than 1,000** a month: they get an email, not a call.
Print them **smallest first**, showing four columns: `subscription_id`, `customer_id`, `plan_name`,
`mrr`. Then print one line in this format:
`Count: ...  MRR: ...  Share of MRR: ...%` (MRR with commas and 2 decimals, share with one decimal).

### Step 3 — Seats by plan
Heading: `3. SEATS BY PLAN`

The renewals team prices by seat. How many **seats** (not MRR) does each plan have? One row per plan,
biggest first. Then print one line: `Total seats: ...`

### Step 4 — The biggest customers
Heading: `4. CUSTOMERS WITH MRR OF 8,000 OR MORE`

David calls these customers himself. A customer can have more than one subscription, so add up
each **customer's** MRR across all their subscriptions first, then keep the customers whose total
is **8,000 or more**. Print them biggest first (`customer_id` and `mrr`), then one line in the same format as Step 2:
`Count: ...  MRR: ...  Share of MRR: ...%`.

---

## Hand in

Commit `submissions/python/pd2_may_questions.py` only: **Source Control** → `+` on the file →
message `Complete: PD2 — May questions` → **Commit** → **Publish Branch**. Then open a PR from
`student/pd2_may_questions` to `main` with this description:

~~~
## PD2 — May questions

## My output (pasted from my terminal)
```
[paste the full output here]
```

## How do I know each answer is right?
For each step, one line: what did you check, and against what?

## One question
In Step 4, CUST025 pays 10,800 a month, but no single subscription in May is above 7,000. How can
both be true?

## How it went
How long did it take, where did you get stuck, and which PD1 example did you go back to?
~~~
