# DataFrame Drill 2 — Build New Columns with Math

### iDynamics Finance Analyst Training Program

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Position-level P&L — stop calculating this by hand
>
> Every position report I get asks the same three questions: what is each position worth, what
> percent of the book is it, and are we up or down on it. None of those are columns anyone hands
> you. You calculate them.
>
> In a spreadsheet you'd write one formula and drag it down. Pandas has a better version of that,
> and it's the thing that makes a DataFrame worth more than a worksheet. That's the one idea in
> this drill.
>
> Work through the examples first and run them. Then do the questions.
>
> — David

---

## Step 0 — Git: do this BEFORE you write any code

**Do this in VS Code, not Command Prompt.** Open the repo in VS Code, then open its built-in
terminal: **Terminal → New Terminal**. A terminal panel opens at the bottom of the window, already
pointed at your repo folder — that's where these commands go.

Everything in this assignment happens in VS Code: these commands, writing the file, and committing
at the end. You should not need to open Command Prompt or PowerShell once. *(This replaces the
Command Prompt steps in `docs/git_workflow_reference.md`.)*

**First, check you have nothing half-finished:**

```
git status
```

It must say `nothing to commit, working tree clean`. If it lists any files, commit them first —
see the box below.

**Then run these four, in this order:**

```
git checkout main
git pull origin main
git checkout -b student/dataframe_drill2
git log origin/main..HEAD --oneline
```

**What each one does:**

| Command | What it does |
|---|---|
| `git status` | Shows whether you have work sitting around that git hasn't saved yet. |
| `git checkout main` | Moves you to `main`. |
| `git pull origin main` | Downloads my latest files. |
| `git checkout -b student/dataframe_drill2` | Creates your new branch and moves you to it. |
| `git log origin/main..HEAD --oneline` | Lists anything on your branch that isn't on `main`. |

⚠️ **That last command must print nothing at all — just a blank line and back to the prompt.**

Printing nothing means your branch started clean from `main`, which is the entire point of Step 0.
If it prints any commits, your branch got built on top of old work. Stop and message me.

> **If a command errors, here's what it means:**
>
> - `Your local changes would be overwritten by checkout` — you had unfinished work. Run
>   `git commit -am "WIP"` to save it, then start Step 0 again from the top.
> - `A branch named 'student/dataframe_drill2' already exists` — you already made it. Run
>   `git checkout student/dataframe_drill2` instead, then re-run the `git log` line.

---

## VS Code — stop typing things it does for you

You've been doing a lot of this by hand. You don't have to. Four things worth knowing before you
start:

**See which branch you're on** — bottom-left corner of the window, always visible. It should read
`student/dataframe_drill2` the entire time you work on this. Glance at it before you start typing.

**Run your file** — the **▶** play button, top-right of the editor. Output appears in the terminal
panel at the bottom. You never need to type `python whatever.py` again.
> If it says `No module named 'pandas'`, press **Ctrl+Shift+P**, type `Python: Select Interpreter`,
> and pick the one with `.venv` in its name.

**Commit your work** — the **Source Control** icon in the left sidebar (the branching arrows).
Stage, write a message, commit, push — all buttons, no git commands. Full steps in the Submission
section at the end.

**Get back a version of a file you saved earlier** — right-click the file → **Open Timeline**.
VS Code keeps its own history of every time you saved, separate from git. If work ever seems to
vanish, look there first, before anything else.

---

## Step 1 — Follow along

Make a scratch file to try the examples in — **this one is not submitted**, it's just for working
through. In the Explorer panel, right-click the `submissions/python` folder → **New File** → name
it `scratch.py`.

Put this at the top, once:

```python
import pandas as pd
```

Every example below uses this portfolio. Type it in underneath. `Prev_Close` is yesterday's closing
price:

```python
rows = [
    {"Ticker": "AAPL", "Sector": "Tech",   "Price": 180.50, "Prev_Close": 178.20, "Shares": 50},
    {"Ticker": "MSFT", "Sector": "Tech",   "Price": 420.00, "Prev_Close": 425.60, "Shares": 30},
    {"Ticker": "TSLA", "Sector": "Auto",   "Price": 210.00, "Prev_Close": 204.75, "Shares": 40},
    {"Ticker": "XOM",  "Sector": "Energy", "Price": 115.20, "Prev_Close": 115.20, "Shares": 100},
]
df = pd.DataFrame(rows)
```

