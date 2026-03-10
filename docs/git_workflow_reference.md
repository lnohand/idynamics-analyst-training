# Git Workflow — Getting Assignments and Submitting Your Work
## Idynamics Analyst Training

---

## Every Time You Start a New Assignment

**Step 1 — Open Command Prompt and navigate to the repo**

```
cd %USERPROFILE%\Documents\idynamics-training\idynamics-analyst-training
```

**Step 2 — Pull the latest from main**

```
git checkout main
git pull origin main
```

This downloads any new assignments or feedback your instructor has added.
Always do this before creating a branch — never work on an outdated copy.

**Step 3 — Create a new branch for this assignment**

```
git checkout -b student/sql-02-window-functions
```

Replace `sql-02-window-functions` with the current assignment name.
**Use a new branch for every assignment — never reuse an old one.**

You're now ready to work. Open your files in DBeaver or your text editor
as normal. Save your `.sql` file into the correct folder inside the repo
(your instructor will tell you where).

---

## When You're Ready to Submit

**Step 4 — Check what Git can see**

```
git status
```

Your file should appear under "Untracked files" or "Changes not staged".

**Step 5 — Stage your file**

```
git add submissions\sql\02_window_functions.sql
```

Replace the filename with your actual file.

**Step 6 — Commit with a clear message**

```
git commit -m "Complete: SQL 02 — window functions, all self-checks pass"
```

**Step 7 — Push your branch to GitHub**

```
git push origin student/sql-02-window-functions
```

**Step 8 — Open a Pull Request on GitHub**

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

Make the fix in your file, then run these commands on the **same branch**:

```
git add submissions\sql\02_window_functions.sql
git commit -m "Fix: SQL 02 — [what you corrected]"
git push origin student/sql-02-window-functions
```

The Pull Request updates automatically. No need to open a new one.

---

## Quick Reference

| What you're doing | Command |
|---|---|
| Go to the repo folder | `cd %USERPROFILE%\Documents\idynamics-training\idynamics-analyst-training` |
| Get the latest assignments | `git checkout main` then `git pull origin main` |
| Start a new assignment | `git checkout -b student/[assignment-name]` |
| Check what's changed | `git status` |
| Stage a file | `git add [filepath]` |
| Commit | `git commit -m "Complete: [assignment] — [description]"` |
| Push to GitHub | `git push origin student/[assignment-name]` |

---

*Git Workflow Reference | Idynamics Analyst Training | March 2026*
