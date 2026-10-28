# Quiz 1 — pandas quick-fire: Feedback

**Status:** One fix needed, then merge
**Reviewed by:** David Chen

Michael, I pulled your branch and ran `quiz1_quickfire.py` against the data, then checked every
answer against my own solution. Q1, Q2, Q4, Q5, Q6, Q7 and Q8 are all correct, and so are
Q9b and Q9c. Good quiz.

## The one fix: the file you committed doesn't run

The last line of the file ends with stray keystrokes after the closing bracket:

```
...should be added. ")   qwerASDDFGHZ
```

Python reads the whole file before it runs anything, so it stops with a `SyntaxError` and
**no question prints at all**. The output in your PR came from an earlier copy. Delete those
characters, run the file from the top, check that the output matches what you pasted, and push.
I'll merge after that.

## Q8: your function is right

We went back and forth on this one, and you were right. The brief asks `genre_stats` to return
**one row as a dictionary**. Yours does exactly that: a single dictionary with three keys.

```python
return {
    "genre": genre,
    "movies": len(genre_movies),
    "minutes": genre_movies["minutes"].sum(),
}
```

Spreading it over several lines is only layout. It's still one value coming back, the same as
building `row = {...}` and then `return row`. The loop calls the function three times, which
gives the three rows of the table. You stuck to your answer and it held up. Good.

## Q3: one table missing

The question has two parts: the full minutes-per-genre table, **then** the genres with at least
400. You printed only the second. The first one should also show Thriller (372) and Animation
(370). The filter itself was right.

## Q9a: what `None` means

Your reasoning was right: the function has no `return`, so nothing comes back. The part to add
is what Python *prints* when nothing comes back. It prints the word `None`. So the full output is:

```
2206
None
```

The first line comes from the `print` inside the function. The second comes from
`print(result)`, and `result` is `None` because the function didn't return anything. Whenever you
see a stray `None` in your output, it's almost always this: a function that printed instead of
returning.

— David
