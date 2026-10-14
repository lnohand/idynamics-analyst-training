import pandas as pd

may = pd.read_csv("closes/2026-05/subscriptions_2026-05-31.csv")

print("1. LOAD AND CHECK")
subs_count = may[("subscription_id")]
subs_mrr = may["mrr"].sum()
subs_count = len(subs_count)
print(f"Total Subs: {subs_count}, Total MRR: {subs_mrr:,.2f}")


print("2. SUBSCRIPTIONS WITH MRR UNDER 1000")

grouped = may.groupby(["subscription_id", "customer_id", "plan_name"],as_index=False)["mrr"].sum()

small = grouped[grouped["mrr"] < 1000]

small = small.sort_values("mrr", ascending=True)
smaller = small["mrr"].sum()
share = small["mrr"].sum() / may["mrr"].sum() * 100

print(small)
print(f"Count: {len(small)}, MRR: {smaller:,.2f}, Share:  {share:,.2f}")

print("3. SEATS BY PLAN")
group = may.groupby(["plan_name"], as_index=False)["seats"].sum()

group = group.sort_values("seats", ascending=False)
group_total = group["seats"].sum()
print(group)
print(f"Total seats: {group_total:,.2f}")

print("4. CUSTOMERS WITH MRR OF 8,000 OR MORE")

total_mrr = may.groupby(["customer_id"], as_index=False)["mrr"].sum()
big = total_mrr[total_mrr["mrr"] >= 8000]
big = big.sort_values("mrr", ascending=False)
bigge = big["mrr"].sum()
share = big["mrr"].sum() / may["mrr"].sum() * 100
print(big)
print(f"Count: {len(big)}, MRR: {bigge}, Share: {share:,.2f}")

