# DC1 — Clean the CRM export
### Idynamics Finance Analyst Training Program

> **From:** David Chen, VP Finance · **To:** Michael · **Subject:** Two numbers for June, which one is right?
>
> Sales Ops sends the sales team a CRM export every month. I opened June's: it says MRR is
> $201,370.50. Our June close says $162,830.50. Same month, same customers, $38,540 apart.
> Find out which one is right, and make the export prove it.
>
> — David

Expect about 90 minutes.

---

## Why this, and when you'd use it

Raw exports are never clean. Text gets typed different ways, rows get repeated, and things end up in
the file that were never real business. Every total you build on that is wrong, and nothing errors.

Cleaning is three moves, **in this order**: tidy the text, take out what isn't real, then **tie to a
number you trust**. Without that last step you've changed the file, but you can't show it's clean.
In Excel this is find-and-replace plus deleting rows by hand, every month, with no record of what
you did. In pandas it's a script you run again next month in one second.

**At the end** you'll have taken a file that's badly wrong and made it match the close to the cent.

---

## Tools you already know

| To do this | You know |
|---|---|
| read a CSV · see it · count rows | `pd.read_csv` · `.head()` · `len(df)` |
| total a column | `df["mrr"].sum()` |
| one row per plan | `groupby(..., as_index=False)[...].sum()` |
| remove exact repeat rows | `df.drop_duplicates()` (FN2) |
| biggest first | `.sort_values(col, ascending=False)` |
| keep some rows | `df[df["col"] != value]` · `df[df["col"] >= n]` |
| a column changed and kept | `df["col"] = ...` (assign it back) |

---

## Step 0 — Set up

```
git checkout main
git pull origin main
git checkout -b student/dc1_clean_export
git status
```

`git status` must say `nothing to commit, working tree clean`, and `git log origin/main..HEAD` must
print nothing. After the pull you have one new file: `closes/2026-06/crm_export_2026-06-30.csv`.

Build your answer in `submissions/python/dc1_clean_export.py`.

---

## Before you start: review, on paper

**Pen and paper, no computer, 10 minutes on a timer.** Write what each snippet prints. Then type
them into `scratch.py`, run them, and mark yourself. Paste your paper answers *and* your marks into
the PR. A wrong answer you caught is worth more than a right one you guessed.

(Why on paper: some tests you may sit later, including the Rotman MMA assessment, give you
60 minutes, a calculator and scratch paper, and no computer to run code on. Reading code
without running it is a skill you can practise.)

**R1.**
```python
may = pd.DataFrame([{"customer_id": "CUST001", "mrr": 100}, {"customer_id": "CUST002", "mrr": 200}])
june = pd.DataFrame([{"customer_id": "CUST002", "mrr": 250}, {"customer_id": "CUST003", "mrr": 300}])
both = pd.merge(may, june, on="customer_id", how="outer", suffixes=("_may", "_june"), indicator=True)
print(both.to_string(index=False))
```
How many rows, and what does `_merge` say on each?

**R2.**
```python
def total_mrr(df):
    print(df["mrr"].sum())

x = total_mrr(may)
print(x)
```
Two lines come out. What are they?

**R3.**
```python
may.sort_values("mrr", ascending=False)
print(may.to_string(index=False))
```
Which customer is on the first line?

---

## Learn it

Two new things. The examples are a sales team, not your files.

### 1. Tidying text: `.str.strip()` and `.str.title()`

Three reps, one office, typed three ways:

```python
deals = pd.DataFrame([{"rep": "Dana", "office": "Toronto", "deals": 4},
                      {"rep": "Omar", "office": "toronto ", "deals": 6},
                      {"rep": "Priya", "office": " TORONTO", "deals": 5}])
print(deals.groupby("office", as_index=False)["deals"].sum().to_string(index=False))
```
```
  office  deals
 TORONTO      5
 Toronto      4
toronto       6
```

To pandas those are three different offices. A space at the end counts, and so does a capital
letter. Any total by office is now split three ways, and nothing warns you.

We fix it in two moves and print after each.

**Move 1: take the spaces off both ends.** `.str` means "do this to the text in every row";
`.strip()` removes spaces at the start and the end.

```python
deals["office"] = deals["office"].str.strip()
print(deals.to_string(index=False))
```
```
  rep  office  deals
 Dana Toronto      4
 Omar toronto      6
Priya TORONTO      5
```

**Move 2: one capitalisation.** `.title()` gives every word a capital first letter and the rest
lower case, which is how the close files write plan names.

```python
deals["office"] = deals["office"].str.title()
print(deals.to_string(index=False))
```
```
  rep  office  deals
 Dana Toronto      4
 Omar Toronto      6
Priya Toronto      5
```

Group again: one office, 15 deals. You can do both moves in one line, which is what you'll write:
`deals["office"].str.strip().str.title()`. Read it aloud: take the column, strip the text, then
title-case the text.

**Common mistake: leaving out `.str`.** `deals["office"].strip()` gives
`AttributeError: 'Series' object has no attribute 'strip'`. The column isn't text. The *rows* are
text, and `.str` is how you reach them.

**Common mistake: not assigning it back.** `deals["office"].str.title()` on its own line changes
nothing; the table still says `toronto `. Same rule as `.round(2)` and `fillna`.

### 2. Average and middle: `.mean()` and `.median()`

Five reps' deals this quarter: Dana 4, Omar 6, Priya 5, Lee 3, Sam 42.

**On paper first:** the *mean* is the total divided by the count. The *median* is the middle value
once they're in order: 3, 4, **5**, 6, 42. (With an even count, it's halfway between the middle
two.) Work out both before you look.

