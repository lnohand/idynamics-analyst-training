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

## Where this fits

PY02 is **one script, built in three parts**, on one branch with one PR:

| Part | What you do | File |
|---|---|---|
| 02-a | build the table, print it to the console | `asset_classes.py` |
| **02-b (you are here)** | **style that same file's `df` into a web page** | **same `asset_classes.py`** |
| 02-c | a preview of what's coming + start your own repo | `sp500_preview.py` |

You are **editing the file you already wrote in 02-a** — not starting a new one.

## Before you start

If you skipped the `jinja2` install back in 02-a, do it now — this is the part that needs it:

```powershell
pip install -r assignments/python/requirements.txt
```

The Styler below builds its HTML with `jinja2`. Without it you'll get `ImportError: Missing optional dependency 'jinja2'`, which means "run the line above," not "your code is wrong."

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

### One thing about that file path — read this before you run it

The path `"submissions/python/py02_asset_classes/asset_classes.html"` is **relative to the folder you run the command from — not the folder the script lives in.** This trips up everyone once, so let's make it concrete.

Your script sits *inside* `py02_asset_classes/`, but the path is written to work when you run it **from the repo root** — the same place you run every command in this course (rule zero in `docs/assignment_workflow.md`: you're always standing in the repo root). From there, `submissions/python/py02_asset_classes/asset_classes.html` points exactly where it should:

```powershell
# standing in the repo root — CORRECT
python submissions/python/py02_asset_classes/asset_classes.py
```

If instead you `cd` into `py02_asset_classes/` first and run `python asset_classes.py`, Python looks for a *`submissions/` folder inside `py02_asset_classes/`*, doesn't find one, and stops with:

```
FileNotFoundError: [Errno 2] No such file or directory:
  'submissions/python/py02_asset_classes/asset_classes.html'
```

**The fix is to move yourself, not to edit the path.** `cd` back to the repo root and run it again. Do **not** rewrite the path to patch around where you happen to be standing — the path in the given code is correct, and the graded file has to keep it. (This is the same rule for the `sp500_preview.py` path in 02-c.)

**In VS Code, the usual cause is opening the wrong folder.** Open **`idynamics-analyst-training` itself** (File → Open Folder → pick the repo folder), *not* the folder that contains it. VS Code's terminal starts wherever the open folder is — if you opened one level too high, `pwd` shows the parent and every write path is off by the repo name. Check with `pwd` (PowerShell): it should end in `\idynamics-analyst-training`. If you find yourself typing `idynamics-analyst-training\` into a path to make it work, that's the tell — you're a folder too high; reopen the repo folder instead.

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
