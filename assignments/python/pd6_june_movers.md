# PD6b — Who moved in June?
### Idynamics Finance Analyst Training Program

> **From:** David Chen, VP Finance · **To:** Michael · **Subject:** Names behind the June bridge
>
> The board saw your June bridge and asked the obvious next question: *who* are these customers?
> They want one list — company name, industry, what kind of move, and how much. `CUST048` means
> nothing to them.
>
> You've been on Excel and quizzes for three weeks, so this one is mostly a rebuild of ground you
> already covered, from memory and with no code in front of you. Two small new things in the
> middle of it.
>
> — David

Expect about 90 minutes.

---

## Why this, and when you'd use it

Your June bridge is **four separate tables** — new, expansion, contraction, churn. Fine for a bridge,
where you only want four totals. Useless for the board, who want **one list they can read down**.
So: put the four on top of each other and still be able to tell which row came from which. Two moves
— **label** each table, then **stack** them. In Excel that's copy, paste under, and type the type in
by hand; fine for four tables, and the reason nobody does it for twelve months.

**At the end** you'll have a named list of every June mover, biggest gain first, saved as a CSV, plus
change by industry — and you'll have rebuilt the whole bridge with nothing given to you, which is the
real point of this one.

**"Isn't that just `.append`?"** Almost, and you already append in a loop (PD5, Quiz 3 Q8). `.append()`
adds **one item to a list** — what you appended was a **dictionary**, one row, so you finished with
`pd.DataFrame(rows)`. Here each piece is a **whole table**, and a list of tables won't go through
`pd.DataFrame()`; `pd.concat()` is the one that takes tables. Same idea either way — collect the
pieces, build once at the end. Nothing you learned is being replaced.

---

## Tools you already know

Steps 1–4 and 7–8 use only these, and I'm giving you the code for none of them. If you can't remember
the wording, look it up in **your own earlier submissions** — `pd3_june_movements.py` has the groupby,
the outer merge, the `fillna` and the `_merge` filters; `pd5_every_month.py` the column select and
`to_csv`; `pd2_may_questions.py` has `sort_values` — or `docs/pandas_merge_cheatsheet.md`. Looking up
your own code isn't cheating; it's the job.

| To do this | You know |
|---|---|
| read a CSV · see what's in it | `pd.read_csv` · `.head()` |
| one row per customer | `groupby(..., as_index=False)[...].sum()` |
| two months side by side | `pd.merge(..., on=, how="outer", suffixes=, indicator=True)` |
| blanks from a merge → 0 | `.fillna(0)` assigned back |
| which table a row came from | the `_merge` column |
| a new calculated column | `df["change"] = ...` |
| keep some rows · some columns | `df[df["col"] > 0]` · `df[["a", "b"]]` |
| order it · count it | `.sort_values(col, ascending=)` · `len(df)` |
| look a value up from another table | `pd.merge(..., how="left")` |
| save it | `.to_csv(path, index=False)` |

---

## Step 0 — Set up

```
git checkout main
git pull origin main
git checkout -b student/pd6_june_movers
git status
```

`git status` must say `nothing to commit, working tree clean`, and `git log origin/main..HEAD` must
print nothing. After the pull you should have **three** files:

- `closes/2026-05/subscriptions_2026-05-31.csv`
- `closes/2026-06/subscriptions_2026-06-30.csv`
- `closes/2026-06/customers_2026-06-30.csv` ← the new one

Build your answer in `submissions/python/pd6_june_movers.py`. Run it after **every** step and read
the print before writing the next one.

---

## Learn it

Two new things, one line each. The examples are a sales team, not your close files, so you can see
the mechanic without copying anything.

**Plan before you type**, same four questions. Here: (1) one table, one row per rep, saying which
office they're in; (2) the information is in two tables, one per office — and neither has an `office`
column, it's only in the *name of the table*; (3) so put the office in as a column, then stack;
(4) right if rows and deals after stacking equal the two tables added up. **Question 2 is what tells
you a label is needed at all.**

### A label — a column with the same value on every row

```python
toronto = pd.DataFrame([{"rep": "Dana", "deals": 4}, {"rep": "Omar", "deals": 7}])
toronto["office"] = "Toronto"
print(toronto.to_string(index=False))
```

```
 rep  deals  office
Dana      4 Toronto
Omar      7 Toronto
```

One value in, every row gets it — no loop, no list. That's how you keep track of which piece is
which once they're no longer separate tables.

