# Quiz 2 — pandas quick-fire
### Idynamics Finance Analyst Training Program

Nine short questions, the kind you get in a technical interview. Same format as Quiz 1, with new
made-up data: a small library. Every question uses tools you already know. No hints.

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
git checkout -b student/quiz2_quickfire
```

Create `submissions/python/quiz2_quickfire.py` and answer every question in it. Print each answer under
its label (`Q1`, `Q2`, …), with a blank line between questions. Print tables with `.to_string(index=False)`.

## The data — `assignments/python/quiz2_data/`

**`books.csv`**: one row per book in the catalogue: `book_id`, `title`, `category`, `year`, `pages`, `price`.

**`loans.csv`**: one row per loan: `loan_id`, `book_id`, `branch`, `days` (how long it was borrowed).
A book can be borrowed many times.

## Rules

- Use the tools you've used so far. If you look something up, say what in the PR.
- Read every condition word by word before you type the sign.

---

## Questions

**Q1.** How many books are there, how many pages in total, and how many loans? Print `Books: ...`,
`Pages: ...` (with a comma for thousands) and `Loans: ...`.

**Q2.** Books from **2015 or later** that cost **under $20**: show `title`, `year`, `price`, cheapest first.

**Q3.** Total pages per category, most first (`category`, `pages`). Then print only the categories with
**more than 1,000** pages (same columns, same order).

**Q4.** At 40 pages an hour, how long does each book take to read? Add a column `hours` (pages ÷ 40,
rounded to 1 decimal). Show `title` and `hours` of the books that take **10 hours or more**, longest first.

**Q5.** What is the average price of all books? Print `Average price: $...` (2 decimals). Then add a
column `vs_average` (each book's price minus the average, rounded to 2 decimals) and print
`Below average: ...` with the number of books cheaper than the average.

**Q6.** Total days borrowed per book, with the book's title. Show `title` and `days` for books borrowed
**30 days or more** in total, most first.

**Q7.** The library wants to clear shelf space, and to fix its records:
- Which books has nobody ever borrowed? Show `book_id`, `title` and `days` (0, not NaN).
- Some loans have a `book_id` that isn't in the catalogue. Which ID, and how many days in total? Show
  `book_id` and `days`.

**Q8.** Write a function `category_stats` with two inputs, a books table and a category, that returns one
row as a dictionary: `category`, `books` (how many), `pages` (total), `avg_pages` (pages per book,
rounded to 1 decimal). Call it in a loop for `"Fiction"`, `"Cooking"` and `"Science"`, make a table of the
three rows, print it, save it as `submissions/python/quiz2_categories.csv` (no index column) and print
`Saved submissions/python/quiz2_categories.csv`.

**Q9. Column or index?** For each snippet, write in the PR what it prints and why **before** you run it.
Then run it in `scratch.py` (read `books.csv` into `books` first) and say if you were right.

a)
```python
by_cat = books.groupby("category")["pages"].sum()
print(by_cat)
print(by_cat["Fiction"])
```
Is `category` a column or the index here?

b)
```python
by_cat = books.groupby("category", as_index=False)["pages"].sum()
print(by_cat)
print(by_cat["Fiction"])
```
What's different from a), and why? How would you get Fiction's pages from this table instead?

c)
```python
by_cat = books.groupby("category")["pages"].sum()
by_cat.to_csv("submissions/python/scratch_cat.csv", index=False)
```
Open `scratch_cat.csv`. What's in it, and what's missing? Which version of `by_cat`, a) or b), would
you save?

d)
```python
print(books["title"].head())
```
What are the numbers on the left? Is that a column? Does one column on its own have an index?

---

## Hand in

Run the whole file from the top. Then commit `submissions/python/quiz2_quickfire.py` only (the CSVs stay
on your laptop: the repo doesn't store CSV files): **Source Control** → `+` on the file → message
`Complete: Quiz 2` → **Commit** → **Publish Branch**. Then open a PR from `student/quiz2_quickfire` to
`main` with this description:

~~~
## Quiz 2 — pandas quick-fire

## My output (after running the whole file)
```
[paste the full output here]
```

## Conditions
For Q2, Q3, Q4 and Q6: copy the code line with the sign, and the words in the question it comes from.

## Q9
a) My prediction: ... / Right? ...
b) My prediction: ... / Right? ...
c) My prediction: ... / Right? ...
d) My prediction: ... / Right? ...

## Time
How long did it take, and which question took longest?
~~~
