# Python Assignment 01a: Pipeline Drills
### iDynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Drills before the real build — and your IDE
>
> Watchlist's coming along, so here's one more fundamentals set before we
> start building the board for real. No market data this time — just
> Python: functions, decisions, loops, running totals. These four patterns
> are 90% of what analysts actually write, so I want them automatic.
>
> Also, you asked the right question about the IDE, so this assignment
> STARTS there: Part 0 sets up VS Code and the handful of terminal
> commands you've been missing. Ten minutes, and you'll never be lost in
> a folder tree again.
>
> Standing rules apply: stuck >15 min → paste what you see and stop.
>
> — David

---

## Part 0 — VS Code + finding your way around (do this first)

1. Install **VS Code** (code.visualstudio.com) and, inside it, the **Python extension** (Extensions icon → search "Python" → the Microsoft one).
2. File → **Open Folder** → your `idynamics-analyst-training` clone. The Explorer sidebar is now your folder tree.
3. Read `docs/terminal_vscode_basics.md` (in the repo — one page). It covers the five terminal commands (`pwd`, `dir`, `cd`, `cd ..`, `mkdir`) and their VS Code equivalents.
4. Practice both ways, for real:
   - In the VS Code terminal (View → Terminal): `pwd`, then `mkdir submissions/python/py01a_python_drills`, then `cd` into it, then `dir` (empty — you just made it), then `cd ..\..\..` back to the root.
   - In the Explorer sidebar: right-click the new folder → New File → `drills.py`.
   - Back in the terminal, at the root: `dir submissions/python/py01a_python_drills` — now it shows `drills.py`. That's the loop closed: made in the terminal, created in the editor, verified in the terminal.
   - Activate the venv in the terminal as always (`.venv\Scripts\Activate.ps1`).
5. **📋 Paste in your PR:** the terminal lines from step 4 — the `pwd` output, the `mkdir`, and that final `dir` showing `drills.py` exists.

## The scenario — a sales pipeline

Every SaaS company keeps a **pipeline**: the list of deals sales is working on that haven't closed yet. Each deal has a dollar size, and finance looks at this list constantly, asking the same few questions every week:

- **How big is each deal?** Big deals ("Enterprise") get executive attention and are riskier to count on; small ones ("SMB") close often but move the needle less. Tiering the pipeline is how you talk about it without reading 200 rows.
- **What's the total, and how much sits in the big deals?** Total pipeline vs. quota tells you if the quarter is even possible; concentration in a few large deals tells you how fragile that answer is.
- **What are the extremes?** The biggest deal is the one whose slip wrecks the forecast; the smallest tells you where the noise floor is.
- **If revenue keeps growing at this rate, when do we hit a target?** The classic planning question — compounding forward.

Those four questions ARE the four drills below. The Python patterns you'll use (a function that classifies, a loop with a running total, a best-so-far tracker, a compounding loop) are the same ones you'll use on the market board — and in any analyst job. The pipeline here is fictional and tiny so you can check every answer by hand.

## The data (paste at the top of `drills.py`)

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

A list of dicts — each dict is one deal in the sales pipeline. `for deal in DEALS:` gives you one dict at a time; `deal["amount"]` reads a field (all PY01 moves). One more: `DEALS[0]` is the FIRST dict in the list — handy as a starting value when you need to track a best-so-far.

## Four new tools (read before the drills — type each example in and RUN it; the outputs shown are exactly what you should see)

### 1. `elif` — more than two branches

You know `if`/`else`: one test, two outcomes. But "which tier is this deal?" has THREE outcomes, and that's what `elif` ("else-if") is for — a chain of tests.

How Python executes a chain: **top to bottom, and it STOPS at the first test that's true.** Everything below the winner is skipped — not tested, not run. If nothing wins, `else` catches whatever's left.

Trace it by hand with `amount = 72`: is `72 >= 100`? No → drop to the `elif`. Is `72 >= 50`? Yes → `label = "medium"`, chain over, `else` never looked at.

```python
for amount in [156, 72, 20]:
    if amount >= 100:
        label = "big"
    elif amount >= 50:
        label = "medium"
    else:
        label = "small"
    print(amount, "->", label)
```
```
156 -> big
72 -> medium
20 -> small
```

**The classic mistake is ordering the tests wrong.** Swap the first two tests (`>= 50` first) and run it again — you get `156 -> medium`, because 156 IS `>= 50`, that test wins first, and the `>= 100` line below never gets a chance. Rule of thumb: **test the most demanding condition first.**

### 2. `+=` — running totals

