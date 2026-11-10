# Quiz 3 — which merge?
### Idynamics Finance Analyst Training Program

Nine short questions, same format as Quizzes 1 and 2, with new made-up data: a small online school
that sells courses. This one is mostly about **merge**: four questions need one, and each time you
choose which kind. Everything else uses tools you already know.

Expect about an hour.

---

## Set up

In VS Code, **Terminal → New Terminal**:

```
git status
```

It must say `nothing to commit, working tree clean`. If it doesn't, message me before going on.

```
git checkout main
git pull origin main
git checkout -b student/quiz3_merge
```

Create `submissions/python/quiz3_merge.py` and answer every question in it. Print each answer under
its label (`Q1`, `Q2`, …), with a blank line between questions. Print tables with `.to_string(index=False)`.

## The data — `assignments/python/quiz3_data/`

**`courses.csv`**: the catalogue, one row per course: `course_id`, `title`, `category`, `price`, `instructor_id`.

**`instructors.csv`**: one row per instructor: `instructor_id`, `name`, `city`.

**`enrollments.csv`**: one row per purchase: `enroll_id`, `course_id`, `student`, `month`, `paid`.
A course can be bought many times, or never.

## One idea for this quiz: which list has the data?

In Quiz 2, Q7, the books nobody borrowed were hard to find. Not every book gets lent, so a book that
was never borrowed **isn't in `loans.csv` at all**. The only list with every book is `books.csv`.

So before every merge, ask: **which list has every item my answer needs?**

| The answer needs… | Do this |
|---|---|
| every item from one list (even ones with no match) | put that list **first** and use `how="left"`; then `.fillna(0)` |
| only rows that match on both sides | leave `how` out (the default keeps matches only) |
| what's missing on **either** side | `how="outer", indicator=True`, then filter `_merge` |

The examples and real output for each are in `docs/pandas_merge_cheatsheet.md` (pull main). Read it
before Q4.

Before each merge in this quiz, write that question as a comment above it, with your answer:
```python
# Which list has every item? ...
```

## Rules

- Use the tools you've used so far, plus the cheat sheet. If you look something up, say what in the PR.
- Read every condition word by word before you type the sign.

---

## Questions

**Q1.** How many courses, instructors and enrollments are there, and how much was paid in total? Print
`Courses: ...`, `Instructors: ...`, `Enrollments: ...` and `Total paid: $...` (comma for thousands).

**Q2.** Courses that cost **$50 or more** but **under $80**: show `title`, `category`, `price`, most
expensive first.

**Q3.** Total paid per month (`month`, `paid`), most first.

**Q4.** The school wants sales for **every course in the catalogue**, including courses nobody bought
(those show `0`, not NaN). Show `course_id`, `title`, `paid`, lowest first. Then print
`Courses with no sales: ...`.

**Q5.** The September report lists each September purchase with the course title: `student`, `title`,
`paid`. It should only show courses that are in the catalogue. Then print `Total in report: $...` and
`Total paid in September: $...` (from `enrollments.csv`). If the two totals differ, explain why in the PR.

**Q6.** Check the instructor records:
- Which instructors don't teach any course? Show `instructor_id` and `name`.
- Which courses have an `instructor_id` that isn't in `instructors.csv`? Show `course_id`, `title`, `instructor_id`.

**Q7.** Total paid per instructor, for **every instructor on the list** (`0` if their courses sold
nothing, or they teach nothing). Show `name` and `paid`, most first. Then print `Total: $...`.
(Hint: you need the instructor of each course first. You already have a table with every course.)

**Q8.** Write a function `month_stats` with two inputs, an enrollments table and a month, that returns
one row as a dictionary: `month`, `enrollments` (how many), `paid` (total), `avg_paid` (paid per
enrollment, rounded to 2 decimals). Call it in a loop for `"2026-07"`, `"2026-08"` and `"2026-09"`,
make a table of the three rows, print it, save it as `submissions/python/quiz3_months.csv` (no index
column) and print `Saved submissions/python/quiz3_months.csv`.

**Q9. Predict, then run.** In `scratch.py`, read `courses.csv` and `enrollments.csv`, and make
`sales = enrollments.groupby("course_id", as_index=False)["paid"].sum()`. For each line below, write in
the PR **before you run it**: how many rows it gives, and which course IDs are missing or have NaN.
Then run it with `print(len(...))` and say if you were right.

```python
a = pd.merge(courses, sales, on="course_id")
b = pd.merge(courses, sales, on="course_id", how="left")
c = pd.merge(sales, courses, on="course_id", how="left")
```
Which one would you use for Q4, and why?

---

## Hand in

Run the whole file from the top. Then commit `submissions/python/quiz3_merge.py` only (the CSVs stay
on your laptop): **Source Control** → `+` on the file → message `Complete: Quiz 3` → **Commit** →
**Publish Branch**. Then open a PR from `student/quiz3_merge` to `main` with this description:

~~~
## Quiz 3 — which merge?

## My output (after running the whole file)
```
[paste the full output here]
```

## Conditions
For Q2: copy the code lines with the signs, and the words in the question they come from.

## Q5
Do the two totals match? If not, why?

## Q7
Your Q7 total is less than Q1's total paid. Which two things explain the gap?

## Q9
a) My prediction: ... / Right? ...
b) My prediction: ... / Right? ...
c) My prediction: ... / Right? ...
For Q4 I'd use ... because ...

## Time
How long did it take, and which question took longest?
~~~
