# FN2 — Build a big function from small ones
### Idynamics Finance Analyst Training Program

> **From:** David Chen, VP Finance · **To:** Michael · **Subject:** How many customers did we win and lose?
>
> The board liked the MRR bridge. Their next question is about customers, not dollars: how many did
> we start the half with, how many did we win, how many did we lose, and how many do we have now?
> I'd like that as a customer bridge for H1.
>
> — David

Expect about 1.5 hours.

## The goal

A customer bridge: the same shape as your MRR bridge, but counting customers instead of adding up MRR.

```
      period  opening  new  churned  closing  check
H1 (Dec-Jun)      ...  ...      ...      ...      0
```

## Why this, and when you'd use it

Boards look at two bridges side by side: the MRR bridge (how much money) and the customer bridge
(how many customers). MRR can grow while customer numbers fall, if a few big customers expand and
many small ones leave, so the board wants both.

`bridge` was a long function, and long functions are hard to write in one go. The way analysts
write them: **split the job into small functions, test each one on its own, then call them inside
the big one.** If the big function goes wrong, you already know the small ones work, so you know
where to look. In Excel it's the same idea as helper columns: you check each column before you build
the final formula on top of them. It's standard practice for any calculation longer than a few lines.

You'll write two small functions, `list_customers` and `combine_lists`, and then `customer_bridge`, which calls them.

Here are the tools you know. Everything in this assignment uses them, plus two new things:

| If a step needs… | Tool | Where you learned it |
|---|---|---|
| **how many rows** a table has | `len(table)` | PF1, FN1 |
| **some rows** of a table | filter: `df[df["col"] == ...]` | PD1, PD1b |
| **two lists in one table**, with a label for which list each row is on | `pd.merge(..., how="outer", indicator=True)` | PD3 |
| **one column** of a table, kept as a table | `df[["col"]]` | PD1 |
| **a row** of a table, from a function | a dictionary `{"period": ..., ...}`, then `return row` | PD4 |
| **the same steps more than once** | a function that `return`s its answer | PD4, FN1 |
| **NEW:** a **big job in small pieces** | call your own function inside another function | this assignment |
| **NEW:** **remove repeated rows** | `df.drop_duplicates()` | this assignment, Step 1 |

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

### First, the plan for the whole job

**The job:** count how customers moved between two month-ends: how many we had at the start
(`opening`), how many we won (`new`), how many we lost (`churned`), and how many we have at the end
(`closing`). Only customers are counted here, not MRR. The information is in the month-end
subscription lists.

**The idea:** turn each month-end list into a list of customers → put the opening and closing
customer lists in one table, with a label on each customer → count the customers and the labels →
put the counts in one row.

You'll write three functions. Here's why each one is needed, and what it does:

**1. `list_customers`.** *Why:* the month-end files are subscription lists, not customer lists.
`customer_id` is not a primary key there (as in SQL: a column where each value appears only once):
a customer with two subscriptions appears twice. To count customers, each customer must appear
once. If our files were customer lists, we wouldn't need this function. *How:* keep only the
`customer_id` column and remove the repeats. We need this for the opening list and for the closing
list, every time, so we write it once, as a function.

**2. `combine_lists`.** *Why:* to find who is new and who left, we need both customer lists in one
table. *How:* merge them (PD3), keeping every customer from either list. The merge adds a `_merge`
column that labels each customer: on both lists, only on the opening list, or only on the closing
list. The function doesn't count anything: it only builds the table. It calls `list_customers` for
each list instead of repeating its lines.

**3. `customer_bridge`.** *Why:* the board wants the counts in one row. *How:* `opening` and
`closing` count the rows of each customer list (from `list_customers`); `new` and `churned` count
the labels in `combine_lists`'s table. It doesn't read or merge anything itself: it calls the two
functions.

In short:

| Step | Function | What it gives back | Which of your functions it calls |
|---|---|---|---|
| 1 | `list_customers(file)` | a customer list: one column, `customer_id`, one row per customer | none |
| 2 | `combine_lists(opening_file, closing_file)` | one table with both customer lists: `customer_id` and `_merge` | `list_customers`, twice |
| 3 | `customer_bridge(period, opening_file, closing_file)` | one row of counts (a dictionary) | `list_customers` and `combine_lists` |

**The rule for this assignment:** when a step needs something an earlier function already does,
**call that function. Don't copy its lines.** If `customer_bridge` has a `read_csv` or a `merge` in
it, it's doing work that belongs to Steps 1 and 2.

At the top of `fn2_customer_bridge.py`:

```python
import pandas as pd

DEC = "closes/2025-12/subscriptions_2025-12-31.csv"
JUN = "closes/2026-06/subscriptions_2026-06-30.csv"
```

Each step: fill the plan's blanks first, then the code's blanks, then run the file and do the check.
Try each step in `scratch.py` as you go, if that helps.

