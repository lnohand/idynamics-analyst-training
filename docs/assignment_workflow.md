# Assignment Workflow — Start Clean, Commit Clean, Every Time
### iDynamics Finance Analyst Training Program

Follow this for EVERY assignment, top to bottom. Each step says **where you must be standing** and **what you should see** — if what you see doesn't match, stop there and ping me; don't push through.

## Rule zero — every command runs from the repo root

The **repo root** is the folder that contains `assignments/`, `submissions/`, `docs/`, and `.git`. On your machine that's:

```
C:\Users\venti\Downloads\idynamics-training\idynamics-analyst-training
```

How to be there, reliably: open VS Code → File → **Open Folder** → pick that folder → View → **Terminal**. The built-in terminal always opens AT the repo root. That's the whole trick — if you use VS Code's terminal, you're in the right place by default.

**How to verify you're in the right place** (do this whenever unsure):

```powershell
pwd          # should print the path above
git status   # should answer something about a branch — ANY answer is fine
```

If `git status` says `fatal: not a git repository` → you're in the wrong folder. `cd` to the repo root (or reopen the folder in VS Code) before doing anything else.

---

## PHASE 1 — Before you start (get the latest, make your branch)

**You are in: repo root.** Every step below, same place.

**1.1 Switch to main.** You're probably still on your LAST assignment's branch — VS Code shows the current branch in the bottom-left corner.

```powershell
git checkout main
```
You should see: `Switched to branch 'main'` (or `Already on 'main'`).

**1.2 Pull the latest.** This downloads the new brief, updated requirements, and anything I've fixed since your last pull.

```powershell
git pull origin main
```
You should see: either `Already up to date.` or a list of changed files. Both are good.

**Why 1.1 before 1.2:** `git pull origin main` only updates the branch you're standing on. Pull while standing on an old branch and main stays stale — you'd start the new assignment from old material.

**1.3 Wake up the environment.**

**First time on a machine only — create the venv.** The `.venv` folder is not stored in git (it's specific to your computer), so a fresh clone won't have one yet. You build it **once**:

```powershell
py -3.14 -m venv .venv
```
You should see: a new `.venv` folder appear in the repo root. Do this once per clone — never again after that.

**Every session — activate, then a quick install check:**

```powershell
.venv\Scripts\Activate.ps1
pip install -r assignments/python/requirements.txt
```
You should see: the `(.venv)` prefix appear on your prompt — that's activation, and you do it in **every new terminal** (it's per-terminal, not permanent). Then pip mostly printing "Requirement already satisfied" — that line means it's just **checking**, not reinstalling. Packages install *into* `.venv` and stay there; the only times pip actually installs anything are right after you created a fresh venv, or when I tell you I've changed the requirements. If you don't see the `(.venv)` prefix, activation didn't take — run the activate line again in this terminal.

**1.4 Create the assignment branch — from main, named exactly as the brief says.**

```powershell
git checkout -b submission/py02-asset-classes
git branch --show-current
```
You should see: the second command prints exactly the branch name you just created. That's your receipt.

**Why this ordering is sacred:** a new branch grows FROM WHEREVER YOU'RE STANDING. Standing on freshly-pulled main → your branch contains your work and nothing else. Standing on an old assignment's branch → your new PR drags the whole old assignment along, and it can't be merged until someone untangles it.

---

## PHASE 2 — While you work

**2.1 Where your file lives.** Create and edit the assignment file DIRECTLY in its submissions folder — in VS Code's Explorer: right-click `submissions/python/` → New Folder (e.g. `py02_asset_classes`) → right-click that → New File (e.g. `asset_classes.py`). Working in the right place from the start means there's nothing to move later.

**2.2 If you worked somewhere else anyway** (a scratch file on the Desktop, a copy in Downloads — it happens): copy it into the assignment folder before committing. Two ways:

- **Drag & drop** the file from Windows Explorer into the correct folder in VS Code's sidebar, or
- in the terminal (from repo root):
  ```powershell
  Copy-Item C:\Users\venti\Desktop\asset_classes.py submissions\python\py02_asset_classes\
  dir submissions\python\py02_asset_classes
  ```
  You should see: your file in the `dir` listing. Git only sees files INSIDE the repo folder — a file on your Desktop does not exist as far as the PR is concerned.

**2.3 Run your script — from the repo root, always** (paths inside briefs assume it):

```powershell
python submissions/python/py02_asset_classes/asset_classes.py
```

**2.4 Check in with git while you work:**

```powershell
git status
```
You should see: your assignment files in red ("Untracked" or "modified"). Red = git noticed them but they're not staged yet — normal. **If you see files you don't recognize** (a stray HTML at the root, `scratch.py`, anything mentioning `.venv`) — deal with them NOW: delete, move out of the repo, or ask me.

---

## PHASE 3 — Commit and push

**You are in: repo root**, on your assignment branch (check the bottom-left corner).

**3.1 Stage YOUR folder by name — never everything:**