### Stacking — `pd.concat`

`pd.concat` takes **a list of tables** and puts them on top of each other, in list order; columns
line up by name.

```python
halifax = pd.DataFrame([{"rep": "Priya", "deals": 2}])
halifax["office"] = "Halifax"

all_reps = pd.concat([toronto, halifax])
print(all_reps.to_string(index=False))
print()
print(f"Rows: {len(all_reps)}  Total deals: {all_reps['deals'].sum()}")
```

```
  rep  deals  office
 Dana      4 Toronto
 Omar      7 Toronto
Priya      2 Halifax

Rows: 3  Total deals: 13
```

Two tables in, one out, and `office` still says where each row came from. 2 + 1 = 3 rows and
4 + 7 + 2 = 13 deals — that check is the only way you'd notice a table missing from the list.

**Common mistake — labelling after you stack.** Too late; nothing is left saying which was which, so
the label goes on every row:

```python
t2 = pd.DataFrame([{"rep": "Dana", "deals": 4}, {"rep": "Omar", "deals": 7}])   # unlabelled
h2 = pd.DataFrame([{"rep": "Priya", "deals": 2}])                               # unlabelled
mixed = pd.concat([t2, h2])
mixed["office"] = "Toronto"
print(mixed.to_string(index=False))
```

```
  rep  deals  office
 Dana      4 Toronto
 Omar      7 Toronto
Priya      2 Toronto
```

Priya is in Halifax. Nothing errored. **Label each piece first, while you still know what it is.**

**Common mistake — forgetting the list.** `pd.concat(toronto, halifax)` gives
`TypeError: concat() takes 1 positional argument but 2 were given`. It wants one thing (a list) and
you handed it two. The brackets *are* the list: `pd.concat([a, b])`.

### What `_merge` actually is

You've used `indicator=True` since PD3 without me ever saying what it does. It adds one column,
`_merge`, holding which table each row came from — only ever `both`, `left_only` (left table only) or
`right_only` (right table only). That's why one outer merge answers several questions at once: you're
not re-joining, you're filtering a column that's already there.

It's also your Quiz 3 error, `ValueError: Cannot use name of an existing column for indicator column`
— pandas goes to add `_merge`, finds one already there from an earlier merge, and won't overwrite it.
Your two-chained-merges workaround was fine, but what it was really asking is that you stop carrying a
column you've finished with: cut to the columns you need, or `.drop(columns="_merge")`.

---

## Your turn

**No code from me from here on** — you write all of it. Five steps. Print each under its numbered
heading so the output reads top to bottom, the way PD3 and PD5 did. The shapes below are the
**layout**, not the answers; `...` is yours to fill.

### Step 1 — Get May and June side by side

Three small moves, and run after each one:

- **a.** Read the three files and print `.head()` of each. Which columns does the customer list have,
  and which one does it share with your month-end lists?
- **b.** The month-end lists have one row per *subscription*, and a customer can hold more than one.
  The bridge is about customers, so collapse each month to one row per customer with their total MRR.
  *Check:* each month's total after collapsing equals its total before — if not, you grouped on the
  wrong thing. (Both totals are in your PD3 output.)
- **c.** Put the two months side by side: one row per customer, May's MRR and June's MRR next to each
  other, **keeping every customer, including ones in only one of the two months.** Those are the whole
  point: missing from May is new, missing from June is churn. Fill the blanks the merge leaves with
  zero, then add a `change` column, June minus May.

*Finish this plan in comments above your code:*

```
# 1. The answer looks like: one row per customer, with mrr_may, mrr_june, _merge and change.
# 2. The information is in: ______________________
# 3. Steps → tools: ______________________
# 4. I'll know it's right because: ______________________
```

```
1. MAY AND JUNE SIDE BY SIDE
customer_id  mrr_may  mrr_june     _merge  change
    CUST...      ...       ...        ...     ...
Customers: ...   Total change: ...
```

**Check:** total change across every customer = June total MRR − May total MRR. That's your PD3
tie-out, and it's the number every step after this has to keep matching.

### Step 2 — Split it into the four movements

Four tables out of the one: **new**, **expansion**, **contraction**, **churn**.

New and churn come off `_merge`. If you're not certain which `_merge` value is which, don't go from
memory — **read it off your own Step 1 output.** Find a customer whose May MRR is zero: they weren't
there in May, so they're new, and whatever their `_merge` says is your value for new. The opposite
value is churn. Working it out from the table in front of you beats remembering, and it takes ten
seconds.

