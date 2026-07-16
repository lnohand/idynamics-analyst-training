# Python 02-b: Style It for the Browser — the HTML Panel
### iDynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** First board panel — make it a web page
>
> In 02-a you printed the indices table to the console. Now we turn that
> same table into a small **web page** you can open in a browser — numbers
> formatted, gains green, losses red. From here on, every assignment ends
> with something you can actually SEE.
>
> The styling uses one tool you haven't learned yet, so I'm giving you the
> code for it. You'll understand every line by a later assignment — today
> you'll use it, and I'll walk you through what each piece does so it isn't
> a black box.
>
> Same branch as 02-a, next commit.
>
> — David

---

## What we're adding

Your 02-a script ends with a sorted DataFrame `df` and a console print. We're adding one thing: writing that `df` out as a styled **HTML file** — the actual panel. Same data, now colored and formatted for a screen.

## Given code: turning a DataFrame into a styled web page

pandas has a **Styler** — a tool that takes a DataFrame and produces formatted HTML. You'll learn to write Stylers yourself later; for now, paste this in and I'll explain what each line does:

```python
def color_sign(v):
    return "color: green" if v >= 0 else "color: red"

styled = (df.style
          .map(color_sign, subset=["1D Change", "1D %"])
          .format({"Last": "{:,.2f}", "1D Change": "{:+,.2f}", "1D %": "{:+.2f}%"})
          .hide(axis="index"))

with open("submissions/python/py02_asset_classes/asset_classes.html", "w") as f:
    f.write(styled.to_html())
```

Reading it line by line:

- **`color_sign(v)`** — a small function that takes one number and returns a CSS instruction: green text if it's zero or positive, red if negative. (CSS is the language web pages use for styling; `"color: green"` is just "make this text green.")
- **`df.style`** — starts a Styler from your DataFrame.
- **`.map(color_sign, subset=["1D Change", "1D %"])`** — runs `color_sign` on every cell in *just those two columns*, coloring each by its own sign. (`subset` = which columns to touch.)
- **`.format({...})`** — applies number formatting per column, using the same f-string codes you already know: `"{:,.2f}"` = commas + 2 decimals (the `Last` column), `"{:+,.2f}"` = a forced +/− sign (the point change), `"{:+.2f}%"` = signed percent with a `%`.
- **`.hide(axis="index")`** — hides pandas' row-number column, same idea as `index=False` when you printed to the console.
- **`with open(...) as f: f.write(styled.to_html())`** — `styled.to_html()` turns the styled table into a chunk of HTML text, and this writes that text into a file. (`with open(path, "w")` opens a file for **w**riting and closes it for you when the block ends — the standard way to write a file in Python.)

> **The classic mistake — given code still has a contract.** The `subset=["1D Change", "1D %"]` names your columns *exactly*. If your DataFrame's columns are spelled differently — `"1D Chg"`, or a stray space — `.map` finds nothing and your colors silently don't appear. If the page opens with no green/red, check that your column names match these strings letter for letter.

## Your task

1. Extend `submissions/python/py02_asset_classes/asset_classes.py` (your 02-a script): after you build and sort `df`, add the styling block above so it also writes `asset_classes.html`. Keep the console `print` too.
2. Run it from the repo root:
   ```powershell
   python submissions/python/py02_asset_classes/asset_classes.py
   ```
3. Open `submissions/python/py02_asset_classes/asset_classes.html` in your browser (double-click it, or right-click → Open in browser). That's panel one of your board.
4. Commit **both** files — the script and the generated `asset_classes.html`.

## Self-check (open the HTML in the browser and look)

- [ ] The page shows your 5 indices as a table, sorted the same as the console (best `1D %` on top).
- [ ] **Positive** `1D Change` / `1D %` values are **green**; **negative** ones are **red**.
- [ ] `Last` shows thousands commas where they apply — four of the five indices (the VIX, around 15, won't have one).
- [ ] The two change columns show an explicit **+** or **−** sign; `1D %` ends in `%`.
- [ ] There is **no row-number column** on the left.

## Submission

- Same branch as 02-a: `submission/py02-asset-classes`.
- Files now: `asset_classes.py` + `asset_classes.html` (both committed).
- Commit this part on its own, e.g. `PY02-b: styled HTML panel`.
