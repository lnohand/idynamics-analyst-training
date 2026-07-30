# DataFrame Drill 1 — Portfolio Table: Feedback

**Status:** Redo on the same branch — Section B stays held until this clears
**Reviewed by:** David Chen — I ran `dataframe_drill1_portfolio.py` exactly as you submitted it,
then re-ran the one line you'd commented out.

Michael — your read in the PR ("more work is needed for mastery") is honest and it's the right
read. Good news: the pandas isn't the problem. Four of the seven answers are correct, and the two
wordy ones you *did* answer are the two most people get wrong. What's missing is one rep and one
habit. Both are quick.

## What landed — keep it

- **Q1** — "each dict is a row, the keys become the column names." That's the definition, in your
  own words. Exactly right.
- **Q2** — `print(df["Shares"])`. Correct, and note what came back: the column *with* its index and
  a `dtype` line. That's a Series — one column of the table.
- **Q4** — the Energy filter. Correct.
- **Q5** — "NaN indicates that we do not have the price on record, it does not mean the stock has a
  price of $0." That's the whole idea, said cleanly. Missing ≠ zero.
- **Q7's code fix is the right one.** You wrote `pd.DataFrame([row])` — you wrapped the dict in a
  list. The error message pushes you toward `index=[0]` and you didn't take the bait. That's the
  better fix and it's the one I wanted.
- **The file runs clean**, top to bottom, no crash. After the checkpoint, that's worth saying.

## Four things to fix

**1. Q3 — your answer is correct, and it never ran.** Line 25 is commented out:

```python
# print(df.sort_values("Shares", ascending=False).to_string(index=False))
```

I deleted the `#` and ran it: it prints the self-check output *character for character*. So you knew
the answer. But as submitted, that line produces nothing — which means when you compared against the
self-check, there was nothing on your screen to compare. This is the third assignment in a row where
a correct answer was sitting behind a `#`. A commented line is not a submitted answer. Uncomment it.

**2. Q6 — the table is right, but the loop is missing. This is the one that matters.**

You wrote:

```python
HOLDINGS = [{"Ticker": "AAPL", "Shares": 50},
            {"Ticker": "MSFT", "Shares": 30},
]
print(pd.DataFrame(HOLDINGS).to_string(index=False))
```

Your printout matches the self-check, so I understand why this felt done. But look at what the
question asked: *"Starting from `HOLDINGS = {"AAPL": 50, "MSFT": 30}`, **write the loop** that builds
a DataFrame."* `HOLDINGS` is a **dict** — `{"AAPL": 50}` — and the work is turning it into rows. You
changed it into a list of finished rows and handed that straight to pandas. The table came out right
because you built it by hand; the step the question was asking for never happened.

**Use Example 5 as your reference — "Build the rows with a loop," the section right above Example 6
in the brief.** It's the same variable name, the same two columns, four tickers instead of two:

> ```python
> rows = []                                             # start with an empty list
> for ticker, shares in HOLDINGS.items():               # key, value each pass
>     rows.append({"Ticker": ticker, "Shares": shares}) # append ONE row-dict per lap
> df = pd.DataFrame(rows)                                # hand the finished list to pandas
> ```
>
> Three steps to burn in: **empty list → append a row-dict each pass → hand the finished list to
> `pd.DataFrame`.**

That's the move — and it's the same move as checkpoint **B3**, which is why Section B is waiting on
this. Redo Q6 with `HOLDINGS` as a dict, exactly as the question writes it, and **paste both the loop
you wrote and what it printed** into the PR. I need to see the loop, not just the table.

**3. Q7 — the code is there, the answer isn't.** The question asks three things in words: what the
error is, why it happens, and which of the two fixes is better. You submitted code and no
explanation. You clearly know it — you picked the right fix — so write it out: name the error, say in
one line why pandas can't proceed, and say why wrapping in a list beats `index=[0]`. The reasoning is
the part I'm grading.

**4. Line 40 — `df = print(...)`.** You wrote:

```python
df = print(pd.DataFrame([row]).to_string(index=False))
```

That runs, but `df` is now `None`. I checked. `print` **displays** a value; it doesn't **hand one
back**. So you've just overwritten the DataFrame you built on line 16 with nothing. Two separate
jobs, two separate lines:

```python
df = pd.DataFrame([row])          # build it, keep it
print(df.to_string(index=False))  # show it
```

I want to sit on this one longer than a one-liner deserves, because I also picked up your checkpoint
push tonight — and in it you changed `total_value` from `return total` back to `print(total)`, and
took the `return` out of `biggest_deal` too. Those two had *landed*. So this isn't a typo on line 40;
`print` and `return` aren't yet two different things in your head. Here's the whole distinction:

- **`print`** puts characters on your screen. It hands back nothing (`None`). It's for *you*, the
  human reading the terminal.
- **`return`** hands a value back to the code that called it, so you can keep it, format it, or feed
  it into the next step. It's for the *program*.

A function that prints has already spent its answer — you can't reuse it. A function that returns
gives you the answer to do whatever you want with, including printing it. That's why `return` is the
one I keep asking for. Read that back and tell me if it clicks; if it doesn't, say so and we'll do it
live instead of over more written rounds.

## The pre-submit checklist — from now on, every PR

Three of the four items above aren't pandas problems; they're submit-time problems. So let's make
this mechanical. **Copy this into your PR description and tick it before you ask me to look:**

