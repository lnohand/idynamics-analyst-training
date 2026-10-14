import pandas as pd

june = pd.read_csv("closes/2026-06/subscriptions_2026-06-30.csv")

print("1. MONTHLY SUBSCRIPTIONS, STEP BY STEP")
cycle = june["billing_cycle"]
print(cycle.head())                # NEW: .head() prints only the first 5 rows
is_monthly = cycle == "Monthly"
print(is_monthly.head())
monthly = june[is_monthly]
print(monthly[["subscription_id", "billing_cycle", "mrr"]].head())
print(f"Steps:    {len(monthly)} subscriptions")
monthly_one_line = june[june["billing_cycle"] == "Monthly"]
print(f"One line: {len(monthly_one_line)} subscriptions")

print()
print("2. PLANS WITH 30,000 MRR OR MORE, STEP BY STEP")
grouped = june.groupby("plan_name", as_index=False)
print(grouped)
by_plan = grouped["mrr"].sum()
print(by_plan)
is_large = by_plan["mrr"] >= 30000
print(is_large)
large_plans = by_plan[is_large]
print(large_plans)
large_one_line = by_plan[by_plan["mrr"] >= 30000]
print(f"Steps: {len(large_plans)} plans  One line: {len(large_one_line)} plans")

print()
print("3. FIXED LINES")
print(len(june))
print(f"{june['mrr'].sum():,.2f}")

#1. This line sets the annual variable as the values in the June dataframe that have a billing cycle of annual
#2. This line sets the share variable as the sum of the biggest mrr's in the june dataframe divided by the sum of all the biggest mrr's in the june dataframe multiplied by 100.
#3. This line sets by_seats to be the total seats of each customer_id in the june dataframe.
#4. This line prints the total mrr of the june dataframe and has a 2 decimal format with commas. 