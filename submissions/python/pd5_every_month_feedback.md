# PD5 — Every month in one go: Feedback

**Status:** One thing to find and fix, then approved
**Reviewed by:** David Chen

## Your writing is getting better

You told me you were worried about your writing, so this comes first. Look back at PD3 and PD4: one
answer used the wrong word for the movement, the other compared with Excel when the question was
about the function. This time both answers are about exactly what was asked. That's the hard part,
and you've got it. What's left is polish: put the numbers in, and use one clear word per idea.

### One question

Right months, March and June, and the right idea. This is your clearest written answer so far: it
answers exactly the question that was asked. Two small upgrades: put the numbers in (100.3 and
100.2, so the reader doesn't have to look them up), and remember that losses include downgrades as
well as customers who leave. Model answer:

*"NRR was above 100% in March (100.3) and June (100.2). In those months the customers we already had
added more through upgrades than we lost from downgrades and cancellations, so they paid us more at
the end of the month than at the start, even before counting new customers."*

### Why pandas?

Good reasons: automation, fewer manual errors, and doing it the same way next time. To make it
sharper, use one word per idea ("consistently" appears twice) and say *how* the function and loop do
it. The strongest version: *"The function holds the steps once, and the loop runs them for every
month, so all six months are calculated the same way. Next month I add one line to `MONTHS`."*

## What you did well in the code

- **Steps 1–3 are right, line for line.** Your function runs every month from January to June, every
  `check` is 0.0, and GRR and NRR match mine. I added 1 to one customer in a copy of the December
  list and ran your script again: January moved by 1 and every check stayed 0.0. Your numbers come
  from the files.
- **Your Step 4 thinking was right.** Adding up the four movements across the six months, and taking
  June's closing minus January's opening, are exactly the two numbers I asked for. Using January's
  opening was the right call, and you didn't need November: January's opening *is* the December 31
  list, the opening file you gave `bridge` for January.

## Step 4 has an error: find it yourself

Your four movement totals are right. The last two lines, `Net change` and `Jun minus Dec`, are not.
I'm not going to tell you what's wrong: you'll learn more finding it. Work through these five in order.

**1. Is the number too big?** Before trusting a number, ask whether it could be true. Look at your
Step 2 table: what was MRR at the start of January, and at the end of June? Roughly how much did it
grow? Now compare that with your 118,566.

**2. Print the table.** Make it a habit to print after every move (each new variable, new column,
filter or merge) and look at the result before you use it in the next line. Here, add one print
right after the two lines where you make `net_change` and `june_dec`, showing those two columns next
to `month`. Look at every row. What do you notice, and what does `.sum()` then do with it?

**3. Why didn't the check catch it?** The brief said the last two lines must match, and yours did:
both say 118,566.0. So how can they match and both be wrong? Think about what the two lines have in
common in your code.

**4. Check it another way.** A check only works when the two sides can't share the same mistake.
Work out June minus December a second way that doesn't go through `table` at all. Hint: you have
the two files, `closes/2025-12/subscriptions_2025-12-31.csv` and
`closes/2026-06/subscriptions_2026-06-30.csv`. Open PD1, Step 1: it reads a file and adds up its
`mrr` column. Do that for both files, take one total from the other, and print it.

**5. Fix it.** Ask yourself about each Step 4 answer: is it **one number per month**, or **one number
for the whole half**? Your Step 3 `check` is one per month, so a column was right there. Step 4's
answers are one number each. PD1 Step 2 shows how to keep one number under a plain name:
`share = big["mrr"].sum() / june["mrr"].sum() * 100`. Change Step 4 so both lines are right, run it,
and push to the same branch: the PR updates by itself.

**In the PR description, add this section:**

~~~
## Step 4 fix
What was wrong: (1–2 sentences)
Why the "must match" check didn't catch it: (1 sentence)
How I checked it another way, and what it gave: (paste the line)
~~~

Do not touch Steps 1–3: they're right.

## How it went

I'm glad this was your favourite, and I've heard you: you want more of the work to be yours to
figure out. This Step 4 fix is the first piece of that.

— David
