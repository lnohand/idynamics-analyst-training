# Excel Assignment 06 — Solution Guide
### Instructor Use Only

---

## Verified Actuals (database — subscriptions_v2.csv + subscription_events.csv)

| Metric | Value | Source |
|--------|-------|--------|
| Opening MRR (Dec 31, 2025) | $143,069.50 | Snapshot query, 51 active subs |
| New MRR | $1,710.00 | SUB040 / CUST040 — Analytics Growth, 18 seats × $95 |
| Expansion MRR | $0.00 | No expansion events in Jan 2026 |
| Contraction MRR | $0.00 | No contraction events |
| Churned MRR | $0.00 | No cancellations |
| Net New MRR | $1,710.00 | |
| Closing MRR (Jan 31, 2026) | $144,779.50 | 52 active subs |
| Active subscriptions | 52 | |
| Active customers | 39 | |

**New customer detail:**
- CUST040 — BC Education Innovations, Vancouver BC, Education sector
- Content Marketing lead source, Account owner: Michael Rodriguez
- 1 new customer this month. Plan assumed 4 per quarter ÷ 3 = ~1.3/month.

---

## Monthly Forecast Derivation

Q1 plan ÷ 3 for each movement line. This is the correct approach for a
quarterly model with even monthly distribution assumption.