---

## Example 1 — A new column from two other columns

How much money is in each position? Price times shares. Write it once:

```python
df["Total_Value"] = df["Price"] * df["Shares"]
print(df.to_string(index=False))
```

```
Ticker Sector  Price  Prev_Close  Shares  Total_Value
  AAPL   Tech  180.5      178.20      50       9025.0
  MSFT   Tech  420.0      425.60      30      12600.0
  TSLA   Auto  210.0      204.75      40       8400.0
   XOM Energy  115.2      115.20     100      11520.0
```

Read the left side, `df["Total_Value"] = ...`, as **"make a column called Total_Value."** The name
in the brackets doesn't exist yet — this line is what creates it.

The right side, `df["Price"] * df["Shares"]`, multiplies the two columns **row by row**: AAPL's
price by AAPL's shares, MSFT's by MSFT's, and so on down. Pandas keeps the rows lined up for you.
One line, whole column filled. This is called **vectorized** math — the operation lands on the whole
column at once.

Subtraction works exactly the same way. Today's move per share is price minus yesterday's close:

```python
df["Day_Change"] = df["Price"] - df["Prev_Close"]
print(df.to_string(index=False))
```

```
Ticker Sector  Price  Prev_Close  Shares  Total_Value  Day_Change
  AAPL   Tech  180.5      178.20      50       9025.0        2.30
  MSFT   Tech  420.0      425.60      30      12600.0       -5.60
  TSLA   Auto  210.0      204.75      40       8400.0        5.25
   XOM Energy  115.2      115.20     100      11520.0        0.00
```

MSFT is down on the day, so its `Day_Change` is negative. XOM closed exactly where it opened —
`0.00`, which is not the same as being down.

---

## Example 2 — A column that needs one number from the whole table

Weight means "what percent of the book is this position." To get it you need the portfolio total —
a **single number** summarising the whole column. That's `.sum()`:

```python
print(df["Total_Value"].sum())
```

```
41545.0
```

Look at those two things side by side, because this is the distinction that matters:

- `df["Total_Value"]` → the **whole column**, 4 values
- `df["Total_Value"].sum()` → **one number**, 41545.0

Now the weight — each position's value divided by that total, times 100:

```python
df["Weight_%"] = df["Total_Value"] / df["Total_Value"].sum() * 100
print(df.to_string(index=False))
```

```
Ticker Sector  Price  Prev_Close  Shares  Total_Value  Day_Change  Weight_%
  AAPL   Tech  180.5      178.20      50       9025.0        2.30 21.723432
  MSFT   Tech  420.0      425.60      30      12600.0       -5.60 30.328559
  TSLA   Auto  210.0      204.75      40       8400.0        5.25 20.219040
   XOM Energy  115.2      115.20     100      11520.0        0.00 27.728969
```

Dividing a **column** by a **single number** applies that one number to every row. MSFT is about
30% of the book.

---

## Example 3 — `.round(2)` cleans up the decimals

Six decimal places is not how you hand a weight to anyone. `.round(2)` takes a column and gives you
the same column at 2 decimal places:

```python
df["Weight_%"] = df["Weight_%"].round(2)
print(df.to_string(index=False))
```

```
Ticker Sector  Price  Prev_Close  Shares  Total_Value  Day_Change  Weight_%
  AAPL   Tech  180.5      178.20      50       9025.0        2.30     21.72
  MSFT   Tech  420.0      425.60      30      12600.0       -5.60     30.33
  TSLA   Auto  210.0      204.75      40       8400.0        5.25     20.22
   XOM Energy  115.2      115.20     100      11520.0        0.00     27.73
```

⚠️ **The classic mistake:** `.round(2)` does not change the column — it hands you back a *rounded
copy*. So this line looks right and does nothing at all:

```python
df["Weight_%"].round(2)          # rounds, throws the result away, column unchanged
```

You have to **assign it back**, which is what `df["Weight_%"] = df["Weight_%"].round(2)` does.

You can also round at the moment you build the column. Wrap the whole calculation in brackets
first, then round the result:

```python
df["Weight_%"] = (df["Total_Value"] / df["Total_Value"].sum() * 100).round(2)
```

---

## Example 4 — Your new columns are just columns

Nothing about `Total_Value` is second-class because you calculated it. Sorting and filtering work
on it exactly like any other column.

**Biggest positions first:**

