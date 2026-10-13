# PD1b — Read a pandas line
### Idynamics Finance Analyst Training Program

> **From:** David Chen, VP Finance · **To:** Michael · **Subject:** One short one before PD2
>
> In your PD1 notes you said you had to review the basics first, and that Step 5 was hard until you
> saw the filter goes on `by_seats`. Before you write pandas from a blank file in PD2, let's make sure
> you can *read* a line. Do this one first, then PD2.
>
> — David

Expect about 1 hour.

## Why this

A line like `june[june["mrr"] >= 5000]` is a few small steps written together. You'll learn to read
it, and to take it apart: build each piece as its own variable and print it, so you see what it
holds. When a line doesn't do what you expect, that's how you find out why.

## Step 0 — Set up

In VS Code, **Terminal → New Terminal**:

```
git status
```

It must say `nothing to commit, working tree clean`. If it lists files, message me before going on.

```
git checkout main
git pull origin main
git checkout -b student/pd1b_read_pandas
git log origin/main..HEAD --oneline
```

The last command must print nothing.

---

## Learn it

Use `scratch.py` in `submissions/python` (not submitted; if it's gone: right-click
`submissions/python` → **New File** → `scratch.py`). Clear it and start with:

```python
import pandas as pd

subs = pd.read_csv("assignments/python/pd1_examples/example_list.csv")
```

That's PD1's 5-row example list. We print without `.to_string(index=False)` here, so you see the row
numbers on the left.

### Example 1 — The three kinds of brackets

| Bracket | Means | Examples you've used |
|---|---|---|
| `( )` | **do something** | `len(subs)`, `.sum()`, `.sort_values("mrr")`, `print(...)` |
| `[ ]` right after a name | **pick from it** | `subs["mrr"]` |
| `[ ]` on its own | **a list** | `["subscription_id", "mrr"]` |
| `{ }` | a **dict**, or in an f-string **put a value here** | `{"name": "Delta"}`, `f"{total:,.2f}"` |

A **dot** means "then do this to it": `subs["mrr"].sum()` is "pick mrr, then add it up".

### Example 2 — A filter, read from the inside out

`subs[subs["mrr"] >= 1000]` is three steps. Build each one and print it.

**Step 1: pick the column.**

```python
mrr = subs["mrr"]
print(mrr)
```

```
0    1200
1    3000
2     800
3     950
4    6000
Name: mrr, dtype: int64
```

**Step 2: ask the question of every row.** The answer is not one True or False, it's one per row.

```python
is_big = mrr >= 1000       # NEW: a True/False for every row
print(is_big)
```

```
0     True
1     True
2    False
3    False
4     True
Name: mrr, dtype: bool
```

`dtype: bool` means the column holds True/False.

**Step 3: keep the True rows.**

```python
big = subs[is_big]         # NEW: True/False inside [ ] keeps the True rows
print(big)
```

```
  subscription_id customer_id       plan_name billing_cycle   mrr
0          SUB901     CUST901       Sales Hub       Monthly  1200
1          SUB902     CUST902       Sales Hub        Annual  3000
4          SUB905     CUST904  Platform Suite        Annual  6000
```

Rows 0, 1 and 4 are exactly the rows that were True.

**Why `[ ]` gave a column in Step 1 but rows in Step 3:** square brackets after a table look at what
you put inside them.

| Inside `subs[ ]` | You get | Example |
|---|---|---|
| a column name | that **column** | `subs["mrr"]` |
| a list of names | those **columns** | `subs[["subscription_id", "mrr"]]` |
| a True/False for every row | the **rows** that are True | `subs[is_big]` |

**The same in one line:** put each step's code where its name was.

```python
big = subs[subs["mrr"] >= 1000]
print(len(big))
```

```
3
```

Same 3 rows. You'll usually write the one line; the steps are how you check it.

### Example 3 — A groupby, in steps

```python
grouped = subs.groupby("plan_name", as_index=False)   # rows put into groups, one per plan
print(grouped)
```

```
<pandas.api.typing.DataFrameGroupBy object at 0x119525940>
```

Not a table yet: pandas is waiting to be told what to add up. (The `0x...` number changes every run.)

```python
by_plan = grouped["mrr"].sum()                         # pick mrr, add it up in each group
print(by_plan)
```

```
        plan_name   mrr
0   Marketing Pro  1750
1  Platform Suite  6000
2       Sales Hub  4200
```

In one line, as in PD1: `by_plan = subs.groupby("plan_name", as_index=False)["mrr"].sum()`

`by_plan` is a table, so you filter it like `subs`, but the True/False must come from **its own**
column. Here it comes from `subs` (5 rows) instead:

```python
print(by_plan[subs["mrr"] >= 1000])
```

```
...scratch.py:12: UserWarning: Boolean Series key will be reindexed to match DataFrame index.
  print(by_plan[subs["mrr"] >= 1000])
        plan_name   mrr
0   Marketing Pro  1750
1  Platform Suite  6000
```

