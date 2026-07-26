# DataFrame Drill — Get Comfortable with a Portfolio Table

### iDynamics Finance Analyst Training Program
> **From:** David Chen, VP Finance
> **To:** Michael
>
> You flagged DataFrames as the weak spot on the checkpoint — good, that's the right read. So
> before you redo Section B, let's just get *comfortable* with one. We'll build one table and then
> live in it: read from it, sort it, and filter it. Once that feels natural, you'll answer
> a few questions, and only then we'll look at the one mistake that tripped you up.
>
> Work along in a scratch file. Put this at the **top, once** — you don't repeat it, everything
> below runs in the same file, top to bottom:
> ```python
> import pandas as pd
> ```
> Theme is a stock portfolio, because that's what a DataFrame is *for*.
> — David

---

## The idea: a DataFrame is a table

A **dictionary** is one labeled lookup — `{"AAPL": 50}` answers "how many shares of AAPL?" and
nothing else. A **DataFrame** (from `pandas`) is a whole **table**: rows and named columns, like a
spreadsheet or a SQL result — and unlike a dict, you can read, sort, filter, and change it.

---

## Example 1 — Build the table

You build a DataFrame from a **list**, where each item is one **row** written as a dict. Each
dict is a row; its keys become the column names (they line up because every row uses the same
keys).

```python
rows = [
    {"Ticker": "AAPL", "Sector": "Tech",   "Price": 180.50, "Shares": 50},
    {"Ticker": "MSFT", "Sector": "Tech",   "Price": 420.00, "Shares": 30},
    {"Ticker": "TSLA", "Sector": "Auto",   "Price": 210.00, "Shares": 40},
    {"Ticker": "XOM",  "Sector": "Energy", "Price": 115.20, "Shares": 100},
]
df = pd.DataFrame(rows)
print(df)
```

```
  Ticker  Sector  Price  Shares
0   AAPL    Tech  180.5      50
1   MSFT    Tech  420.0      30
2   TSLA    Auto  210.0      40
3    XOM  Energy  115.2     100
```

See that `0 1 2 3` running down the left? That's the **index** — a row number pandas adds
automatically. Often you don't want it in your printout. Hide it with `.to_string(index=False)`:

```python
print(df.to_string(index=False))
```

```
Ticker Sector  Price  Shares
  AAPL   Tech  180.5      50
  MSFT   Tech  420.0      30
  TSLA   Auto  210.0      40
   XOM Energy  115.2     100
```

That's the same table without the row-number column — the "no index" printout your checkpoint
asked for. (Also: `180.50` shows as `180.5` — pandas just drops the trailing zero. Nothing lost.)

---

## Example 2 — Read from the table

Two everyday moves: grab a whole **column**, or grab one **cell**.

**A whole column** — `df["ColumnName"]`:

```python
print(df["Price"])
```

```
0    180.5
1    420.0
2    210.0
3    115.2
Name: Price, dtype: float64
```

(You get the column with its index down the side — that's one column of the table, called a
*Series*. `Name` and `dtype` at the bottom just tell you which column it is and that it holds
floats.)

**One cell** — `df.loc[row, "ColumnName"]` (row number, then column name):

```python
print(df.loc[0, "Ticker"])   # AAPL   -> row 0, Ticker column
print(df.loc[2, "Price"])    # 210.0  -> row 2, Price column
```

So: `df["Price"]` = the whole Price column; `df.loc[2, "Price"]` = the single Price in row 2.

---

## Example 3 — Sort it and filter it

**Sort — `df.sort_values("column")`.** It hands you back a **new table** with the rows reordered by
that column. By default it sorts smallest-to-largest (ascending); add `ascending=False` for
largest-first. The whole row travels together — only the order changes.

```python
print(df.sort_values("Price", ascending=False).to_string(index=False))
```

```
Ticker Sector  Price  Shares
  MSFT   Tech  420.0      30
  TSLA   Auto  210.0      40
  AAPL   Tech  180.5      50
   XOM Energy  115.2     100
```

Important: `sort_values` does **not** change `df` — it returns a sorted *copy*, and `df` keeps its
original order. To keep the sorted table, save it to a variable:
`ranked = df.sort_values("Price", ascending=False)`.

**Filter — `df[ condition ]`.** It hands you back a **new table** containing only the rows where
the condition is true (this is called *boolean indexing*):

```python
print(df[df["Sector"] == "Tech"].to_string(index=False))
```

```
Ticker Sector  Price  Shares
  AAPL   Tech  180.5      50
  MSFT   Tech  420.0      30
```

Read `df[df["Sector"] == "Tech"]` as: "from `df`, keep the rows where Sector equals Tech." (`==`
means "is equal to" — two equals signs, not one.) Like sort, this returns a new table and leaves
`df` unchanged.

---

## Example 4 — Missing values show up as `NaN`