### Step 1 — `list_customers`: a customer list

**What it's for:** turning a subscription list into a customer list (reason 1 above).

**First, look at the data.** Make this a habit: before you work with any CSV, print a few rows to
see its column names and what's in them. In `scratch.py`, read June's list into a table called
`subs` and print its first rows:

```python
subs = pd.read_csv(JUN)
print(subs.head().to_string(index=False))       # the first 5 rows
```

```
subscription_id customer_id            plan_name billing_cycle  seats  price_per_seat  discount_percent    mrr
         SUB002     CUST002       Platform Suite        Annual     26            1800                 0 3900.0
         SUB003     CUST003        Marketing Pro       Monthly     23              85                 0 1955.0
         SUB004     CUST004            Sales Hub       Monthly     18             110                 0 1980.0
         SUB006     CUST006 Analytics Enterprise        Annual     31            2160                 0 5580.0
         SUB007     CUST007        Marketing Pro       Monthly     16              85                 0 1360.0
```

One row per subscription. The only column this step needs is `customer_id`.

**New tool: `drop_duplicates()`.** Why not `groupby`? `groupby` is for working something out per
group, such as adding up each customer's MRR. Here we don't use MRR, so there's nothing to work out:
we only need each `customer_id` once. `drop_duplicates()` does exactly that: it removes repeated
rows from a table and keeps the first of each. Try it in `scratch.py`, one move at a time:

```python
ids = subs[["customer_id"]]          # keep only the customer_id column (a table with one column)
print(len(ids))                      # how many rows: one per subscription
customers = ids.drop_duplicates()    # remove the repeated customer_ids, keep the first of each
print(len(customers))                # how many rows now: one per customer
```

```
57
45
```

57 subscriptions, 45 customers. In one line: `subs[["customer_id"]].drop_duplicates()`.

Keep the `customer_id` column first. `subs.drop_duplicates()` on the whole table removes nothing
(it still has 57 rows): a row only counts as a repeat if **every** column is the same, and every
subscription has its own `subscription_id`.

Now the function. Fill the blanks:

```python
# Step 1
# 1. The answer looks like: a table with one column, ____, one row per customer.
# 2. The information is in: one month-end list.
# 3. Steps → tools: read the file → keep the customer_id column → remove the repeats (____) → return it.
# 4. I'll know it's right because: December has ____ customers and June ____ (my FN1 Step 1 output).
# 5. What changes next time (my inputs): the file.
def list_customers(file):
    subs = pd.read_csv(file)
    customers = subs[["customer_id"]].____()
    return ____
```

Print what the function gives back: the first rows of June's customer list, then the number of
customers in each list:

```python
print("1. CUSTOMER LISTS")
jun = list_customers(JUN)                        # call it for June
print(jun.head().to_string(index=False))         # the first 5 rows of the table it gives back
dec = list_customers(____)                       # call it for December
print(f"December: {len(dec)} customers")         # the total number of customers in December
print(f"June: {____} customers")
```

```
1. CUSTOMER LISTS
customer_id
    CUST002
    CUST003
    CUST004
    CUST006
    CUST007
December: ... customers
June: ... customers
```

**Read the output in two parts.** The table is what `list_customers` gives back: a customer list,
one row per customer. The two lines under it are **only a check**: one row per customer, so the
number of rows is the number of customers, and those counts must match FN1. Step 2 uses the
customer lists, not the counts.

