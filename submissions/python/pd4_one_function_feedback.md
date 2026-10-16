# PD4 — May and June from one function: Feedback

**Status:** Approved ✅
**Reviewed by:** David Chen

Michael, this is right, and it's good to hear the function idea clicked. I ran
`pd4_one_function.py` on the month lists, and every number matches mine: June from the function,
May and June side by side, both checks 0.0, and April added in front of them with its check also
0.0. The output you pasted in the PR is exactly what the script prints. Nothing to resubmit.

## How I know it's your code doing the work

In a copy of the April list I added 1 to CUST002, then ran your script again on that copy. April's
closing went to 156,831.50 and its expansion to 441.00. May's opening moved to 156,831.50 and its
contraction to −441.00. All three checks stayed 0.0. The numbers come from the files, and since
April's closing list is May's opening list, one file feeds both months.

## One question

Right idea: the function does the work, so a new month is a couple of lines. Two small
corrections:

- **Count from your file.** Step 4 is four lines: `april = bridge(...)`, the new `table`, the
  `check` column and the `print`. Only the first of those is new work. The other three repeat
  Steps 2–3 with April added.
- **Compare with the right "without".** The question asked what it would take without the
  function, so the comparison is your Python file without `bridge`. Excel is a different
  comparison.

Model answer:

*"Adding April took four lines, and only one was new work: `april = bridge(...)` with March's and
April's files. The other three rebuilt the table and the check with April in it. Without the
function I'd have copied all twenty lines of the bridge and renamed every variable for April,
which is exactly where mistakes come in."*

Next up is PD5: the same function for every month from January to June, in one go.

— David