```markdown
### Pre-submit check
- [ ] Ran the file as submitted and read every line of output — nothing commented out
- [ ] Each answer uses the method the question named (a loop, a `return`, a DataFrame) — not just
      the right output
- [ ] Every "explain it" question has a written answer, not just code
- [ ] Real output pasted in this PR, self-checks ticked against it, no stray files or unused imports
```

The second box is the new one, and it's the one that would have caught Q6. Matching output is not
proof you did the exercise — you can hand-build a table that looks identical to a looped one. Ask
yourself what the question told you to *do*, then check your code does that.

## Next steps

1. Fix all four items above and push to **this same branch** (`student/dataframe_drill`) — the PR
   updates itself.
2. Fill in the PR description with the checklist above, plus your Q3 output, your Q6 loop **and** its
   output, and your written Q7 answer.
3. Do the checkpoint fixes **in this same PR** too — see the section below. That's a change from what
   I said earlier; read it before you touch anything.
4. Once Q6 shows a real loop, Section B unlocks and you redo it.

---

## Your branch — and where your "lost" checkpoint work actually is

**Start with the good part: your checkpoint work is not gone.** You told me you'd made all the
checkpoint changes, found them missing when you went to commit, and retyped them from memory. You
don't have to. The version where A3 and A4 were already correct is sitting safe in **this PR** — I'm
looking at it right now. Nothing to recover, nothing to retype.

Here's why, and it's the same branch habit we need to fix.

### What happened

When you start an assignment, the workflow doc has you do this first:

```
git checkout main
git pull origin main
git checkout -b student/new-assignment-name
```

You've been doing a new *name* every time — good, that part stuck. But the first two lines got
skipped, so each new branch was cut from **wherever you were standing**, which was your last
assignment's branch. Every branch since PF1 on July 15 is one long chain:

```
PF1 → PF2/3 → PF4 → checkpoint1 → dataframe_drill
```

`student/dataframe_drill` was cut from `student/checkpoint1`, not from `main`.

**Before you type `git checkout -b`, run `git branch --show-current`. It must say `main`.** If it says
your last assignment's branch, you're about to stack on top of it. That one check is the whole fix.

### The consequences — three of them

**1. Your PR shows files you never touched.** PR #25 is a one-file drill, but GitHub lists **seven**
changed files: the drill plus `checkpoint1.py`, `checkpoint1.sql`, and all four `pf` files. They ride
along because they're commits on your branch that never reached `main` on their own. Harmless, but it
means neither of us can see at a glance what you actually changed — and *you* can't use "Files
changed" as a check on your own work.

**2. Your two PRs disagree about the same file.** This is the one that bit you. `checkpoint1.py` now
exists in two different states: the good version in **this PR**, and the retyped-from-memory version
in **PR #24**. Same filename, two histories, because you pushed the retyped one to the checkpoint
branch and this branch never received it.

**3. It did *not* cause the lost work.** I want to be clear so you're not chasing the wrong thing:
switching branches never silently deletes edits. `git checkout -b` carries them with you, and
`git checkout <branch>` either carries them or stops with an error. Something else wiped that file —
most likely the **Discard Changes** button (the ↩ icon) in VS Code's Source Control panel, which sits
right next to the **+** stage icon and reverts the file with one confirmation click. Look before you
click that one; it's the only button in VS Code that can undo an hour of work.

And the habit that makes it a non-event: **commit early and often, even half-finished.** A commit is a
save point. `git commit -m "WIP: A2 and A3"` costs you nothing, can be amended, and means no button
in any editor can take that work away. Uncommitted work is the only work you can lose.

### What to do — the checkpoint fixes go in this PR

Just this once we're going to use one PR for both, because this branch holds the good copy and I'd
rather fix your file than re-litigate your history. **From the next assignment, back to one branch per
assignment, cut from `main`.**

Step 1 — get on this branch and pull main into it (this also collapses that seven-file list down to
three, and brings you this feedback file):

```
git checkout student/dataframe_drill
git pull origin main
```

Step 2 — open `submissions/python/checkpoint1.py`. **Check the top of A3: it should already say
`return total`, and A4 should say `return biggest`.** If it does, that's your real work, intact. Leave
those two alone — don't paste in what you retyped last night; the retyped version changed both back to
`print`, which is a step backwards.

Step 3 — make only the three fixes that are still genuinely open, all in Section A:

- **A2** — give it its own block that loops `DEALS` and counts amounts `>= 50000`. The answer is **4**.
  Right now it's tangled into your A1 loop and counting the four tier-test numbers, so it prints `3`.
- **`import yfinance`** — delete line 2. Nothing in the file uses it.
- **A1 detail** — `Enterprise` should be `>= 100000`, not `> 100000`. And drop `61000` from the tier
  loop; that amount is only there for the one `and` band check.

Step 4 — **leave Section B alone.** It's still held until the drill clears. Anything you did to B last
night we'll redo properly afterwards.

Step 5 — commit and push:

```
git add submissions/python/checkpoint1.py submissions/python/dataframe_drill1_portfolio.py
git commit -m "Fix: drill Q3/Q6/Q7 and checkpoint A1/A2, drop yfinance"
git push origin student/dataframe_drill
```

I'll close PR #24 — everything moves here.

You're closer than you think on the drill. The concepts are in — build the table with the loop once,
by yourself, and that's the gap closed. And you lost less than you thought last night.

— David
