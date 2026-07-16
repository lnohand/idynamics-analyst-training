# PF1 — Values & Collections — Feedback (PR #20)

**Verdict:** Changes requested. The Python is correct — the submission itself isn't runnable yet.

## What's right
All five exercises produce the correct values (verified by running your logic):
- **E1** `Foothills Energy: $92,300`
- **E2** first `18,500`, last `47,500`
- **E3** `Cobalt Mining Co: $156,000`
- **E4** combined `$248,300`
- **E5** `9`, `Ironwood Labs`

Nice touches: reaching into `DEALS[5]` instead of hardcoding, and `DEALS[-1]` for the last deal.

## What needs to change (blocking)
1. **It's all commented out.** Every exercise (E1–E5) is behind a `#`, so running `pf1.py` prints *nothing*. Commented code doesn't execute — delete the `#`s so the file actually runs its five lines. (Habit for next time: run your own file before pushing; no output = the tell.)
2. **PR description is empty.** Every submission needs the full program output pasted in **and** the self-check ticked line by line — that's how it gets reviewed without guessing.

## Small placement fixes (going forward — don't redo this one)
- File belongs in your `submissions/python/...` folder, not `drills/`.
- Branch should match the brief: `submission/pf1-values-collections` (not `student/pf1_values_collection`).
- Both are in `docs/assignment_workflow.md`.

## Cosmetic (optional)
- E2/E4: the self-check wanted plain values. `:,.2f` on E4 gives `$248,300.00`; whole-dollar `:,` is enough here. Not wrong, just tighter.

**Next:** uncomment, push (the PR updates itself), fill in the description. Then it's a merge.
