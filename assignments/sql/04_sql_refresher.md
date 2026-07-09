# SQL Assignment: Fundamentals Refresher
### Idynamics Finance Analyst Training Program

---

> **From:** David Chen, VP Finance
> **To:** Michael
> **Subject:** Quick SQL warm-up before the next data pull
>
> Hey Michael — it's been a while since you were in the database, so
> before the next MRR pull I want you to knock the rust off with five
> short queries. We start easy — a couple of single-table queries to warm
> up — then build into joins, which is the muscle I most want you to
> stretch again. No window functions, no CASE WHEN math here; just the
> fundamentals done cleanly.
>
> Same database as always. Validate every answer against the self-check
> values before you submit — if a number doesn't match, fix the query,
> don't explain it away.
>
> — David

---

## Setup

- **Database:** PostgreSQL — the same one you used for the MRR Snapshot work.
- **Tables you'll need:** `customers`, `subscriptions`, `subscription_events`
- Put each answer in its own `.sql` file (or one file with clear
  `-- Question N` headers), and paste your self-check results in the PR.

**Schema reminder:**

| Table | Key columns |
|---|---|
| `customers` | `customer_id`, `company_name`, `account_owner`, `region` |
| `subscriptions` | `subscription_id`, `customer_id`, `plan_name`, `billing_cycle` (`'Monthly'`/`'Annual'`), `seats`, `price_per_seat`, `discount_percent`, `status` (`'active'`/`'cancelled'`), `start_date`, `cancelled_date` |
| `subscription_events` | `event_id`, `subscription_id`, `customer_id`, `event_date`, `event_type` |

The join key between `subscriptions`/`subscription_events` and `customers`
is always `customer_id`.

---

## Question 1 — Warm-up: SELECT + WHERE (single table)

**Business context:** Start simple — pull the current active book.

**Task:** Return every **active** subscription.

- **Columns:** `subscription_id`, `plan_name`, `billing_cycle`, `seats`
- **Filter:** `status = 'active'`
- **Sort:** `subscription_id` ascending

**Self-check:** **51 rows.** Every row's status is active (none cancelled).

---

## Question 2 — Warm-up: COUNT + GROUP BY (single table)

**Business context:** A one-line health check — how many subscriptions are
active vs cancelled.

**Task:** Count subscriptions grouped by `status`.

- **Columns:** `status`, `subscription_count`
- **Sort:** `status` ascending

**Self-check:**

| status | subscription_count |
|---|---|
| active | **51** |
| cancelled | **11** |

Total should be **62** subscriptions.

---

## Question 3 — Your first join: subscriptions → customers

**Business context:** The subscription table doesn't have company names or
regions — those live in `customers`. To report on the business you almost
always have to join these two together. This is the pattern you'll reuse
constantly.

**Task:** List every **active** subscription with its customer details.

- **Columns:** `subscription_id`, `company_name`, `region`, `plan_name`
- **Join:** `subscriptions` INNER JOIN `customers` ON `customer_id`
- **Filter:** `status = 'active'`
- **Sort:** `company_name` ascending

**Self-check:** **51 rows** (same as Q1 — the join adds columns, not rows).
The `region` column shows only these 3 values: Eastern Canada,
Western Canada, Central Canada.

> If you get **more** than 51 rows, your join condition is wrong (a missing
> or incorrect `ON` clause multiplies rows). If you get **fewer**, you may
> have written an INNER JOIN where a customer record is missing — check
> your join key.

---

## Question 4 — Join + GROUP BY: active subscriptions by region

**Business context:** Sales leadership wants to know where our active book
of business sits geographically.

**Task:** For **active** subscriptions only, count how many there are in
each `region`. Same join as Q3, but now aggregate.

- **Columns:** `region`, `active_subscriptions`
- **Join:** `subscriptions` INNER JOIN `customers` ON `customer_id`
- **Filter:** `status = 'active'`
- **Sort:** `active_subscriptions` descending

**Self-check:** **3 rows** (one per region). The three counts must **sum
to 51** (all active subscriptions accounted for).

---

## Question 5 — Join into the events table

**Business context:** The event log (`subscription_events`) records every
change to a subscription. It has a `customer_id` but no region — so to see
activity by region, you join it to `customers`, exactly like you did with
subscriptions.

**Task:** Count how many events have been recorded in each `region`.

- **Columns:** `region`, `event_count`
- **Join:** `subscription_events` INNER JOIN `customers` ON `customer_id`
- **Sort:** `event_count` descending

**Self-check:** **3 rows** (one per region). The counts must **sum to 97**
(the total number of rows in `subscription_events`).

> Sanity check: run `SELECT COUNT(*) FROM subscription_events;` on its own.
> If your region counts don't add up to that number, your join is dropping
> or duplicating rows.

---

## Before you submit

- Run each query and confirm it matches the self-check above.
- Open a PR with your `.sql` file(s) and paste the self-check results as a
  PR comment.
- If anything doesn't reconcile, say so in the PR — don't hide a mismatch.
