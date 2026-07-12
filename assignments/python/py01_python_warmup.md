# Python Assignment 01: Watchlist Warm-up
### iDynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Five tickers, one loop
>
> Setup's done, so let's write some actual Python. Before we touch any
> data tables, I want the core moves back in your fingers: a loop, a
> function, a comparison, clean formatted output. It's been a year — this
> is the knock-the-rust-off session, same as your SQL refresher was.
>
> The ask: a little script that prints a watchlist — one clean line per
> ticker with the last price and today's move — and then tells me which
> name is moving the most. That's it. Small on purpose.
>
> Same standing rule as last time: stuck >15 minutes, or an error that
> mentions HTTP / rate limits / connections → paste it in Slack and stop.
> We debug our code, never the data provider.
>
> — David

---

## Worked example — read this first

Here's the pattern for TWO tickers. Type it into a scratch file (e.g. `scratch.py` somewhere OUTSIDE the repo, or delete it before your PR — only the final script gets submitted) and run it, venv activated as always:

```python
import yfinance as yf

def get_quote(symbol):
    """Return (last_price, 1d_change_percent) for one ticker."""
    info = yf.Ticker(symbol).fast_info
    last = info["lastPrice"]
    prev = info["previousClose"]
    return last, (last - prev) / prev * 100

for symbol in ["AAPL", "MSFT"]:
    last, change = get_quote(symbol)
    print(f"{symbol:6} ${last:>10,.2f}   {change:+.2f}%")
```

What each new piece does:

- `def get_quote(symbol):` — a **function**: named, reusable logic. It takes a ticker in and `return`s two values out.
- `for symbol in [...]:` — a **loop**: runs the indented block once per list item.
- `f"..."` — an **f-string**: text with live values injected. The format codes do the styling: `:6` pads to 6 characters, `:>10,.2f` right-aligns with a thousands comma and 2 decimals, `:+.2f` forces a `+` or `-` sign.

One more pattern you'll need — **keeping a "best so far" while looping**. This finds the longest name in a list:

```python
longest = ""
for name in ["Ana", "Michael", "Bo"]:
    if len(name) > len(longest):
        longest = name
print(f"Longest name: {longest}")
```

- `if condition:` — runs its indented block only when the condition is true. Combined with a variable that survives the loop (`longest`), you can track a running winner and use it after the loop ends.

Run both and make sure you see what you expect before moving on.

## Your task

Build `submissions/python/py01_python_warmup/watchlist.py`:

1. **The watchlist.** Extend the pattern to these five: `AAPL`, `MSFT`, `NVDA`, `AZO`, `TSLA`. One line each, same clean format — prices aligned, comma thousands separators, explicit `+`/`-` on the change. One loop over the watchlist; no copy-pasting the block five times (if you find yourself copying, that's what the loop is for).
2. **The biggest mover.** After the list, print one final line naming the ticker with the largest move *in either direction* (largest absolute % change), e.g.:

   ```
   Biggest mover: NVDA (+4.03%)
   ```

   You have all the pieces: the best-so-far pattern from the example, and `abs()`, which turns any number positive (`abs(-3.1)` → `3.1`) so "largest in either direction" becomes a simple comparison.
3. **One experiment.** Change one ticker to a bogus symbol like `XXXXXX`, run it, and observe. **📋 Paste everything it printed in your PR** and answer in one sentence: at which line of YOUR code does it actually fail, and how did you tell? (Then put the real ticker back — the submitted script must run clean.)

## Submission

- Branch: `submission/py01-python-warmup`
- File: `watchlist.py`
- PR description: **📋 paste the full output of one clean run**, the bogus-ticker observation, and the self-check.

## Self-check

- [ ] Exactly 6 printed lines: 5 watchlist lines + 1 "Biggest mover" line
- [ ] Every price has exactly 2 decimals, and AZO's price shows a thousands comma
- [ ] Every % change shows an explicit `+` or `-` sign
- [ ] The biggest-mover line agrees with the largest absolute % in your own 5 lines
- [ ] One loop over the watchlist — no copy-pasted per-ticker blocks
