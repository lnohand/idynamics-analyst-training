# Checkpoint — Where is our growth coming from?: Feedback

**Status:** Three small edits, then approved
**Reviewed by:** David Chen

## Your writing has improved a lot

Last time I asked you to put the numbers in. You did, and more: your message to Sarah gives the
answer with numbers first, then says what it means ("we continued to be reliant on New MRR... our
existing customers do not provide enough MRR"). That's how a finance message should be built:
answer, number, meaning. Your sentences are clear and each one does one job. This is the best
writing you've sent me.

Your "How it went" was honest too: you noticed you leaned on earlier PDs and didn't type much code
yourself, and you said you didn't like that. Spotting that about your own work is exactly what I
want. Reusing `bridge` was the right call here. The next assignment is about writing functions from
an empty file, so you'll get that practice.

## What you did well in the code, and what you missed

- **Every number is right**, both checks are 0, and your H1 new MRR (23,030) is different from PD5's
  monthly total (21,840): you compared December with June directly, as asked.
- **Your numbers come from the files.** I added 1 to a customer in a copy of the March list and ran
  your script again: Q2 moved, H1 didn't, and both checks stayed 0.
- **Clean reuse.** A list of periods plus your `bridge`, the same pattern as PD5, applied to a new
  question. That's how analysts build on their own work.

But you missed some requirements: the table was never saved as a CSV file, and the heading is
missing its question mark. The edits below fix both.

## Do this — 3 edits

1. **Save the CSV** as `submissions/python/ck1_growth_source.csv`, the way you did in PD5.
2. **Add the question mark to the heading:** `WHERE IS OUR GROWTH COMING FROM?`
3. **Replace the line `rows = [bridge(...) for m in periods]` with the `for` loop and `.append` you
   wrote in PD5.** That line is a *list comprehension*. It works, but we haven't covered it, and you
   said Copilot rewrote your code. Using Copilot is fine, but only keep code you can explain line by
   line. If you can't, ask me. Your PD5 loop does the same thing in three lines you know.

Same branch: the PR updates by itself. Run it and paste the new output into the PR.

**Do not touch** the bridge function, the columns, or your numbers: all ten numbers are right.

## Your message to Sarah: one thing to fix in how you compared

**H1** is right in substance. One word to sharpen: "almost exclusively" understates it. Existing
customers *shrank* by 3,269, so new customers brought in more than all of the growth: 23,030 of new
MRR against 19,761 of total growth. When one part is negative, the other part covers the whole
growth *and* the loss.

**Q2** is where the comparison went wrong. You wrote "Q2 saw a decrease in New MRR as it is now
$11,010". But 11,010 is three months of new MRR and 23,030 is six months. A shorter period always
has smaller totals, so the drop tells you nothing. Q2 is also *part of* H1: March to June sits
inside December to June.

**How to approach "does Q2 look the same?"** Two ways:

1. **Compare the story, not the size.** Which group drove the growth in each period? In both, new
   customers were positive and existing customers were negative. So yes: same story.
2. **If you want to compare amounts, compare equal periods.** Put Q2 next to Q1 (December to March):
   both three months, end to end. Your `bridge` already does this. It's one more row:
   `bridge("Q1 (Dec-Mar)", "closes/2025-12/subscriptions_2025-12-31.csv", "closes/2026-03/subscriptions_2026-03-31.csv")`.
   I ran it:

| Period | New MRR | Existing net change |
|---|---|---|
| Q1 (Dec–Mar) | 10,830 | −214 |
| Q2 (Mar–Jun) | 11,010 | −1,865 |

New MRR didn't decrease. It went **up** a little, from 10,830 to 11,010. The real change is in the
existing customers: they lost 214 in Q1 and 1,865 in Q2, almost nine times as much. That's the line
the board would want to hear about.

Model answer:

*"All of H1's growth came from new customers: they added 23,030 of MRR, while the customers we
already had in December shrank by 3,269, so MRR grew 19,761 in total. Q2 tells the same story: new
customers added 11,010 and existing customers shrank by 1,865. Comparing Q2 with Q1, new customer MRR
held steady (10,830 to 11,010), but losses from existing customers grew from 214 to 1,865, which is
the trend to watch."*

You don't need to rewrite your message: read the model answer and the Q1/Q2 table, and use the
"compare equal periods" rule next time.

— David
