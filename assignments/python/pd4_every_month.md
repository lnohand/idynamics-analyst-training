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

Expect about 2 hours.

## The goal

One table: a row for every month from January to June, with the same numbers your PD3 bridge printed
for June. This is what you'll have at the end:

```
  month  opening    new  expansion  contraction   churn  closing
2026-01      ...    ...        ...          ...     ...      ...
2026-02      ...    ...        ...          ...     ...      ...
...
2026-06 160075.5 2420.0     1340.0       -330.0  -675.0 162830.5
```

Then you'll add the tie-out check and GRR / NRR to every row, and save the table as a file you can
open in Google Sheets.

## The idea

Your PD3 script already does one month. For any other month, the steps are exactly the same. Only
two things change: which list is the opening and which is the closing.

So instead of copying the script six times:

1. **Give the steps a name, with the two files as inputs.** That's a **function**. You run all its
   steps by writing its name and the two files.
2. **Have it hand back one row** of the table: month, opening, new, expansion, contraction, churn,
   closing.
3. **Run it once per month** with a loop, collect the six rows, and turn them into a table.

This is how analysts handle anything that repeats every month. The steps live in one place, so a fix
you make once is fixed for every month, and next month is one more line, not another copy.

The examples below build each of the three pieces on PD3's tiny example lists. Then the steps do the
same on the real lists.

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

Clear `scratch.py` and start with `import pandas as pd`. The examples use PD3's two example lists.

### Example 1 — A function: a name for some steps

Start with the smallest function: one input, one result.

```python
import pandas as pd

def add_up(file):                 # NEW: a function called add_up, with one input called file
    subs = pd.read_csv(file)      # the steps are indented under def
    total = subs["mrr"].sum()
    return total                  # NEW: hand the result back

may_total = add_up("assignments/python/pd3_examples/may_example.csv")   # run it on one file
print(may_total)
june_total = add_up("assignments/python/pd3_examples/june_example.csv")  # same steps, another file
print(june_total)
```

```
2300
2500
```

How to read it:

- `def add_up(file):` creates the function. Nothing runs yet: Python only remembers the steps.
- `file` is the input. Each time you run the function, `file` is whatever you put in the brackets.
- The indented lines are the steps. The function ends where the indenting ends.
- `return total` hands `total` back to the line that ran the function. That's how `may_total` gets 2300.
- `add_up("...may_example.csv")` **runs** the function on that file.

Read the call aloud: "may_total is: run add_up on the May example file."

### Example 2 — Hand back a whole row

A bridge gives several numbers, not one. So the function hands back one **row**, written as a dict:
column name → value, inside `{ }`.

```python
def summary(month, file):         # two inputs this time, separated by a comma
    subs = pd.read_csv(file)
    row = {                       # NEW: one row, column name → value
        "month": month,
        "customers": len(subs),
        "mrr": subs["mrr"].sum(),
    }
    return row

may_row = summary("May", "assignments/python/pd3_examples/may_example.csv")
print(may_row)
```

```
{'month': 'May', 'customers': 3, 'mrr': np.int64(2300)}
```

That's the row: three column names and their values. `np.int64(2300)` is how pandas labels a number
it calculated. It's still 2300.

To see it as a table, put it in a list (`[ ]`) and make a DataFrame:

```python
print(pd.DataFrame([may_row]))    # NEW: a list of rows → a table
```

```
  month  customers   mrr
0   May          3  2300
```

A table is a list of rows. Here the list has one row, so the table has one row.

### Example 3 — Run it for every file, collect the rows

First, a list with one entry per file. Each entry says which month and which file:

```python
FILES = [
    {"month": "May", "file": "assignments/python/pd3_examples/may_example.csv"},
    {"month": "June", "file": "assignments/python/pd3_examples/june_example.csv"},
]
```

**Piece 1: go through the list.** `for f in FILES:` runs the indented lines once for each entry, and
`f` is the current entry:

```python
for f in FILES:                   # NEW: f is the May entry, then the June entry
    print(f["month"], f["file"])
```

```
May assignments/python/pd3_examples/may_example.csv
June assignments/python/pd3_examples/june_example.csv
```

**Piece 2: run the function for each one.**

```python
for f in FILES:
    print(summary(f["month"], f["file"]))
```

```
{'month': 'May', 'customers': 3, 'mrr': np.int64(2300)}
{'month': 'June', 'customers': 3, 'mrr': np.int64(2500)}
```

**Piece 3: keep the rows instead of printing them**, then turn them into one table:

```python
rows = []                                            # an empty list, before the loop
for f in FILES:
    rows.append(summary(f["month"], f["file"]))      # NEW: .append adds the row to the end of the list
table = pd.DataFrame(rows)                           # list of rows → table
print(table)
```

```
  month  customers   mrr
0   May          3  2300
1  June          3  2500
```

Read the loop aloud: "for each f in FILES: run summary with f's month and f's file, and add the row
to rows." Then add a column with column math, the same way you made `change` in PD3:

```python
table["avg_mrr"] = (table["mrr"] / table["customers"]).round(1)   # .round(1): one decimal
print(table)
```

```
  month  customers   mrr  avg_mrr
0   May          3  2300    766.7
1  June          3  2500    833.3
```

### Example 4 — Save the table to a CSV file

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
    rows.append(bridge(m["month"], m["____"], m["____"]))   # Example 3
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
table.to_csv("submissions/python/pd4_h1_bridge.csv", index=____)   # Example 4
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
