# FN2 — Build a big function from small ones
### Idynamics Finance Analyst Training Program

> **From:** David Chen, VP Finance · **To:** Michael · **Subject:** How many customers did we win and lose?
>
> The board liked the MRR bridge. Their next question is about customers, not dollars: how many did
> we start the half with, how many did we win, how many did we lose, and how many do we have now?
> I'd like that as a customer bridge, for H1 and for every month.
>
> — David

Expect about 2 hours.

## The goal

A customer bridge: the same shape as your MRR bridge, but counting customers instead of adding up MRR.

```
      period  opening  new  churned  closing  check
H1 (Dec-Jun)      ...  ...      ...      ...      0
```

Then the same table for every month from January to June, saved as a file.

## Why this, and when you'd use it

Boards look at two bridges side by side: the MRR bridge (how much money) and the customer bridge
(how many customers). MRR can grow while customer numbers fall, if a few big customers expand and
many small ones leave, so the board wants both.

`bridge` was a long function, and long functions are hard to write in one go. The way analysts
write them: **split the job into small functions, test each one on its own, then call them inside
the big one.** If the big function goes wrong, you already know the small ones work, so you know
where to look. In Excel it's the same idea as helper columns: you check each column before you build
the final formula on top of them. It's standard practice for any calculation longer than a few lines.

You'll write three small functions and put them together into `customer_bridge`.

Here are the tools you know. Everything in this assignment uses them, plus one new idea:

| If a step needs… | Tool | Where you learned it |
|---|---|---|
| **one total per group** (one row per customer) | `groupby("customer_id", as_index=False)["mrr"].sum()` | PD1, PD3 |
| **how many rows** a table has | `len(table)` | PF1, FN1 |
| **some rows** of a table | filter: `df[df["col"] == ...]` | PD1, PD1b |
| what **changed between two lists** | `pd.merge(..., how="outer", indicator=True)`, then `fillna(0)` | PD3 |
| **a row** of a table, from a function | a dictionary `{"period": ..., ...}`, then `return row` | PD4 |
| **the same steps for every month** | `rows = []`, a `for` loop with `rows.append(...)`, then `pd.DataFrame(rows)` | PD5 |
| **a file** someone can open in Google Sheets | `df.to_csv(path, index=False)` | PD5 |
| **the same steps more than once** | a function that `return`s its answer | PD4, FN1 |
| **NEW:** a **big job in small pieces** | call your own function inside another function | this assignment |

---

## Step 0 — Set up

In VS Code, **Terminal → New Terminal**:

```
git status
```

It must say `nothing to commit, working tree clean`. If it lists files, message me before going on.

```
git checkout main
git branch --show-current
```

The second command must print `main`. If it prints anything else, stop and message me.

```
git pull origin main
git checkout -b student/fn2_customer_bridge
git log origin/main..HEAD --oneline
```

The last command must print nothing: you've just made the branch from main, so it holds no work yet.
If it prints anything, stop and message me.

Right-click `submissions/python` → **New File** → `fn2_customer_bridge.py`. Try the examples below in
your `scratch.py`, and write your steps in `fn2_customer_bridge.py`.

---

## Learn it — a big function from small ones

**Read this whole section carefully before you start Step 1, and type the examples into
`scratch.py`.**

### First, the plan

Here's a small version of the job: *"For any month-end list, show Monthly MRR, Annual MRR and the
total, as one row, with a check."* My plan, using the same five questions as FN1:

```python
# My plan
# 1. The answer looks like: one row per list: period, monthly, annual, total, check.
# 2. The information is in: the month-end list, billing_cycle and mrr columns.
# 3. Steps → tools: MRR for one billing cycle (a small function: cycle_mrr, from FN1)
#    → call it twice, for Monthly and Annual, inside a bigger function → put the answers in a row → return it.
# 4. I'll know it's right because: monthly + annual - total = 0 (every row is one or the other).
# 5. What changes next time (my inputs): the period name and the file.
```

The plan already splits the job: a small function that does one thing, and a bigger one that uses it.

### Example 1 — The small function, tested on its own

You wrote this function in FN1's Learn it, so write it again yourself, from these instructions.
Clear `scratch.py` and start with:

