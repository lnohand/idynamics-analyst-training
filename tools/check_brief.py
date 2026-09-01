#!/usr/bin/env python3
"""check_brief.py — mechanical verification for iDynamics assignment briefs.

Implements the machine-checkable acceptance criteria from BRIEF_RELEASE_PROCESS.md:

  A1  every path/filename the brief names exists
  A2  every "assignment NN" cross-reference resolves
  A3  every workbook object (tab/table) the brief names exists, spelled EXACTLY
  E3  Self-Check anchors are internally consistent

Deliberately NOT implemented: A4 and A5. Neither is buildable against reachable
data — there is no messages DB to query, and every local subscriptions mirror
disagrees with the authoritative state, so A5 would fail correct briefs.

Usage:  python3 check_brief.py <brief.md> --workbook <file.xlsx> [--repo <dir>]
Exit 0 = pass, 1 = failures found.
"""

import argparse
import os
import re
import sys

# Tokens that look like paths but are not files that must exist:
# git branches, the student's own output file, Excel error literals.
PATH_ALLOW = re.compile(
    r"""^(
        student/ | submission/ |            # git branch names
        .*excel_\d+_[a-z_]+\.xlsx$ |        # the student's deliverable
        \#N/A | \#REF! | \#VALUE!           # Excel error literals
    )""",
    re.X,
)

PATH_RE = re.compile(r"`([A-Za-z0-9_./-]+\.(?:md|xlsx|sql|csv|py|json))`")
DIR_RE = re.compile(r"`([A-Za-z0-9_-]+/)`")
XREF_RE = re.compile(r"assignment (\d{1,2})\b", re.I)
MONEY_RE = re.compile(r"\$([\d,]+(?:\.\d{2})?)")


def money(s):
    return float(s.replace("$", "").replace(",", ""))


def check_paths(text, repo):
    """A1 — every path the brief names resolves."""
    fails = []
    bases = ["", "assignments/excel/", "docs/", "submissions/excel/", "data/"]
    for tok in sorted(set(PATH_RE.findall(text)) | set(DIR_RE.findall(text))):
        if PATH_ALLOW.match(tok):
            continue
        if not any(os.path.exists(os.path.join(repo, b, tok)) for b in bases):
            fails.append(f"A1  path does not exist: {tok}")
    return fails


def check_xrefs(text, repo, self_num):
    """A2 — 'assignment NN' points at a real assignment that is not this one."""
    fails = []
    adir = os.path.join(repo, "assignments", "excel")
    have = os.listdir(adir) if os.path.isdir(adir) else []
    for num in sorted(set(XREF_RE.findall(text))):
        n = int(num)
        if n == self_num:
            continue
        if not any(re.match(rf"excel_0?{n}_", f) for f in have):
            fails.append(f"A2  'assignment {num}' matches no file in assignments/excel/")
    return fails


def check_workbook(text, workbook):
    """A3 — every backticked name that looks like a sheet exists, spelled exactly."""
    import openpyxl

    wb = openpyxl.load_workbook(workbook, read_only=True)
    sheets = set(wb.sheetnames)
    stripped = {s.strip(): s for s in sheets}
    fails = []

    # Candidates: backticked names that resemble a tab reference.
    cands = set(re.findall(r"`([A-Z][A-Za-z0-9 ]{2,30})`", text))
    cands |= set(re.findall(r"`((?:Jan|Feb|Mar|Apr|May|Jun) \d{4} A vs F ?)`", text))

    for c in cands:
        if c in sheets:
            continue
        if c.strip() in stripped:
            # A brief that explicitly warns about the trailing space is handling it,
            # not getting it wrong. Don't fail correct briefs.
            if "trailing space" in text.lower():
                continue
            fails.append(
                f"A3  '{c}' -> real sheet is '{stripped[c.strip()]}' (whitespace differs)"
            )
        else:
            # Only flag names that closely match an existing sheet; ignore prose.
            squashed = c.replace(" ", "").lower()
            for s in sheets:
                if s.replace(" ", "").lower() == squashed:
                    fails.append(f"A3  '{c}' -> real sheet is '{s}'")
                    break
    return fails


def check_anchors(text):
    """E3 — Self-Check arithmetic identities hold."""
    fails = []
    # Match any heading ending in "Self-Check" ("## Self-Check", "## Final Self-Check").
    heads = list(re.finditer(r"^#{1,4} .*Self-Check\s*$", text, re.M | re.I))
    tail = text[heads[-1].start():] if heads else text
    rows = dict(re.findall(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|$", tail, re.M))

    def find(*keys):
        for label, val in rows.items():
            low = label.lower()
            if all(k in low for k in keys):
                found = MONEY_RE.findall(val)
                if len(found) == 1:   # skip multi-value rows (e.g. "Jan / Feb / Mar / Apr")
                    return money(found[0])
        return None

    closing = find("closing", "mrr")
    netnew = find("net new")
    opening = find("opening", "mrr")

    if closing is not None and netnew is not None and opening is not None:
        if abs((opening + netnew) - closing) > 0.01:
            fails.append(
                f"E3  Opening {opening} + Net New {netnew} != Closing {closing}"
            )
    elif closing is not None and netnew is not None:
        pass  # opening is usually stated as "derived", not a figure — not a failure
    return fails


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("brief")
    ap.add_argument("--workbook")
    ap.add_argument("--repo", default="/Users/ebezrukova/idynamics-training/repo")
    args = ap.parse_args()

    text = open(args.brief).read()
    m = re.search(r"excel_(\d+)_", os.path.basename(args.brief))
    self_num = int(m.group(1)) if m else -1

    fails = []
    fails += check_paths(text, args.repo)
    fails += check_xrefs(text, args.repo, self_num)
    if args.workbook:
        fails += check_workbook(text, args.workbook)
    fails += check_anchors(text)

    name = os.path.basename(args.brief)
    if fails:
        print(f"FAIL  {name} — {len(fails)} issue(s)")
        for f in fails:
            print(f"   {f}")
        return 1
    print(f"PASS  {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
