# Quiz 3 — which merge?: Feedback

**Status:** Six fixes, then merge
**Reviewed by:** David Chen

Michael — I pulled your branch, ran the file against the data, and checked every answer against my
own solution. **The hard part of this quiz, you got.** The merge reasoning is the thing I was
testing and it's there. The fixes below are mechanical, and two of them are the reason I'm writing
the middle section.

---

## What you did well

**Every `how=` in the file is the right one, and that was the whole exam.**

- **Q4** — you needed every course in the catalogue including the ones nobody bought. You went
  `how="outer"` with `indicator=True` and pulled `right_only`. That isn't the route I'd written in
  the key, and it's correct: all 16 courses, `C07` and `C12` sitting at 0, and `C99` properly left
  out because it isn't in the catalogue at all. You worked out that the catalogue is the list with
  every item, and you built from it.
- **Q5** — `how="left"` from `enrollments`, which *keeps* `C99`. That's why your two totals came
  out $791 and $851, and your explanation is exactly right: *"the enrollments table includes a
  purchase of a course with the id C99 which does not exist."* Most people merge that difference
  away without ever seeing it.
- **Q6** — `how="outer"` with the indicator again, reading it in both directions: `I06` teaching
  nothing, and `C13` pointing at an instructor `I09` who isn't on the list. One join, two
  questions, both answered.
- **Q7** — the double left merge from `instructors`. You said this one took the longest and I
  believe you; it's the hardest thing in the quiz. Starting from `instructors` is what keeps `I06`
  in the table at 0 instead of silently vanishing. Your per-instructor figures are right.

And your Q7 write-up is the best thing you've sent me:

> *"C13 has an instructor ID that doesn't exist (I09) which is worth $80 and C99 isn't in the
> courses table so it cannot be matched to the instructor table ($120)."*

That's the $200 gap, both halves, correctly attributed. That is the answer to "which list has the
data?" and it means the idea has actually landed rather than been recited.

Q1, Q3 and Q4's numbers are all correct. You also fixed the `avg_paid` column name from last time —
I noticed.

---

## The part I need you to change

I asked you to do Quiz 2's four fixes first, and said they'd take ten minutes. You did Quiz 3
instead. I'm not annoyed about the order for its own sake — I'm pointing it out because of what it
cost you.

**You made two of the same mistakes again, in the same question numbers.**

### The first one: Q2, both times — a line that runs and does nothing

Quiz 2, Q2:
```python
later = books[(books["year"] >= 2015) & (books["price"] < 20)]
later = books.sort_values("price", ascending=False)   # rebuilt from books, not from later
```

Quiz 3, Q2:
```python
chiz = courses[(courses["price"] >= 50) & (courses["price"] < 80)]
chiz.sort_values("price", ascending=False)            # result not assigned to anything
```

Different shapes, same thing: **the sort executed and the answer went nowhere.** In Quiz 2 you
overwrote your filtered table; here you never captured the sorted one. `sort_values` hands you back
a new table — it doesn't rearrange `chiz` in place. So your output is in file order, and the
question said *most expensive first*.

Correct answer, most expensive first: SQL for Analysts 79, Cash Flow Clinic 75, Dashboards that Talk
70, Joins Without Tears 65, Charts in Python 60, Reading a P&L 55, Pivot Tables in a Day 50.

One more thing worth sitting with. In your Conditions section you pasted this:

> Q2. Courses that cost $50 or more but under $80: show title, category, price, **most expensive
> first.**
>
> `chiz.sort_values("price", ascending=False)`

The requirement and the broken line are three lines apart, in your own writing. The quoting
exercise only helps if you read the two against each other — otherwise it's transcription. Same
thing happened on Quiz 2's Q3, where you quoted "more than 1,000" directly above a `>=`.

### The second one: Q8, both times — a variable name in quotes

Quiz 2, Q8:
```python
"books": len("books_category"),          # counts the 14 letters in the word
```

Quiz 3, Q8:
```python
"enrollments": len("enrollments_total"), # counts the 17 letters in the word
```

Identical bug. The quotes make it a piece of text, so `len` measures the word instead of the table.
That's why all three of your months report **17** enrollments. The real counts are **10, 10 and 11**
— and 11 for September is a fact you'd want, because it's the month with the `C99` purchase in it.

Your `paid` and `avg_paid` columns are right, which is what makes this one dangerous: two of three
columns correct, so the table looks fine.

Also still there from Quiz 2: the function takes `table` as a parameter and never uses it —
the body reads the global `enrollments`. It gives the right answer only because you happened to
pass `enrollments`. Call it with anything else and it ignores you.

### Why I'm making a point of it

Nothing here is a knowledge gap. You know how to sort, you know what `len` does, you know what a
parameter is. Both bugs were already written down, with the fix, in a file in this repo — and they
cost you the better part of two hours of "Adjusted / Adjusted AGAIN / Adjusted once more", which is
what your commit messages say.

So the habit I'm asking for is small and it's worth a lot: **when feedback lands, read it and apply
it before you start the next thing.** Ten minutes on Quiz 2 would have removed two of the six fixes
below. Feedback is only worth the time I spend writing it if it changes the next piece of work —
otherwise we both keep paying for the same mistake.

You're not behind. You're moving quickly and the thinking is getting noticeably better. This is the
one process habit that would make the difference show up in the output.

---

## Fix list

1. **Q2** — assign the sorted table (`chiz = chiz.sort_values(...)`), or chain it onto the filter.
   Expect 7 rows, most expensive first.
2. **Q8** — `len(enrollments_total)` without the quotes. Expect 10, 10, 11.
3. **Q8** — make the function read `table`, not the global `enrollments`.
4. **Q7** — the question asks for `name` and `paid`; you printed `instructor_id`. It also asks you
   to print `Total: $...`, which is missing. Your total is $2,029 — worth showing, since it's the
   number your own write-up explains.
5. **Q9c** — you marked this right and it isn't. `pd.merge(sales, courses, how="left")` gives
   **15** rows, not every course: starting from `sales` means `C07` and `C12` are absent entirely,
   because they were never sold. You predicted "every single course". You correctly marked (a)
   wrong, so you're checking some of them — run all three and read the row counts. Your choice of
   (b) for Q4 is right, and for the right reason.
6. **File location** — you committed `assignments/python/quiz3_merge.py`. It belongs in
   `submissions/python/quiz3_merge.py`. `assignments/` is where I put work for you; `submissions/`
   is where you put work for me. Your CSV path was right.

Then re-run the whole file from the top, check the output matches what you paste, and push to the
same branch.

**And do Quiz 2's four fixes in the same sitting** — they're still outstanding, and I'm holding that
PR open until they're in.

— David
