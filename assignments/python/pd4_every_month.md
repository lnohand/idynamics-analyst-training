# PD4 — Every month in one table
### Idynamics Finance Analyst Training Program

> **From:** David Chen, VP Finance · **To:** Michael · **Subject:** The bridge for every month this year
>
> Your June bridge works. The board pack shows every month of the year side by side, with GRR and
> NRR under each one. I've added the December to April month-end lists to `closes/`, so you have
> every list from December to June.
>
> Don't copy your script six times. Write the bridge once, then run it for every month.
>
> — David

Expect about 1 hour 45 minutes.

## Why this, and when you'd use it

When the same steps run on different files, put them in a **function** and call it once per file.
You wrote functions in PF4 (`tier(amount)`, `total_value(deals)`), and loops over a list of dicts
(`for deal in DEALS:`). Here you put pandas inside them. One function, one loop: six months, or
sixty, with the same code. And a fix you make once is fixed for every month, which never happens
with six copied sheets.

At the end you'll save the table to a CSV file and open it in Google Sheets, so the numbers you
built in Python can go straight into a pack.

## Step 0 — Set up

In VS Code, **Terminal → New Terminal**:

```
git status
```

It must say `nothing to commit, working tree clean`. If it lists files, message me before going on.

```
git checkout main
git pull origin main
git checkout -b student/pd4_every_month
git log origin/main..HEAD --oneline
```

The last command must print nothing. In Explorer, check that `closes/` now has a folder for every
month from `2025-12` to `2026-06`.

---

## Learn it

Clear `scratch.py` and use PD3's two example lists again.

### Example 1 — A function that returns one row

A row of a table is a dict: column name → value. So a function can build one row and `return` it.

```python
import pandas as pd

def summary(month, file):           # month and file are the inputs
    subs = pd.read_csv(file)
    row = {                         # one row: column name → value
        "month": month,
        "customers": len(subs),
        "mrr": subs["mrr"].sum(),
    }
    return row                      # hand the row back to whoever called summary

may_row = summary("May", "assignments/python/pd3_examples/may_example.csv")
print(pd.DataFrame([may_row]))
```

```
  month  customers   mrr
0   May          3  2300
```

`pd.DataFrame([may_row])` turns the one row into a table (Drill 1: the `[ ]` around it makes it a
list of rows). If you `print(may_row)` on its own, you'll see the dict with `np.int64(2300)` in it:
that's how pandas labels a number it calculated. It's still 2300.

Read the call aloud: "may_row is: run summary with month "May" and the May example file."

### Example 2 — Call it in a loop, collect the rows

The same pattern as `for deal in DEALS:` in PF3: a list of dicts, one per file.

```python
FILES = [
    {"month": "May", "file": "assignments/python/pd3_examples/may_example.csv"},
    {"month": "June", "file": "assignments/python/pd3_examples/june_example.csv"},
]
rows = []                                            # start with an empty list
for f in FILES:
    rows.append(summary(f["month"], f["file"]))      # run summary, add its row to the list
table = pd.DataFrame(rows)                           # list of rows → table
print(table)
```

```
  month  customers   mrr
0   May          3  2300
1  June          3  2500
```

Read the loop aloud: "for each f in FILES: run summary with f's month and f's file, and add the row
to rows."

Then add columns with column math, as in Drill 2:

```python
table["avg_mrr"] = (table["mrr"] / table["customers"]).round(1)
print(table)
```

```
  month  customers   mrr  avg_mrr
0   May          3  2300    766.7
1  June          3  2500    833.3
```

### Example 3 — Save the table to a CSV file

```python
table.to_csv("submissions/python/scratch_summary.csv", index=False)   # NEW: write the table to a file
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
| no `return row` at the end of the function | `summary(...)` gives back `None`; the table is one column called `0` full of `None`, and the next line that picks a column fails with `KeyError` | end the function with `return row` |
| `rows.append(...)` not indented under `for` | only the last month ends up in the table | indent it so it runs once per month |
| `rows = []` inside the loop | the list starts empty every time, so only the last month survives | put `rows = []` before the loop |
| `print(...)` instead of `return` | the numbers show on screen but nothing comes back to the loop | functions that build data `return` it |

---

## Your turn

Right-click `submissions/python` → **New File** → `pd4_every_month.py`. Type the code, fill each
blank (`____`), press ▶ after every step and look at each print before going on.

### Step 1 — Turn the bridge into a function

This is your PD3 Steps 1–3 inside a function. Two changes from PD3: the files come in as inputs, and
the names say `open` and `close` instead of May and June, because it now works for any month.

```python
import pandas as pd


def bridge(month, opening_file, closing_file):
    opening = pd.read_csv(opening_file)
    closing = pd.read_csv(closing_file)
    open_cust = opening.groupby("customer_id", as_index=False)["mrr"].sum()
    close_cust = closing.groupby("customer_id", as_index=False)["mrr"].sum()
    both = pd.merge(open_cust, close_cust, on="customer_id", how="____",
                    suffixes=("_open", "_close"), indicator=True)
    both = both.fillna(0)
    both["change"] = both["mrr_close"] - both["mrr_open"]
    new = both[both["_merge"] == "right_only"]
    churn = both[both["_merge"] == "left_only"]
    stayed = both[both["_merge"] == "both"]
    expansion = stayed[stayed["change"] > 0]
    contraction = stayed[stayed["change"] < 0]
    row = {                                     # one row of the bridge table
        "month": month,
        "opening": opening["mrr"].sum(),
        "new": new["change"].sum(),
        "expansion": ____["change"].sum(),
        "contraction": contraction["change"].sum(),
        "churn": ____["change"].sum(),
        "closing": closing["mrr"].sum(),
    }
    return ____


print("1. ONE MONTH")
june = bridge("2026-06", "closes/2026-05/subscriptions_2026-05-31.csv",
              "closes/2026-06/subscriptions_2026-06-30.csv")
print(pd.DataFrame([june]).to_string(index=False))
```

Everything from `opening = ...` to `return` is indented under `def`: that's what makes it part of the
function. The `def` block runs only when you call `bridge(...)`.

**Check it worked:** the June row shows the same opening, New, Expansion, Contraction, Churn and
closing as your PD3 output.

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
    rows.append(bridge(m["month"], m["____"], m["____"]))   # Example 2
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
table.to_csv("submissions/python/pd4_h1_bridge.csv", index=____)   # Example 3
print("Saved submissions/python/pd4_h1_bridge.csv")
```

`check` is your PD3 tie-out, for every month at once: opening plus the movements, minus closing.

**Check it worked:** every `check` is 0.0, and GRR is never above 100 (it only counts losses). Then
open the file in Google Sheets: **File → Import → Upload**, choose `pd4_h1_bridge.csv`, then
**Insert new sheet(s)** → **Import data**. You should see the same six rows.

### Step 4 — The first half in one block

No code this time. Add a step that prints the total of each movement across all six months, the net
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

Commit `submissions/python/pd4_every_month.py` only (not `scratch.py`; the CSV won't show up):
**Source Control** → `+` on the file → message `Complete: PD4 — every month` → **Commit** →
**Publish Branch**. Then open a PR from `student/pd4_every_month` to `main` with this description:

~~~
## PD4 — Every month in one table

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
