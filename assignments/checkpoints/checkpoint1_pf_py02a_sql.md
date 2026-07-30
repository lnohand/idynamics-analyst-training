# Checkpoint Quiz 1 — Python Fundamentals, First DataFrame, and SQL
### iDynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** A checkpoint before we build the next panel
>
> You've covered a lot — Python values, decisions, loops, functions, your first
> pandas table, and a run of SQL. Before PY03 builds on top of the DataFrame,
> I want a quick checkpoint that it all actually stuck. Nothing new here: every
> question is something you've already done. **Solve each one** — write the code
> or the query that produces the answer, run it, and confirm it works.
>
> Some questions have a 💡 hint. Most don't — those are the ones I expect to be
> automatic by now. There are no answer values printed in this quiz on purpose;
> the point is for you to produce them.
>
> Same standing rules: no AI autocomplete (turn off inline suggestions), and if
> you're stuck more than 15 minutes on one question, paste what you have and stop
> — tell me where it jammed. I'd rather see where the gap is than have you grind.
>
> — David

---

## How to submit

- Work from the repo root, venv active (`docs/assignment_workflow.md` if you need the refresher).
- Two files:
  - `submissions/checkpoints/checkpoint1.py` — your answers to **Section A** and **Section B**, each clearly labelled with a comment (`# A1`, `# A2`, …). Run it; it should print each answer.
  - `submissions/checkpoints/checkpoint1.sql` — your answers to **Section C**, each labelled (`-- C1`, `-- C2`, …).
- Branch: `submission/checkpoint1`
- **PR description:** 📋 paste your full program output, and paste the result (or row count) of each query. That's how I check it — there are no self-check values in the quiz itself.

---

## Section A — Python Fundamentals

Put this list at the top of `checkpoint1.py` and use it for A1–A4:

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

**A1.** Using an `if` / `elif` / `else` chain, print the tier of an amount — `Enterprise`
(≥ $100,000), `Mid-Market` (≥ $50,000), or `SMB` (below that). Print the tier for **156000**,
then **50000**, then **47500**. Then, using `and`, print `True` or `False` for whether **61000**
falls in the Mid-Market band (at least $50,000 **and** below $100,000).

**A2.** Loop over `DEALS` and print how many deals have an amount of **$50,000 or more**.

**A3.** 💡 Write a function `total_value(deals)` that returns the sum of the amounts in the list
it's handed. Print `total_value(DEALS)` formatted with a `$` and commas. Then make a small
two-deal list `SMALL = [{"name": "Tiny A", "amount": 1000}, {"name": "Tiny B", "amount": 2000}]`
and print `total_value(SMALL)` the same way.
> 💡 Your function has to work on **any** list I pass it — test it on `SMALL`, not just `DEALS`.

**A4.** 💡 Write a function `biggest_deal(deals)` that **returns** the largest deal — the whole
dict, found best-so-far — from whatever list it's given. Then use it to print one line:
`Largest: Cobalt Mining Co: $156,000` (name and amount from the deal it returns).
> 💡 Return the deal, don't print it inside the function — you need the value *back* so you can
> reuse it to build the line.

---

## Section B — Your First DataFrame (pandas)

Start `checkpoint1.py`'s Section B with `import pandas as pd`. Use this list for B1 and B2:

```python
rows = [
    {"Index": "S&P 500",    "Last": 6800.00,  "1D %": 0.42},
    {"Index": "NASDAQ 100", "Last": 25000.00, "1D %": -0.15},
    {"Index": "Dow Jones",  "Last": 44000.00, "1D %": 0.08},
]
```

**B1.** Build a DataFrame from `rows` and print it as a table **with no row-number column** on the
left.

**B2.** Print the same table **sorted by `1D %`, best (highest) first**.

**B3.** 💡 Starting from this dictionary:
```python
INDICES = {"S&P 500": 6800.00, "NASDAQ 100": 25000.00, "Dow Jones": 44000.00}
```
loop over it with `.items()`, build a list of row-dicts with the columns `Index` and `Last`,
turn that into a DataFrame, and print it with no row-number column.
> 💡 Each index is **one row** — build up the *list of row-dicts* first, then hand the finished
> list to `pd.DataFrame`. (The classic slip is building one dict instead of a list of dicts.)

---

## Section C — SQL (the iDynamics database)

The tables you need (same DB you've been using):

- **`customers`** — `customer_id`, `company_name`, `region`, … (region lives **here**)
- **`subscriptions`** — `subscription_id`, `customer_id`, `plan_name`, `seats`,
  `price_per_seat`, `discount_percent`, `billing_cycle` (`Monthly` / `Annual`), `status`
  (`active` / `cancelled`)

**C1.** List the `company_name` of every customer in **Eastern Canada**.

**C2.** Count how many **active** subscriptions each region has. Show the region and the count.
(Region is on `customers`, so you'll need to bring the two tables together.)

**C3.** For **active, Monthly-billed** subscriptions, show the total monthly MRR per plan.
A subscription's monthly MRR is `seats * price_per_seat * (1 - discount_percent / 100.0)`.
Show `plan_name` and the summed MRR, highest first.

**C4.** 💡 Show only the plans that have **more than 9 active subscriptions** — `plan_name` and
the count.
> 💡 A filter on a `COUNT` can't live in `WHERE`.

**C5.** 💡 List the `company_name` of every customer that has **no active subscription**.
> 💡 Every customer should be considered — even ones with nothing active. Which join keeps them,
> and how do you spot the rows that found no match?

---

*When it's in, I'll go through it and send feedback. If a couple of these fight you, that's
useful signal — say so in the PR and we'll close the gap before PY03.*
