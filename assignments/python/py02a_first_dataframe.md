# Python 02-a: Your First DataFrame — the Indices Table
### iDynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** First board panel — building the table
>
> Fundamentals are done, so we start building the actual market board. The
> first panel is the one that sits top-left — the one leadership looks at
> first: the five big market indices, where each one is right now, and how
> much it moved today. Green for up, red for down.
>
> We'll build it in three short parts on one branch: **02-a** (this one) builds
> the table and prints it; **02-b** styles it into a web page you can open;
> **02-c** adds a preview of what's coming and starts your own project repo.
>
> This part introduces one genuinely new tool — the pandas **DataFrame** — and
> reuses the yfinance quote pull you already wrote in PY01.
>
> Standing rules apply: stuck >15 min → paste what you see and stop. And any
> error that names the network, a ticker, or yfinance — or any error you're
> confident you didn't cause — is almost always the data provider, not your
> code: paste it and stop.
>
> — David

---

## Before you start

From the repo root, with your venv active:

```powershell
git pull origin main
pip install -r assignments/python/requirements.txt
```

The first command brings in this assignment; the second is the usual safety check (you'll see "already satisfied" for most lines — that's fine).

One package is new this assignment: **`jinja2`**. Run the install now even though nothing uses it until 02-b — it's what the styled HTML page is built on. If you skip it, 02-b will stop with `ImportError: Missing optional dependency 'jinja2'` the moment you try to style the table. That error means "run the install line above," not "something is wrong with your code."

## What we're building

A small table of the five major market indices:

| Index | Symbol |
|---|---|
| S&P 500 | `^GSPC` |
| NASDAQ 100 | `^NDX` |
| Dow Jones | `^DJI` |
| Russell 2000 | `^RUT` |
| CBOE VIX | `^VIX` |

For each index we want four columns. In plain terms:

- **Index** — the name.
- **Last** — its latest level (the current price of the index).
- **1D Change** — how much it moved *today*, measured in points: today's level minus yesterday's closing level (`last − previous_close`).
- **1D %** — that same move written as a percentage of yesterday's close: `(last − previous_close) / previous_close × 100`.

The finished table is sorted so the best performer (highest **1D %**) is on top. That's the whole panel — five rows, four columns.

## New tool: the pandas DataFrame

In PY01 you collected results by looping tickers and storing numbers. A **DataFrame** is the next step up: a table object — think of a SQL result set, or a range in Google Sheets — that Python can sort, do math on, and turn into a web page. It's the workhorse of every analyst's Python code, and you'll use it in every assignment from here on.

You need four moves today. Type each example in and run it — the output shown is exactly what you should see.

### 1. Build a DataFrame from a list of dicts

This is exactly the shape you already know: **a list of dicts** (from PF and PY01). Each dict is one **row**, and its keys become the **column names**. You hand that list to `pd.DataFrame(...)`:

```python
import pandas as pd

rows = [
    {"Index": "CBOE VIX",   "Last": 15.03,    "1D %": -5.11},
    {"Index": "S&P 500",    "Last": 7575.39,  "1D %": 0.42},
    {"Index": "NASDAQ 100", "Last": 29825.11, "1D %": 0.33},
]
df = pd.DataFrame(rows)
print(df.to_string(index=False))
```
```
     Index     Last  1D %
  CBOE VIX    15.03 -5.11
   S&P 500  7575.39  0.42
NASDAQ 100 29825.11  0.33
```

`print(df.to_string(index=False))` is how you print a DataFrame cleanly — the `index=False` part hides pandas' automatic row-number column, which you don't want.

### 2. Loop a dict of name → symbol pairs with `.items()`

You'll build your table by looping the five indices. When you need *both* the name and the symbol out of a dict, `.items()` hands you both at once:

```python
INDICES = {"S&P 500": "^GSPC", "CBOE VIX": "^VIX"}
for name, symbol in INDICES.items():
    print(name, "->", symbol)
```
```
S&P 500 -> ^GSPC
CBOE VIX -> ^VIX
```

`name` is the key, `symbol` is the value — one pair per pass. (Plain `for name in INDICES:` gives you only the keys, like in PF; `.items()` gives you both.)

### 3. Assemble the rows with a loop

Real data doesn't arrive as a finished list — you build it. In PF3 you made a running total by starting at `0` and adding inside the loop; assembling a *list of rows* is the same habit, one level up: **start with an empty list, and `.append()` one row-dict each pass.** (`list.append(x)` adds `x` to the end of a list.)

```python
import pandas as pd

INDICES = {"S&P 500": "^GSPC", "CBOE VIX": "^VIX"}
rows = []                                           # start empty, like a running total starts at 0
for name, symbol in INDICES.items():
    rows.append({"Index": name, "Symbol": symbol})  # append one row-dict each pass
df = pd.DataFrame(rows)
print(df.to_string(index=False))
```
```
   Index Symbol
 S&P 500  ^GSPC
CBOE VIX   ^VIX
```

