# PD3 — Where did June's MRR change come from?
### Idynamics Finance Analyst Training Program

> **From:** David Chen, VP Finance · **To:** Michael · **Subject:** June's MRR bridge for the board pack
>
> June's MRR went from 160,075.50 to 162,830.50. The board will ask where the 2,755 came from:
> how much from new customers, how much from customers who grew or shrank, and how much we lost.
> That's the MRR bridge, and it goes in every month's pack.
>
> This is the first of three short ones. After them you'll build a small project of your own: a
> script that makes the whole first half of 2026's MRR pack in one run. Everything you need for
> it, you'll learn in these three.
>
> — David

Expect about 1 hour 30 minutes.

## Why this, and when you'd use it

The MRR bridge answers "what changed between two month-end lists?" In Excel 17 you did it by hand:
a list of every ID from both months, a SUMIFS for each month, a Difference column and a label. In
pandas, **`pd.merge`** lines the two lists up side by side in one command, including the IDs that
are only in one of them. Use it whenever you compare two lists that share an ID: this month vs last
month, our billing vs the bank, the CRM vs the database. It's the standard way analysts do this in
pandas.

**Movements are about customers.** A **new** customer, an existing customer who **expanded** (pays
more), one who **contracted** (pays less), and a customer who **churned** (left). A customer who
buys a second subscription pays us more: that's expansion, not a new customer. So you'll add up MRR
per customer first (PD1's `groupby`), then compare the two months.

## Step 0 — Set up

In VS Code, **Terminal → New Terminal**:

```
git status
```

It must say `nothing to commit, working tree clean`. If it lists files, message me before going on.

```
git checkout main
git pull origin main
git checkout -b student/pd3_june_movements
git log origin/main..HEAD --oneline
```

The last command must print nothing.

---

## Learn it

Use `scratch.py` in `submissions/python` (not submitted; if it's gone: right-click
`submissions/python` → **New File** → `scratch.py`). Clear it and start with:

```python
import pandas as pd

may = pd.read_csv("assignments/python/pd3_examples/may_example.csv")
june = pd.read_csv("assignments/python/pd3_examples/june_example.csv")
```

Two tiny made-up lists, already one row per customer. May has CUST901 (1,000), CUST902 (500),
CUST903 (800). June has CUST901 (1,200), CUST903 (600), CUST904 (700). So CUST902 left, CUST904 is
new, CUST901 grew and CUST903 shrank. As in PD1b, we print without `.to_string(index=False)` so you
see the row numbers.

### Example 1 — `pd.merge`, built one piece at a time

**Piece 1: match the rows on an ID.**

```python
both = pd.merge(may, june, on="customer_id")   # NEW: put may and june side by side, matched on customer_id
print(both)
```

```
  customer_id  mrr_x  mrr_y
0     CUST901   1000   1200
1     CUST903    800    600
```

`may` is the **left** list, `june` the **right** one. `on="customer_id"` is the column that matches
rows up, like the lookup key in a SUMIFS. Both lists have a column called `mrr`, so pandas called
them `mrr_x` (left) and `mrr_y` (right).

Only 2 rows: CUST902 and CUST904 are missing. By default merge keeps only the IDs that are in
**both** lists. For a bridge that's wrong: those two are your churn and your new customer.

**Piece 2: keep every ID from both lists.**

```python
both = pd.merge(may, june, on="customer_id", how="outer")   # new option: how="outer" keeps IDs from either list
print(both)
```

```
  customer_id   mrr_x   mrr_y
0     CUST901  1000.0  1200.0
1     CUST902   500.0     NaN
2     CUST903   800.0   600.0
3     CUST904     NaN   700.0
```

All 4 customers. This is your "list of every ID from both months" from Excel 17. `NaN` means **no
value**: CUST904 had no May row, so there's no May MRR.

**Piece 3: give the two `mrr` columns real names.**

```python
both = pd.merge(may, june, on="customer_id", how="outer",
                suffixes=("_may", "_june"))   # new option: name the left and right mrr columns
print(both)
```

```
  customer_id  mrr_may  mrr_june
0     CUST901   1000.0    1200.0
1     CUST902    500.0       NaN
2     CUST903    800.0     600.0
3     CUST904      NaN     700.0
```

The first name goes on the left list's column, the second on the right list's. A line in `( )` can
go onto the next line, as here; Python reads it as one line until the `)` closes.

**Piece 4: say where each row came from.**

```python
both = pd.merge(may, june, on="customer_id", how="outer",
                suffixes=("_may", "_june"), indicator=True)   # new option: indicator=True adds a _merge column
print(both)
```

```
  customer_id  mrr_may  mrr_june      _merge
0     CUST901   1000.0    1200.0        both
1     CUST902    500.0       NaN   left_only
2     CUST903    800.0     600.0        both
3     CUST904      NaN     700.0  right_only
```

`_merge` says `both`, `left_only` (only in May: they left) or `right_only` (only in June: they're
new). That column will sort customers into movements for you.

**Read it aloud:** "both is: merge may and june on customer_id, keep every ID, call the columns
_may and _june, and add a column saying where each row came from."

### Example 2 — `.fillna(0)`: no row means zero MRR

Try the change column straight away:

```python
print(both["mrr_june"] - both["mrr_may"])
```

```
0    200.0
1      NaN
2   -200.0
3      NaN
dtype: float64
```

Any sum with `NaN` in it is `NaN`, so the new customer and the churned one have no change at all.
But a customer with no May row had **zero** May MRR. Fill the gaps with 0 first:

```python
both = both.fillna(0)          # NEW: replace every NaN with 0
print(both)
```

```
  customer_id  mrr_may  mrr_june      _merge
0     CUST901   1000.0    1200.0        both
1     CUST902    500.0       0.0   left_only
2     CUST903    800.0     600.0        both
3     CUST904      0.0     700.0  right_only
```

`fillna(0)` gives back a filled copy, so assign it back to `both` (like `sort_values`). Now the
change column works for every row (Drill 2: a new column from column math):

```python
both["change"] = both["mrr_june"] - both["mrr_may"]
print(both)
```

```
  customer_id  mrr_may  mrr_june      _merge  change
0     CUST901   1000.0    1200.0        both   200.0
1     CUST902    500.0       0.0   left_only  -500.0
2     CUST903    800.0     600.0        both  -200.0
3     CUST904      0.0     700.0  right_only   700.0
```

### Example 3 — Filter on `_merge`

`_merge` is a text column, so you filter it like `billing_cycle` in PD1b:

```python
new = both[both["_merge"] == "right_only"]   # keep the rows only in June
print(new)
```

```
  customer_id  mrr_may  mrr_june      _merge  change
3     CUST904      0.0     700.0  right_only   700.0
```

### When it goes wrong

| You write | What happens | Fix |
|---|---|---|
| `pd.merge(may, june, on="customer_id")` | no error; new and churned customers are silently missing, so the bridge won't tie | add `how="outer"` |
| no `.fillna(0)` | no error; New and Churn come out as `0.00` because `.sum()` skips `NaN` | `both = both.fillna(0)` before the change column |
| `both.fillna(0)` on its own line | no error; nothing changes | assign it back: `both = both.fillna(0)` |

None of these give an error message. The check at the end of each step is how you catch them.

---

## Your turn

Right-click `submissions/python` → **New File** → `pd3_june_movements.py`. Type the code, fill each
blank (`____`), press ▶ after every step and look at each print before going on.

### Step 1 — Add up MRR per customer

Movements are counted per customer, so first turn each month's subscription list into one row per
customer.

```python
import pandas as pd

may = pd.read_csv("closes/2026-05/subscriptions_2026-05-31.csv")
june = pd.read_csv("closes/2026-06/subscriptions_2026-06-30.csv")

print("1. MRR PER CUSTOMER")
may_cust = may.groupby("____", as_index=False)["mrr"].sum()     # one row per customer, MRR added up
june_cust = june.groupby("____", as_index=False)["mrr"].sum()
print(f"May:  {len(may_cust)} customers, MRR {may_cust['mrr'].sum():,.2f}")
print(f"June: {len(june_cust)} customers, MRR {june_cust['mrr'].sum():,.2f}")
```

`len(may_cust)` now counts customers, not subscriptions.

**Check it worked:** both MRR totals equal the two figures in my message at the top. If they
don't, you're reading the wrong file.

### Step 2 — Put May and June side by side

```python
print()
print("2. MAY AND JUNE SIDE BY SIDE")
both = pd.merge(may_cust, june_cust, on="____", how="____",
                suffixes=("_may", "_june"), indicator=True)   # Example 1, on your real lists
both = both.____(0)                                           # Example 2: no row = zero MRR
both["change"] = both["mrr_june"] - both["mrr_may"]
changed = both[both["change"] != 0]                           # != means "not equal to"
print(changed.to_string(index=False))
print(f"Rows: {len(both)}  May MRR: {both['mrr_may'].sum():,.2f}  June MRR: {both['mrr_june'].sum():,.2f}")
```

`changed` keeps only the customers whose MRR changed, so you can read them all at once.

**Check it worked:** the May MRR and June MRR on the last line equal Step 1's totals. If they
don't, a customer was dropped: check `how=`.

### Step 3 — Split the change into movements

```python
print()
print("3. MOVEMENTS")
new = both[both["_merge"] == "____"]           # only in June
churn = both[both["_merge"] == "____"]         # only in May
stayed = both[both["_merge"] == "both"]        # in both months
expansion = stayed[stayed["change"] > 0]       # stayed and pays more
contraction = stayed[stayed["change"] ____ 0]  # stayed and pays less
print(f"New:         {new['change'].sum():,.2f}  customers: {len(new)}")
print(f"Expansion:   {expansion['change'].sum():,.2f}  customers: {len(expansion)}")
print(f"Contraction: {contraction['change'].sum():,.2f}  customers: {len(contraction)}")
print(f"Churn:       {churn['change'].sum():,.2f}  customers: {len(churn)}")
```

Expansion and contraction are two filters, one after the other: first keep the `both` rows, then
split them by the sign of `change`. Contraction and churn print as negative numbers: they take MRR
away.

**Check it worked:** every customer Step 2 printed (the ones whose MRR changed) lands in exactly one
movement, so the four customer counts add up to the number of rows Step 2 printed.

### Step 4 — Prove it ties

No code this time. Add a step that rebuilds June's closing MRR from May's opening MRR plus the four
movements, and compares it with June's actual closing MRR. Use the total MRR of the two **original**
lists (`may` and `june`) for opening and closing. Your output must look like this, with your
numbers:

```
4. DOES IT TIE?
Opening (May):    ...
Rebuilt closing:  ...
Closing (June):   ...
Difference:       ...
```

Every number must be calculated by your code: no typed-in figures. If the difference isn't 0.00,
the bridge is wrong: go back to Steps 2 and 3.

---

## Hand in

Commit `submissions/python/pd3_june_movements.py` only (not `scratch.py`): **Source Control** → `+`
on the file → message `Complete: PD3 — June movements` → **Commit** → **Publish Branch**. Then open
a PR from `student/pd3_june_movements` to `main` with this description:

~~~
## PD3 — June movements

## My output (pasted from my terminal)
```
[paste the full output here]
```

## One question
Two new subscriptions started in June: SUB070 and SUB071. Does your New include both? Find the
customer behind SUB071 in the June list, paste that customer's row from your Step 2 table, and say
where SUB071's MRR shows up in your movements and why. (2–3 sentences)

## Why pandas?
Why would you use this instead of Excel for the monthly bridge? (2 sentences)

## How it went
How long did it take, and where did you get stuck?
~~~
