# PD4 — May and June from one function
### Idynamics Finance Analyst Training Program

> **From:** David Chen, VP Finance · **To:** Michael · **Subject:** One bridge, any month
>
> Your June bridge works. The board pack needs the same bridge for every month, and copying the
> script once per month is how mistakes creep in. This one turns your bridge into something you can
> run for any month. Start with May and June.
>
> — David

Expect about 1 hour 15 minutes.

## The goal

The bridge for May and June side by side, from **one** piece of code, each month checked to tie:

```
  month  opening    new  expansion  contraction   churn  closing
2026-05      ...    ...        ...          ...     ...      ...
2026-06 160075.5 2420.0     1340.0       -330.0  -675.0 162830.5
```

June's row is the one you built in PD3.

## The idea

Your PD3 script does one month. For May, the steps are exactly the same. Only two things change:
which list is the opening (April's) and which is the closing (May's).

So instead of copying the script:

1. **Give the steps a name, with the two files as inputs.** That's a **function**. You run all its
   steps by writing its name and the two files.
2. **Have it hand back one row** of the bridge: month, opening, new, expansion, contraction, churn,
   closing.
3. **Run it for May and for June**, and put the two rows in one table.

This is how analysts handle anything that repeats every month: the steps live in one place, so a
fix you make once is fixed for every month.

The examples below build the first two pieces on PD3's tiny example lists. Then the steps do the
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
git checkout -b student/pd4_one_function
git log origin/main..HEAD --oneline
```

The last command lists any work on your new branch that isn't on main yet. You just made the branch
from main, so it must print nothing: that means you're starting clean.

In Explorer, check that `closes/` has a folder for every month from `2025-12` to `2026-06`.

---

## Learn it

Clear `scratch.py` and start with `import pandas as pd`. The examples use PD3's two example lists.

### Example 1 — A function: a name for some steps

Start with the smallest function: one input, one result.

```python
import pandas as pd

def add_up(file):                       # create a function called add_up, with one input called file
    customers = pd.read_csv(file)       # read the file into a table (a DataFrame)
    total = customers["mrr"].sum()      # add up its mrr column
    return total                        # hand total back to the line that ran add_up

may_total = add_up("assignments/python/pd3_examples/may_example.csv")    # run add_up on the May file
print(may_total)
june_total = add_up("assignments/python/pd3_examples/june_example.csv")  # same steps, the June file
print(june_total)
```

```
2300
2500
```

`def` only creates the function: nothing runs until a line calls it, like `add_up("...")`. Each time,
`file` is whatever you put in the brackets. The steps are the lines indented under `def`, and the
function ends where the indenting ends. Two things to watch: indent every step by the same amount,
and end with `return`. Without `return`, the function hands back nothing (Python shows `None`).

### Example 2 — Return a whole row

A bridge gives several numbers, not one. So the function returns one **row**, written as a dict:
column name → value, inside `{ }`. The example lists have one row per customer, so this row counts
customers.

```python
def summary(month, file):                 # two inputs this time, separated by a comma
    customers = pd.read_csv(file)         # read the file into a table
    row = {                               # one row: column name → value
        "month": month,                   # the month you passed in
        "customers": len(customers),      # how many customers (rows) in the file
        "mrr": customers["mrr"].sum(),    # their total MRR
    }
    return row                            # hand the whole row back

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
print(pd.DataFrame([may_row]))            # a list with one row → a one-row table
```

```
  month  customers   mrr
0   May          3  2300
```

A table is a list of rows. Two rows work the same way: put both in the list.

```python
june_row = summary("June", "assignments/python/pd3_examples/june_example.csv")
print(pd.DataFrame([may_row, june_row]))  # two rows → a two-row table, in the order you list them
```

```
  month  customers   mrr
0   May          3  2300
1  June          3  2500
```

The `[ ]` matters: `pd.DataFrame(may_row)` without it fails with
`ValueError: If using all scalar values, you must pass an index`.

---

## Your turn

Right-click `submissions/python` → **New File** → `pd4_one_function.py`. Type the code, fill each
blank (`____`), press ▶ after every step and look at each print before going on.

### Step 1 — Turn your June bridge into a function

This is your PD3 Steps 1–3 inside a function, so open your `pd3_june_movements.py` next to it: the
comments show which PD3 step each block comes from, and the blanks are the same as in PD3. Two
changes from PD3: the files come in as inputs, and the names say `open` and `close` instead of May
and June, because it now works for any month.

```python
import pandas as pd


