# Python Fundamentals 2: Decisions
### iDynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Making code choose
>
> PF1 was about storing values. Now we make code *react* to them — "if the deal
> is big, call it Enterprise; otherwise SMB." That's a **decision**, and it's how
> every rule an analyst writes gets encoded. One new idea at a time again:
> comparisons, then `if`/`elif`/`else`, then combining conditions with
> `and`/`or`. Still no loops — one deal at a time.
>
> Type in every example and run it. Standing rule: stuck >15 min → paste and stop.
>
> — David

---

Keep the `DEALS` block from PF1 at the top of your file — we'll classify individual deals
from it.

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

## 1. Comparisons — questions that answer True or False

A **comparison** asks a yes/no question about values. The answer is always a `bool`
(`True` or `False`) — the type you met in PF1.

| Operator | Asks | `18500 ? 50000` |
|----------|------|------|
| `>` | greater than | `False` |
| `>=` | greater than or equal | `False` |
| `<` | less than | `True` |
| `==` | **equal** (two equals signs!) | `False` |
| `!=` | not equal | `True` |

```python
print(18500 > 50000)      # False
print(156000 >= 100000)   # True
print(47500 == 47500)     # True
print(47500 != 50000)     # True
```
```
False
True
True
True
```

> **The classic mistake:** `=` vs `==`. One equals *assigns* a value (`amount = 47500`);
> two equals *compares* (`amount == 47500`). Using `=` where you meant `==` is an error —
> when you're asking a question, always `==`.

**✅ Quick check:** what does `print(50000 >= 50000)` give?  *(answer: `True` — the "or
equal" part counts)*

---

## 2. `if` / `else` — one test, two paths

`if` runs a block **only when** its comparison is `True`. `else` catches everything else.
Watch the colon and the indentation — the indented lines are what runs:

```python
amount = 92300

if amount >= 50000:
    print("Big deal")
else:
    print("Small deal")
```
```
Big deal
```

Change `amount` to `18500` and rerun — now the `else` block wins and it prints
`Small deal`. Exactly one of the two branches ever runs.

> **The classic mistake:** forgetting the colon `:` at the end of the `if` line, or not
> indenting the line under it. Python uses the indentation to know what belongs to the
> `if` — it's not decoration.

**✅ Quick check:** with `amount = 50000`, does the code above print `Big deal` or
`Small deal`?  *(answer: `Big deal` — 50000 `>= 50000` is True)*

---

## 3. `elif` — more than two outcomes

"Which tier?" has THREE answers, and that's what `elif` ("else-if") is for — a chain of
tests. Python reads it **top to bottom and stops at the first one that's True**;
everything below the winner is skipped. If none match, `else` catches the rest.

```python
amount = 47500

if amount >= 100000:
    print("Enterprise")
elif amount >= 50000:
    print("Mid-Market")
else:
    print("SMB")
```
```
SMB
```

Trace it: is `47500 >= 100000`? No → try the `elif`. Is `47500 >= 50000`? No → fall to
`else` → `SMB`. (A $47,500 deal is SMB, not Mid-Market — the boundary catches people.)

> **The classic mistake — wrong order.** Put `>= 50000` *first* and a $156,000 deal
> prints `Mid-Market`, because 156000 is `>= 50000`, that test wins, and the `>= 100000`
> line below never gets a chance. **Rule: test the most demanding condition first.**

**✅ Quick check:** in the chain above, what tier does `50000` get?  *(answer:
`Mid-Market` — fails `>= 100000`, passes `>= 50000`)*

---

## 4. `and` / `or` — combining conditions

Sometimes one test isn't enough.

- `and` is True **only when BOTH** sides are True.
- `or` is True when **EITHER** side is True.

```python
amount = 61000

print(amount >= 50000 and amount < 100000)   # True  and True  -> True   (it's Mid-Market)
print(amount >= 100000 or amount < 5000)      # False or  False -> False  (not a whale, not tiny)
```
```
True
False
```

`and` is how you say "between": `amount >= 50000 and amount < 100000` is the whole
Mid-Market band in one line.

> **The classic mistake:** you can't shorten `amount >= 50000 and amount < 100000` to
> `50000 <= amount < 100000` in your head and drop the second `amount` — each side of
> `and` must be a *complete* comparison with its own value on both ends.

**✅ Quick check:** `True and False` is ___, and `True or False` is ___.  *(answers:
`False`, `True`)*

---

## Exercises

Keep `DEALS` at the top. Each exercise looks at ONE deal by its index (no loops yet).
Print each answer.

**E1 — A plain comparison.** Print whether the third deal's amount (`DEALS[2]["amount"]`)
is `>= 100000`.

**E2 — if/else.** Look at the sixth deal (`DEALS[5]`). Print `Big` if its amount is
`>= 50000`, otherwise `Small`.

**E3 — Tier one deal.** Using an `if`/`elif`/`else` chain, print the tier
(`Enterprise` / `Mid-Market` / `SMB`) of the **fourth** deal (`DEALS[3]`). Mind the
boundary.

**E4 — Between (and).** For the eighth deal (`DEALS[7]`), print `Mid-Market` if its amount
is `>= 50000 and < 100000`, otherwise `not Mid-Market`.

**E5 — Either (or).** For the seventh deal (`DEALS[6]`), print `Notable` if its amount is
`>= 100000` **or** `< 5000` (a whale or a tiny deal), otherwise `Ordinary`.

## Self-check (exact)

- [ ] **E1:** `True`
- [ ] **E2:** `Big`
- [ ] **E3:** `SMB`  *(Delta Logistics is $47,500 — under 50k)*
- [ ] **E4:** `Mid-Market`  *(Harborview is $61,000)*
- [ ] **E5:** `Notable`  *(Glacier is $3,100 — under 5k)*

## Submission

- Follow `docs/assignment_workflow.md`.
- Branch: `submission/pf2-decisions`
- File: `pf2.py`
- PR description: **📋 the full program output** and the self-check ticked line by line.
