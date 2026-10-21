# FN1 — Write your own functions
### Idynamics Finance Analyst Training Program

> **From:** David Chen, VP Finance · **To:** Michael · **Subject:** Four small questions from James
>
> James asks the same small questions at every month-end: how many customers we have, who the big
> ones are, how much we grew, and how much came from new customers. Write him a function for each,
> so next month every answer is one line of code.
>
> — David

Expect about 2 hours.

## Why this, and when you'd use it

So far you've used `bridge`, a function we built together. This time you write four functions
yourself, from an empty file, and you learn how to get from a question to the right code without
being told the commands. That's how analysts work: whenever you'd copy and paste the same steps
with a different file or number (in Excel, copying a sheet and changing the inputs), you write the
steps once as a function and call it with the new input. It's standard practice for anything you do
more than once: one copy of the steps means one place to fix a mistake. For a one-off question, plain
steps are fine. By the end you'll have written the core of `bridge` on your own.

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
git checkout -b student/fn1_from_scratch
git log origin/main..HEAD --oneline
```

The last command must print nothing: you've just made the branch from main, so it holds no work yet.
If it prints anything, stop and message me.

Right-click `submissions/python` → **New File** → `fn1_from_scratch.py`. Try the examples below in
your `scratch.py`, and write your steps in `fn1_from_scratch.py`.

---

## Learn it — how to approach any question

**Read this whole section carefully before you start Step 1, and type the examples into
`scratch.py`.** Every step after it uses this approach.

When a question arrives, don't start with code. Answer these four questions first (they're the
same four as your checkpoint plan):

1. **What does the answer look like?** One number? A table? One per what (per list, per customer)?
2. **Where's the information?** Which file, and which columns. Look before you guess:
   `print(table.head().to_string(index=False))` shows the first five rows.
3. **What has to happen to the data?** Say it in plain words first ("keep some rows", "one total per
   customer", "compare two lists"). Then find the tool for each part in the table below.
4. **How will I know it's right?** Find a number from somewhere else that must agree with yours.

And one more, when the question will come back: **5. Will I be asked this again?** Then make it a
function.

| If you need… | Tool | Where you learned it |
|---|---|---|
| to **look** at a table | `.head()` | PD1b |
| **some rows** of a table | filter: `df[df["col"] == ...]` (or `>=`, `<`…) | PD1, PD1b |
| the **total** of a column | `df["col"].sum()` | PD1 |
| **one total per group** (one row per customer, per plan…) | `groupby(...)[...].sum()` | PD1, PD2 |
| **how many rows** a table has | `len(table)` | PF1 |
| **biggest first** | `.sort_values("col", ascending=False)` | PD1 |
| what **changed between two lists** | `pd.merge(..., how="outer", indicator=True)` | PD3 |
| **the same steps more than once** | a function | PD4 |

### Worked example: "How much of June's MRR comes from customers billed Monthly?"

**1. What does the answer look like?** One number, for one list.

**2. Where's the information?** In the June month-end list. Look at it first:

```python
import pandas as pd

june = pd.read_csv("closes/2026-06/subscriptions_2026-06-30.csv")
print(june.head().to_string(index=False))
```

```
subscription_id customer_id            plan_name billing_cycle  seats  price_per_seat  discount_percent    mrr
         SUB002     CUST002       Platform Suite        Annual     26            1800                 0 3900.0
         SUB003     CUST003        Marketing Pro       Monthly     23              85                 0 1955.0
         SUB004     CUST004            Sales Hub       Monthly     18             110                 0 1980.0
         SUB006     CUST006 Analytics Enterprise        Annual     31            2160                 0 5580.0
         SUB007     CUST007        Marketing Pro       Monthly     16              85                 0 1360.0