```python
import pandas as pd

DEC = "closes/2025-12/subscriptions_2025-12-31.csv"
JUN = "closes/2026-06/subscriptions_2026-06-30.csv"
```

Then write a function called `cycle_mrr` with two inputs: `file` and `cycle`. Inside it:

1. read the file with `pd.read_csv`, into a table called `subs`;
2. filter `subs` on `billing_cycle` equal to `cycle` (`==`), and keep the result in a table called `picked`;
3. use `.sum()` on `picked`'s `mrr` column, and `return` that total.

Call it twice for June, once with `"Monthly"` and once with `"Annual"`, and print both answers.
You should see:

```
126075.0
36755.5
```

Two different answers, so both inputs are used. If yours are different, compare your function with
the one in FN1's Learn it. Once the numbers match, the small function works, and you can build on it.

### Example 2 — Build one row, then a function that returns it, then a table

**What we want:** one row per month-end list, with that list's Monthly MRR, Annual MRR, the total,
and a check. Later, a table of those rows.

A table is built from rows. So we go in three moves, and print after each one so you see what you
have: **(a)** build one row for June with plain steps; **(b)** put those steps in a function that
returns the row; **(c)** call it for two lists and put the rows in a table.

**(a) One row for June, with plain steps.** First the three numbers. Use your `cycle_mrr` to put
June's Monthly MRR in a variable called `monthly`, and June's Annual MRR in `annual`. Then the
whole list's total, read straight from the file:

```python
total = pd.read_csv(JUN)["mrr"].sum()      # read June's list and add up all its MRR, in one line
```

Print the three:

```
126075.0
36755.5
162830.5
```

Now put them in a row. A row is a dictionary, as in your `bridge` (PD4): each **key** (on the left
of `:`) becomes a **column name**, and each **value** (on the right) is what goes in that column:

```python
row = {
    "period": "2026-06",                   # column "period" holds the text 2026-06
    "monthly": monthly,                    # column "monthly" holds the number in monthly
    "annual": annual,
    "total": total,
    "check": monthly + annual - total,     # worked out here: must be 0
}
print(row)
```

```
{'period': '2026-06', 'monthly': np.float64(126075.0), 'annual': np.float64(36755.5), 'total': np.float64(162830.5), 'check': np.float64(0.0)}
```

That's one row: five column names, each with its value. `np.float64(126075.0)` is how pandas labels
a number it calculated (as in PD4). It's still 126075.0. On your laptop it may print as just `126075.0`:
that depends on the versions installed, and either is fine.

To see it as a table, put the row in a list (`[ ]`) and make a DataFrame:

```python
print(pd.DataFrame([row]).to_string(index=False))
```

```
 period  monthly  annual    total  check
2026-06 126075.0 36755.5 162830.5    0.0
```

The keys became the column names and the values filled the one row.

The `total` comes straight from the file, not from `monthly + annual`. That's what makes the check
worth having: if `cycle_mrr` were wrong, `check` would not be 0.

**(b) Make it a function.** Next month you'll want the same row for another list. What changes? The
**period name** and the **file**: those are the inputs. Put the steps from (a) inside a function and
swap each fixed value for its input. The first line is the new idea: the big function **calls your
small function** and keeps what it returns. Fill the blanks:

```python
def cycle_split(period, file):
    monthly = cycle_mrr(file, "Monthly")   # run cycle_mrr on this file; keep its answer in monthly
    annual = ____                          # the same for Annual
    total = pd.read_csv(____)["mrr"].sum()
    row = {
        "period": ____,
        "monthly": monthly,
        "annual": annual,
        "total": total,
        "check": monthly + annual - total,
    }
    return ____                            # hand the row back, as bridge does

print(cycle_split("2026-06", JUN))
print(cycle_split("2025-12", DEC))
```

```
{'period': '2026-06', 'monthly': np.float64(126075.0), 'annual': np.float64(36755.5), 'total': np.float64(162830.5), 'check': np.float64(0.0)}
{'period': '2025-12', 'monthly': np.float64(106314.0), 'annual': np.float64(36755.5), 'total': np.float64(143069.5), 'check': np.float64(0.0)}
```

The June row is the same as in (a), so the function does what the plain steps did. The December row
is different, so the inputs are used.

