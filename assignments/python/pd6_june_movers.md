# PD6b — Who moved in June?
### Idynamics Finance Analyst Training Program

> **From:** David Chen, VP Finance · **To:** Michael · **Subject:** Names behind the June bridge
>
> The board saw your June bridge and asked the obvious next question: *who* are these customers?
> They want one list of everyone who moved in June — company name, industry, what kind of move,
> and how much. `CUST048` means nothing to them.
>
> The company names are in the customer list. It's in the repo next to the June month-end list:
> `closes/2026-06/customers_2026-06-30.csv`. You'll get it when you pull main.
>
> One other thing. On Quiz 3 you hit `ValueError: Cannot use name of an existing column for
> indicator column` and worked around it with two chained merges. The workaround was fine, but
> the error was telling you something useful, so I've explained it below.
>
> — David

Expect about 90 minutes.

---

## Why this one

You can already split May and June into new / expansion / contraction / churn. What you can't do
yet is **put those four tables back together into one**.

That matters more than it sounds. Almost every finance deliverable is several small tables stacked
into one: twelve months of a bridge, four quarters of a P&L, three regions of a pipeline. You build
each piece, label it so you can still tell them apart, and stack them. Do it with a loop and it
scales to any number of pieces, which is the whole trick behind "one script, every month".

Two new things here, and that's all: **labelling a table**, and **stacking tables**.

---

## Step 0 — Set up

```
git checkout main
git pull origin main
git checkout -b student/pd6_june_movers
git status
```

`git status` must say `nothing to commit, working tree clean`. After the pull you should have
`closes/2026-06/customers_2026-06-30.csv` — check it's there before you start, and
`print(customers.head())` to see the columns.

---

## Learn it

### What `_merge` actually is

You've used `indicator=True` several times now, so here is what it's doing.

It adds **one extra column**, called `_merge`, which records **which table each row came from**. It
only ever holds three values:

| `_merge` | means |
|---|---|
| `both` | the key was in both tables |
| `left_only` | in the left table only |
| `right_only` | in the right table only |

That's why one outer merge answers several questions at once — you're not re-joining, you're just
filtering a column that was already there.

And that is also the error you hit:

```
ValueError: Cannot use name of an existing column for indicator column
```

pandas wants to add a column called `_merge`, looks, and finds you already have one — because a
previous merge put it there. It won't overwrite it, so it stops.

Two ways out, and you want the first:

```python
movers = movers[["customer_id", "movement", ...]]   # keep only what you need; _merge goes
movers = movers.drop(columns="_merge")              # or drop it explicitly
```

Keeping only the columns you need is the better habit anyway. A table that carries every column
from every merge gets unreadable fast, and this is pandas telling you so.

Your two-chained-merges workaround on Quiz 3 worked, and knowing both routes is genuinely useful —
but reach for it because you chose to, not because something broke.

### Stack tables — `pd.concat`

`pd.concat` takes a **list** of tables and puts them on top of each other, in list order:

```python
movers = pd.concat([new, expansion, contraction, churn])
```

Four tables in, one table out. The columns line up by name.

You already know the loop version of this. Here is your own Quiz 3, Q8:

```python
enrollments_row = []
for enroll in ["2026-07", "2026-08", "2026-09"]:
    enrollments_row.append(month_stats(enrollments, enroll))
enrollments_table = pd.DataFrame(enrollments_row)
```

Identical shape — empty list, loop, `.append`, build once at the end. The only difference is what
you append. There you appended **dictionaries**, so you finished with `pd.DataFrame(...)`. When you
append **tables**, you finish with `pd.concat(...)` instead. Same pattern, one word changes.

**Common mistake:** `pd.concat(new, expansion)` — passing the tables as separate arguments. It
needs one list: `pd.concat([new, expansion])`. The error is
`TypeError: concat() takes 1 positional argument but 2 were given`, which is pandas telling you it
wanted one thing (a list) and you handed it two.

### Label a table — a column with the same value on every row

Give a column one value and every row gets it:

```python
new["movement"] = "New"
```

No loop, no list — pandas fills the whole column. That's how you keep track of which piece is which
once you've concatenated them, and it's the step people forget: stack four unlabelled tables and you
get one table where nothing tells you which row came from where.

**Common mistake:** labelling *after* you stack. Once they're one table it's too late — label each
piece first, while you still know what it is.

---

## Your turn

### Step 1 — Label June's four movements

Build the four tables as you did for the bridge, then give each one a `movement` column:
`New`, `Expansion`, `Contraction`, `Churn`.

*Plan it first, in comments above your code:* what does the answer look like · where is the
information · which tool for each step · how will you know it's right.

Print it under a numbered heading, as in PD3 and PD5, so the four sections are easy to read:

```
1. LABEL EACH MOVEMENT
customer_id  mrr_may  mrr_june  change  movement
    CUST...      ...       ...     ...       New
```

*Check:* the four tables' changes should add up to June MRR minus May MRR.

### Step 2 — One list of movers

Stack the four into one table, then keep only the columns the board list needs.

```
2. ONE LIST OF MOVERS
customer_id    movement  ...  change
    CUST...         New  ...     ...
Movers: ...  Total change: ...
```

*Check:* print the row count and the total change. The total must still be June minus May — if
stacking changed it, you've either dropped a table or counted one twice.

### Step 3 — Add the names, check, save

Look up `company_name` and `industry` from the customer list, biggest gain first, and save it to
`submissions/python/pd6_june_movers.csv`.

```
3. ADD THE CUSTOMER NAMES
Rows: ...  Not found: ...
customer_id  company_name  industry  movement  change
    CUST...           ...       ...       ...     ...
```

*Check:* row count after the lookup must equal the row count before it, and nothing should fail to
find a name. Print both. If a name is missing, say so rather than letting a blank through.

### Step 4 — Change by industry

One short table: total change per industry, biggest first. No hints for how — but print it in the
same shape as the others:

```
4. CHANGE BY INDUSTRY
   industry  change
        ...     ...
Total: ...
```

*Check:* it should still total June minus May.

---

## Hand in

`submissions/python/pd6_june_movers.py`, committed to your branch, and a PR with this
description:

~~~
## PD6b — Who moved in June?

## My output (pasted from my terminal)
```
[paste the whole thing]
```

## One question
In your own words: what does the `_merge` column do, and what was the ValueError on Quiz 3
telling you?

## Why pandas?
Why do this in pandas rather than Excel? Two sentences.

## How it went
How long, and where did you get stuck?
~~~
