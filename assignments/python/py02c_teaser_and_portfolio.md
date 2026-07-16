# Python 02-c: A Peek Ahead + Your Portfolio Repo
### iDynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** First board panel — a preview, and making this yours
>
> Two short things to finish PY02. First, a taste of where the board is
> going — a real interactive chart, from code I'll hand you (you'll build
> it yourself in a couple of assignments). Second, and more important:
> we start publishing this work as YOUR portfolio, on your own GitHub. The
> market board is public data and generic Python — nothing iDynamics-
> confidential — so it's perfect to show off.
>
> Last commit on the PY02 branch.
>
> — David

---

## Part 1 — a peek ahead (given code, just run it)

You won't understand every line here yet — by assignment PY04 you will. Save it as `submissions/python/py02_asset_classes/sp500_preview.py`, run it from the repo root, and open the result:

```python
import yfinance as yf
import plotly.graph_objects as go

close = yf.Ticker("^GSPC").history(period="1y")["Close"]
fig = go.Figure(go.Scatter(x=close.index, y=close.values, mode="lines", name="S&P 500"))
fig.update_layout(title="S&P 500 — 1 year")
fig.write_html("submissions/python/py02_asset_classes/sp500_preview.html", include_plotlyjs="cdn")
```

That's a year of the S&P 500, interactive — open `sp500_preview.html` and hover it, zoom it, drag across it. This is the board's center panel, and in two assignments you'll build it yourself, line by line. For now it's here to show you what's coming.

**📋 Put a screenshot of the chart in your PR**, and commit both preview files (`sp500_preview.py` and `sp500_preview.html` — the HTML is small).

## Part 2 — start your own portfolio repo (do this once, then feed it every assignment)

This project runs on public market data and generic Python — none of it is iDynamics-confidential. That makes it ideal **portfolio material**, and I want you to treat it that way from the start. Two worlds, kept separate: the *work process* (briefs, feedback, grades) stays here in the training repo; the *finished product* lives in a repo of your own.

Do this once:

1. **Create a public repo on your personal GitHub.** Name it like a product, not homework — `market-dashboard` is a good choice; your call. If you haven't made one before: github.com → **New repository** → set it **Public** → check **"Add a README"** → **Create**. Then `git clone` it to a folder **outside** the training repo (so the two never mix).
2. **Write a short README in your own words** — 2–4 sentences: what it is, what it's built with (Python, pandas), and where it's headed (a live market board). Written like it's yours, because it is.
3. **After this PR is merged here**, copy your finished `asset_classes.py` into that repo and commit it as a normal feature — a message like `Add asset classes panel: major indices with 1D change`. **Not** "assignment 02." It's a project, not a course.
4. **Drop the repo link in this PR's comments** once it's up.

**One rule — keep the two worlds clean:** only your own code crosses over. No briefs, no self-check tables, no grades, no mention of iDynamics or training in the public repo. If you're about to paste something and you didn't write it, it doesn't go.

From here on, every finished panel becomes a feature commit in that repo — so by the end you have a real, public, working market dashboard with your name on it.

## Self-check

- [ ] `sp500_preview.html` opens in the browser and shows an interactive 1-year S&P line (you can hover and zoom).
- [ ] Both `sp500_preview.py` and `sp500_preview.html` are committed (the HTML is small — a few dozen KB, not multiple MB).
- [ ] Your public repo exists, is **Public**, has a README in your own words, and its link is in this PR's comments.

## Submission

- Same branch as 02-a/02-b: `submission/py02-asset-classes`.
- New files: `sp500_preview.py` + `sp500_preview.html`.
- Commit this part on its own, e.g. `PY02-c: chart preview`.
- **Now open the PR** (if you haven't) with the full write-up: 📋 the console table (02-a), a note that the HTML panel opens with colors (02-b), 📋 the chart screenshot (02-c), the three self-checks ticked, and your portfolio-repo link in a comment.