| Line | Q1 Forecast | Monthly (÷ 3) |
|------|-------------|---------------|
| Opening MRR | $143,069.50 | $143,069.50 (same — it's a starting balance) |
| + New MRR | $12,000.00 | $4,000.00 |
| + Expansion | $2,146.04 | $715.35 |
| − Churned | $2,861.39 | $953.80 |
| Net New | $11,284.65 | $3,761.55* |
| Closing MRR | $154,354.15 | $146,831.05 |

*Note: monthly net new = $4,000 + $715.35 − $953.80 = $3,761.55

**Monthly P&L:**

| Line | Q1 Forecast | Monthly |
|------|-------------|---------|
| Revenue (closing × 1) | n/a | $146,831.05 |
| Gross Profit (70%) | n/a | $102,781.74 |
| S&M | $90,000 | $30,000.00 |
| R&D + G&A | $132,000 | $44,000.00 |
| Total OpEx | $222,000 | $74,000.00 |
| EBITDA | n/a | $28,781.74 |
| EBITDA Margin | n/a | 19.6% |

---

## Full Variance Table

### MRR Waterfall

| Line | Actual | Forecast | $ Var | % Var | F/U |
|------|--------|----------|-------|-------|-----|
| Opening MRR | $143,069.50 | $143,069.50 | $0 | 0.0% | — |
| + New MRR | $1,710.00 | $4,000.00 | ($2,290.00) | (57.3%) | U |
| + Expansion | $0.00 | $715.35 | ($715.35) | (100.0%) | U |
| − Contraction | $0.00 | $0.00 | $0 | n/a | — |
| − Churned | $0.00 | $953.80 | $953.80 | 100.0% | F |
| = Net New | $1,710.00 | $3,761.55 | ($2,051.55) | (54.5%) | U |
| Closing MRR | $144,779.50 | $146,831.05 | ($2,051.55) | (1.4%) | U |
| Closing ARR | $1,737,354.00 | $1,761,972.60 | ($24,618.60) | (1.4%) | U |

### P&L

| Line | Actual | Forecast | $ Var | % Var | F/U |
|------|--------|----------|-------|-------|-----|
| Revenue | $144,779.50 | $146,831.05 | ($2,051.55) | (1.4%) | U |
| COGS | ($43,433.85) | ($44,049.32) | $615.47 | (1.4%) | F |
| Gross Profit | $101,345.65 | $102,781.74 | ($1,436.09) | (1.4%) | U |
| Gross Margin % | 70.0% | 70.0% | 0.0 pp | — | — |
| S&M | ($30,000.00) | ($30,000.00) | $0 | 0.0% | — |
| R&D | — | — | — | — | — |
| G&A | — | — | — | — | — |
| Total OpEx | ($74,000.00) | ($74,000.00) | $0 | 0.0% | — |
| EBITDA | $27,345.65 | $28,781.74 | ($1,436.09) | (5.0%) | U |
| EBITDA Margin % | 18.9% | 19.6% | (0.7 pp) | — | U |

*R&D and G&A line items: Michael should pull the Q1 OpEx split from his
Assumptions tab. The total is $74K/mo; the individual line breakdown
depends on what his assumptions tab shows. Accept any split that sums
to $74K.*

---

## Variance Sign Convention

Michael will have to decide how to handle signs. The correct approach:

- **Revenue / profit rows:** Actual − Forecast. Positive = favorable.
- **Cost / churn rows:** Forecast − Actual (or flip sign). A cost
  that came in lower than forecast is favorable. A churn that came
  in at zero vs $954 forecast is favorable.
- Use conditional formatting or (parentheses) to mark unfavorable
  variances in red/pink.

**Red flag:** If his churned variance shows as unfavorable when actual
churn = $0, his sign is backwards. Push back on this — in real FP&A,
getting the favorable/unfavorable direction right is non-negotiable.

---

## Expected Management Commentary

Grade on specificity and audience awareness, not exact wording.

**Good commentary:**

> January closed at $144,780 MRR, $2,052 (1.4%) below plan. The
> shortfall was driven by new customer volume — one customer signed
> versus the plan's ~1.3/month assumption, and that customer's MRR
> ($1,710) came in below the $3,000/customer planning rate. No
> expansion activity was recorded. Partially offsetting, there were
> no cancellations in the month, adding a $954 favorable churn
> variance. EBITDA of $27,346 missed plan by $1,436, driven entirely
> by the gross profit shortfall; operating expenses were in line.
> At current run rate, Q1 is tracking to close approximately $6,000
> below plan — a gap that a strong February could recover.

**What makes it good:**
- Names the dollar and percent miss up front
- Isolates each movement driver
- Calls out both the unfavorable (new MRR) and favorable (churn) lines
- Connects to the Q1 run rate implication
- No vague language ("slightly below", "mixed results")

**Red flags:**
- "January was slightly below plan" → no specifics → send back
- Mentions revenue but not the driver → incomplete
- Favorable churn not mentioned → missed a teaching moment
- Wall of prose with no structure → communication skill issue

---

## Error Patterns

| Error | Symptom | Cause |
|-------|---------|-------|
| Closing MRR = $146,831 (not $144,780) | Zero variance on closing | Copied forecast into actual column |
| Monthly forecast = Q1 forecast (no ÷3) | Variance on opening MRR | Forgot to convert quarterly → monthly |
| Churned variance shows unfavorable | Sign backwards on churn line | Actual $0 < forecast $954 = correct sign is favorable |
| Expansion = $715 actual | Copied forecast | No expansion events occurred in Jan |
| No commentary, or commentary too vague | — | Coach on communication |
| Margin % variance shows % of % | e.g. 70.0% / 70.0% − 1 = 0 | Should be pp arithmetic: 70.0% − 70.0% = 0.0 pp |
| Revenue uses opening × 1 | ~$1,710 too low | Should use closing MRR per the forecast convention |

---

## Teaching Points

**1. The monthly derivation step is where most analysts trip.** They
have a quarterly model and need monthly actuals, so they compare the
wrong things. Michael needs to internalize: the forecast baseline must
match the actual period being measured. Q1 ÷ 3 is the right method
here because the model assumed even monthly distribution.

**2. Sign convention matters.** In variance analysis, "favorable" and
"unfavorable" are defined by impact on profit. A $954 churn miss
(actual < forecast) is favorable because it adds to MRR. Getting this
backwards signals the analyst doesn't understand what they're measuring.

**3. The EBITDA miss is small but real.** $1,436 is not a crisis.
The right coaching question: "What do you need to see in February and
March to still hit Q1 EBITDA?" That's forward-looking variance thinking.

**4. One new customer, below-plan MRR.** Both dimensions missed:
count (1 vs 1.3) and MRR per customer ($1,710 vs $3,000). Neither is
alarming in isolation for a single month, but both should be named
explicitly. The $3,000 planning assumption was a management target —
if customers are systematically coming in smaller, that's a signal.

**5. This is the first time Michael sees a blank month.** No expansion,
no churn. For a real company, January often starts slow (contracts
closing in Q4 land in January, churn often happens at renewal dates
in later months). He should comment on whether this looks unusual,
not just report the zeros.

---

## Recurring Assignment Note

This is the first instance of a **recurring monthly task**. After
grading, tell Michael:

> "This is now your job every month. February 28 closes and you have
> this workbook open. You add February actuals the same way. By April
> you'll have Q1 actual vs Q1 forecast and we can roll the variance
> forward. The model doesn't change — your actuals tab grows one
> column per month."

The assignment framework should feel like a real FP&A workflow, not a
one-time exercise.

---

*Solution Guide — Instructor Use Only*
*Excel Assignment 06 — Actual vs Forecast: January 2026*
*April 2026*
