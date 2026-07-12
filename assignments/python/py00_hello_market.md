# Python Assignment 00: Hello, Market
### iDynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** New tooling track — let's get Python on your machine
>
> Michael — nice work getting the SQL set wrapped up. Next tool: Python.
> Over the coming weeks you're going to build us a live market monitoring
> board — the kind of dashboard leadership can open to see indices,
> sectors, and the day's big movers at a glance. Market data is public,
> so we'll build it piece by piece and you'll see a working result at
> every step.
>
> Today is deliberately small: get Python installed, get a clean project
> environment set up, and prove your machine can pull a live market price.
> Nothing ships this week except evidence that your setup works — so
> follow the steps exactly this once. Setup is the one place where I
> *don't* want creativity.
>
> One standing rule for this whole track: if you're stuck on any step for
> more than ~15 minutes, paste exactly what you see into Slack and stop.
> Setup problems are my problem, not yours.
>
> — David

---

## Part 1 — Install Python

1. Download **Python 3.14** (latest 3.14.x) from <https://www.python.org/downloads/>.
2. Run the installer. On the FIRST screen, **check the box "Add python.exe to PATH"** before clicking Install. The steps below use the `py` launcher and would survive without it, but later tools assume it — check it now and forget about it. (If your installer screen looks different from this description, screenshot it and ask before proceeding.)
3. Open **PowerShell** (Start menu → type "PowerShell") and run:

   ```powershell
   py --version
   ```

   You should see `Python 3.14.x`. **📋 Paste this output in your PR description.**

## Part 2 — Project folder and virtual environment

A *virtual environment* (venv) is a private copy of Python for one project, so the packages we install for the board can't collide with anything else on your machine. Every Python project gets its own venv — this is a professional habit, not an option.

1. In PowerShell, go to your local copy of the training repo (`git pull` first, as always) and run:

   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
   ```

   One-time step. Windows blocks locally-created scripts by default; this allows them for your user account only. Answer `Y` if prompted.

2. Create and activate the venv (from the repo root):

   ```powershell
   py -3.14 -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   Your prompt should now start with `(.venv)`. That prefix means "pip and python now act inside this project." **If you open a new PowerShell window later, you must activate again** — no `(.venv)` prefix, no venv.

3. Open `.gitignore` at the repo root and **confirm** `.venv/` is listed (it is — under the `# Python` heading). That line is why your venv folder — machine-specific and huge — will never reach GitHub. Nothing to change; just know it's doing that job.

4. Install the project packages — the exact pinned versions we'll all use:

   ```powershell
   pip install -r assignments/python/requirements.txt
   ```

   Then run:

   ```powershell
   pip freeze
   ```

   **📋 Paste the full `pip freeze` output in your PR description.**

## Part 3 — First live pull (with one bug to fix)

Create `submissions/python/py00_hello_market/hello_market.py` with EXACTLY this content:

```python
import yfinance as yf

spx = yf.Ticker("^GSPC")
last = spx.fast_info["lastPrice"]
prev = spx.fast_info["previousClose"]
print(f"S&P 500: {last_price:,.2f}   1D change: {(last - prev) / prev * 100:+.2f}%")
```

(Don't worry about the `f"..."` formatting syntax yet — that's next assignment. Today you only need to run this, not understand every character.)

Run it:

```powershell
python submissions/python/py00_hello_market/hello_market.py
```

**It will crash. That's intentional.** There is exactly one bug in the script, and it produces a traceback pointing at a line in *your file*.

> ⚠ **If the error mentions HTTP, 404, "rate limit", "connection", or a URL instead — that's NOT the bug.** That's the data source having a moment. Paste it to me in Slack and stop; never spend time debugging the data provider.

1. **📋 Paste the full error message (the "traceback") in your PR description** — reading tracebacks is the single most useful Python skill, so we start here. Read it bottom line first.
2. Fix the bug (one small edit), run again.
3. **📋 In one sentence in your PR: what did the error message tell you, and what was the fix?**
4. Run the fixed script **twice, a few minutes apart**, and **📋 paste both outputs**. If the market is open, the two prices may differ — that's the point: this is live data, not a saved file.

## Submission

- Branch: `submission/py00-hello-market`
- File: the fixed `hello_market.py`
- PR description must contain all four 📋 pastes plus the self-check below.

## Self-check (paste your answers next to each line)

- [ ] `py --version` shows Python 3.14.x
- [ ] `pip freeze` includes `yfinance==1.5.1`, `curl_cffi==0.15.0`, `pandas==3.0.3`
- [ ] None of your pasted outputs contain a warning mentioning `curl_cffi not available` (if one does, say so — it means one package isn't working right on your machine and I need to know)
- [ ] The price printed is a positive number
- [ ] The 1D change is between −10% and +10% (if not, something is wrong — investigate before submitting)
- [ ] Both runs completed without errors
- [ ] Your PR diff contains **no** `.venv` files
