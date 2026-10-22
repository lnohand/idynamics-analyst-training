# FN1 — Write your own functions: Feedback

**Status:** Three edits, then approved
**Reviewed by:** David Chen

## This was a hard one

Writing functions from an empty file is a big step, and nobody gets fluent with it from one
assignment. You'll keep writing functions in the next assignments, so it will get easier.

What went well:

- **You chose good inputs.** `customer_count(month)`, `big_customers(month, amount)` and
  `growth(start, end)`: you asked what changes next time, and you got it right every time. That was
  the main point of this assignment.
- **You knew Step 4 needed `pd.merge`.** You said so in your PR: picking the right tool for the job
  is the hard part, and you're getting it.

One habit to build: **answer the five questions before you write any code.** They're how you catch
a mistake like Step 4's before you hand it in.

## Where to find your checks

You asked how you're supposed to do the "I'll know it's right" check, and whether it's in Excel. It's
not in Excel. The check is a number you **already have from somewhere else**, from work you've
already done:

| Step | Check against | Where it is |
|---|---|---|
| 1. Customers | `len()` of the same list, the number of subscriptions (June has 57). Your count must be smaller | Run `len()` in `scratch.py` |
| 2. Big customers | Every MRR in the table is at least the threshold, and the 9,500 table is the top of the 8,000 table | Your own output |
| 3. Growth | `closing` minus `opening` in your **checkpoint** table: 162,830.50 − 143,069.50 = 19,761.00 | Your checkpoint PR on GitHub (#38) → "My output" |
| 4. New MRR | The `new_mrr` column in your **checkpoint** table: 23,030.00 (H1) and 11,010.00 (Q2) | Same place: PR #38 → "My output" |

Your checkpoint file isn't on `main` yet, so you won't see it in VS Code on this branch. Open your
checkpoint pull request on GitHub instead: the output you pasted there is your check.

## Step 1 — right

38 and 45 customers. Nothing to change.

## Step 2 — two things to fix

### `print` or `return`

Your function prints the table inside itself. That shows it on screen, but it doesn't hand
anything back. Try storing what your function gives you:

```python
result = big_customers(JUN, 9500)
print(result)
```

```
9500 or more: customer_id
CUST025    10800.0
CUST016     9530.0
Name: mrr, dtype: float64
None
```

The first four lines are the `print` inside your function. Then `result` is `None`: nothing came
back. James can't sort it, count it or save it, because there's nothing to work with.

With `return`, the function hands the table back, and you decide what to do with it:

```python
def big_customers(month, amount):
    m = pd.read_csv(month)
    totals = m.groupby("customer_id", as_index=False)["mrr"].sum()
    above = totals[totals["mrr"] >= amount]
    return above.sort_values("mrr", ascending=False)

result = big_customers(JUN, 9500)
print(result.to_string(index=False))
print(len(result))
```

```
customer_id     mrr
    CUST025 10800.0
    CUST016  9530.0
2
```

A rule that works every time: **a function hands its answer back with `return`, and you print
outside it.**

### Why `.to_string(index=False)`?

You might wonder why we turn a table into a string just to print it. It doesn't change your table:
`result` stays a table you can still sort, count and save. `.to_string()` only builds the **text**
that gets printed, and it's the only way to tell pandas how to print it. `print()` itself has no
setting to hide the row labels. Here's the same table both ways:

```python
print(result)
print(result.to_string(index=False))
```

```
   customer_id      mrr
23     CUST025  10800.0
14     CUST016   9530.0
customer_id     mrr
    CUST025 10800.0
    CUST016  9530.0
```

The 23 and 14 are leftover row numbers from June's full list: they mean nothing to the reader. On a
table straight from `groupby`, the labels are just 0, 1, 2, so the two prints can look almost the
same. The difference shows up after a filter or a sort, which is most of the time. It
also matters for long tables: a plain `print` cuts out the middle rows and shows `...`, while
`.to_string()` always prints every row. For now, print every table this way.

### `>` or `>=`

James asked for customers at **8,000 or more**. Here's the difference on three made-up customers:

```python
mrr = pd.DataFrame({"customer_id": ["CUST1", "CUST2", "CUST3"], "mrr": [7999.0, 8000.0, 8001.0]})
print(mrr[mrr["mrr"] > 8000].to_string(index=False))
print(mrr[mrr["mrr"] >= 8000].to_string(index=False))
```

```
customer_id    mrr
      CUST3 8001.0
customer_id    mrr
      CUST2 8000.0
      CUST3 8001.0
```

`>` drops CUST2, who is exactly on 8,000. Your answer happened to be right this time only because
no June customer is exactly on 8,000 or 9,500. Next month one could be.

**What to change:** return the table, use `>=`, add `as_index=False` to the groupby, and print the
result under the headings in the brief with `.to_string(index=False)`.

## Step 3 — one small fix

The numbers are right. Add `:,.2f` to the two print lines, so they read `19,761.00` and `9,145.00`.

## Step 4 — what went wrong

Compare it with your checkpoint: 43,080 against 23,030 is far too high, so something is wrong. Two
lines work together.

**1. Your groupby has no `as_index=False`:**

```python
start_mrr = start.groupby("customer_id")["mrr"].sum()
print(start_mrr.head(3))
```

```
customer_id
CUST001    1760.0
CUST002    5885.5
CUST003    4045.0
Name: mrr, dtype: float64
```

`customer_id` isn't a column here. It's the index (the labels down the left side). The only
column left is `mrr`.

**How to tell from the output.** Look at the top line:

- **An index:** its name sits on a line **by itself**, above the values (`customer_id` above, then
  the rows), and there's a footer `Name: mrr, dtype: float64`. That footer means you have a single
  column (a Series), with `customer_id` only as its labels.
- **A column:** all the column names are on **one header line**, side by side.

Here's the same groupby with `as_index=False`:

```python
start_mrr = start.groupby("customer_id", as_index=False)["mrr"].sum()
print(start_mrr.head(3))
```

```
  customer_id     mrr
0     CUST001  1760.0
1     CUST002  5885.5
2     CUST003  4045.0
```

Now `customer_id` and `mrr` share the header line: both are columns. The 0, 1, 2 on the left are
the index, the plain row numbers. This is the shape `pd.merge(..., on="customer_id")` needs.

**2. So the merge couldn't use `customer_id`, and you merged `on="mrr"`.** That matches customers by
their MRR **amount**, not by who they are. Any customer whose MRR changed between December and June
looks like a different customer, so it shows up as "new". That's why you got 16 "new" rows when
only 9 customers are actually new, and 43,080 instead of 23,030.

**The fix:** add `as_index=False` to both groupbys (it keeps `customer_id` as a column, as in PD3),
and merge `on="customer_id"`. The new customers' MRR is then in the column for the ending list.
Run it and compare with your checkpoint again: 23,030.00 and 11,010.00.

## When you've made the changes

Same branch: the PR updates by itself. Run the file, check each step against the table above, then
paste the new output into the PR.

— David