Read it aloud: "cycle_split takes a period and a file; it asks cycle_mrr for the Monthly total and the
Annual total, reads the whole list's total on its own, and returns them as one row with a check."

**(c) Two rows, one table.** Each call gives one row. Put the rows in a list, then make the table,
as in PD5:

```python
rows = [cycle_split("2025-12", DEC), cycle_split("2026-06", JUN)]   # a list of two rows
print(len(rows))
table = pd.DataFrame(____)                                          # a list of rows → a table
print(table.to_string(index=False))
```

```
2
 period  monthly  annual    total  check
2025-12 106314.0 36755.5 143069.5    0.0
2026-06 126075.0 36755.5 162830.5    0.0
```

Two rows in the list, two rows in the table. That's how every bridge you've built works: a function
builds one row, and the table is the rows put together.

### Watch out: `print` instead of `return`

When one function calls another, `return` is what passes the answer along. Here `cycle_mrr` prints
its total instead of returning it:

```python
def cycle_mrr(file, cycle):
    subs = pd.read_csv(file)
    picked = subs[subs["billing_cycle"] == cycle]
    print(picked["mrr"].sum())                       # shows the number, hands nothing back

print(cycle_split("2026-06", JUN))
```

```
126075.0
36755.5
Traceback (most recent call last):
  ...
    "check": monthly + annual - total,
             ~~~~~~~~^~~~~~~~
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
```

The numbers appear on screen, but `monthly` and `annual` are `None`: nothing came back, so
`cycle_split` can't add them. **A function hands its answer back with `return`, and you print
outside it.** If you see `NoneType` in an error, look for a function that prints instead of
returning.

Put `return picked["mrr"].sum()` back before you go on.

---

## Your turn — the customer bridge

At the top of `fn2_customer_bridge.py`:

```python
import pandas as pd

DEC = "closes/2025-12/subscriptions_2025-12-31.csv"
JUN = "closes/2026-06/subscriptions_2026-06-30.csv"
```

For every step, write your plan as comments first (the five questions), then the function under it.
Try it in `scratch.py` as you go. Each step gives you less help than the one before. If you get
stuck, go back to Learn it: it does the same thing on a smaller job.

### Step 1 — One row per customer

The bridge compares customers, but a month-end list has one row per **subscription**. So the first
small function turns a list into one row per customer.

Fill the blanks in the plan, then in the code:

```python
# Step 1
# 1. The answer looks like: a table, one row per customer, with ____ and ____ as columns.
# 2. The information is in: one month-end list.
# 3. Steps → tools: read the file → one row per customer (____) → return the table.
# 4. I'll know it's right because: December has ____ customers and June ____ (my FN1 Step 1 output).
# 5. What changes next time (my inputs): the file.
def per_customer(file):
    subs = pd.read_csv(file)
    customers = subs.groupby("customer_id", as_index=____)["mrr"].sum()
    return ____
```

Then print, using `len()` outside the function:

```
1. ONE ROW PER CUSTOMER
December: ... customers
June: ... customers
```

