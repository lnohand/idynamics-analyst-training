import pandas as pd

june = pd.read_csv("closes/2026-06/subscriptions_2026-06-30.csv")

print("1. LOAD AND CHECK")
print(f"Subscriptions: {len(june)}")
print(f"Total MRR: {june['mrr'].sum():,.2f}")

print()
print("2. SUBSCRIPTIONS WITH MRR OF 5,000 OR MORE")
big = june[june["mrr"] >= 5000]
big = big.sort_values("mrr", ascending=False)
print(big[["subscription_id", "plan_name", "mrr"]].to_string(index=False))
share = big["mrr"].sum() / june["mrr"].sum() * 100
print(f"Count: {len(big)}  Share of MRR: {share:.1f}%")

print()
print("3: ANNUAL VS MONTHLY")
annual = june[june["billing_cycle"] == "Annual"]
monthly = june[june["billing_cycle"] == "Monthly"]
print(f"Annual: {len(annual)} subscriptions, MRR {annual['mrr'].sum():,.2f}")
print(f"Monthly: {len(monthly)} subscriptions, MRR {monthly['mrr'].sum():,.2f}")

print()
print("4. MRR BY PLAN")
by_plan = june.groupby("plan_name", as_index = False)["mrr"].sum()
by_plan = by_plan.sort_values("mrr", ascending=False)
print(by_plan.to_string(index=False))

print(june)

print()
print("5. CUSTOMERS WITH 50 OR MORE SEATS")
by_seats = june.groupby("customer_id", as_index = False)["seats"].sum()
by_seats = by_seats[by_seats["seats"] >= 50]
print(by_seats)
by_seats = by_seats.sort_values("seats", ascending=False)

print(by_seats.to_string(index=False))
print(f"Count: {len(by_seats)}")