def bridge(month, opening_file, closing_file):
    # PD3 Step 1: read the two lists, one row per customer
    opening = pd.read_csv(opening_file)
    closing = pd.read_csv(closing_file)
    open_cust = opening.groupby("customer_id", as_index=False)["mrr"].sum()
    close_cust = closing.groupby("customer_id", as_index=False)["mrr"].sum()
    # PD3 Step 2: side by side, no row = zero MRR, change per customer
    both = pd.merge(open_cust, close_cust, on="customer_id", how="____",
                    suffixes=("_open", "_close"), indicator=True)
    both = both.fillna(0)
    both["change"] = both["mrr_close"] - both["mrr_open"]
    # PD3 Step 3: split into the four movements
    new = both[both["_merge"] == "right_only"]
    churn = both[both["_merge"] == "left_only"]
    stayed = both[both["_merge"] == "both"]
    expansion = stayed[stayed["change"] > 0]
    contraction = stayed[stayed["change"] < 0]
    row = {                                     # Example 2: one row of the bridge
        "month": month,
        "opening": opening["mrr"].sum(),
        "new": new["change"].sum(),
        "expansion": ____["change"].sum(),
        "contraction": contraction["change"].sum(),
        "churn": ____["change"].sum(),
        "closing": closing["mrr"].sum(),
    }
    return ____


print("1. JUNE FROM THE FUNCTION")
june = bridge("2026-06", "closes/2026-05/subscriptions_2026-05-31.csv",
              "closes/2026-06/subscriptions_2026-06-30.csv")
print(pd.DataFrame([june]).to_string(index=False))
```

Everything from `opening = ...` to `return` is indented under `def`: that's what makes it part of the
function. The `def` block runs only when you call `bridge(...)`, on the line `june = bridge(...)`.

**Check it worked:** the June row shows the same opening, New, Expansion, Contraction, Churn and
closing as your PD3 output.

### Step 2 — Run it for May too

May's opening is April's closing list, and its closing is May's list.

```python
print()
print("2. MAY AND JUNE")
may = bridge("2026-05", "closes/2026-04/subscriptions_2026-04-30.csv",
             "closes/2026-05/subscriptions_2026-05-31.csv")
table = pd.DataFrame([____, ____])                     # May first, then June
print(table.to_string(index=False))
```

That's it: the same function, two different files. You didn't copy a single step.

**Check it worked:** two rows, May then June, and May's `closing` is the same number as June's
`opening`. (May's closing list is June's opening list.)

### Step 3 — Check that each month ties

Your PD3 Step 4 checked June: opening + the four movements − closing = 0. As a **column**, the same
check runs for every row of the table at once (column math, like `change` in PD3):

```python
print()
print("3. DOES EACH MONTH TIE?")
table["check"] = table["opening"] + table["new"] + table["expansion"] + table["contraction"] + table["churn"] - table["closing"]
print(table[["month", "opening", "closing", "____"]].to_string(index=False))
```

**Check it worked:** `check` is 0.0 for both months. If it isn't, the bridge has dropped a customer:
check `how=` in Step 1.

### Step 4 — Add April

No hints this time: write this step's code yourself. Add April as a third month (April's opening
is March's list, its closing is April's), and print all three months with their check, April first.
Your output must look like this, with your numbers:

```
4. APRIL TOO
  month  opening    new  expansion  contraction   churn  closing  check
2026-04      ...    ...        ...          ...     ...      ...    ...
2026-05      ...    ...        ...          ...     ...      ...    ...
2026-06      ...    ...        ...          ...     ...      ...    ...
```

Every number comes from the function: no typed-in figures. Every `check` must be 0.0.

---

## Hand in

Commit `submissions/python/pd4_one_function.py` only (not `scratch.py`): **Source Control** → `+` on
the file → message `Complete: PD4 — one function` → **Commit** → **Publish Branch**. Then open a PR
from `student/pd4_one_function` to `main` with this description:

~~~
## PD4 — May and June from one function

## My output (pasted from my terminal)
```
[paste the full output here]
```

## One question
How many lines of code did it take to add April in Step 4, and what would it have taken without
the function? (2 sentences)

## How it went
How long did it take, and where did you get stuck?
~~~
