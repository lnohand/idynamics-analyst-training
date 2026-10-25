# My plan
# 1. The numbers will explain where the growth is coming from and thus, answer the board's question.
# 2. PD5's months list can be used to segregate H1 and Q2 then the additional rows can be used. the bridge function can also be borrowed from pd4.
# 3. Step 1 is to port the bridge function. Step 2 is to port the old months function from PD5 and rework it to fit the needs of the assignment. Step 3 is to add the Check, New_MRR, and Existing_Net_Change columns to the table.
# 4. I'll know it's correct when I compare the numbers from the actual spreadsheet to the numbers calculated by the script. PD5 can also be referenced and checked. 

import pandas as pd

def bridge(period, opening_file, closing_file):
    """Build a bridge row for a single period."""
    opening = pd.read_csv(opening_file)
    closing = pd.read_csv(closing_file)

    open_cust = opening.groupby("customer_id", as_index=False)["mrr"].sum()
    close_cust = closing.groupby("customer_id", as_index=False)["mrr"].sum()

    both = pd.merge(
        open_cust,
        close_cust,
        on="customer_id",
        how="outer",
        suffixes=("_open", "_close"),
        indicator=True,
    )
    both = both.fillna(0)
    both["change"] = both["mrr_close"] - both["mrr_open"]

    new = both[both["_merge"] == "right_only"]
    churn = both[both["_merge"] == "left_only"]
    stayed = both[both["_merge"] == "both"]
    expansion = stayed[stayed["change"] > 0]
    contraction = stayed[stayed["change"] < 0]

    row = {
        "period": period,
        "opening": opening["mrr"].sum(),
        "new": new["change"].sum(),
        "expansion": expansion["change"].sum(),
        "contraction": contraction["change"].sum(),
        "churn": churn["change"].sum(),
        "closing": closing["mrr"].sum(),
    }
    return row

periods = [
        {"period": "H1 (Dec-Jun)", "opening": "closes/2025-12/subscriptions_2025-12-31.csv", "closing": "closes/2026-06/subscriptions_2026-06-30.csv",},
        {"period": "Q2 (Mar-Jun)","opening": "closes/2026-03/subscriptions_2026-03-31.csv","closing": "closes/2026-06/subscriptions_2026-06-30.csv",}]

for m in MONTHS:
    rows.append(bridge(m["month"], m["opening"], m["closing"]))
table = pd.DataFrame(rows)

table["check"] = (table["opening"] + table["new"] + table["expansion"] + table["contraction"]+ table["churn"]- table["closing"])
table["new_mrr"] = table["new"]
table["existing_net_change"] = table["expansion"] + table["contraction"] + table["churn"]
table.to_csv("submissions/python/ck1_growth_source.csv", index=False)
print("Saved submissions/python/ck1_growth_source.csv")

summary_columns = ["period","opening","new_mrr","existing_net_change","closing","check"]
print("WHERE IS OUR GROWTH COMING FROM?")
print(table[summary_columns].to_string(index=False))
