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
print("2. MAY AND JUNE")
may = bridge("2026-05", "closes/2026-04/subscriptions_2026-04-30.csv","closes/2026-05/subscriptions_2026-05-31.csv")
table = pd.DataFrame([may, june])                     # May first, then June
print(table.to_string(index=False))

print()
print("3. DOES EACH MONTH TIE?")
table["check"] = table["opening"] + table["new"] + table["expansion"] + table["contraction"] + table["churn"] - table["closing"]
print(table[["month", "opening", "closing", "check"]].to_string(index=False))

print()
print("4. APRIL TOO")
april = bridge("2026-04", "closes/2026-03/subscriptions_2026-03-31.csv", "closes/2026-04/subscriptions_2026-04-30.csv")
table = pd.DataFrame([april, may, june])
table["check"] = table["opening"] + table["new"] + table["expansion"] + table["contraction"] + table["churn"] - table["closing"]
print(table[["month", "opening", "new", "expansion", "contraction", "churn", "closing", "check"]].to_string(index=False))