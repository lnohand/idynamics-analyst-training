import pandas as pd

print("1. MRR PER CUSTOMER")

may = pd.read_csv("closes/2026-05/subscriptions_2026-05-31.csv")
june = pd.read_csv("closes/2026-06/subscriptions_2026-06-30.csv")

may_cust = may.groupby("customer_id", as_index=False)["mrr"].sum()
june_cust = june.groupby("customer_id", as_index=False)["mrr"].sum()

print(f"Total Customers in May: {len(may_cust)}, Total MRR: {may_cust["mrr"].sum():,.2f}")
print(f"Total Customers in June: {len(june_cust)}, Total MRR: {june_cust["mrr"].sum():,.2f}")

print("2. MAY AND JUNE SIDE BY SIDE")
both = pd.merge(may_cust, june_cust, on="customer_id", how="outer", suffixes=("_may", "_june"), indicator=True)
both = both.fillna(0)
both["change"] = both["mrr_june"] - both["mrr_may"]
changed = both[both["change"] != 0]
print(changed.to_string(index=False))
print(f"Rows: {len(both)}  May MRR: {both['mrr_may'].sum():,.2f}  June MRR: {both['mrr_june'].sum():,.2f}")

print()
print("3. MOVEMENTS")
new = both[both["_merge"] == "right_only"]
churn = both[both["_merge"] == "left_only"]
stayed = both[both["_merge"] == "both"]
expansion = stayed[stayed["change"] > 0]
contraction = stayed[stayed["change"] < 0]
print(f"New:         {new['change'].sum():,.2f}  customers: {len(new)}")
print(f"Expansion:   {expansion['change'].sum():,.2f}  customers: {len(expansion)}")
print(f"Contraction: {contraction['change'].sum():,.2f}  customers: {len(contraction)}")
print(f"Churn:       {churn['change'].sum():,.2f}  customers: {len(churn)}")

print()
print("4. DOES IT TIE")
print(f"Opening (May): {may_cust["mrr"].sum():,.2f}")
print(f"Rebuilt Closing: {new["change"].sum()+expansion["change"].sum()+churn["change"].sum()+contraction["change"].sum():,.2f}")
print(f"Closing (June): {june_cust["mrr"].sum():,.2f}")
print(f"Difference: {may_cust["mrr"].sum() + new["change"].sum()+expansion["change"].sum()+churn["change"].sum()+contraction["change"].sum()-june_cust["mrr"].sum():,.2f}")

