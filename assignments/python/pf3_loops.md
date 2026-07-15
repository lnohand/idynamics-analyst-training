# Python Fundamentals 3: Loops
### iDynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Doing it to every deal at once
>
> So far you've handled one deal at a time. Real analysis means doing the same
> thing to a *whole list* — total every deal, count the big ones, find the
> largest. That's a **loop**, and it's the single biggest jump in power you'll
> make. We'll do four things: loop a list, loop numbers with `range()`, build
> **running totals**, and track a **best-so-far**. Everything from PF1 and PF2
> comes together here.
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

## 1. `for` — do something to every item

A `for` loop takes your list and hands you **one item at a time**. You write the body
once; Python runs it for each item.

```python
for deal in DEALS:
    print(deal["name"])
```
```
Acadia Software
Blue Harbor Foods
Cobalt Mining Co
Delta Logistics
Echo Media Group
Foothills Energy
Glacier Insurance
Harborview Clinics
Ironwood Labs
```

`deal` is a name *you* pick; on the first pass it's `DEALS[0]`, then `DEALS[1]`, and so on
to the end. Inside the loop, `deal` is one dict — so everything you learned in PF1
(`deal["name"]`, `deal["amount"]`) works. Nine deals in the list → nine lines out.

> **The classic mistake:** forgetting to indent the body, or reaching for `DEALS[i]` with
> a counter. You don't need a counter — `for deal in DEALS` already walks the list.

**✅ Quick check:** how many lines does the loop above print?  *(answer: `9` — one per
deal)*

---

## 2. `range()` — loop over numbers

Sometimes you want to loop a *count* of times — month 1, 2, 3 — not over a list.
`range(start, stop)` gives you the numbers from `start` up to **but not including** `stop`:

```python
for month in range(1, 4):
    print("month", month)
```
```
month 1
month 2
month 3
```

Notice it did NOT print `month 4`. **The stop number is where it stops — never included.**
So "six months" is `range(1, 7)`.

> **The classic mistake:** `range(1, 6)` when you meant six months gives you only five;
> if the last one is missing, check the stop number.

**✅ Quick check:** what numbers does `range(1, 5)` produce?  *(answer: `1, 2, 3, 4`)*

---

## 3. Accumulators — running totals and counts

To add up a list, you need a variable that **survives** the loop: created *before* it,
updated *inside* it, read *after* it. That's an **accumulator**. `total += x` is shorthand
for `total = total + x`.

```python
total = 0                      # before the loop
for deal in DEALS:
    total += deal["amount"]    # each pass adds one more
print(f"Total: ${total:,}")    # after the loop: the answer
```
```
Total: $441,500
```

**Counting** is the same idea with `+= 1`, usually guarded by an `if` (PF2):

```python
count = 0
value = 0
for deal in DEALS:
    if deal["amount"] >= 50000:
        count += 1
        value += deal["amount"]
print(f"{count} deals worth ${value:,}")
```
```
4 deals worth $359,300
```

> **The classic mistake:** putting `total = 0` *inside* the loop — every pass wipes it back
> to zero and you end with just the last value. If your total suspiciously equals the last
> item, that's what happened.

**✅ Quick check:** where must `total = 0` go — before the loop or inside it?  *(answer:
before)*

---

## 4. Best-so-far — finding the biggest

To find the largest deal, keep a "champion" variable, start it on the first deal, and
replace it whenever you meet a bigger one. Track the **whole deal** (the dict), so you keep
its name too:

```python
biggest = DEALS[0]                          # start on a real deal
for deal in DEALS:
    if deal["amount"] > biggest["amount"]:  # found a bigger one?
        biggest = deal                      # it's the new champion
print(f"{biggest['name']} ${biggest['amount']:,}")
```
```
Cobalt Mining Co $156,000
```

Seeding with `DEALS[0]` (a real deal) is the trick. For a *smallest*, flip the `>` to `<`
— but never seed "smallest" with `0`, because nothing is ever smaller than 0 and it stays
stuck at 0.

> **The classic mistake:** seeding `biggest = 0` works for amounts but throws away the
> name. Seed with the whole first deal and you carry the name for free.

**✅ Quick check:** to find the *smallest* instead, which comparison do you use?
*(answer: `<`)*

---

## Exercises

Keep `DEALS` at the top. Print each answer.

**E1 — List every deal.** Loop the pipeline and print one line per deal, formatted
`Name: $amount` (commas). Nine lines.

**E2 — Total pipeline.** Use a running total to add every deal's amount. Print
`Total pipeline: $...`.

**E3 — Count and value of big deals.** In one loop, count the deals `>= $50,000` and add up
their combined value. Print `N deals worth $...`.

**E4 — Biggest deal.** Use a best-so-far tracker (track the whole deal) to find the largest.
Print `Biggest: Name $amount`.

**E5 — Growth projection.** MRR is $42,000 today and grows 4% per month (`mrr *= 1.04`).
Using `range(1, 7)`, print six lines `Month N: $xx,xxx.xx` (Month 1 is *after* the first
month's growth). Then print one final line naming the **first** month MRR crosses $50,000
— set that month once and don't let it change (`if mrr >= 50000 and first_above == 0:`).

## Self-check (exact)

- [ ] **E1:** 9 lines, first `Acadia Software: $18,500`, last `Ironwood Labs: $50,000`
- [ ] **E2:** `Total pipeline: $441,500`
- [ ] **E3:** `4 deals worth $359,300`
- [ ] **E4:** `Biggest: Cobalt Mining Co $156,000`
- [ ] **E5:** `Month 6: $53,143.40` on the sixth line; final line `First month above $50,000: month 5`

## Submission

- Follow `docs/assignment_workflow.md`.
- Branch: `submission/pf3-loops`
- File: `pf3.py`
- PR description: **📋 the full program output** and the self-check ticked line by line.