Wrong: Sales Hub (4,200) is missing. pandas matched `subs`'s rows 0 and 1 (True) onto `by_plan`'s rows
0 and 1, which are different things. It only warns and carries on. (The start of the warning line is your
file's path and line number.) The right way: `by_plan[by_plan["mrr"] >= 1000]`.

### Example 4 — Read a line aloud

Find the `=`: the name on the left is what you're creating. Then read the right side: brackets
inside brackets from the inside out, dots left to right.

| Line | Read aloud |
|---|---|
| `big = subs[subs["mrr"] >= 1000]` | "big is: from subs, keep the rows where subs's mrr is at least 1,000." |
| `by_plan = subs.groupby("plan_name", as_index=False)["mrr"].sum()` | "by_plan is: group subs by plan_name, pick mrr, add it up in each group." |
| `print(big[["subscription_id", "mrr"]])` | "print: from big, pick the columns subscription_id and mrr." |

### When it goes wrong

| You write | Python says | Fix |
|---|---|---|
| `subs("mrr")` | `TypeError: 'DataFrame' object is not callable` | you can't *do* a table, pick from it: `subs["mrr"]` |
| `len[subs]` | `TypeError: 'builtin_function_or_method' object is not subscriptable` | you can't *pick from* an action, do it: `len(subs)` |
| `by_plan[subs["mrr"] >= 1000]` | `UserWarning: Boolean Series key will be reindexed to match DataFrame index.` and the wrong rows | build the True/False from the table you are filtering: `by_plan[by_plan["mrr"] >= 1000]` |

"not callable" → you need `[ ]`. "not subscriptable" → you need `( )`. The third one only warns and
carries on with wrong rows, so read warnings.

---

## Your turn

Right-click `submissions/python` → **New File** → `pd1b_read_pandas.py`. Type the code, fill each
blank (`____`), press ▶ after every step and look at each print before going on.

### Step 1 — Monthly subscriptions, in steps

How many of June's subscriptions are billed monthly?

```python
import pandas as pd

june = pd.read_csv("closes/2026-06/subscriptions_2026-06-30.csv")

print("1. MONTHLY SUBSCRIPTIONS, STEP BY STEP")
cycle = june["____"]
print(cycle.head())                # NEW: .head() prints only the first 5 rows
is_monthly = cycle == "____"
print(is_monthly.head())
monthly = june[____]
print(monthly[["subscription_id", "billing_cycle", "mrr"]].head())
print(f"Steps:    {len(monthly)} subscriptions")
monthly_one_line = june[june["billing_cycle"] == "Monthly"]
print(f"One line: {len(monthly_one_line)} subscriptions")
```

`dtype: str` under `cycle` means the column holds text.

**Check it worked:** both counts are the same, and every row in the `monthly` peek says `Monthly`.

### Step 2 — Plans with 30,000 MRR or more, in steps

```python
print()
print("2. PLANS WITH 30,000 MRR OR MORE, STEP BY STEP")
grouped = june.groupby("____", as_index=False)
print(grouped)
by_plan = grouped["____"].sum()
print(by_plan)
is_large = by_plan["mrr"] >= ____
print(is_large)
large_plans = ____[is_large]
print(large_plans)
large_one_line = by_plan[by_plan["mrr"] >= 30000]
print(f"Steps: {len(large_plans)} plans  One line: {len(large_one_line)} plans")
```

The blank before `[is_large]` is the table you are filtering: which table does `is_large` belong to?

**Check it worked:** both counts are the same, and every plan in `large_plans` has `mrr` of 30,000 or more.

### Step 3 — Fix two broken lines

Add these to the end of your file exactly as written and press ▶:

```python
print()
print("3. FIXED LINES")
print(len[june])
print(f"{june('mrr').sum():,.2f}")
```

Read the last line of the error, fix that bracket, run again, and fix the next one. Before each fix,
copy the error's last line into a comment (`#`) at the bottom of `scratch.py`.

**Check it worked:** the file runs to the end and prints 57 and the June total MRR, the same as your
PD1 Step 1.

### Step 4 — Read four lines aloud

These are from your PD1 script. Write one sentence for each, as in Example 4, as a comment at the
bottom of `scratch.py`. If you're unsure, take the line apart and print each piece, as in Example 2.

1. `annual = june[june["billing_cycle"] == "Annual"]`
2. `share = big["mrr"].sum() / june["mrr"].sum() * 100`
3. `by_seats = june.groupby("customer_id", as_index=False)["seats"].sum()`
4. `print(f"Total MRR: {june['mrr'].sum():,.2f}")`

---

## Hand in

Commit `submissions/python/pd1b_read_pandas.py` only (not `scratch.py`): **Source Control** → `+` on
the file → message `Complete: PD1b — read a pandas line` → **Commit** → **Publish Branch**. Open a PR
from `student/pd1b_read_pandas` to `main` with this description (the errors and sentences are the
comments in your `scratch.py`):

~~~
## PD1b — Read a pandas line

## My output (after the fixes)
```
[paste the full output here]
```

## Step 3 — the two errors (last line of each)
1.
2.

## Step 4 — four lines read aloud
1.
2.
3.
4.

## How it went
How long did it take, and where did you get stuck (if anywhere)?
~~~

Then start PD2.