**Check:** the two counts must equal your FN1 Step 1 output. They're in your FN1 pull request on
GitHub (#39) → "My output". Then, in `scratch.py`, print `per_customer(JUN).head()`: `customer_id` and `mrr` must be
side by side on one header line. If `customer_id` sits on a line by itself, it's the index, not a
column (FN1 feedback, Step 4), and the merge in Step 2 won't work.

### Step 2 — Opening and closing side by side

The second small function puts two lists side by side, the way `bridge` did in PD3/PD4. This time
it calls `per_customer` instead of repeating the groupby.

Fill the blanks in the plan, then write the code yourself:

```python
# Step 2
# 1. The answer looks like: one table, ____
# 2. The information is in: ____
# 3. Steps → tools: ____ twice → ____ on customer_id → ____ → a change column → return the table.
# 4. I'll know it's right because: ____
# 5. What changes next time (my inputs): ____
```

Call the function `side_by_side`. Use `suffixes=("_open", "_close")`, so the MRR columns are
`mrr_open` and `mrr_close`, and add a `change` column (closing minus opening).

Call it for H1 (December to June). Outside the function, keep the new customers (rows only on the
closing list) and print how many there are and their MRR, after a blank line:

```
2. SIDE BY SIDE
H1 new customers: ...  New MRR: ...
```

`New MRR` is the sum of their `change`, printed with `:,.2f`.

**Check:** `New MRR` must equal the H1 `new_mrr` in your checkpoint table. It's in your checkpoint
pull request on GitHub (#38) → "My output".

### Step 3 — The customer bridge for H1

Now the big function, built from your two small ones. No blanks from here: write all five plan
lines yourself, then the code. You've already done every piece of it; this step puts them together.

Call it `customer_bridge`. It returns one row with these keys, in this order: `period`, `opening`,
`new`, `churned`, `closing`, `check`.

- `opening` and `closing`: how many customers are on the opening list and on the closing list.
- `new`: how many customers are only on the closing list. `churned`: how many are only on the opening list.
- `check`: opening + new − churned − closing. It must be 0.

Make the check worth having, as `total` was in Learn it: it should be able to catch a mistake.

Try to write it yourself first, from the list above. Only if you get stuck, look at where you've
already done each piece:

**If you're stuck: where you've done each piece**

| To get… | You did it in… |
|---|---|
| how many customers are on a list | Step 1: `len()` of what `per_customer` returns |
| the customers only on the closing list | Step 2: the filter you used for the new customers |
| the customers only on the opening list | the same filter, with the other `_merge` value (PD3) |
| a function that returns one row | Learn it, Example 2(b): `cycle_split` |

**A good way to start:** do it for H1 with plain steps in `scratch.py` first, and print each number,
as in Example 2(a). When the four numbers look right, put the steps inside the function, swap the
fixed values for its inputs, and `return` the row.

Call it for H1 (December to June), and print the row as a table, as in Example 2(a), after a blank
line:

```
3. H1 CUSTOMER BRIDGE
      period  opening  new  churned  closing  check
H1 (Dec-Jun)      ...  ...      ...      ...    ...
```

**Check:** `check` is 0. `opening` and `closing` equal your Step 1 counts, and `new` equals your
Step 2 count.

### Step 4 — Every month

On your own: write all five plan lines yourself, then the code. It's a small step, and it's your
PD5 loop with a different function inside.

Run `customer_bridge` for every month from January to June. The list of months is `MONTHS` in your
PD5 file, `submissions/python/pd5_every_month.py`: copy it into this file. Print the table after a
blank line, then save it to `submissions/python/fn2_customer_bridge.csv`:

```
4. EVERY MONTH
 period  opening  new  churned  closing  check
2026-01      ...  ...      ...      ...    ...
...
2026-06      ...  ...      ...      ...    ...
Saved submissions/python/fn2_customer_bridge.csv
```

Try to write it yourself first. Only if you get stuck, look back:

**If you're stuck:** the loop in your PD5 file (`rows = []` before the loop,
`rows.append(...)` inside it, `pd.DataFrame(rows)` after it) and the `to_csv` line from PD5. Two
things to look at as you adapt it: call `customer_bridge` instead of `bridge`, and make every name
inside `m[...]` one of the keys in `MONTHS` (`"month"`, `"opening"`, `"closing"`). A name that
isn't there stops the loop with a `KeyError`.

**Check:** every `check` is 0. January's `opening` equals December's count from Step 1, June's
`closing` equals June's count from Step 1, and the six `new` values add up to H1's `new` in Step 3.

**Run the whole file once more before you commit,** and paste that output, not an earlier one.

---

## Hand in

Commit `submissions/python/fn2_customer_bridge.py` only (not `scratch.py`; the CSV won't show up):
**Source Control** → `+` on the file → message `Complete: FN2 — customer bridge` → **Commit** →
**Publish Branch**. Then open a PR from `student/fn2_customer_bridge` to `main` with this description:

~~~
## FN2 — Build a big function from small ones

## My output (pasted from my terminal)
```
[paste the full output here]
```

## One question
Two sentences for the board, using your Step 3 and Step 4 tables: how did our customer count
change in H1, and in which months did we lose customers?

## Why small functions?
Why build customer_bridge from per_customer and side_by_side, instead of writing it as one long
function? (2 sentences)

## How it went
How long did it take, and where did you get stuck?
~~~
