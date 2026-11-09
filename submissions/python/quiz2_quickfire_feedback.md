# Quiz 2 — pandas quick-fire: Feedback

**Status:** Fixes needed on Q2, Q3 and Q8, then merge
**Reviewed by:** David Chen

Michael, I pulled your branch, ran `quiz2_quickfire.py` against the data, and checked every answer
against my own solution. **Q1, Q4, Q5 and Q7 are correct, and so are Q9 a, b and c.** Q7 is the
best work in the file — more on that below.

Four need fixing. Two of them are the same lesson, and it's the most important one in this quiz,
so I'm putting it first.

---

## The headline: both wrong answers ran without complaint

Q2 and Q3 didn't crash. They printed clean, well-formatted, plausible-looking tables. They were
just answering a different question than the one asked.

This is the failure mode that matters in finance. A `SyntaxError` costs you ten minutes. A filter
that silently didn't apply goes into a board pack.

### Q2 — the filter never ran

```python
later = books[(books["year"] >= 2015) & (books["price"] < 20)]
later = books.sort_values("price", ascending=False)
```

Look at what the second line is built from: `books`, not `later`. So line 1 computes the filtered
table, assigns it to `later`, and line 2 immediately throws it away and replaces it with all 18
books. The condition was correct. It just never reached the output.

You printed **18 rows. The answer is 7.**

And notice why it slipped through: the `price` column descends perfectly, so the table *looks*
deliberate. Nothing about it says "this is wrong."

Two things also went wrong with the sort. "Cheapest first" is `ascending=True` — you used
`ascending=False`. And you sorted a table you'd already discarded.

The correct answer:

```
             title  year  price
    Harbour Lights  2023   9.99
Small Gods of Rain  2015  14.99
       Seven Moons  2020  15.75
   The Glass Atlas  2022  16.00
   Rooftop Gardens  2020  17.25
     The Salt Road  2016  18.50
   Starfield Notes  2024  19.00
```

**The habit that catches this:** before you print, know roughly how many rows you expect. "Books
from 2015 or later, under $20" out of 18 books should be a handful, not all of them. When 18 rows
come back, that's the signal. `print(len(later))` costs you nothing.

A smaller point on style: reassigning the same name twice is what let this hide. If the second
line had been `later = later.sort_values("price")`, the bug would have been impossible. Chain it
in one statement and there's nowhere for the mistake to live:

```python
later = (books[(books["year"] >= 2015) & (books["price"] < 20)]
         .sort_values("price"))
```

### Q3 — `>=` where the question said "more than"

```python
piz = piz[(piz["pages"] >= 1000)]
```

Science has exactly 1,000 pages. "**More than** 1,000" excludes it. `>=` includes it.

The answer is Fiction (1602) and History (1560). You printed three categories.

I want to point at something in your own PR. You quoted the question directly above your code:

> *"Then print only the categories with more than 1,000 pages"*

...and then wrote `>=` underneath it. Both halves were on screen at once. The quoting exercise is
supposed to catch exactly this, so when you do it, read the two lines against each other rather
than just pasting them in. "More than" is `>`. "At least" / "or more" is `>=`. Science sitting at
exactly 1,000 is not an accident in the data — it's there to find out which one you'd write.

You got the sign right in Q4 ("10 hours or more" → `>=`) and Q6 ("30 days or more" → `>=`). So
you can do this. Q3 is the one where the wording changed and the code didn't.

---

## Q8 — three things, one of which is a quiet trap

```python
"books": len("books_category"),
```

Those quotes make it a **string**, not your variable. `len("books_category")` counts the
characters in the word — 14. That's why all three categories reported `books = 14`:

```
category  books  pages  average
 Fiction     14   1602    320.4      <- should be 5
 Cooking     14    800    200.0      <- should be 4
 Science     14   1000    333.3      <- should be 3
```

Your `pages` and `avg_pages` figures are all correct, which is what makes it sneaky — two of
three columns were right, so the table looked fine.

**Second: the column name.** The brief asks for `avg_pages`. You wrote `average`. The numbers are
right but `quiz2_categories.csv` has the wrong header, so anything reading that file by column
name breaks. When a brief names a field, treat it as a contract — downstream code depends on it.

**Third, and this is the one worth your time:** your function takes `table` as a parameter and
never uses it.

```python
def category_stats(table, category):
    books_category = books[books["category"] == category]   # <- reads the global, not `table`
```

It gives the right answer only because you happened to pass `books`. Call it with anything else —
a different year's catalogue, a filtered subset — and it silently ignores you and returns figures
for the global `books`. That's a function that lies about what it does.

