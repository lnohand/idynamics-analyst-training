# Python Assignment 01 — Automate the Actuals Pull
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Stop doing this by hand
>
> You just spent time manually pulling January actuals from the database
> and typing them into Excel. You're going to do this every month.
>
> Write a script that does it for you. Connect to the database, pull
> the numbers, drop them into the workbook. Same numbers you calculated
> in Assignment 06 — just automated.
>
> Use whatever tools help you figure it out. That includes AI.
>
> — David

---

## What You're Building

A Python script that:

1. Connects to the Neon DB (same credentials you use in DBeaver)
2. Queries January 2026 actuals — the MRR waterfall numbers
3. Writes those numbers into the **Actual column** of your
   `Jan 2026 A vs F` tab in the forecast workbook

When the script runs, the Actual column should be populated.
No manual typing.

---

## What to Pull

The same numbers from Assignment 06:

- Opening MRR (active subs as of Dec 31, 2025)
- New MRR (subscriptions starting in January)
- Expansion MRR (events in January)
- Churned MRR (cancellations in January)
- Closing MRR (active subs as of Jan 31, 2026)

You already wrote these queries. Start there.

---

## Libraries You'll Need

- **`psycopg2`** — connects Python to PostgreSQL
- **`openpyxl`** — reads and writes Excel files

You've never used these before. That's fine — this is exactly
the kind of thing AI is good at explaining. Ask it how to:

- Install and import `psycopg2`
- Open a connection using a connection string
- Run a query and read the results
- Open an existing `.xlsx` file with `openpyxl`
- Write a value to a specific cell

Don't ask AI to write the whole script. Ask it to explain
the pieces you don't know, then assemble it yourself. You'll
understand it better and be able to debug it when it breaks.

---

## A Few Things to Figure Out

- Your connection string has credentials in it. Do not hardcode
  it in the script. Look up how to load it from an environment
  variable or a separate config file.
- `openpyxl` opens a workbook and lets you access sheets by name.
  You'll need to know which cells hold the Actual column in your tab.
- Run the script, check the numbers match your Assignment 06 values.
  If they don't, the bug is in your query — not the library.

---

## Deliverable

```
submissions/python/01_actuals_pull.py
```

PR description:

```
## What this does
[One sentence]

## Self-check
Opening MRR written to workbook: $___________
Closing MRR written to workbook: $___________
Matches Assignment 06 values:    ✅ / ❌

## What I used AI for
[Be specific — what did you ask, what did it explain]

## Questions
```

---

*Module 6 — Python Automation*
*Python Assignment 01 — April 2026*