```python
sales = pd.DataFrame([{"rep": "Dana", "deals": 4}, {"rep": "Omar", "deals": 6},
                      {"rep": "Priya", "deals": 5}, {"rep": "Lee", "deals": 3},
                      {"rep": "Sam", "deals": 42}])
print(f"Mean {sales['deals'].mean()}  Median {sales['deals'].median()}")
```
```
Mean 12.0  Median 5.0
```

Four of the five reps closed six or fewer, so "the average rep closes 12" describes nobody. One big
value dragged the mean up, and the median barely noticed. Take Sam out and both become 4.5.

That's the whole reason to print both. **When the mean sits well above the median, a few big values
are pulling it, and you go and look at them.** Sometimes they're your best customers. Sometimes
they're a mistake.

**Common mistake: `mean(sales["deals"])`.** That gives `NameError: name 'mean' is not defined`.
It's a method on the column, called with the dot: `sales["deals"].mean()`.

---

## Your turn

You write all of it. Print each step under its numbered heading.

**Plan before you type.** Same four questions as always, written as comments above each step:
(1) what the answer looks like · (2) where the information is · (3) the steps and the tool for each ·
(4) how I'll know it's right. Step 1's plan is half filled in; you write more of each one after that.

### Step 1 — Look before you touch anything

Read both files: the export, and the June close, `closes/2026-06/subscriptions_2026-06-30.csv`
(the file you've used since PD3). Print the export's `.head()`, then rows and total MRR for each
file, then the gap.

```
# 1. The answer looks like: rows and MRR for each file, and the gap between them.
# 2. The information is in: the export and ______________________
# 3. Steps → tools: ______________________
# 4. I'll know it's right because: the close's total is the $162,830.50 in David's email.
```

```
1. THE RAW EXPORT AGAINST THE CLOSE
Export: ... rows, MRR ...
Close:  ... rows, MRR ...
Gap:    ...
```

**Check:** the gap is the $38,540 in my email.

### Step 2 — Tidy the text

Count how many plans the export has **before** you touch it: group by `plan_name`, then `len`.
The close has six. Then tidy `plan_name` **and** `billing_cycle` with strip and title, assigned
back, and group by plan again. Print the grouped table and the count. Then group by
`billing_cycle` and print that too. Last, print the export's total MRR again.

```
2. TIDY THE TEXT
Plans before: ...
(the grouped plan table)
Plans after: ...
(the grouped billing-cycle table)
Export MRR after tidying: ...
```

```
# 1. The answer looks like: ______________________
# 2. The information is in: ______________________
# 3. Steps → tools: ______________________
# 4. I'll know it's right because: ______________________
```

**Check:** six plans after, and two billing cycles. The total MRR is the **same** as Step 1's
export total, because tidying text doesn't change a single number. If it changed, you dropped rows.

### Step 3 — Take out what isn't real

**a. Duplicates. Predict first, on paper:** `drop_duplicates()` removes a row only if *every* column
matches another row exactly. How many rows do you think it would remove from the export **as it came
in**, and how many from your **tidied** table? Write both numbers down, then find out. For the first,
read the file again and drop duplicates on that; for the second, use your Step 2 table. Print both
counts. Keep the tidied, de-duplicated table.

**b. Anything that can't be real.** Sort your table by MRR, biggest first, and print the top five
with `.head().to_string(index=False)`. A plain `print(...head())` hides the middle columns behind
`...`, and the middle columns are the ones you need. Read every column of each row. One row can't be a real subscription. Compare its IDs and its price
per seat with the rows around it. Take it out by its `customer_id`.

**c. Tie out.** Print rows and MRR for your clean table and the close, and the gap.

```
# 1. The answer looks like: ______________________
# 2-4: your own.
```

```
3. TAKE OUT WHAT ISN'T REAL
Duplicates removed before tidying: ...   after tidying: ...
(top five rows)
Clean:  ... rows, MRR ...
Close:  ... rows, MRR ...
Gap:    ...
```

**Check:** the gap is 0.0 and the row counts match. That's the only check that proves the file is
clean. Every step before it just changed the file.

### Step 4 — Average and middle

No plan given; write all four lines yourself. Print the mean and median MRR of your tidied
export from Step 2 (before you removed anything) and of your clean table. Then: **how many
clean subscriptions bring in 5,400 or more a month?**

```
4. AVERAGE AND MIDDLE
Tidied: mean ...   median ...
Clean: mean ...   median ...
Subscriptions at 5,400 or more: ...
```

**Check:** the clean mean is the clean total from Step 3 divided by the clean rows. Do it on a
calculator.

Before you close the file, read Steps 1 to 4 top to bottom. Is there anything the business should
know that I didn't ask about?

---

## Hand in

`submissions/python/dc1_clean_export.py`, committed to your branch, and a PR with this description:

~~~
## DC1 — Clean the CRM export

## My output (pasted from my terminal)
```
(Steps 1-4 here, inside these marks)
```

## Review answers
R1, R2, R3: my paper answer · what it actually printed · right or wrong.

## Prediction (Step 3a)
My two numbers on paper, the real two, and in one sentence why they're different.

## Conditions
The line of code for "5,400 or more", and next to it the words from the brief.

## On paper (calculator only, no code)
P1. Five customers pay 1,200, 900, 15,000, 1,100 and 1,000 a month. What's the mean, what's the
    median, and which would you quote as what a typical customer pays? One sentence why.
P2. The close has 57 subscriptions totalling 162,830.50. If one 6,840 row were duplicated, what
    would the mean become? Show the sum you did.

## My finding
Three lines: what I found · why it matters in dollars · what I'd recommend, and to whom.
Write "nothing" if you found nothing.

## Why pandas?
Why do this in pandas rather than Excel? Two sentences.

## How it went
How long did it take, and where did you get stuck?
~~~
