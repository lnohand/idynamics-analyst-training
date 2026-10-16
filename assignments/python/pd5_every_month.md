# PD5 — Every month in one go
### Idynamics Finance Analyst Training Program

> **From:** David Chen, VP Finance · **To:** Michael · **Subject:** The bridge for every month this year
>
> Your `bridge` function runs any month you give it. The board pack shows every month from January
> to June, with GRR and NRR under each one. Calling the function six times by hand works, but a
> **loop** does it for you, and next month is one more line in a list.
>
> — David

Expect about 1 hour 15 minutes.

## The goal

One table: a row for every month from January to June, each with its tie-out check, GRR and NRR,
saved as a file you can open in Google Sheets:

```
  month  opening    new  expansion  contraction   churn  closing
2026-01      ...    ...        ...          ...     ...      ...
...
2026-06 160075.5 2420.0     1340.0       -330.0  -675.0 162830.5
```

## The idea

In PD4 you called `bridge` once per month, one line each. For six months:

1. **Write the months down once**, as a list: each entry says the month and its two files.
2. **A loop goes through the list** and runs `bridge` for each entry, collecting the rows.
3. **The rows become one table**, the same way your two or three rows did in PD4.

Then the table gets three more columns (check, GRR, NRR) and is saved to a file.

## Step 0 — Set up

In VS Code, **Terminal → New Terminal**:

```
git status
```

It must say `nothing to commit, working tree clean`. If it lists files, message me before going on.

```
git checkout main
git pull origin main
git checkout -b student/pd5_every_month
git log origin/main..HEAD --oneline
```

The last command lists any work on your new branch that isn't on main yet. You just made the branch
from main, so it must print nothing: that means you're starting clean.

---

## Learn it

Clear `scratch.py` and start with `import pandas as pd`. The examples use PD3's two example lists.

### Example 1 — Run it for every file, collect the rows

Start with PD4's `summary` function (Example 2 in PD4):

```python
def summary(month, file):                 # create a function called summary, with two inputs
    customers = pd.read_csv(file)         # read the file into a table
    row = {                               # one row: column name → value
        "month": month,                   # the month you passed in
        "customers": len(customers),      # how many customers (rows) in the file
        "mrr": customers["mrr"].sum(),    # their total MRR
    }
    return row                            # hand the whole row back
```

Then a list with one entry per file. Each entry is a dict, like the row above, that says which month
and which file:

```python
FILES = [                                                                    # a list of two entries
    {"month": "May", "file": "assignments/python/pd3_examples/may_example.csv"},   # entry 1
    {"month": "June", "file": "assignments/python/pd3_examples/june_example.csv"}, # entry 2
]
```

**Piece 1: go through the list.** `for f in FILES:` runs the indented lines once for each entry, and
`f` is the current entry:

```python
for f in FILES:                   # for each entry in FILES, call it f (May first, then June)
    print(f["month"], f["file"])  # print f's month and f's file
```

```
May assignments/python/pd3_examples/may_example.csv
June assignments/python/pd3_examples/june_example.csv
```

**Piece 2: run the function for each one.**

```python
for f in FILES:                             # for each entry in FILES, call it f
    print(summary(f["month"], f["file"]))   # run summary with f's month and f's file, print the row
```

```
{'month': 'May', 'customers': 3, 'mrr': np.int64(2300)}
{'month': 'June', 'customers': 3, 'mrr': np.int64(2500)}
```

**Piece 3: keep the rows instead of printing them**, then turn them into one table:

```python
rows = []                                            # an empty list, before the loop
for f in FILES:                                      # for each entry in FILES, call it f
    rows.append(summary(f["month"], f["file"]))      # run summary, add its row to the end of rows
table = pd.DataFrame(rows)                           # list of rows → table
print(table)                                         # show the table
```

```
  month  customers   mrr
0   May          3  2300
1  June          3  2500
```

Read the loop aloud: "for each f in FILES: run summary with f's month and f's file, and add the row
to rows." Then add a column with column math, the same way you made `change` in PD3:

```python
table["avg_mrr"] = (table["mrr"] / table["customers"]).round(1)   # mrr ÷ customers, 1 decimal
print(table)                                                        # show it with the new column
```

```
  month  customers   mrr  avg_mrr
0   May          3  2300    766.7
1  June          3  2500    833.3
```

### Example 2 — Save the table to a CSV file

```python
table.to_csv("submissions/python/scratch_summary.csv", index=False)   # save to this file, no row numbers
```

Nothing prints. In Explorer, open `submissions/python/scratch_summary.csv`:

```
month,customers,mrr,avg_mrr
May,3,2300,766.7
June,3,2500,833.3
```

Without `index=False` the file gets an extra first column of row numbers (0, 1) with no header.
Running it again overwrites the file. The repo ignores CSV files, so it won't show in Source Control.

### When it goes wrong

| You write | What happens | Fix |
|---|---|---|
| `rows.append(...)` not indented under `for` | only the last month ends up in the table | indent it so it runs once per month |
| `rows = []` inside the loop | the list starts empty every time, so only the last month survives | put `rows = []` before the loop |