```

`billing_cycle` says Monthly or Annual, and `mrr` is the money. So the answer needs two columns.

**3. What has to happen to the data?** In words: keep the Monthly rows, then add up their `mrr`.
In the table, "keep some rows" is a filter, and "the total of a column" is `.sum()`. Only now do you
write code:

```python
monthly = june[june["billing_cycle"] == "Monthly"]      # keep the Monthly rows
print(monthly["mrr"].sum())                             # add up their MRR
```

```
126075.0
```

**4. How will I know it's right?** Every row is either Monthly or Annual, so Monthly plus Annual must
equal the whole list's total:

```python
annual = june[june["billing_cycle"] == "Annual"]
print(annual["mrr"].sum())
print(june["mrr"].sum())
```

```
36755.5
162830.5
```

126,075 + 36,755.5 = 162,830.5. It agrees.

**5. Will I be asked this again?** Yes: James will want it every month, and maybe for Annual too.
The things that would change are the **file** and the **billing cycle**, so those are the function's
inputs. Put the steps under `def`, swap each fixed value for its input, and `return` the answer:

```python
def cycle_mrr(file, cycle):                          # name, then the two inputs
    subs = pd.read_csv(file)                         # was: the June path → now: file
    picked = subs[subs["billing_cycle"] == cycle]    # was: "Monthly" → now: cycle
    return picked["mrr"].sum()                       # hand the answer back to whoever called
```

Read it aloud: "cycle_mrr takes a file and a cycle; it reads the file, keeps the rows on that cycle,
and returns their total MRR." `return` hands the answer back, so you can print it, store it, or do
maths with it. Then call it at least twice, and check one call against your plain steps:

```python
print(cycle_mrr("closes/2026-06/subscriptions_2026-06-30.csv", "Monthly"))
print(cycle_mrr("closes/2026-06/subscriptions_2026-06-30.csv", "Annual"))
print(cycle_mrr("closes/2025-12/subscriptions_2025-12-31.csv", "Monthly"))
```

```
126075.0
36755.5
106314.0
```

The first call gives the same number as the plain steps, so the function does what they did. The
other two give different numbers, so the inputs really are being used.

### Watch out: a fixed value left inside

The most common mistake is forgetting to swap a fixed value for its input. Here the body still
reads the June path instead of `file`:

```python
def cycle_mrr(file, cycle):
    subs = pd.read_csv("closes/2026-06/subscriptions_2026-06-30.csv")   # forgot to swap
    picked = subs[subs["billing_cycle"] == cycle]
    return picked["mrr"].sum()

print(cycle_mrr("closes/2026-06/subscriptions_2026-06-30.csv", "Monthly"))
print(cycle_mrr("closes/2025-12/subscriptions_2025-12-31.csv", "Monthly"))
```

```
126075.0
126075.0
```

No error, but December gives June's number. **Two different inputs giving the same answer is the
sign.** That's why you always call a function at least twice.

### A function can return a table, too

`return` can hand back anything: a number, a row (like `bridge`), or a whole table.

```python
def plan_table(file):
    subs = pd.read_csv(file)
    plans = subs.groupby("plan_name", as_index=False)["mrr"].sum()   # one row per plan
    return plans                                                     # the whole table

print(plan_table("closes/2026-06/subscriptions_2026-06-30.csv").to_string(index=False))
```

```
           plan_name     mrr
Analytics Enterprise 32580.0
    Analytics Growth 22125.5
   Analytics Starter  2430.0
       Marketing Pro 31365.0
      Platform Suite 39900.0
           Sales Hub 34430.0
```

---

## Your turn — four questions from James

If you get stuck on any step, go back to the worked example in Learn it: it does the same thing on a
different question.

At the top of `fn1_from_scratch.py`, put the three file paths in variables so you don't retype them:

```python
import pandas as pd

DEC = "closes/2025-12/subscriptions_2025-12-31.csv"
MAR = "closes/2026-03/subscriptions_2026-03-31.csv"
JUN = "closes/2026-06/subscriptions_2026-06-30.csv"
```

For every step, work through the four questions in `scratch.py` first: look at the data, try the
steps once, check them. Then write your five answers as comments above the function in
`fn1_from_scratch.py`, like this:

```python
# Step 1
# 1. The answer looks like: ...
# 2. The information is in: ...
# 3. What happens to the data: ...  → tools: ...
# 4. I'll know it's right because: ...
# 5. What changes next time (my inputs): ...
def customer_count(...):
    ...
