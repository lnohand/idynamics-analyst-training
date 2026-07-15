# Python Fundamentals 1: Values & Collections
### iDynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Starting Python from the ground up
>
> We're going to build Python the way we built SQL: one idea at a time, with
> worked examples you can copy the shape of, then a few exercises to make it
> stick. No market data, no loops yet — just the raw materials every program is
> made of: **values**, and the two ways Python stores a bunch of them (**lists**
> and **dictionaries**).
>
> Read each section, TYPE IN the examples and run them (don't just read — the
> outputs shown are exactly what you should see), then do the exercises.
>
> Standing rule: stuck >15 min → paste what you see and stop.
>
> — David

---

## Before the code — what you're actually running

You keep typing `venv`, `activate`, `pip install`. Here's what those actually are, so
they stop being magic words:

- **Python** is the program that runs your `.py` files.
- **A package** is code someone else wrote that you can use (e.g. `pandas`). You get them
  with `pip install`.
- **A virtual environment (`venv`)** is a private toolbox *for one project*. Instead of
  installing packages onto your whole computer, you install them into the project's
  `.venv` folder. That way each project has exactly the tools it needs and nothing
  collides. The `.venv` folder is **not** stored in git — it's specific to your machine —
  so a fresh clone won't have one until you create it: `py -3.14 -m venv .venv` (once).
- **`requirements.txt`** is the shopping list of packages a project needs.
  `pip install -r requirements.txt` reads that list and installs them **into `.venv`**.
  They stay there — you don't reinstall every time. Re-running it just checks
  ("Requirement already satisfied") and does nothing.