```python
print(df.sort_values("Total_Value", ascending=False).to_string(index=False))
```

```
Ticker Sector  Price  Prev_Close  Shares  Total_Value  Day_Change  Weight_%
  MSFT   Tech  420.0      425.60      30      12600.0       -5.60     30.33
   XOM Energy  115.2      115.20     100      11520.0        0.00     27.73
  AAPL   Tech  180.5      178.20      50       9025.0        2.30     21.72
  TSLA   Auto  210.0      204.75      40       8400.0        5.25     20.22
```

**Only positions worth more than $10,000:**

```python
print(df[df["Total_Value"] > 10000].to_string(index=False))
```

```
Ticker Sector  Price  Prev_Close  Shares  Total_Value  Day_Change  Weight_%
  MSFT   Tech  420.0       425.6      30      12600.0        -5.6     30.33
   XOM Energy  115.2       115.2     100      11520.0         0.0     27.73
```

(Look closely — `425.60` prints as `425.6` here. Once the row needing two decimals is filtered out,
pandas stops padding the column. The number didn't change, only how it's shown.)

That's the payoff. Once a number is *in* the table, every tool you already have works on it.

---

## Example 5 — Don't reach for a loop

The instinct from ordinary Python is to walk the rows one at a time. Try it and see what you
actually get:

```python
for row in df:
    print(row)
```

```
Ticker
Sector
Price
Prev_Close
Shares
Total_Value
Day_Change
Weight_%
```

**Those are the column names, not the rows.** Looping a DataFrame walks across the *headers*. It
isn't a broken version of what you wanted — it's a different thing entirely, and it won't error, so
nothing warns you. You'd just build garbage.

The real point isn't "loop it differently." It's that for math across a column, **you don't need a
loop at all** — `df["Price"] * df["Shares"]` already does every row. When you catch yourself
starting to write `for` over a DataFrame, that's the signal you're about to do by hand what pandas
does in one line.

---

## Step 2 — Your turn

Now make the file you'll actually submit. Explorer panel → right-click the `submissions/python`
folder → **New File** → name it exactly:

```
dataframe_drill2_columns.py
```

Start it with the import and this book of positions:

```python
import pandas as pd

POSITIONS = [
    {"Ticker": "AAPL", "Sector": "Tech",    "Shares": 120, "Cost": 145.00, "Price": 180.50},
    {"Ticker": "MSFT", "Sector": "Tech",    "Shares":  40, "Cost": 390.00, "Price": 420.00},
    {"Ticker": "TSLA", "Sector": "Auto",    "Shares":  60, "Cost": 250.00, "Price": 210.00},
    {"Ticker": "XOM",  "Sector": "Energy",  "Shares": 200, "Cost":  98.40, "Price": 115.20},
    {"Ticker": "JNJ",  "Sector": "Health",  "Shares":  75, "Cost": 160.00, "Price": 152.75},
    {"Ticker": "PG",   "Sector": "Staples", "Shares":  90, "Cost": 155.00, "Price": 155.00},
]
book = pd.DataFrame(POSITIONS)
```

`Cost` is what we paid per share. `Price` is what it's worth now.

**How to answer:**

- Questions marked **(write it)** get real, working, uncommented code. Every one of them must print
  something when you run the file.
- Questions marked **(in words)** get a written answer as a comment. **Put a `#` at the start of
  every line**, like this:

```python
# Q1: pandas applies the multiplication to every row at the same time,
# so I don't have to walk the rows myself.
```

- Run the file after each question and read what printed. Where there's a self-check, compare it to
  **what your screen actually shows**, character by character — not to what you expected.

---

**Q1. (in words)** Example 1 filled all four rows without a `for` loop. In your own words: what is
pandas doing on the line `df["Price"] * df["Shares"]` that makes the loop unnecessary?

**Q2. (write it)** Add a column `Market_Value` — price times shares. Print the whole table with no
row-number column.
> Self-check — your output should be exactly:
> ```
> Ticker  Sector  Shares  Cost  Price  Market_Value
>   AAPL    Tech     120 145.0 180.50      21660.00
>   MSFT    Tech      40 390.0 420.00      16800.00
>   TSLA    Auto      60 250.0 210.00      12600.00
>    XOM  Energy     200  98.4 115.20      23040.00
>    JNJ  Health      75 160.0 152.75      11456.25
>     PG Staples      90 155.0 155.00      13950.00
> ```