After the loop, `rows` holds one dict per index — exactly the list `pd.DataFrame` wants. That's the real build: loop the five indices, append a row-dict for each, then hand the finished list to `pd.DataFrame`.

### 4. Sort it

`df.sort_values("1D %", ascending=False)` hands back the *same table, re-ordered* by the column you name. `ascending=False` means biggest first (build a small table first so the example stands alone):

```python
import pandas as pd

df = pd.DataFrame([
    {"Index": "CBOE VIX",   "Last": 15.03,    "1D %": -5.11},
    {"Index": "S&P 500",    "Last": 7575.39,  "1D %": 0.42},
    {"Index": "NASDAQ 100", "Last": 29825.11, "1D %": 0.33},
])
df_sorted = df.sort_values("1D %", ascending=False)
print(df_sorted.to_string(index=False))
```
```
     Index     Last  1D %
   S&P 500  7575.39  0.42
NASDAQ 100 29825.11  0.33
  CBOE VIX    15.03 -5.11
```

Same three rows — now ordered best-to-worst by `1D %`. Notice the rows moved together: sorting a DataFrame keeps each row intact, it just reorders them.

One small helper you'll use: **`round(number, 2)`** rounds to two decimals — `round(0.42371, 2)` gives `0.42`, `round(31.749, 2)` gives `31.75`. Round each number as you put it into its row.

> **The classic mistake:** building the DataFrame from a *dict* instead of a *list of dicts*. `pd.DataFrame` wants a **list**, where each item is one row-dict. If you pass a single dict, or forget to `.append()` each row into the list, you'll get one row or a confusing shape. Build the list first (start it empty, append inside the loop — the PF accumulator habit), then hand the finished list to `pd.DataFrame`.

**✅ Quick check 1:** in `pd.DataFrame(rows)`, what does each dict in `rows` become?  *(answer: one row; its keys become the column names)*

**✅ Quick check 2:** which gives you both the name and the symbol in one loop — `for name in INDICES:` or `for name, symbol in INDICES.items():`?  *(answer: `.items()`)*

## Reusing your PY01 quote pull

In PY01 you wrote a small function that pulled a ticker's `lastPrice` and `previousClose`. That code is yours and it's already on `main` — open `submissions/python/py01_python_warmup/watchlist.py` and look at it before you start here. You're reusing it, not rewriting it from memory.

Two reminders so nothing is guesswork. Your script needs **two** imports at the top:

```python
import pandas as pd
import yfinance as yf
```

and the quote pull itself is the same pair of `fast_info` lookups you used in PY01:

```python
info = yf.Ticker(symbol).fast_info
info["lastPrice"]        # where it is now
info["previousClose"]    # where it closed yesterday
```

Reuse that shape here, but return **three** numbers per index — the last level, the point change, and the percent change:

- point change = `last − previous_close`
- percent change = `(last − previous_close) / previous_close × 100`

Wrap those in a function that takes a symbol and returns all three, exactly like your PY01 helper returned two. Because it returns three values, you unpack three when you call it — `last, chg, pct = get_quote(symbol)` — the same move as PY01's two-value unpack, just one more name. (If pulling a quote throws an error, that's the provider — paste it and stop, per the standing rule.)

## Your task

Build `submissions/python/py02_asset_classes/asset_classes.py` so that it:

1. Loops the five indices with `.items()`, and for each one calls your quote function to get the last level, the 1D point change, and the 1D percent.
2. Appends one dict per index — keys `Index`, `Last`, `1D Change`, `1D %` — into a `rows` list, rounding the three numbers to 2 decimals as you go.
3. Builds a DataFrame from `rows` and sorts it by `1D %`, best first.
4. Prints the table with `print(df.to_string(index=False))`.

Run it from the repo root:

```powershell
python submissions/python/py02_asset_classes/asset_classes.py
```

You'll extend this same script in 02-b (styling) — leave it in place when you're done here.

## Self-check

The numbers change with the live market, so these check the *shape*, not exact values:

- [ ] The printed table has exactly **5 rows** and the four columns `Index`, `Last`, `1D Change`, `1D %`.
- [ ] Rows are sorted so **`1D %` decreases** top to bottom (best performer first).
- [ ] On **every row, `1D Change` and `1D %` have the same sign** (both positive or both negative). If one row's signs disagree, one of the two formulas is wrong.
- [ ] Every number shows at most **2 decimals** (you rounded).
- [ ] No automatic row-number column on the left (that's the `index=False`).

## Submission

- This is part of the PY02 branch — **one branch, one PR** for 02-a/b/c, a commit per part.
- Branch: `submission/py02-asset-classes`
- File so far: `submissions/python/py02_asset_classes/asset_classes.py`
- Commit this part on its own, e.g. `PY02-a: indices table printed to console`.
- **📋 Save your console table** — you'll paste it, with this self-check ticked, into the PR description when you open the PR at the end of 02-c. (One PR covers all three parts.)
