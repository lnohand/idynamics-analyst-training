# Quiz 1 — pandas quick-fire
### Idynamics Finance Analyst Training Program

Nine short questions, the kind you get in a technical interview. No story, no MRR: a small made-up
movie dataset. Every question uses tools you already know. No hints.

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
git checkout -b student/quiz1_quickfire
```

Create `submissions/python/quiz1_quickfire.py` and answer every question in it. Print each answer under
its label (`Q1`, `Q2`, …), with a blank line between questions. Print tables with `.to_string(index=False)`.

## The data — `assignments/python/quiz1_data/`

**`movies.csv`**: one row per movie: `movie_id`, `title`, `genre`, `year`, `minutes`, `rating`.

**`screenings.csv`**: one row per screening: `screening_id`, `movie_id`, `cinema`, `tickets`. A
movie can have several screenings.

## Rules

- Only tools you've used in PD1–PD5, the Checkpoint and FN1. No `.mean()`, no `&`, nothing from
  Copilot or the internet. If you think you need something new, there's a way with what you know.
- Read every condition word by word before you type the sign.

---

## Questions

**Q1.** How many movies are there, and how many minutes in total? Print `Movies: ...` and
`Minutes: ...` (minutes with a comma for thousands).

**Q2.** Movies from **2010 or later** with a rating of **8.0 or more**: show `title`, `year`, `rating`,
highest rating first.

**Q3.** Total minutes per genre, most first (`genre`, `minutes`). Then print only the genres with
**at least 400** minutes (same columns, same order).

**Q4.** Add a column `hours` (minutes ÷ 60, rounded to 2 decimals). Show `title` and `hours` of the
movies **longer than 2.5 hours**, longest first.

**Q5.** What is the average rating of all movies? Print `Average rating: ...` (2 decimals). Then add a
column `vs_average` (each movie's rating minus the average, rounded to 2 decimals) and print
`Above average: ...` with the number of movies above the average.

**Q6.** Total tickets per movie, with the movie's title. Show `title` and `tickets` for movies with
**1,000 tickets or more**, most first.

**Q7.** Two data checks, using `movies.csv` and your Q6 ticket totals for **every** movie (before the
1,000 filter):
- which movies were never screened? Show `movie_id`, `title` and `tickets` (0, not NaN).
- which `movie_id` has screenings but isn't in `movies.csv`? Show `movie_id` and `tickets`.

**Q8.** Write a function `genre_stats` with two inputs, a movies table and a genre, that returns one row
as a dictionary: `genre`, `movies` (how many), `minutes` (total). Call it in a loop for `"Drama"`,
`"Comedy"` and `"Sci-Fi"`, make a table of the three rows, print it, save it as
`submissions/python/quiz1_genres.csv` (no index column) and print `Saved submissions/python/quiz1_genres.csv`.

**Q9.** What does each snippet print, and why? Answer in the PR **before** you run it, then check in
`scratch.py` (read `movies.csv` into `movies` first).

a)
```python
def total_minutes(table):
    print(table["minutes"].sum())

result = total_minutes(movies)
print(result)
```

b)
```python
movies["average"] = movies["rating"].sum() / len(movies)
print(movies["average"].sum())
```
Is this the average rating?

c)
```python
by_genre = movies.groupby("genre")["minutes"].sum()
print(by_genre)
```
Is `genre` a column here? How can you tell, and how would you make it one?

---

## Hand in

Run the whole file from the top. Then commit `submissions/python/quiz1_quickfire.py` only (the CSV stays
on your laptop: the repo doesn't store CSV files): **Source Control** → `+` on the file → message
`Complete: Quiz 1` → **Commit** → **Publish Branch**. Then open a PR from `student/quiz1_quickfire` to
`main` with this description:

~~~
## Quiz 1 — pandas quick-fire

## My output (after running the whole file)
```
[paste the full output here]
```

## Q9
a) My prediction: ... / Right? ...
b) My prediction: ... / Right? ...
c) My prediction: ... / Right? ...

## Time
How long did it take, and which question took longest?
~~~
