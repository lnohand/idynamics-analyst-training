# PD1 — Meet pandas: ask your June list questions
### Idynamics Finance Analyst Training Program

> **From:** David Chen, VP Finance · **To:** Michael · **Subject:** Four quick facts about June
>
> Sarah wants four facts about June's subscriptions for the board pack: how many and how much,
> which are the big ones, annual versus monthly, and MRR by plan. She'll ask the same four
> questions every month.
>
> Answer them in Python this time, not Excel. It's a short script, and next month it answers July.
> I've added one question of my own at the end.
>
> — David

Expect about 2 hours.

---

## Why this, and when you'd use it

In Excel, you'd answer Sarah with filters, a few SUMs and a pivot table, and next month you'd do it
all again by hand. **pandas** does the same thing in a few lines you save. Next month you change
the file name, run it, and the answers are there. Nobody has to trust that you clicked the right
filter: the script shows exactly how each number was made.

Reach for pandas when:
- you answer **the same questions every month**,
- the file is the **record** and shouldn't be touched by hand (like a frozen month-end list),
- someone needs to **reproduce** your number.

Excel is still the place to look at data and to show it to people.

You already know the DataFrame basics from DataFrame Drills 1 and 2: picking a column,
filtering rows, sorting, `.sum()`. This assignment adds two things: **reading a real file** and
**adding up by group**. By the end you'll have a script that answers Sarah in one click.

---

## Step 0 — Set up

In VS Code, open the repo, then **Terminal → New Terminal**:

```
git status
```

It must say `nothing to commit, working tree clean`. If it lists files, message me before going on.

Then:

```
git checkout main
git pull origin main
git checkout -b student/pd1_june_list
git log origin/main..HEAD --oneline
```

The last command must print nothing. You don't need to install anything: pandas is already in
your venv. If ▶ says `No module named 'pandas'`, press **Ctrl+Shift+P** → `Python: Select
Interpreter` → pick the one with `.venv`.

Check you have the June list: in Explorer, open `closes/2026-06/`. You should see
`subscriptions_2026-06-30.csv`, the frozen June list from your SQL 09.

---

## Learn it

Make a scratch file to try the examples: right-click `submissions/python` → **New File** →
`scratch.py` (not submitted). Put `import pandas as pd` at the top.

The examples use a small made-up list, `assignments/python/pd1_examples/example_list.csv`. It has
the same column names as your June list, just fewer rows and columns.

### Example 1 — `pd.read_csv`: a file becomes a DataFrame

So far you typed your rows in. Real data comes in files. `pd.read_csv("path")` reads a CSV file into
a DataFrame. The first line of the file becomes the column names.

```python
subs = pd.read_csv("assignments/python/pd1_examples/example_list.csv")
print(subs.to_string(index=False))
print(len(subs))
print(subs["mrr"].sum())
```

```
subscription_id customer_id      plan_name billing_cycle  mrr
         SUB901     CUST901      Sales Hub       Monthly 1200
         SUB902     CUST902      Sales Hub        Annual 3000
         SUB903     CUST903  Marketing Pro       Monthly  800
         SUB904     CUST901  Marketing Pro       Monthly  950
         SUB905     CUST904 Platform Suite        Annual 6000
5
11950
```

From here it's a DataFrame like the ones you built: everything from Drills 1 and 2 works on it.

The path starts from the **repo root**, the top folder that contains `closes/` and `assignments/`.
The VS Code terminal and the ▶ button both run from there.

**Common mistake:** `FileNotFoundError: [Errno 2] No such file or directory: 'example_list.csv'`.
That means the path is incomplete: give the whole path from the repo root, folders included.

### Example 2 — `groupby`: add up by group

"MRR by plan" means: put the rows into groups, one group per plan, and add up `mrr` in each group.
In Excel that's a pivot table. In pandas:

```python
by_plan = subs.groupby("plan_name", as_index=False)["mrr"].sum()
print(by_plan.to_string(index=False))
```

```
     plan_name  mrr
 Marketing Pro 1750
Platform Suite 6000
     Sales Hub 4200
```

