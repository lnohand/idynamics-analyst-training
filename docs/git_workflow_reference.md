# Git Workflow — Getting Assignments and Submitting Your Work
## Idynamics Analyst Training

---

## Every Time You Start a New Assignment

**Do this in VS Code.** You don't need Command Prompt or PowerShell.

**Step 1 — Get the latest `main`**

Source Control panel → the `...` button at the top → **Pull, Push** →
**Fetch From All Remotes**.

Nothing obvious happens on screen. That's normal — it's downloading any new
assignments and feedback your instructor has added.

**Step 2 — Create the new branch, from `main`**

1. Click the **branch name in the bottom-left corner** of the window. A menu
   drops down from the top of the screen.
2. Choose **`Create new branch from...`**

   ⚠️ Two options look almost identical. Read them:
   - `Create new branch...` — branches from wherever you are right now. **Not this one.**
   - `Create new branch from...` — lets you choose. **This one.**
3. Type the branch name, e.g. `student/sql-02-window-functions`, then Enter.
4. A list of branches appears. Choose **`origin/main`**.

The bottom-left corner now shows your new branch, and it started from `main`.

**Why this way:** step 4 is the point — you pick `main` from a list, on purpose.
`git checkout -b` never mentions `main` anywhere; it branches from wherever you
happen to be standing, which is usually your *last* assignment's branch. Then your
pull request shows all your old work on top of the new work.

**Use a new branch for every assignment — never reuse an old one.**

You're now ready to work. Save your files into the correct folder inside the repo
(your instructor will tell you where).

<details>
<summary>If you'd rather type the commands</summary>

Chain them with `&&` so the sequence stops if one fails, instead of carrying on
from the wrong branch:

```
git checkout main && git pull origin main && git checkout -b student/sql-02-window-functions
```

Then check it worked — this must print **nothing at all**:

```
git log origin/main..HEAD --oneline
```

If it prints commits, your branch was built on top of old work. Tell your instructor
before you start.
</details>

---

## When You're Ready to Submit

Again — all of this is in VS Code.

**Step 3 — Save the file** (Ctrl+S).

**Step 4 — Stage it**

Click the **Source Control** icon in the left sidebar (the branching arrows).
Your file appears under **Changes**. Hover it and click the **`+`**.

⚠️ The **`+`** stages your work. The **`↩`** next to it *throws your changes away*.
Don't click that one.

**Step 5 — Commit**

Type a message in the box at the top, e.g.
`Complete: SQL 02 — window functions, all self-checks pass`, then click **Commit**.

**Step 6 — Push**

Click **Publish Branch** (first time pushing this branch) or **Sync Changes**
(every time after).

**Step 7 — Open a Pull Request on GitHub**

1. Go to `https://github.com/lnohand/idynamics-analyst-training`
2. Click **Compare & pull request** from the banner at the top
3. Set the title to match your assignment: `SQL 02 — Window Functions`
4. Fill in the description:

```
## What this does
[One sentence describing what your query does in business terms]

## Self-check
[Paste the expected value and your result — e.g., Last row total_mrr = $142,110.50 ✅]

## Questions for reviewer
[Anything you're unsure about, or leave blank]
```

5. Click **Create pull request**

Your instructor will review it and leave comments. You'll get an email
from GitHub when they do.

---

## If Your Instructor Asks You to Fix Something

Make the fix, then **stay on the same branch** and repeat Steps 3–6: save, `+`,
commit message (`Fix: SQL 02 — [what you corrected]`), **Sync Changes**.

The Pull Request updates automatically. No need to open a new one, and no need
to make a new branch.

---

## Files you never want to commit

A file showing in **red** in `git status` just means git can see it and it isn't
committed. There are two kinds, handled differently:

- **A file already in the repo that you changed** → commit it, or undo the change.
- **A file git has never seen** → commit it, *or* tell git to ignore it forever.

For the second kind — scratch files, practice files, anything that isn't a
submission — add its name to the `.gitignore` file in the top folder of the repo,
one name per line. It stops appearing immediately.

Aim for `git status` saying `nothing to commit, working tree clean` before you
switch branches.

---

## Quick Reference

| What you're doing | In VS Code |
|---|---|
| Get the latest assignments | Source Control → `...` → **Pull, Push** → **Fetch From All Remotes** |
| **Start a new assignment** | Click the **branch name, bottom-left** → **`Create new branch from...`** → type the name → pick **`origin/main`** |
| See which branch you're on | Look at the **bottom-left corner** — it's always showing |
| Check what's changed | **Source Control** panel, left sidebar |
| Stage a file | Hover the file → click **`+`** (never `↩`) |
| Commit | Type the message at the top → **Commit** |
| Push to GitHub | **Publish Branch**, or **Sync Changes** after the first time |
| Run a Python file | The **▶** button, top-right of the editor |
| Get back an earlier saved version | Right-click the file → **Open Timeline** |

**The one that matters most:** *Start a new assignment.* Use
`Create new branch from...` and pick `origin/main` — never `Create new branch...`,
which silently branches from your last assignment.

---

*Git Workflow Reference | Idynamics Analyst Training | updated July 2026*