```powershell
git add submissions/python/py02_asset_classes/
git status
```
You should see: your assignment's files now in GREEN ("Changes to be committed"), and nothing else green. **Never use `git add .`** — it grabs everything lying around, which is exactly how stray files end up in PRs. If the brief names an extra file elsewhere, add it by its explicit path.

**3.2 Commit:**

```powershell
git commit -m "PY02: asset classes panel - indices table + styled HTML"
```
You should see: a summary like `2 files changed`. If it says "nothing to commit" → step 3.1 didn't stage anything; run `git status` and look again.

**3.3 The pre-push gate — 10 seconds, every time:**

```powershell
git diff origin/main...HEAD --name-only
```
You should see: **a list containing ONLY this assignment's files.** That list is exactly what your PR will show me. If ANY file from an older assignment appears → do not push; paste the list in Slack. At this stage it's a 2-minute fix; after pushing it's everyone's problem.

**3.4 Push:**

```powershell
git push origin submission/py02-asset-classes
```
You should see: git creating the remote branch and printing a link — GitHub will also show a "Compare & pull request" button on the repo page.

**3.5 Open the PR.** Base `main` ← your branch. The description carries the full evidence package: every 📋 paste the brief asks for + the self-check ticked line by line (like your PY01 — that's the standard now).

---

## PHASE 4 — After the merge

Right after I merge (not next week — future-you forgets):

```powershell
git checkout main
git pull origin main
```
You should see: your merged work now arriving into your local main. You're reset and ready for the next assignment. Optional tidy: `git branch -d submission/py02-asset-classes`.

---

## Special case — "re-pull, I've updated the brief"

If I announce a brief change **before you've started**: you're on main anyway — just `git pull origin main`.

If it happens **mid-assignment** (you're on your branch already):

```powershell
git checkout main
git pull origin main
git checkout submission/py02-asset-classes
git merge main
```
You should see: the updated brief available on your branch, your work untouched. If git says anything about "conflict" — stop and ping me, don't improvise.

---

## Special case — removing a file you shouldn't have committed

Sometimes a file ends up in the repo that shouldn't be there — a scratch copy, or a file you made in the wrong folder and then re-created in the right one (so now there are two). Deleting it from the folder in Explorer isn't enough: git is still **tracking** it, so you have to tell git it's gone, then commit that removal like any other change. One command does both:

```powershell
git rm drills/pf1.py
```
You should see: `rm 'drills/pf1.py'`, and `git status` now shows `deleted: drills/pf1.py` staged (green). `git rm` both deletes the file AND stages the deletion.

Then commit and push exactly as always:

```powershell
git commit -m "Remove stray drills/pf1.py"
git push
```
Then run the pre-push gate (3.3) to confirm it's gone:

```powershell
git diff origin/main...HEAD --name-only
```
You should see: your real files, and NOT the one you just removed. The now-empty folder disappears on its own — git doesn't track empty folders.

**Moving a file is the same idea** — a delete of the old path plus an add of the new one. If you built a file in the wrong place and remade it correctly, `git rm` the wrong copy and `git add` the right one, then commit both together.

**VS Code way:** right-click the file in the Explorer → **Delete** → it shows up as a staged deletion in the Source Control panel; commit + push as usual.

---

## Troubleshooting quick table

| You see | It means | Do |
|---|---|---|
| `fatal: not a git repository` | Wrong folder | `cd` to the repo root / reopen folder in VS Code |
| `can't open file ... No such file or directory` when running a script | You're not at the repo root, or the file isn't where you think | `pwd`, then `dir` the folder the path points to |
| `FileNotFoundError: ... No such file or directory` when a script tries to *write* a file | The path inside `open(...)`/`write_html(...)` is relative to the folder you RAN from, not the folder the script lives in — and you ran it from the wrong folder | `cd` back to the repo root and run it again. **Don't edit the path in the code** — the path is correct for the repo root |
| `ImportError: Missing optional dependency '...'` (e.g. `jinja2`) | A required package isn't installed in this venv | `pip install -r assignments/python/requirements.txt` — it's an install, not a code bug |
| `nothing to commit` | Nothing staged | `git status`, then `git add <your folder>` |
| Old assignment's files in the 3.3 list | Branch didn't start from main | Don't push — paste the list in Slack |
| No `(.venv)` prefix in the prompt | venv not active in THIS terminal | `.venv\Scripts\Activate.ps1` |
| `The module '.venv' could not be loaded`, or activate "not recognized" | No `.venv` folder in this clone yet (it's not in git) | Create it once: `py -3.14 -m venv .venv`, then activate |
| A file you deleted still shows up in the PR | You deleted it in the folder but didn't tell git | `git rm <path>`, then commit + push |

## VS Code equivalents (once the commands make sense)

- Current branch + switching: bottom-left corner of the window
- `git status` / staging: the Source Control icon — stage individual files with the `+` next to each; never the top-level `+` on all of "Changes"
- Commit: message in the box, Ctrl+Enter · Push: "Sync Changes" / "Publish Branch"

The terminal commands come first in this guide because they're what every job, tutorial, and error message speaks — the buttons are shortcuts for later.
