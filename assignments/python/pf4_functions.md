# Python Fundamentals 4: Functions
### iDynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Naming a piece of work so you can reuse it
>
> Last one before you're ready for the real drills. A **function** is a named
> piece of work you write once and reuse — `tier(amount)` instead of copy-pasting
> the same `if`/`elif` chain everywhere. It's how code stays clean as it grows.
> We'll cover `def`, passing values in (**parameters**), and handing a value back
> (**return**) — then a short capstone that pulls PF1–PF4 together.
>
> Type in every example and run it. Standing rule: stuck >15 min → paste and stop.
>
> — David

---

Keep `DEALS` at the top of your file:

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

## 1. `def` — naming a block of code

`def` defines a function: a name for some code that runs only when you **call** it.

```python
def greet(name):
    print(f"Reviewing {name}")

greet("Acadia Software")
```
```
Reviewing Acadia Software
```

Two separate moments: **defining** it (`def greet(...):` — Python just remembers it, runs
nothing yet) and **calling** it (`greet("Acadia Software")` — now the body runs). The body
is the indented block, same as a loop or an `if`.

> **The classic mistake:** defining a function and never calling it, then wondering why
> nothing happened. Defining ≠ running.

**✅ Quick check:** does `def greet(name):` by itself print anything?  *(answer: no — not
until you call `greet(...)`)*

---

## 2. Parameters — passing values in

The name in the parentheses (`name`, `amount`) is a **parameter** — a placeholder for
whatever value you pass when you call it. The same function works on any value:

```python
def tier(amount):
    if amount >= 100000:
        return "Enterprise"
    elif amount >= 50000:
        return "Mid-Market"
    else:
        return "SMB"
```

Now `tier(156000)`, `tier(50000)`, `tier(47500)` each run that chain with a different
`amount`. Write the rule once, use it everywhere.

**✅ Quick check:** in `def tier(amount):`, what is `amount`?  *(answer: a parameter — the
value you pass in when you call it)*

---

## 3. `return` — handing a value back

`return` sends a value *back to whoever called the function*, so you can use it. This is
different from `print`, which just shows text on screen:

```python
print(tier(156000))   # Enterprise
print(tier(50000))    # Mid-Market
print(tier(47500))    # SMB
```
```
Enterprise
Mid-Market
SMB
```

`tier(156000)` **becomes** the value `"Enterprise"`, which `print` then shows. Because it
*returns* a value (not prints it), you can also store it (`label = tier(156000)`) or drop
it into an f-string.

> **The classic mistake — `print` vs `return`.** A function that `print`s shows you
> something but hands back `None`, so `label = tier(...)` would capture nothing usable.
> When you want to *use* the result, `return` it.

**✅ Quick check:** which keyword lets you write `label = tier(50000)` and get
`"Mid-Market"` into `label` — `print` or `return`?  *(answer: `return`)*

---

## 4. Functions + loops — the payoff

A function inside a loop applies your rule to every deal:

```python
for deal in DEALS:
    print(f"{deal['name']}: {tier(deal['amount'])}")
```
```
Acadia Software: SMB
Blue Harbor Foods: SMB
Cobalt Mining Co: Enterprise
Delta Logistics: SMB
Echo Media Group: SMB
Foothills Energy: Mid-Market
Glacier Insurance: SMB
Harborview Clinics: Mid-Market
Ironwood Labs: Mid-Market
```

One `tier` function, called nine times. That's the whole point — the rule lives in one
place, so a change fixes every use at once.

**✅ Quick check:** how many times is `tier` called by that loop?  *(answer: 9 — once per
deal)*

---

## Exercises

Keep `DEALS` at the top. Print each answer.

**E1 — A formatting function.** Write `def format_deal(deal):` that **returns** the string
`Name: $amount` (commas). Call it on the first deal (`DEALS[0]`) and print the result.

**E2 — Tier function.** Write `def tier(amount):` returning `Enterprise` (≥ $100,000),
`Mid-Market` (≥ $50,000), or `SMB`. Print `tier(156000)`, `tier(50000)`, `tier(47500)`.

**E3 — Tier the whole pipeline.** Loop `DEALS` and print `Name — Tier` for every deal,
using your `tier()` function.

**E4 — A total function.** Write `def total_value(deals):` that loops a list of deals and
**returns** the sum of their amounts. Print `total_value(DEALS)` formatted with `$` and
commas.

**E5 — Capstone report.** Write `def biggest_deal(deals):` that **returns** the largest
deal (the whole dict, best-so-far). Then print a two-line report reusing your functions:
- line 1: `Pipeline: N deals worth $...` (use `len()` and `total_value`)
- line 2: `Largest: Name: $amount (Tier)` (use `biggest_deal`, `format_deal`, `tier`)

## Self-check (exact)

- [ ] **E1:** `Acadia Software: $18,500`
- [ ] **E2:** `Enterprise`, `Mid-Market`, `SMB`
- [ ] **E3:** 9 lines; `Cobalt Mining Co — Enterprise`, `Foothills Energy — Mid-Market`, `Delta Logistics — SMB`
- [ ] **E4:** `$441,500`
- [ ] **E5:** `Pipeline: 9 deals worth $441,500` / `Largest: Cobalt Mining Co: $156,000 (Enterprise)`

## Submission

- Follow `docs/assignment_workflow.md`.
- Branch: `submission/pf4-functions`
- File: `pf4.py`
- PR description: **📋 the full program output** and the self-check ticked line by line.

---

*After PF4 you've got every tool PY01a (Pipeline Drills) uses — that assignment is your
next step, and it'll feel like review.*
