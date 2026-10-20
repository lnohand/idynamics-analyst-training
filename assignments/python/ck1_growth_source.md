# Checkpoint — Where is our growth coming from?
### Idynamics Finance Analyst Training Program

> **From:** David Chen, VP Finance · **To:** Michael · **Subject:** A board question for Sarah
>
> Sarah got a question from the board ahead of next week's meeting: *"Is our growth coming from new
> customers, or from the customers we already had?"* They want it for the first half (end of
> December to end of June) and for Q2 (end of March to end of June).
>
> Please build the numbers and send Sarah a short answer. There's no step-by-step this time: this
> is how a real request arrives. You've already built everything you need in PD1 to PD5.
>
> — David

Expect about 1 hour 30 minutes.

## The goal

Three things:

1. **A table**, printed and saved as `submissions/python/ck1_growth_source.csv`, one row per period:

```
WHERE IS OUR GROWTH COMING FROM?
      period  opening  new_customers  existing_customers  closing  check  nrr
H1 (Dec-Jun)      ...            ...                 ...      ...    ...  ...
Q2 (Mar-Jun)      ...            ...                 ...      ...    ...  ...
```

2. **A short plan** at the top of your file, written before any code (see "The idea").
3. **A message to Sarah**, three sentences, in your PR.

What each column means:

| Column | Meaning |
|---|---|
| `period` | exactly `H1 (Dec-Jun)` or `Q2 (Mar-Jun)` |
| `opening` | total MRR on the list at the start of the period |
| `new_customers` | MRR at the end of the period from customers who **weren't** on the opening list |
| `existing_customers` | what the customers who **were** on the opening list added or lost by the end: their growth, minus their shrinking, minus the ones who left. It can be negative. |
| `closing` | total MRR on the list at the end of the period |
| `check` | opening + new_customers + existing_customers − closing. Must be 0. |
| `nrr` | (opening + existing_customers) ÷ opening × 100, rounded to 1 decimal: how much of the opening MRR the existing customers still pay at the end |

The month-end lists are in `closes/`: you need `closes/2025-12/subscriptions_2025-12-31.csv`,
`closes/2026-03/subscriptions_2026-03-31.csv` and `closes/2026-06/subscriptions_2026-06-30.csv`.

## The idea

A real request doesn't come with steps. Before writing code, an analyst makes a short plan. Write
yours as comments at the top of the file, answering these four questions:

```python
# My plan
# 1. What does the answer look like?            (the table above, in your own words)
# 2. Do I already have code that does part of it?   (which file, and which part)
# 3. What are my steps, and which tool for each?
# 4. How will I know it's right?                (compare with a number from somewhere else)
```

For question 3, here are the tools you know:

| If a step needs… | Tool | Where you learned it |
|---|---|---|
| **some rows** of a table | filter: `df[df["col"] == ...]` | PD1, PD1b |
| **one total per group** | `groupby(...)[...].sum()` | PD1, PD2 |
| **a new column** worked out from other columns | column math: `df["new"] = ...` | PD3, PD5 |
| what **changed between two lists** | `pd.merge(..., how="outer", indicator=True)` | PD3 |
| **the same steps more than once** | a function (and a loop, if it's many times) | PD4, PD5 |
| **a file** someone can open in Google Sheets | `df.to_csv(path, index=False)` | PD5 |

---

## Step 0 — Set up

In VS Code, **Terminal → New Terminal**:

```
git status
```

It must say `nothing to commit, working tree clean`. If it lists files, message me before going on.

```
git checkout main
git pull origin main
git checkout -b student/ck1_growth_source
git log origin/main..HEAD --oneline
```

The last command lists any work on your new branch that isn't on main yet. You just made the branch
from main, so it must print nothing: that means you're starting clean.

---

## Your task

Right-click `submissions/python` → **New File** → `ck1_growth_source.py`. Write your plan first,
then the code. Print the heading `WHERE IS OUR GROWTH COMING FROM?`, then the table with exactly
the columns above, then save it.

No hints this time: write the code yourself. If you're stuck, go back to the PD your plan points
to and find the example that does something similar. Print after every move (each new variable,
column, filter or merge) and look at the result before you go on.

**Done means:**

- Both `check` values are 0.
- H1's `closing` is the same as June's closing in your PD5 output, and Q2's `opening` is the same
  as March's closing there.
- H1's closing minus opening is the same as the `Jun minus Dec` line in your PD5 output.
- H1's `new_customers` is **not** the same as the `New` total in your PD5 output. PD5 added up six
  one-month bridges; this question compares December with June directly, so a customer who joined in
  January and grew later counts as new in full. If yours matches PD5, you've added up months instead
  of comparing the December and June lists.
- The CSV opens in Google Sheets (**File → Import → Upload**) with the same two rows.

---

## Hand in

Commit `submissions/python/ck1_growth_source.py` only (the CSV won't show up): **Source Control** →
`+` on the file → message `Complete: Checkpoint — growth source` → **Commit** → **Publish Branch**.
Then open a PR from `student/ck1_growth_source` to `main` with this description:

~~~
## Checkpoint — Where is our growth coming from?

## My output (pasted from my terminal)
```
[paste the full output here]
```

## Message to Sarah
Three sentences she could read out to the board: where H1's growth came from, what the existing
customers did, and whether Q2 looks the same. Use your numbers.

## How it went
How long did it take, what did your plan say for question 2, and where did you get stuck?
~~~