To add up a list, you need a variable that *survives* the loop — created before it, updated inside it, read after it. That's called an **accumulator**, and `total += x` is the update (it's exactly `total = total + x`, just shorter).

```python
total = 0                 # 1) start at zero, BEFORE the loop
for x in [10, 25, 5]:
    total += x            # 2) each pass adds one more value
    print("after adding", x, "total is", total)
print("final:", total)    # 3) after the loop: the answer
```
```
after adding 10 total is 10
after adding 25 total is 35
after adding 5 total is 40
final: 40
```

Watch the middle column grow — that's the accumulator doing its job, one pass at a time. It's the same idea as your PY01 best-so-far tracker, except this one *adds* instead of *replaces*. Counting works the same way: `count += 1` inside an `if`.

**The classic mistake:** putting `total = 0` INSIDE the loop. Then every pass wipes the total back to zero, and you end with just the last value (5, not 40). If your total suspiciously equals the final item — that's what happened.

### 3. `range()` — loops that count

Your loops so far walked a list of things. `range(start, stop)` lets you loop over *numbers* instead — month 1, month 2, month 3… — without building a list by hand.

```python
for month in range(1, 4):
    print("month", month)
```
```
month 1
month 2
month 3
```

Note what it did NOT print: month 4. **The stop number is where it stops — it's never included.** So "six months" is `range(1, 7)` → 1, 2, 3, 4, 5, 6. (Why? So the gap between the numbers is the count: 7 − 1 = 6 months. Every programming language you'll meet does some version of this, and everyone trips on it exactly once.)

**The two classic mistakes:** `range(6)` — with one number it starts at ZERO (0…5), so your "months" are off by one; and `range(1, 6)` when you meant six months — you get five. If your last month is missing, check the stop number.

### 4. `and` — two conditions at once

Sometimes one test isn't enough: "MRR is above target AND it's still the first year." `and` glues two conditions into one — **true only when BOTH sides are true.**

```python
mrr = 52000
month = 3
print(mrr > 50000 and month < 12)   # True  and True  -> True
print(mrr > 50000 and month < 3)    # True  and False -> False
```
```
True
False
```

You'll use it in D4 for a "set it only once" pattern: `if mrr > 50000 and first_above == 0:` — condition one says "we've crossed the line," condition two says "and we haven't recorded it yet." Both must hold, so the variable gets written exactly once and then the `and` protects it forever after.

## The drills

Build all four in `drills.py`, each printing its section in order.

**D1 — Deal tiers.** Write `def tier(amount):` returning `"Enterprise"` for $100,000 and up, `"Mid-Market"` for $50,000 to $99,999, `"SMB"` below. Loop the pipeline and print one line per deal: name (padded to 20), amount (right-aligned, comma, no decimals — `:>9,`), tier. Watch the boundaries: is a $47,500 deal Mid-Market?

**D2 — Pipeline stats.** Three lines, computed with running totals (no shortcuts — build the `+=` muscle). Money formatted like D1 (commas); average with 2 decimals:
- total pipeline value
- count AND combined value of deals $50,000+
- average deal size (total ÷ number of deals — `len(DEALS)` gives the count)

**D3 — Extremes.** Biggest and smallest deal — name and amount, one line each. Two best-so-far trackers (or two passes — your call). Tip: seed each tracker with `DEALS[0]` and let the loop correct it — seeding "smallest" with 0 is a classic bug (nothing is ever smaller than 0).

**D4 — Growth projection.** MRR is $42,000 today and grows 4% per month. Print 6 lines — `Month N: $xx,xxx.xx`, where Month 1 is AFTER the first month of growth ($43,680.00) — then one final line naming the FIRST month MRR crosses $50,000. Use `range()`, a running `mrr *= 1.04`, and an `if` with `and` that sets a variable only while it's still 0 — a cousin of PY01's best-so-far, except once set it must never change.

## Submission

- Branch: `submission/py01a-python-drills`
- File: `drills.py`
- PR description: **📋 the Part 0 terminal paste, 📋 the full program output**, and the self-check.

## Self-check (data is fixed, so these are exact)

- [ ] D1: 9 lines; exactly 1 Enterprise, 3 Mid-Market, 5 SMB — Delta Logistics ($47,500) is SMB and Ironwood Labs (exactly $50,000) is Mid-Market
- [ ] D2: total $441,500; deals $50k+: 4 worth $359,300; average $49,055.56
- [ ] D3: biggest Cobalt Mining Co $156,000; smallest Glacier Insurance $3,100
- [ ] D4: Month 6 shows $53,143.40; first month above $50,000 is month 5
- [ ] One `tier()` function; loops over DEALS — no copy-pasted per-deal blocks