```python
def category_stats(table, category):
    rows = table[table["category"] == category]
    return {
        "category": category,
        "books": len(rows),
        "pages": int(rows["pages"].sum()),
        "avg_pages": round(rows["pages"].mean(), 1),
    }
```

One-word change, but it's the difference between a function and a shortcut. The reason you take
an argument is so the function has no opinion about where the data came from. This matters more
than it looks right now — once you're writing the month-end scripts, a function that secretly
reads a global is how April's numbers end up in May's report.

Correct output:

```
category  books  pages  avg_pages
 Fiction      5   1602      320.4
 Cooking      4    800      200.0
 Science      3   1000      333.3
```

---

## Q9d — you had it and then talked yourself out of it

> *"The numbers on the left count the number of entries. It is not a column I believe. It does not
> have an index."*

You're right that it isn't a column. But those numbers **are** the index — that's precisely what
you're looking at. They're not a count of anything; they're labels, one per value.

And you proved it yourself two answers earlier. In (a), `by_cat["Fiction"]` worked. That only
works because a Series *has* an index and `Fiction` was a label in it. Same object, same
structure.

A Series is one column of values **plus** an index. `books["title"].head()` gives you five titles
and their five index labels `0 1 2 3 4` — inherited straight from the DataFrame row positions.
Which is why `.reset_index(drop=True)` exists: after filtering, those labels keep the *original*
row numbers, so a filtered Series can start at 7 and skip to 11.

You marked all four ✅ in the PR. a, b and c were genuinely right — b especially, where you
predicted the `KeyError` *and* gave the correct `by_cat[by_cat["category"] == "Fiction"]`
alternative. But go back and check a prediction against the real output rather than against your
memory of what you expected; d is the one where running it would have shown you the answer.

---

## Q7 — this is the best thing in the file

Keep doing this.

```python
both = pd.merge(books[["book_id","title"]], loaned, how="outer", on="book_id", indicator=True)
never  = both[both["_merge"] == "left_only"]
no_id  = both[both["_merge"] == "right_only"]
```

One outer join, then `indicator=True` to answer two different questions from it — books with no
loans, and loans with no book. That's exactly how you find breaks between two systems, and it's
the same shape as the reconciliation work you've been doing in Excel: what's on the left and not
the right, what's on the right and not the left. `B14`/`B17` never borrowed, `B99` a loan against
a book that doesn't exist. Both correct, and `fillna(0)` gave the `0` the question asked for
instead of `NaN`.

One cosmetic note: the days print as `0.0` and `21.0` rather than `0` and `21`. The outer join
introduces `NaN`, which forces the column to float, and it stays float after `fillna`. If you
want clean integers, `.astype(int)` after the `fillna`.

---

## Two process notes

**The stray `print(loaned)` in Q6.** You spotted it and told me, which is the right instinct — but
you deleted it from the pasted output rather than from the file. That means the PR shows output
the code doesn't actually produce. Always fix the file, re-run from the top, and paste what it
really prints. The paste is evidence; editing it defeats the point. (Your Q6 answer itself is
correct.)

**The Conditions section.** It's still got the instruction text under the heading. You put the
quotes inline in the output block instead, which I actually prefer — the code and the question sit
next to each other there. Delete the leftover heading next time so it doesn't read as skipped.

---

## Fix list

1. **Q2** — build the sort from `later`, not `books`, and sort ascending. Expect 7 rows.
2. **Q3** — `>` not `>=`. Expect Fiction and History only.
3. **Q8** — `len(books_category)` without the quotes; rename `average` → `avg_pages`; make the
   function read `table`, not the global `books`.
4. **Q6** — delete the `print(loaned)` from the file.
5. Re-run the whole file from the top, confirm the output matches, and update the PR with the real
   output. Correct your Q9d answer in the PR while you're there.

Q7 and Q9b don't need touching.

---

## On the four hours

You estimated against my "about an hour" and it took two sessions of two. That's on me, not you —
Q8 alone asks you to write a function, loop it, build a DataFrame out of dictionaries, and save a
CSV. That's four new-ish things wearing one question number, and you said yourself it took the
longest. Noted for the next quiz.

The bugs in here are all the same species: the code ran, so it looked finished. None of them are
about not knowing pandas — you clearly do. They're about verifying the answer rather than
verifying that it executed. Expected row counts, re-reading the condition against the sign you
typed, and running the snippet before marking your prediction correct. That's the whole gap, and
it's a habit, not knowledge.

— David