Read it left to right: **group** the rows by `plan_name`, take the `mrr` column, and **sum** each
group. Sales Hub has two rows (1,200 + 3,000), so they became one row of 4,200.

`as_index=False` keeps `plan_name` as an ordinary column, so the result is a normal table you can
sort and print like any other. Always include it in this assignment.

The same pattern works for any column you want to group by:

```python
by_cycle = subs.groupby("billing_cycle", as_index=False)["mrr"].sum()
print(by_cycle.to_string(index=False))
```

```
billing_cycle  mrr
       Annual 9000
      Monthly 2950
```

**Common mistake:** `KeyError: 'plan'`. The column name doesn't exist. Use the exact name from the
file's first line (`plan_name`, not `plan`).

### Example 3 — filter: keep only the rows you want (reminder from Drill 1)

**Filtering** means keeping only the rows that meet a condition, like Excel's filter button. In
Drill 1 you wrote `df[df["col"] > n]`. Here: keep the subscriptions with `mrr` of 1,000 or more.

```python
big = subs[subs["mrr"] >= 1000]
print(big.to_string(index=False))
```

```
subscription_id customer_id      plan_name billing_cycle  mrr
         SUB901     CUST901      Sales Hub       Monthly 1200
         SUB902     CUST902      Sales Hub        Annual 3000
         SUB905     CUST904 Platform Suite        Annual 6000
```

SUB903 (800) and SUB904 (950) are gone. `big` is a new, smaller DataFrame; `subs` is unchanged.

To print only some columns, put their names in a list inside the brackets: `big[["subscription_id", "mrr"]]`
(two pairs of brackets: the outer pair picks, the inner pair is the list). And a filtered table
works with `len` and `.sum()` like any other:

```python
big = big.sort_values("mrr", ascending=False)
print(big[["subscription_id", "mrr"]].to_string(index=False))
print(len(big))
print(big["mrr"].sum())
```

```
subscription_id  mrr
         SUB905 6000
         SUB902 3000
         SUB901 1200
3
10200
```

**Which one when:** a **filter** answers "which rows?" and "how many, how much for this one
condition?". **groupby** answers "how much for *each* plan / cycle / customer?" in one table.

---

## Your turn

In Explorer, right-click `submissions/python` → **New File** → `pd1_june_list.py`.

Each step below gives you the code with a few blanks (`____`). Type it in yourself (don't paste:
typing is how it sticks), fill each blank, and press ▶ after every step. Read the explanation
under each block: the next assignment asks similar questions **without** the code, so make sure you
know what every line does.

A reminder you'll need for printing: `f"Subscriptions: {len(june)}"` is an **f-string**. Python
puts the value inside `{ }` into the text. A format code after a colon controls how a number looks:
`{x:,.2f}` adds thousands commas and 2 decimals (`162830.5` → `162,830.50`).

### Step 1 — Load and check

Sarah's first question: how many subscriptions, and how much MRR?

```python
import pandas as pd

june = pd.read_csv("closes/2026-06/subscriptions_2026-06-30.csv")

print("1. LOAD AND CHECK")
print(f"Subscriptions: {len(____)}")
print(f"Total MRR: {june['____'].sum():,.2f}")
```

- Line 3 reads the frozen June list into a DataFrame called `june` (Example 1).
- `len(...)` counts the rows: one row = one subscription.
- `june["..."]` picks one column; `.sum()` adds it up.

Inside an f-string the column name goes in single quotes (`june['...']`), because the f-string
itself uses double quotes.

**Check it worked:** both numbers must equal the June line in the **Close log** on the shared
drive, which you filled in when you froze June. If they don't, stop: you're reading the wrong file.

### Step 2 — The big ones

Which subscriptions are worth **5,000 or more** a month, and how much of June's MRR do they make
up? Add under Step 1:

```python
print()
print("2. SUBSCRIPTIONS WITH MRR OF 5,000 OR MORE")
big = june[june["mrr"] >= ____]
big = big.sort_values("____", ascending=False)
print(big[["subscription_id", "plan_name", "mrr"]].to_string(index=False))
share = big["mrr"].sum() / june["mrr"].sum() * 100
print(f"Count: {len(big)}  Share of MRR: {share:.1f}%")
```

