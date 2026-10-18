import pandas as pd

def bridge(month, opening_file, closing_file):
    # PD3 Step 1: read the two lists, one row per customer
    opening = pd.read_csv(opening_file)
    closing = pd.read_csv(closing_file)
    open_cust = opening.groupby("customer_id", as_index=False)["mrr"].sum()
    close_cust = closing.groupby("customer_id", as_index=False)["mrr"].sum()
    # PD3 Step 2: side by side, no row = zero MRR, change per customer
    both = pd.merge(open_cust, close_cust, on="customer_id", how="outer",suffixes=("_open", "_close"), indicator=True)
    both = both.fillna(0)
    both["change"] = both["mrr_close"] - both["mrr_open"]
    # PD3 Step 3: split into the four movements
    new = both[both["_merge"] == "right_only"]
    churn = both[both["_merge"] == "left_only"]
    stayed = both[both["_merge"] == "both"]
    expansion = stayed[stayed["change"] > 0]
    contraction = stayed[stayed["change"] < 0]
    row = {                                     # Example 2: one row of the bridge
        "month": month,
        "opening": opening["mrr"].sum(),
        "new": new["change"].sum(),
        "expansion": expansion["change"].sum(),
        "contraction": contraction["change"].sum(),
        "churn": churn["change"].sum(),
        "closing": closing["mrr"].sum(),
    }
    return row

print("1. JUNE FROM THE FUNCTION")
june = bridge("2026-06", "closes/2026-05/subscriptions_2026-05-31.csv", "closes/2026-06/subscriptions_2026-06-30.csv")
print(pd.DataFrame([june]).to_string(index=False))

print()
print("2. EVERY MONTH")
MONTHS = [
    {"month": "2026-01", "opening": "closes/2025-12/subscriptions_2025-12-31.csv", "closing": "closes/2026-01/subscriptions_2026-01-31.csv"},
    {"month": "2026-02", "opening": "closes/2026-01/subscriptions_2026-01-31.csv", "closing": "closes/2026-02/subscriptions_2026-02-28.csv"},
    {"month": "2026-03", "opening": "closes/2026-02/subscriptions_2026-02-28.csv", "closing": "closes/2026-03/subscriptions_2026-03-31.csv"},
    {"month": "2026-04", "opening": "closes/2026-03/subscriptions_2026-03-31.csv", "closing": "closes/2026-04/subscriptions_2026-04-30.csv"},
    {"month": "2026-05", "opening": "closes/2026-04/subscriptions_2026-04-30.csv", "closing": "closes/2026-05/subscriptions_2026-05-31.csv"},
    {"month": "2026-06", "opening": "closes/2026-05/subscriptions_2026-05-31.csv", "closing": "closes/2026-06/subscriptions_2026-06-30.csv"},
]
rows = []
for m in MONTHS:
    rows.append(bridge(m["month"], m["opening"], m["closing"]))
table = pd.DataFrame(rows)
print(table.to_string(index=False))

print()
print("3. CHECKS AND RATES")
table["check"] = table["opening"] + table["new"] + table["expansion"] + table["contraction"] + table["churn"] - table["closing"]
table["grr"] = ((table["opening"] + table["contraction"] + table["churn"]) / table["opening"] * 100).round(1)
table["nrr"] = ((table["opening"] + table["expansion"] + table["contraction"] + table["churn"]) / table["opening"] * 100).round(1)
print(table[["month", "check", "grr", "nrr"]].to_string(index=False))
table.to_csv("submissions/python/pd5_h1_bridge.csv", index=False)
print("Saved submissions/python/pd5_h1_bridge.csv")

print()
print("4. FIRST HALF")
jan = bridge("2026-01", "closes/2025-12/subscriptions_2025-12-31.csv", "closes/2026-01/subscriptions_2026-01-31.csv")
table["net_change"] = table["new"].sum() + table["expansion"].sum() + table["contraction"].sum() + table["churn"].sum()
table["june_dec"] = june["closing"] - jan["opening"]
print(f"New: {table["new"].sum()}")
print(f"Expansion: {table["expansion"].sum()}")
print(f"Contraction: {table["contraction"].sum()}")
print(f"Churn: {table["churn"].sum()}")
print(f"Net Change: {table["net_change"].sum()}")
print(f"Jun minus Dec: {table["june_dec"].sum()}")