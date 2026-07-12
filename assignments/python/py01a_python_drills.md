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

## Four new tools (read before the drills)

**1. `elif` — more than two branches.** You know `if`/`else`; `elif` chains them:

```python
if amount >= 100:
    label = "big"
elif amount >= 50:
    label = "medium"      # only checked if the first test failed
else:
    label = "small"
```

Order matters — the first true branch wins and the rest are skipped.

**2. `+=` — running totals.** `total = total + x` has a shorthand: `total += x`. Start the variable at `0` BEFORE the loop, add inside the loop, use it after.

**3. `range()` — loops that count.** `for month in range(1, 7):` runs the block with `month` = 1, 2, 3, 4, 5, 6 (the end number is NOT included).

**4. `and` — two conditions at once.** `if mrr > 50000 and month < 12:` runs only when BOTH are true.

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