- `print()` with nothing inside prints a blank line, so each step's answer stands apart.
- Line 3 is the **filter** (Example 3): keep only the rows where `mrr` is 5,000 or more. The result,
  `big`, is a new, smaller DataFrame; `june` is unchanged. The other comparisons work the same way:
  `>` more than, `<` less than, `<=` at most, `==` equal to.
- Line 4 sorts `big`, biggest first. `ascending=False` means biggest first; `ascending=True` means
  smallest first. `sort_values` returns a sorted copy, so you assign it back to `big`.
- Line 5 prints just three columns (the list inside the double brackets).
- Line 6 is the share: the big ones' MRR ÷ all of June's MRR × 100.
- `:.1f` means one decimal, no thousands comma: `f"{29.6123:.1f}"` gives `29.6`.

**Check it worked:** every `mrr` printed is 5,000 or more, biggest first.

### Step 3 — Annual vs monthly

How much of June's MRR is on annual contracts, and how much on monthly? Sarah wants the **number
of subscriptions** too, so this uses two filters rather than groupby (groupby here would give only
the MRR).

```python
print()
print("3. ANNUAL VS MONTHLY")
annual = june[june["billing_cycle"] == "____"]
monthly = june[june["billing_cycle"] == "____"]
print(f"Annual:  {len(annual)} subscriptions, MRR {annual['mrr'].sum():,.2f}")
print(f"Monthly: {len(monthly)} subscriptions, MRR {monthly['mrr'].sum():,.2f}")
```

- `==` means "is equal to" (two equals signs; one `=` would be an assignment and gives an error).
- The text must match the file exactly, capital letter included: look at the `billing_cycle`
  column in Example 1's output.

**Check it worked:** the two counts add up to Step 1's count, and the two MRRs add up to Step 1's
total.

### Step 4 — MRR by plan

Which plans does June's MRR come from?

```python
print()
print("4. MRR BY PLAN")
by_plan = june.groupby("____", as_index=False)["mrr"].sum()
by_plan = by_plan.sort_values("mrr", ascending=False)
print(by_plan.to_string(index=False))
```

- Line 3 is Example 2: one row per plan, with that plan's MRR added up. That's a pivot table in
  one line.
- Line 4 puts the biggest plan first.
- The column in `["mrr"]` is the one that gets added up. Put another number column there (for
  example `["seats"]`) to add that up instead.
- `by_plan` is an ordinary table, so you can filter it like any other: `by_plan[by_plan["mrr"] >= 30000]`
  keeps only the plans with 30,000 or more.

**Check it worked:** the plan totals add up to Step 1's total MRR.

### Step 5 — On your own: customers with 50 or more seats

My question: Customer Success offers free onboarding to every customer with **50 or more seats in
total**, across all their subscriptions. Which customers qualify?

You need `groupby`, a filter and `sort_values`. Think about the order: a customer can have more
than one subscription, so add up each customer's seats first.

Add it at the end of your script. Your output must look like this:

```
5. CUSTOMERS WITH 50 OR MORE SEATS
customer_id  seats
    CUST016     80
    CUST025     74
    CUST009     71
    CUST018     70
    CUST006     64
    CUST022     59
    CUST027     59
    CUST024     57
Count: 8
```

(CUST022 and CUST027 both have 59 seats, so they may print in either order.)

**Check it worked:** your output matches the one above. If you get no rows at all, look at the
order of your filter and your groupby: no single subscription has 50 seats.

---

## Hand in

Commit `submissions/python/pd1_june_list.py` only (not `scratch.py`): **Source Control** → `+` on
the file → message `Complete: PD1 — meet pandas` → **Commit** → **Publish Branch**. Then open a PR
from `student/pd1_june_list` to `main` with this description:

~~~
## PD1 — Meet pandas

## My output (pasted from my terminal)
```
[paste the full output here]
```

## Three questions
1. Next month Sarah asks the same questions about July. What would you change in your script?
2. Why would you use pandas for this instead of Excel? (2 sentences)
3. In Step 5, why did you have to group before filtering?

## How it went
How long did it take, and where did you get stuck (if anywhere)?
~~~
