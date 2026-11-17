import pandas as pd

may_subs = pd.read_csv("closes/2026-05/subscriptions_2026-05-31.csv")
june_subs = pd.read_csv("closes/2026-06/subscriptions_2026-06-30.csv")
june_cust = pd.read_csv("closes/2026-06/customers_2026-06-30.csv")

print("May Subs:")
print(may_subs.head())
print("June Subs:")
print(june_subs.head())
print("June Customers:")
print(june_cust.head())

# 1. The answer looks like: one row per customer, with mrr_may, mrr_june, _merge and change.
# 2. The information is in: May and June's subscription tables
# 3. Steps → tools: group may_subs and june_subs by customer_id, merge the two tables, create a change column
# 4. I'll know it's right because: I'll compare the results with the tables before the merge
print()
print("Question 1:")
may_subs = may_subs.groupby("customer_id", as_index=False)["mrr"].sum()
june_subs = june_subs.groupby("customer_id", as_index=False)["mrr"].sum()

nahoy = pd.merge(may_subs, june_subs, on="customer_id", how="outer", indicator=True, suffixes=("_may", "_june"))
nahoy[["mrr_may", "mrr_june"]] = nahoy[["mrr_may", "mrr_june"]].fillna(0)
nahoy["change"] = nahoy["mrr_june"] - nahoy["mrr_may"]
print(nahoy[["customer_id", "mrr_may", "mrr_june", "_merge", "change"]].to_string(index=False))
print(f"Customers: {nahoy["customer_id"].count()}")
print(f"Total Change: {nahoy["mrr_june"].sum() - nahoy["mrr_may"].sum()}")

# 1. The answer looks like: 4 columns indicating the amount of new, expansion, contraction, and churn change along with the amount of customers in each category
# 2. The information is in: may_subs and june_subs
# 3. Steps → tools: create the definitions for new and churn and expansion and contraction then print them
# 4. I'll know it's right because: I'll compare the results with the original may and june tables
print()
print("Question 2:")
new = nahoy[nahoy["_merge"] == "right_only"]
churn = nahoy[nahoy["_merge"] == "left_only"]
stayed = nahoy[nahoy["_merge"] == "both"]
expansion = stayed[stayed["change"] > 0]
contraction = stayed[stayed["change"] < 0]

print(f"New:         {new['change'].sum():,.2f}  customers: {len(new)}")
print(f"Expansion:   {expansion['change'].sum():,.2f}  customers: {len(expansion)}")
print(f"Contraction: {contraction['change'].sum():,.2f}  customers: {len(contraction)}")
print(f"Churn:       {churn['change'].sum():,.2f}  customers: {len(churn)}")

# 1. The answer looks like: a column named movement indicating whether a movement is new, expansion, contraction, or churn
# 2. The information is in: the may_subs and june_subs tables
# 3. Steps → tools: create a new column called movement, assign the previous variables to this column, concat the new variables, print the table
# 4. I'll know it's right because: I'll compare with the results of question 2
print()
print("Question 3:")
new = new.assign(movement="New")
expansion = expansion.assign(movement="Expansion")
contraction = contraction.assign(movement="Contraction")
churn = churn.assign(movement="Churn")

movers = pd.concat([new, expansion, contraction, churn])
movers = movers[["customer_id", "movement", "mrr_may", "mrr_june", "change"]]
print(movers.to_string(index=False))
print(f"Movers: {movers["customer_id"].count()}")
print(f"Total change: {movers["change"].sum()}")


# 1. The answer looks like: Adding the name of the companies to the table
# 2. The information is in: june_cust 
# 3. Steps → tools: merge the movers table with june_cust to get the names, order the change values by biggest first, print the table
# 4. I'll know it's right because: I'll compare with the june customer table and the movers table
print()
print("Question 4:")
pizdi = pd.merge(movers, june_cust, on="customer_id", indicator=True)
pizdi = pizdi.sort_values("change", ascending=False)
print(pizdi[["customer_id", "company_name", "industry", "movement", "change"]].to_string(index=False))
pizdi.to_csv("submissions/python/pd6_june_movers.csv", index=False)
print("Saved submissions/python/pd6_june_movers.csv")

# 1. The answer looks like: Each industry and its total change
# 2. The information is in: june_cust
# 3. Steps → tools: group by industry and change, order by biggest first, print the table
# 4. I'll know it's right because: I'll compare with the june_cust table
print()
print("Question 5:")
pizdi = pizdi.groupby("industry", as_index=False)["change"].sum()
pizdi = pizdi.sort_values("change", ascending=False)
print(pizdi.to_string(index=False))