**Check:** the two counts must equal your FN1 Step 1 output: GitHub → your FN1 pull request (#39)
→ "My output".

### Step 2 — `combine_lists`: both customer lists in one table

**What it's for:** putting the opening and closing customer lists in one table, with a label on each
customer (reason 2 above). It doesn't read the files itself: it **calls `list_customers`** for each
list.

Here is the whole function: the code has no blanks, but the five plan lines still do. Type it in
yourself (don't paste it) and read each comment as you go. Then fill the plan's blanks: lines 1–3
and 5 from the code, and line 4 from the test you'll run below it.

```python
# Step 2
# 1. The answer looks like: one table, one row per customer from either list, with customer_id and ____.
# 2. The information is in: the opening and the closing month-end lists.
# 3. Steps → tools: a customer list for each (call ____, twice) → both in one table, with labels (____).
# 4. I'll know it's right because: ____
# 5. What changes next time (my inputs): ____
def combine_lists(opening_file, closing_file):   # create a function called combine_lists, with two inputs
    opening = list_customers(opening_file)       # run Step 1's function on the opening file; keep the customer list it gives back
    closing = list_customers(closing_file)       # the same for the closing file
    both = pd.merge(opening, closing, on="customer_id", how="outer", indicator=True)   # both lists in one table
    return both                                  # hand the table back
```

Read the merge line aloud: "merge the opening and the closing customer lists, matching on
`customer_id`; keep every customer from either list (`how="outer"`); and add a `_merge` column that
says which list each customer is on (`indicator=True`)", as in PD3. Without `how="outer"`, the merge
keeps only the customers on both lists, and you can't see who is new or who left.

The `_merge` column has three labels:

| `_merge` | The customer is… | So they are… |
|---|---|---|
| `both` | on both lists | a customer who stayed |
| `left_only` | only on the opening list (the first table in the merge) | churned |
| `right_only` | only on the closing list (the second table in the merge) | new |

Print what the function gives back for H1 (December to June), then a test:

```python
print()
print("2. BOTH LISTS IN ONE TABLE")
h1 = combine_lists(DEC, JUN)                     # December to June
print(h1.head().to_string(index=False))          # the first 5 rows of the table it gives back
stayed = h1[h1["_merge"] == "both"]              # on both lists
churned = h1[h1["_merge"] == "left_only"]        # only on the opening list
new = h1[h1["_merge"] == "right_only"]           # only on the closing list
print(f"December: {len(stayed) + len(churned)} customers")   # stayed + churned = everyone in December
print(f"June: {len(stayed) + len(new)} customers")           # stayed + new = everyone in June
```

```
2. BOTH LISTS IN ONE TABLE
customer_id _merge
    CUST001   both
    CUST002   both
    CUST003   both
    CUST004   both
    CUST006   both
December: ... customers
June: ... customers
```

**Read the output in two parts.** The table is what `combine_lists` gives back: every customer from
either list, one row each, with a label. The first rows are all `both`; further down are
`left_only` and `right_only`.

The two lines under it are **only a test** of the table: everyone in December either stayed or
churned, and everyone in June either stayed or is new.

**Check:** the two counts must equal your Step 1 counts. If they don't, look at `how=` in the merge.

### Step 3 — `customer_bridge`: the big function

**What it's for:** the board's answer, one row of customer counts (reason 3 above).

The four numbers, and where each one comes from:

| Number | What it is | Where it comes from |
|---|---|---|
| `opening` | customers on the opening list | `len()` of the customer list from `list_customers`, opening file |
| `closing` | customers on the closing list | `len()` of the customer list from `list_customers`, closing file |
| `new` | customers only on the closing list | `len()` of the `combine_lists` rows where `_merge` is `right_only` |
| `churned` | customers only on the opening list | `len()` of the `combine_lists` rows where `_merge` is `left_only` |

`check` is opening + new − churned − closing, and must be 0. It can catch a mistake because the
numbers come by two different routes: `opening` and `closing` are counted straight from each list,
while `new` and `churned` come from the merge. If the merge lost customers (for example, without
`how="outer"`), the check wouldn't be 0.

```python
# Step 3
# 1. The answer looks like: one row: period, ____, ____, ____, ____ (customer counts), check.
# 2. The information is in: the two month-end lists, through my functions ____ and ____.
# 3. Steps → tools: count each list (call ____, then len) → both lists in one table (call ____)
#    → count the new and the churned rows (filter on ____, then len) → a row → return it.
# 4. I'll know it's right because: ____
# 5. What changes next time (my inputs): ____
def customer_bridge(period, opening_file, closing_file):
    opening = len(list_customers(opening_file))  # call Step 1's function, count its rows
    closing = ____
    both = ____(opening_file, closing_file)      # call Step 2's function
    new = len(both[both["_merge"] == "right_only"])
    churned = ____
    row = {
        "period": period,
        "opening": opening,
        "new": new,
        "churned": churned,
        "closing": closing,
        "check": ____,
    }
    return ____

print()
print("3. H1 CUSTOMER BRIDGE")
h1_row = customer_bridge("H1 (Dec-Jun)", DEC, JUN)
print(pd.DataFrame([h1_row]).to_string(index=False))   # one row → a list of one row → a table
```

```
3. H1 CUSTOMER BRIDGE
      period  opening  new  churned  closing  check
H1 (Dec-Jun)      ...  ...      ...      ...    ...
```

**Check:** `check` is 0, and `opening` and `closing` equal your Step 1 counts.

**Run the whole file once more before you commit,** and paste that output, not an earlier one.

---

## Hand in

Commit `submissions/python/fn2_customer_bridge.py` only (not `scratch.py`):
**Source Control** → `+` on the file → message `Complete: FN2 — customer bridge` → **Commit** →
**Publish Branch**. Then open a PR from `student/fn2_customer_bridge` to `main` with this description:

~~~
## FN2 — Build a big function from small ones

## My output (pasted from my terminal)
```
[paste the full output here]
```

## One question
Two sentences for the board, using your Step 3 table: how did our customer count change in H1,
and how much of that change came from new customers and how much from customers we lost?

## Why small functions?
Why build customer_bridge from list_customers and combine_lists, instead of writing it as one long
function? (2 sentences)

## How it went
How long did it take, and where did you get stuck?
~~~