---

## Your turn

Right-click `submissions/python` → **New File** → `pd5_every_month.py`. Type the code, fill each
blank (`____`), press ▶ after every step and look at each print before going on.

### Step 1 — Bring your function

Copy your whole `bridge` function from `pd4_one_function.py` (from `def` down to `return row`) to the
top of the new file, under `import pandas as pd`. Then check it still runs:

```python
print("1. JUNE FROM THE FUNCTION")
june = bridge("2026-06", "closes/2026-05/subscriptions_2026-05-31.csv",
              "closes/2026-06/subscriptions_2026-06-30.csv")
print(pd.DataFrame([june]).to_string(index=False))
```

**Check it worked:** the same June row as in PD4.

### Step 2 — Run it for every month

Copy this list exactly: it's every month from January to June, with its opening and closing file.
Each month's opening list is the month before's closing list.

```python
print()
print("2. EVERY MONTH")
MONTHS = [
    {"month": "2026-01", "opening": "closes/2025-12/subscriptions_2025-12-31.csv", "closing": "closes/2026-01/subscriptions_2026-01-31.csv"},
    {"month": "2026-02", "opening": "closes/2026-01/subscriptions_2026-01-31.csv", "closing": "closes/2026-02/subscriptions_2026-02-28.csv"},
    {"month": "2026-03", "opening": "closes/2026-02/subscriptions_2026-02-28.csv", "closing": "closes/2026-03/subscriptions_2026-03-31.csv"},
    {"month": "2026-04", "opening": "closes/2026-03/subscriptions_2026-03-31.csv", "closing": "closes/2026-04/subscriptions_2026-04-30.csv"},
    {"month": "2026-05", "opening": "closes/2026-04/subscriptions_2026-04-30.csv", "closing": "closes/2026-05/subscriptions_2026-05-31.csv"},
    {"month": "2026-06", "opening": "closes/2026-05/subscriptions_2026-05-31.csv", "closing": "closes/2026-06/subscriptions_2026-06-30.csv"},
]
rows = []
for m in MONTHS:
    rows.append(bridge(m["month"], m["____"], m["____"]))   # Example 1
table = pd.DataFrame(____)
print(table.to_string(index=False))
```

**Check it worked:** six rows, and each month's `opening` is the same number as the month before's
`closing`. If one isn't, a file name in `MONTHS` is wrong.

### Step 3 — Add the checks and the rates, then save

You calculated GRR and NRR in your monthly closes. Here they are as column math, for every month at
once. Both start from the opening MRR and ask how much of it we still have at the end of the month:

- **GRR** (gross revenue retention) counts only the losses: (opening + contraction + churn) ÷ opening × 100.
- **NRR** (net revenue retention) also counts growth from existing customers: (opening + expansion + contraction + churn) ÷ opening × 100.

Contraction and churn are already negative, so you **add** them. Neither rate counts new customers:
they measure the customers we already had.

```python
print()
print("3. CHECKS AND RATES")
table["check"] = table["opening"] + table["new"] + table["expansion"] + table["contraction"] + table["churn"] - table["closing"]
table["grr"] = ((table["opening"] + table["contraction"] + table["churn"]) / table["opening"] * 100).round(1)
table["nrr"] = ((table["opening"] + table["____"] + table["contraction"] + table["churn"]) / table["opening"] * 100).round(1)
print(table[["month", "check", "grr", "nrr"]].to_string(index=False))
table.to_csv("submissions/python/pd5_h1_bridge.csv", index=____)   # Example 2
print("Saved submissions/python/pd5_h1_bridge.csv")
```

`check` is your PD3 tie-out, for every month at once: opening plus the movements, minus closing.

**Check it worked:** every `check` is 0.0, and GRR is never above 100 (it only counts losses). Then
open the file in Google Sheets: **File → Import → Upload**, choose `pd5_h1_bridge.csv`, then
**Insert new sheet(s)** → **Import data**. You should see the same six rows.

### Step 4 — The first half in one block

No hints this time: write this step's code yourself. Add a step that prints the total of each movement across all six months, the net
change (the four totals added together), and, as a check, June's list total minus December's list
total, read from the two files. Your output must look like this, with your numbers:

```
4. FIRST HALF
New:          ...
Expansion:    ...
Contraction:  ...
Churn:        ...
Net change:   ...
Jun minus Dec: ...
```

Every number must be calculated by your code: no typed-in figures. The last two lines must match.

---

## Hand in

Commit `submissions/python/pd5_every_month.py` only (not `scratch.py`; the CSV won't show up):
**Source Control** → `+` on the file → message `Complete: PD5 — every month` → **Commit** →
**Publish Branch**. Then open a PR from `student/pd5_every_month` to `main` with this description:

~~~
## PD5 — Every month in one go

## My output (pasted from my terminal)
```
[paste the full output here]
```

## One question
In which months was NRR above 100%, and what does that mean about our existing customers in those
months? (2 sentences)

## Why pandas?
Why would you use a function and a loop here instead of six copies of the same sheet? (2 sentences)

## How it went
How long did it take, and where did you get stuck?
~~~