- **`activate`** switches your terminal *into* that toolbox. This one you DO run every new
  terminal (you'll see `(.venv)` on your prompt) — activation is per-terminal, not
  permanent.

Shorthand: **create once, install once, activate every time.**

*(This assignment uses no packages — plain Python — so you don't even need the install
step here. But now you know what it's for.)*

---

## 1. Values and variables

Everything in Python is a **value**, and every value has a **type**. The four you'll use
constantly:

| Type | What it is | Example |
|------|-----------|---------|
| `int` | a whole number | `18500` |
| `float` | a number with a decimal | `3.5` |
| `str` | text ("string"), in quotes | `"Acadia Software"` |
| `bool` | true/false | `True`, `False` |

A **variable** is a name you attach to a value with `=`, so you can reuse it:

```python
company = "Acadia Software"
amount = 18500
is_enterprise = False

print(company)
print(amount)
print(is_enterprise)
```
```
Acadia Software
18500
False
```

`type(x)` tells you what type a value is — handy when something misbehaves:

```python
print(type(amount))         # <class 'int'>
print(type(3.5))            # <class 'float'>
print(type(company))        # <class 'str'>
print(type(is_enterprise))  # <class 'bool'>
```

> **The classic mistake:** quotes make it a string. `amount = "18500"` is *text*, not a
> number — you can't do math on it. `18500` and `"18500"` look the same when printed but
> behave completely differently.

**✅ Quick check:** what does `type(4200)` print?  *(answer: `<class 'int'>`)*

---

## 2. f-strings — printing values inside text

To drop a value into a sentence, put `f` before the opening quote and the variable in
`{ }`:

```python
name = "Cobalt Mining Co"
amount = 156000
print(f"{name}: ${amount:,}")
```
```
Cobalt Mining Co: $156,000
```

The `:,` after the variable adds thousands commas. For money with cents, use `:,.2f`
(comma + 2 decimals):

```python
average = 49055.5555
print(f"Average deal size: ${average:,.2f}")
```
```
Average deal size: $49,055.56
```

> Two formats you'll reuse all track: `:,` for whole dollars, `:,.2f` for dollars and
> cents. The `$` is just a plain character you type — Python only handles what's inside
> the `{ }`.

**✅ Quick check:** what does `print(f"${1234567:,}")` produce?  *(answer: `$1,234,567`)*

---

## 3. Lists — many values in a row

A **list** holds several values in order, in square brackets:

```python
amounts = [18500, 4200, 156000]

print(amounts[0])     # 18500  — the FIRST item is index 0, not 1
print(amounts[2])     # 156000 — the third item
print(len(amounts))   # 3      — how many items
```
```
18500
156000
3
```

Two things everyone trips on once:
- **Counting starts at 0.** `amounts[0]` is the first, `amounts[1]` the second. So the
  *last* item of a 3-item list is `amounts[2]`, not `amounts[3]`.
- **`len(list)` gives the count** — the number of items.

**A list *can* hold mixed types** — `["Acadia", 18500, True]` is legal Python. But we
almost always keep a list all-one-type (all numbers, all names), because the whole point
of a list is to do the *same thing* to *every* item — which only makes sense if they're
alike. When you need to bundle values of *different* types that belong together (a name
AND an amount), that's the next tool: a dictionary.

**✅ Quick check:** for `amounts = [18500, 4200, 156000]`, what is `amounts[1]`?
*(answer: `4200`)*

---

## 4. Dictionaries — a labeled record

A list finds things by *position* (`[0]`, `[1]`). A **dictionary** finds things by
*name* — a **key**. It's how you store one record with labeled fields:

```python
deal = {"name": "Delta Logistics", "amount": 47500}

print(deal["name"])      # Delta Logistics
print(deal["amount"])    # 47500
```
```
Delta Logistics
47500
```

You read a field with `dict["key"]`. This is perfect for a deal: `name` is a string,
`amount` is an int, and they live together under one variable. Combine with an f-string:

```python
print(f"{deal['name']}: ${deal['amount']:,}")
```
```
Delta Logistics: $47,500
```

> **Watch the quotes** inside the f-string: the outer string uses `"..."`, so inside the
> `{ }` use single quotes — `deal['name']` — so they don't clash.

**✅ Quick check:** for `deal = {"name": "Delta Logistics", "amount": 47500}`, how do you
get `47500`?  *(answer: `deal["amount"]`)*

---

## 5. A list of dictionaries — the real shape of data

Now put them together: a **list of dicts** — many records, each a labeled dictionary.
This is how a whole sales pipeline is stored, and it's the shape you'll use all track.

**Paste this at the top of your file:**

```python
DEALS = [
    {"name": "Acadia Software",    "amount": 18500},
    {"name": "Blue Harbor Foods",  "amount": 4200},
    {"name": "Cobalt Mining Co",   "amount": 156000},
    {"name": "Delta Logistics",    "amount": 47500},
    {"name": "Echo Media Group",   "amount": 8900},
    {"name": "Foothills Energy",   "amount": 92300},
    {"name": "Glacier Insurance",  "amount": 3100},
    {"name": "Harborview Clinics", "amount": 61000},
    {"name": "Ironwood Labs",      "amount": 50000},
]
```

`DEALS` is a **list** (use `[0]`, `len()`), and each item is a **dict** (use `["name"]`,
`["amount"]`). You reach a field in two steps — pick the record, then the field:

```python
print(DEALS[0])            # {'name': 'Acadia Software', 'amount': 18500}
print(DEALS[0]["name"])    # Acadia Software  — first deal's name
print(DEALS[2]["amount"])  # 156000           — third deal's amount
print(len(DEALS))          # 9                — nine deals
```

Read `DEALS[2]["amount"]` left to right: "of `DEALS`, take item 2, then its `amount`."
That two-step reach is the single most useful move in the whole track — the loops and
functions coming next are just ways to do it to *every* deal at once.

**✅ Quick check:** what is `DEALS[1]["name"]`?  *(answer: `Blue Harbor Foods`)*

---

## Exercises

Build these in a file `pf1.py`, with the `DEALS` block at the top. **No loops or `if`
needed yet** — everything here is variables, indexing, `len()`, dict access, and
f-strings. Print each answer.

**E1 — One deal, formatted.** Make two variables for the Foothills Energy deal (its name
and amount) and print them as `Foothills Energy: $92,300`.

**E2 — First and last.** Given `amts = [18500, 4200, 156000, 47500]`, print the first
item and the last item using indexing. (For the last one, `len(amts) - 1` gives you the
last index — no counting by hand.)

**E3 — Reach into the pipeline.** From `DEALS`, print the third deal formatted exactly
like E1 — name, colon, dollar amount with commas.

**E4 — Combine two fields.** Print the combined value of the third deal (`DEALS[2]`) and
the sixth deal (`DEALS[5]`) — reach each amount, add them, format the result with `$` and
commas.

**E5 — Size it up.** Print how many deals are in the pipeline using `len()`, then print
the name of the **last** deal using `DEALS[-1]` (a negative index counts from the end —
`-1` is the last item).

## Self-check (data is fixed, so these are exact)

- [ ] **E1:** `Foothills Energy: $92,300`
- [ ] **E2:** `18500` then `47500`
- [ ] **E3:** `Cobalt Mining Co: $156,000`
- [ ] **E4:** `$248,300`  *(156,000 + 92,300)*
- [ ] **E5:** `9` then `Ironwood Labs`

## Submission

- Follow `docs/assignment_workflow.md` (branch from main, work in your submissions folder,
  the pre-push check).
- Branch: `submission/pf1-values-collections`
- File: `pf1.py`
- PR description: **📋 the full program output** and the self-check ticked line by line.