**Q3. (write it)** Print the **single number** for the whole book's market value.
> Self-check: `99506.25`

**Q4. (write it)** Add a column `Weight_%` — each position's `Market_Value` as a percent of the
book total, rounded to 2 decimals. Print the whole table, no row-number column.
> Self-check — the `Weight_%` column should read, top to bottom:
> ```
> 21.77
> 16.88
> 12.66
> 23.15
> 11.51
> 14.02
> ```

**Q5. (write it)** Add a column `Gain_$` — how much money we're up or down on each position. That's
the price move per share, times how many shares we hold: price minus cost, then multiplied by
shares. Print the table **sorted by `Gain_$`, biggest gain first**, no row-number column.
> Self-check — your output should be exactly:
> ```
> Ticker  Sector  Shares  Cost  Price  Market_Value  Weight_%   Gain_$
>   AAPL    Tech     120 145.0 180.50      21660.00     21.77  4260.00
>    XOM  Energy     200  98.4 115.20      23040.00     23.15  3360.00
>   MSFT    Tech      40 390.0 420.00      16800.00     16.88  1200.00
>     PG Staples      90 155.0 155.00      13950.00     14.02     0.00
>    JNJ  Health      75 160.0 152.75      11456.25     11.51  -543.75
>   TSLA    Auto      60 250.0 210.00      12600.00     12.66 -2400.00
> ```

**Q6. (write it)** Print only the positions we're **losing** money on. Read that carefully — one
position is exactly break-even, and break-even is not losing.
> Self-check — two rows: `TSLA` at `-2400.00` and `JNJ` at `-543.75`. If `PG` shows up, your
> condition is wrong.

**Q7. (in words, then write it)** A teammate wants the total gain across the whole book and writes
this. **Don't paste it into your file — just read it:**

```python
total = 0
for row in book:
    total = total + row["Gain_$"]
```

It crashes with `TypeError: string indices must be integers, not 'str'`.

- **(in words)** What is `row` actually holding on each pass through that loop, and why does that
  produce this error?
- **(write it)** Get the total gain the pandas way instead — one line, no loop — and print it.
> Self-check: `5876.25`

---

## Before you submit

Run the whole file one last time, top to bottom, and read the output.

- [ ] The file runs with **no error**
- [ ] Every **(write it)** question printed something
- [ ] Q1 and the first half of Q7 are answered in words, with `#` on every line
- [ ] Each self-check matches what actually printed — you compared them side by side
- [ ] Each column was **calculated** by your code, not typed in as a list of numbers
- [ ] `scratch.py` is not part of what you're committing

---

## Submission

File: `submissions/python/dataframe_drill2_columns.py`

Commit and push it from VS Code — no Command Prompt or PowerShell needed:

1. **Save the file** (Ctrl+S).
2. Click the **Source Control** icon in the left sidebar (the branching arrows).
3. `dataframe_drill2_columns.py` shows up under **Changes**. Hover it and click the **`+`** to
   stage it. *(The `+` stages your work. The `↩` next to it throws it away — don't click that one.)*
   Don't stage `scratch.py`.
4. Type the commit message in the box at the top:
   `Complete: DataFrame Drill 2 — computed columns`
5. Click **Commit**.
6. Click **Publish Branch** (or **Sync Changes** if it's already been pushed once).

Then open a PR on GitHub from `student/dataframe_drill2` → `main` with this description:

```
## DataFrame Drill 2 — computed columns
- Added Market_Value, Weight_%, Gain_$

## Pre-submit check
- [ ] I ran the file and read every line of output
- [ ] Each answer uses the method the question named — not just the right output
- [ ] Nothing is commented out except my written answers
- [ ] The self-checks below are pasted from my terminal, not copied from the brief

## My output — pasted from my actual terminal
Q1 answer:
[paste]

Q2 Market_Value table:
[paste]

Q3 book total:
[paste]

Q4 Weight_% table:
[paste]

Q5 sorted by Gain_$:
[paste]

Q6 losing positions:
[paste]

Q7 answer + total:
[paste]

## The lines that built my columns
[paste the three lines that created Market_Value, Weight_% and Gain_$]

## Questions for reviewer
[anything you're unsure about, or leave blank]
```

**Paste what your terminal printed, not what the self-check says.** If the two disagree, that gap
is the thing I most want to see — leave it in and flag it in the PR.