```

Each step gives you less help than the one before.

### Step 1 — How many customers are on a list?

I'll walk you through the five questions. You find the tools and write the code.

1. **What does the answer look like?** One number per list: how many customers are on it.
2. **Where's the information?** In the month-end list, `customer_id` column. But look before you
   count: is one row one customer? Print June's rows for one customer:

   ```python
   june = pd.read_csv(JUN)
   print(june[june["customer_id"] == "CUST002"].to_string(index=False))
   ```

   ```
   subscription_id customer_id        plan_name billing_cycle  seats  price_per_seat  discount_percent    mrr
            SUB002     CUST002   Platform Suite        Annual     26            1800                 0 3900.0
            SUB054     CUST002 Analytics Growth        Annual     22            1140                 5 1985.5
   ```

   CUST002 has two rows: one row is a **subscription**, not a customer. Counting rows would count
   subscriptions.
3. **What has to happen to the data?** In words: make one row per customer, then count the rows.
   Which tool in the table makes one row per group? Which one counts rows?
4. **How will I know it's right?** Your count must be smaller than `len(june)`, the number of
   subscriptions, because some customers have more than one. Print both and compare.

5. **What will change next time James asks?** Not the steps: only which list he's asking about.
   That's your one input.

Then make it a function called `customer_count` and print it like this:

```python
print("1. CUSTOMERS ON THE LIST")
print(f"December: {customer_count(DEC)}")
print(f"June: {customer_count(JUN)}")
```

The two numbers should be different. If they're the same, look for a fixed value left inside (see Learn it).

### Step 2 — Who are the big customers?

James wants the customers whose MRR is at least a number he picks, biggest first.

Answer the five questions in `scratch.py`, trying each step as you go, then write your answers as
comments above the function:

1. What does the answer look like?
2. Where's the information?
3. What has to happen to the data, and which tools?
4. How will I know it's right?
5. What will change next time James asks? Those are your function's inputs.

Make it a function called `big_customers` that returns the table. Call it twice, for June at
8,000 or more and for June at 9,500 or more, and print the tables with `.to_string(index=False)`
under these headings (a blank line first):

```
2. BIG CUSTOMERS IN JUNE
8,000 or more:
...
9,500 or more:
...
```

### Step 3 — How much did MRR grow?

James wants to know how much the list's total MRR grew from the opening list to the closing list.

Answer the five questions, then write your answers as comments above the function:

1. What does the answer look like?
2. Where's the information?
3. What has to happen to the data, and which tools?
4. How will I know it's right?
5. What will change next time James asks? Those are your function's inputs.

Make it a function called `growth` that returns one number. Call it for H1 (December to June) and
for Q2 (March to June), and print the results with `:,.2f` under this heading (a blank line first):

```
3. GROWTH
H1 (Dec-Jun): ...
Q2 (Mar-Jun): ...
```

### Step 4 — How much MRR came from new customers?

James wants the MRR on the closing list from customers who **weren't** on the opening list.

No hints this time. Answer the five questions, write your answers as comments, then write a
function called `new_mrr` that returns that number:

1. What does the answer look like?
2. Where's the information?
3. What has to happen to the data, and which tools?
4. How will I know it's right?
5. What will change next time James asks? Those are your function's inputs.

Call it for H1 and Q2 and print it the same way as Step 3, so your output looks like this, with
your numbers:

```
4. NEW MRR
H1 (Dec-Jun): ...
Q2 (Mar-Jun): ...
```

---

## Hand in

Commit `submissions/python/fn1_from_scratch.py`: **Source Control** → `+` on the file → message
`Complete: FN1 — write your own functions` → **Commit** → **Publish Branch**. Then open a PR from
`student/fn1_from_scratch` to `main` with this description:

~~~
## FN1 — Write your own functions

## My output (pasted from my terminal)
```
[paste the full output here]
```

## Why would you use a function instead of copying the steps (or the sheet, in Excel)? (2 sentences)

## How it went
How long did it take, and where did you get stuck?
~~~