A DataFrame is always a full rectangle — every row has every column. So if you build a table and
one row is missing a value, pandas doesn't leave a hole; it fills that spot with **`NaN`** ("not a
number" = *missing*). Here NVDA has no price yet:

```python
holdings = [
    {"Ticker": "AAPL", "Sector": "Tech", "Price": 180.50, "Shares": 50},
    {"Ticker": "MSFT", "Sector": "Tech", "Price": 420.00, "Shares": 30},
    {"Ticker": "NVDA", "Sector": "Tech",                  "Shares": 10},  # no Price
]
print(pd.DataFrame(holdings).to_string(index=False))
```

```
Ticker Sector  Price  Shares
  AAPL   Tech  180.5      50
  MSFT   Tech  420.0      30
  NVDA   Tech    NaN      10
```

`NaN` is not `0` and not the text `"NaN"` — it means *we don't have this value*. (A price of `0`
would mean the stock is actually free, which is a different thing.)

---

## Check yourself — Part 1

You've now built a table, read from it, sorted it, filtered it, and seen what a missing value looks
like. Try these in your scratch file (use the `df` from Example 1). Answer the wordy ones in your
own words.

**Q1.** In `pd.DataFrame(rows)` where `rows` is a list of dicts, what does each dict become in the
table, and what do its keys become?

**Q2. (write it)** Print just the `Shares` column.

**Q3. (write it)** Print the table sorted by `Shares`, largest first, with no row-number column.
> Self-check — your output should be exactly:
> ```
> Ticker Sector  Price  Shares
>    XOM Energy  115.2     100
>   AAPL   Tech  180.5      50
>   TSLA   Auto  210.0      40
>   MSFT   Tech  420.0      30
> ```

**Q4. (write it)** Print only the rows in the `Energy` sector.

**Q5.** One stock in your table shows `NaN` for Price. Is that the same as a Price of `0`? Explain
the difference in one line.

*(Send me these before moving on — then keep going below.)*

---

## Example 5 — Build the rows with a loop

In Example 1 the list of rows was already written out. Real data isn't — you build it. You often
start from a plain dict like `{ticker: shares}` and turn it into rows: loop it with `.items()`
(hands you the key *and* the value each pass), and `.append()` one row-dict per lap — the same
running-total habit, one step up.

```python
HOLDINGS = {"AAPL": 50, "MSFT": 30, "TSLA": 40, "XOM": 100}

rows = []                                             # start with an empty list
for ticker, shares in HOLDINGS.items():               # key, value each pass
    rows.append({"Ticker": ticker, "Shares": shares}) # append ONE row-dict per lap
df = pd.DataFrame(rows)                                # hand the finished list to pandas
print(df.to_string(index=False))
```

```
Ticker  Shares
  AAPL      50
  MSFT      30
  TSLA      40
   XOM     100
```

Three steps to burn in: **empty list → append a row-dict each pass → hand the finished list to
`pd.DataFrame`.** This is the exact move that got you on the checkpoint.

---

## Example 6 — The one mistake to avoid

Now that building a table is familiar, here's the trap. `pd.DataFrame` needs to know **how many
rows** you have — and **the list is what tells it.** Each item in the list is one row:
`[rowA, rowB]` → 2 rows, `[rowA]` → 1 row.

So what happens if you forget the list and hand it a **single dict**?

```python
one = {"Ticker": "AAPL", "Sector": "Tech", "Price": 180.50, "Shares": 50}
pd.DataFrame(one)     # ValueError: If using all scalar values, you must pass an index
```

Pandas sees the keys (fine — those look like columns), but each value is a *single* item, not a
list — so it can't tell how many rows you mean. One row? It has no way to know, so it stops. The
error *"If using all scalar values, you must pass an index"* is pandas saying: *"I can't count the
rows here."*

**The fix:** wrap the dict in a list, so it's clearly one row:

```python
print(pd.DataFrame([one]).to_string(index=False))   # a list with one row-dict -> a clean 1-row table
```

⚠️ **Don't be fooled by the error's advice.** It says "pass an index," and
`pd.DataFrame(one, index=[0])` *does* run — but that's a side door that trains the wrong mental
model. Keep it simple: **rows live in a list.** A list of dicts → a table. A bare dict → not a
table.

---

## Check yourself — Part 2

**Q6. (write it)** Starting from `HOLDINGS = {"AAPL": 50, "MSFT": 30}`, write the loop that builds
a DataFrame with columns `Ticker` and `Shares`, printed with no row-number column.
> Self-check — your output should be exactly:
> ```
> Ticker  Shares
>   AAPL      50
>   MSFT      30
> ```

**Q7. (spot the bug)** A teammate writes:
```python
row = {"Ticker": "AAPL", "Shares": 50}
df = pd.DataFrame(row)
```
…and it **raises an error** instead of building a table. What's the error, why does it happen, and
what's the right fix? *(The error message suggests one fix — but the better fix, the one from this
drill, is different. Which?)*

Send me your answers, then knock out the Section B redo.
