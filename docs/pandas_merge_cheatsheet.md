# pandas merge — Quick Reference

> You've used `how="outer"` with `indicator=True` to find rows with no match. This page shows
> the other three options and how to pick one. They are the same idea as SQL JOINs
> (see `sql_joins_cheatsheet.md`).

---

## What merge does

`pd.merge` lines up two tables by a shared column (the key, e.g. `customer_id`) and glues
matching rows side by side. It's like XLOOKUP, but it brings back every column at once.

`how=` decides **what happens to rows that have no match on the other side.**

```python
pd.merge(left_table, right_table, on="customer_id", how="...")
#        ^ first = LEFT  ^ second = RIGHT
```

**Left is simply the table you write first.** Right is the second one.

---

## The example tables

```
customers                   invoices
customer_id  company        customer_id  amount
         C1   Aurora                 C1     500
         C2 Borealis                 C1     300
         C3  Cascade                 C3     450
                                     C9     200   <- no such customer
```

C2 has no invoices. C9 has an invoice but isn't a customer.

---

## The four options (real output, pandas 3.0)

### `how="inner"` — only IDs in both tables. **This is the default if you leave `how` out.**
```
customer_id company  amount
         C1  Aurora     500
         C1  Aurora     300
         C3 Cascade     450
```
C2 and C9 are dropped **without any warning**.

### `how="left"` — every row of the first table, plus matches
```
customer_id  company  amount
         C1   Aurora   500.0
         C1   Aurora   300.0
         C2 Borealis     NaN
         C3  Cascade   450.0
```
Every customer stays; C2 gets NaN. C9 is dropped. This is the XLOOKUP behaviour.

### `how="right"` — every row of the second table, plus matches
```
customer_id company  amount
         C1  Aurora     500
         C1  Aurora     300
         C3 Cascade     450
         C9     NaN     200
```
Same as left, with the tables' roles swapped. Rarely needed: swap the order and use left.

### `how="outer"` — every ID from both tables
```
customer_id  company  amount     _merge
         C1   Aurora   500.0       both
         C1   Aurora   300.0       both
         C2 Borealis     NaN  left_only
         C3  Cascade   450.0       both
         C9      NaN   200.0 right_only
```
(with `indicator=True`). `left_only` = only in the first table, `right_only` = only in the second.

---

## Does the order matter?

| how | Swap the tables and… |
|---|---|
| inner | same rows (only the column order changes) |
| outer | same rows, but **`left_only` and `right_only` swap** — C2 becomes `right_only` |
| left | different result: you now keep every invoice instead of every customer |

So put first **the list you are checking against, or the one you must not lose rows from**
(usually the master list: customers, books, accounts).

---

## Which one do I use?

Ask: **"If a row has no match, do I want to see it?"**

| I want… | Use |
|---|---|
| only rows that match on both sides | `inner` |
| my main list kept whole, with values looked up | `left` (main list first) |
| what's missing on **either** side (a reconciliation) | `outer` + `indicator=True` |

---

## Common mistake: one row per ID

C1 has two invoices, so C1 appears **twice** after every merge above. If you wanted one row per
customer, `groupby` the right table first:

```python
totals = invoices.groupby("customer_id", as_index=False)["amount"].sum()
pd.merge(customers, totals, on="customer_id", how="left")
```
```
customer_id  company  amount
         C1   Aurora   800.0
         C2 Borealis     NaN
         C3  Cascade   450.0
```
Add `.fillna(0)` on `amount` if a missing match should count as zero.