For the other two, out of the customers in **both** months: expansion is the ones whose MRR **went
up** between May and June, contraction the ones whose MRR **went down**. Read those two phrases again
before you type the comparison, and write the sign the words actually say — not the one that looks
about right.

*Plan it first, same four comments, two blanks fewer filled in for you.*

```
2. THE FOUR MOVEMENTS
                 New  Expansion  Contraction  Churn
customers        ...        ...          ...    ...
change           ...        ...          ...    ...
```

(However you lay that out is fine, but print **both rows** — how many customers in each, and how
much change each accounts for. You need the counts again in Step 3.)

**Check — three parts, and you need all three, because the first passes even when the answer is
wrong:**

1. The four tables' changes add up to Step 1's total change.
2. Count the customers whose change is exactly zero — they moved nowhere, so they belong in none of
   the four. Print that count, then check your four counts don't include them.
3. **Print your new and churn tables and look at the MRR columns.** A new customer has no May MRR;
   a churned one has no June MRR. If yours say the opposite they're the wrong way round — which
   `_merge` value means which depends on the month you put on the *left* of that merge, and no total
   will tell you, because the two swap cleanly and still add up.

Check 3 is the one that matters: get it wrong and the board gets a customer who left us, listed as a
new win, with every total tying perfectly.

### Step 3 — Label each one, then stack them

Both new things, in that order — and the order is the point.

- **a.** Give each of the four a `movement` column saying which it is: `New`, `Expansion`,
  `Contraction`, `Churn` — exactly those words, that spelling; `New` and `new` sort into different
  places. Print one table to see the column landed, and check it has one more column than it did in
  Step 2 with the same word on every row.
- **b.** Stack the four into one table, then cut it to the columns a board list needs — customer,
  what the move was, May, June, change — and nothing else.

```
3. ONE LIST OF MOVERS
customer_id    movement  mrr_may  mrr_june  change
    CUST...         ...      ...       ...     ...
Movers: ...  Total change: ...
```

**Check:** print both numbers. Row count = Step 2's four counts added up — short means a table is
missing from the list, over means one went in twice. Total change = Step 1's total, still. And ask
whether that count looks like the word *movers*: if nearly every customer we have is on the board's
list of people who moved, something upstream is wrong.

### Step 4 — Add the names and save

The board wants company name and industry, not IDs. Look both up from the customer list, keep
`customer_id`, `company_name`, `industry`, `movement`, `change`, biggest gain first, and save to
`submissions/python/pd6_june_movers.csv`. Think about which way round that merge goes — your movers
list is the one that must survive intact.

```
4. WITH THE CUSTOMER NAMES
Rows: ...  Not found: ...
customer_id  company_name  industry  movement  change
    CUST...           ...       ...       ...     ...
```

**Check:** print both numbers. Rows after the lookup must equal rows before (Step 3's count) — a
lookup that changes the count has duplicated or dropped somebody. And **not found must be 0**: print
it, don't just hope. If a name is missing, say so in your PR rather than letting a blank reach the
board.

### Step 5 — Change by industry

One short table: total change per industry, biggest first, total underneath. No hints for this
one — plan it in comments, write it, check it.

```
5. CHANGE BY INDUSTRY
   industry  change
        ...     ...
Total: ...
```

**Check:** still Step 1's total change.

Then read that table before you close the file. Anything in it you'd want to tell me without being
asked?

---

## Hand in

`submissions/python/pd6_june_movers.py` **and** `submissions/python/pd6_june_movers.csv`, committed
to your branch, and a PR with this description:

~~~
## PD6b — Who moved in June?

## My output (pasted from my terminal)
```
[paste the whole thing, Steps 1-5]
```

## Conditions
For expansion and for contraction: the line of code, and next to it the words from the brief it
came from.

## The append question
In your own words: when do you use `.append` and when `pd.concat`? And what does `_merge` do — what
was that ValueError on Quiz 3 telling you?

## My finding
Anything in the numbers worth telling me that nobody asked for. Three lines: what I found · why it
matters in dollars · what I'd recommend. Write "nothing" if you got nothing.

## Why pandas?
Why do this in pandas rather than Excel? Two sentences.

## How it went
How long, which step did you have to go and look up, and where did you get stuck?
~~~
