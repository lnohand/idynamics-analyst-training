# PF4 — Functions & Capstone: Feedback

**Status:** Merged ✅
**Reviewed by:** David Chen

Michael — this one's done. I pulled your branch, ran `pf4.py`, and tested each
function on its own. Merging it now.

## What landed — and this is the important part

The whole point of PF4 was **parameters and `return`**: a function should work on
whatever list you hand it, not on the global `DEALS` it happens to see. Earlier
versions got the right numbers for the wrong reason — they looped `DEALS` no matter
what you passed in. This version doesn't. I proved it by calling your functions on a
tiny two-deal list:

- `total_value([Tiny A $1,000, Tiny B $2,000])` → **$3,000** (not $441,500). It's
  summing the list I handed it, not `DEALS`.
- `biggest_deal(...)` on that same list → **Tiny B / $2,000**, a deal that's actually
  *in* the list. Your seed is `biggest = deals[0]`, not `DEALS[0]`. That's the fix.
- `format_deal(...)` **returns** the string now (it doesn't `print` and hand back
  `None`), which is exactly why you can reuse it inside the E5 report.

That's the concept, and it stuck. Good work — this was the one that kept biting you.

## Cleanup — also done right

You repaired `submissions/python/pf4.py` in place (no more conflict markers, no more
`SyntaxError`) and deleted the stray `drills/pf4.py`. The branch now contains exactly
the four files it should. That's the clean-branch discipline we've been building.

## Two things to carry forward — habits, not blockers

1. **Paste your *actual* output into the PR, then tick the self-check against it.**
   The output in your PR comment was from an older run — it still showed
   `Name: Cobalt Mining Co, Tier: Enterprise`, but the ticks under it claimed the
   corrected `Cobalt Mining Co — Enterprise`. The ticks were describing what the brief
   *wanted*, not what your program *printed*. Every time: run the file, copy what
   actually comes out, then check each line against that. When a line doesn't match,
   that mismatch is the bug pointing at itself.

2. **Small one on E3:** the brief asks for `Name — Tier` with an em-dash (`—`); yours
   prints a hyphen (`-`). Fussy detail, and honestly on us for specifying a character
   that's a pain to type — I'm not holding anything for it. Just flagging so "exact
   self-check" stays exact.

Everything runs, every value is right, and the concept is there. Nice work getting
this one over the line — you're through the fundamentals.

— David
