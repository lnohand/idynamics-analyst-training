# Assignment Workflow — Start Clean, Commit Clean, Every Time
### iDynamics Finance Analyst Training Program

Follow this for EVERY assignment. It exists because the most expensive git problems don't look like problems until your PR contains three assignments at once.

## The 60-second version

| Phase | Commands |
|---|---|
| Before starting | `git checkout main` → `git pull origin main` → activate venv → `pip install -r assignments/python/requirements.txt` → `git checkout -b submission/pyNN-<slug>` |
| While working | `git status` early and often |
| Before committing | `git status` → `git add submissions/python/pyNN_<slug>/` → `git commit -m "PYnn: <what you did>"` |
| Before pushing | `git diff origin/main...HEAD --name-only` — the list you see IS your PR |
| Submit | `git push origin submission/pyNN-<slug>` → open PR → paste evidence + self-check |
| After merge | `git checkout main` → `git pull origin main` |

## Step by step, with the WHY

### 1. Start from main — always

```powershell
git checkout main
git pull origin main
```

**Why both:** you're probably still standing on your LAST assignment's branch (check the bottom-left corner of VS Code — it shows the current branch). A new branch grows from wherever you're standing. Branch from an old submission branch and your new PR will drag every commit of the old assignment along with it — the reviewer sees two assignments tangled into one, and the PR can't be merged until it's rebuilt. Starting from a freshly-pulled `main` is what makes your PR contain your work and nothing else.

`git pull` also brings down the newest brief and any updated `requirements.txt` — briefs do get amended.

### 2. Environment check (30 seconds)

```powershell
.venv\Scripts\Activate.ps1
pip install -r assignments/python/requirements.txt
```

If everything's already installed, pip prints "already satisfied" — that's the good outcome, not an error. This exists so a requirements change never surprises you mid-assignment.

### 3. Create the assignment branch — from main, named by the convention

```powershell
git checkout -b submission/py02-asset-classes
git branch --show-current
```

The second command is your receipt — it must print the branch you just named. Naming convention: `submission/pyNN-<slug>` exactly as the brief states (singular `submission`, dashes in the slug). One assignment = one branch = one PR, always.

### 4. Work — and know what you're changing

Do your work in the assignment's folder (`submissions/python/pyNN_<slug>/`), run scripts from the repo root as usual. Along the way:

```powershell
git status
```

Run it whenever you pause. Red files = changed but not staged. If you see files you don't recognize — a stray HTML at the repo root, a `scratch.py`, anything in `.venv` — deal with them NOW (move, delete, or ignore), not at commit time.

### 5. Stage deliberately — add the folder, never "everything"

```powershell
git add submissions/python/py02_asset_classes/
git status
```

Add the assignment folder by name. **Do not use `git add .`** — it stages everything that happens to be lying around, and that's how scratch files and stray outputs end up in PRs. If the brief names another file to include, add it explicitly by path. The second `git status` confirms: green list = exactly the brief's deliverables, nothing else.

### 6. Commit with a message that says what it is

```powershell
git commit -m "PY02: asset classes panel — indices table + styled HTML"
```

### 7. The pre-push check — 10 seconds that prevent the worst PR problems

```powershell
git diff origin/main...HEAD --name-only
```

This prints exactly the files your PR will show. Read the list. **Every file should belong to THIS assignment.** If anything from an older assignment appears, stop — don't push — and paste the list in Slack; it means the branch didn't start from main, and pushing makes it everyone's problem instead of a 2-minute fix.

### 8. Push and open the PR

```powershell
git push origin submission/py02-asset-classes
```

GitHub will show a "Compare & pull request" button. The PR description carries the full evidence package, every time:
- every 📋 paste the brief asks for
- the self-check, ticked **line by line** (like your PY01 — that's the standard now)

### 9. After the merge — reset for next time

```powershell
git checkout main
git pull origin main
```

Do this right after a PR merges, not when the next assignment starts — future-you always forgets. (Optional tidy-up: `git branch -d submission/py02-asset-classes` deletes the local copy of the merged branch.)

## VS Code equivalents (once the commands make sense)

- Current branch + switching: bottom-left corner of the window
- `git status` / staging: the Source Control icon (branch with dots) — stage individual files with the `+` next to each, never the top-level `+` on "Changes"
- Commit: type the message in the box, Ctrl+Enter
- Push: "Sync Changes" / "Publish Branch" button

The terminal commands come first in this guide because they're what you'll find in every job, every tutorial, and every error message — the buttons are shortcuts for later.
