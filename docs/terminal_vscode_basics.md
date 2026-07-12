# Terminal & VS Code Basics — Quick Reference
### iDynamics Finance Analyst Training Program

Keep this open until the commands are muscle memory.

## The five commands that cover 95% of terminal life (PowerShell)

| You want to… | Type | Notes |
|---|---|---|
| See where you are | `pwd` | "print working directory" |
| See what's here | `dir` | lists files + folders |
| Go into a folder | `cd submissions\python` | Tab key auto-completes names — use it constantly |
| Go up one level | `cd ..` | repeat as needed: `cd ..\..` |
| Make a new folder | `mkdir submissions\python\py01a_python_drills` | creates the whole path at once |

Two habits that prevent 95% of confusion:
1. **Always know where you are.** Every command runs *relative to your current folder* — if a script "can't find" a file, `pwd` first.
2. **Tab-complete everything.** Typing full paths by hand is how typos happen.

## The VS Code way (do most things here instead)

- **Open the project:** File → Open Folder → select your `idynamics-analyst-training` clone. (First time it asks about "Workspace Trust" — click **Yes, I trust the authors**.) The left sidebar (Explorer) is now your folder tree — no `dir` needed.
- **Create a folder/file:** right-click in the Explorer → New Folder / New File. Type the name (e.g. `drills.py`) — done. This replaces `mkdir` + hunting in Notepad.
- **Built-in terminal:** View → Terminal (or `` Ctrl+` ``). It's the same PowerShell, already opened AT the project folder — activate your venv there (`.venv\Scripts\Activate.ps1`) and run scripts as usual.
- **Run a script:** with the terminal open: `python submissions\python\py01a_python_drills\drills.py` — or click the ▶ button top-right of the editor (make sure the venv is selected as the interpreter, bottom-right corner should show `.venv`).
- **The Python extension** underlines errors as you type and colors your code. Install it once from the Extensions icon (four squares) → search "Python" → the one by Microsoft.

Forward slashes vs backslashes: PowerShell accepts both `submissions\python\...` and `submissions/python/...` — the briefs write `/`, your Tab-completion may write `\`. Both fine.
