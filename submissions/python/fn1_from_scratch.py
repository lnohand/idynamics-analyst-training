import pandas as pd

DEC = "closes/2025-12/subscriptions_2025-12-31.csv"
MAR = "closes/2026-03/subscriptions_2026-03-31.csv"
JUN = "closes/2026-06/subscriptions_2026-06-30.csv"

# Step 1
# 1. The answer looks like: a count of the amount of customers
# 2. The information is in: the December and June CSV files, the customer_id column
# 3. What happens to the data: make one row per customer by grouping → count the rows.
# 4. I'll know it's right because: the count will be less than len(june)
# 5. What changes next time (my inputs): the month will be different

def customer_count(month):
    m = pd.read_csv(month)
    m = m.groupby(m["customer_id"])
    l = len(m)
    return l

print("1. CUSTOMERS ON THE LIST")
print(f"December: {customer_count(DEC)}")
print(f"June: {customer_count(JUN)}")

# Step 2
# 1. The answer looks like: a list of customers with a MRR greater than 8000 in June. 
# 2. The information is in: the December and June CSV files, particularly in the MRR column grouped by customer_id
# 3. What happens to the data: The MRR column is grouped by customer_id then summed then checked to see if it is greater than 8000 and 9500. 
# 4. I'll know it's right because: The MRR's of each individual customer will be above the amount threshold of 8000 / 9500.
# 5. What changes next time (my inputs): the month and amount inputs.

def big_customers(month, amount):
    m = pd.read_csv(month)
    totals = m.groupby("customer_id")["mrr"].sum()
    above = totals[totals > amount]
    above = above.sort_values(ascending=False)
    print(f"{amount} or more: {above}")

print()
print("2. BIG CUSTOMERS IN JUNE")
big_customers(JUN, 8000)
big_customers(JUN, 9500)

# Step 3
# 1. The answer looks like: a number
# 2. The information is in: the June and December CSV files
# 3. What happens to the data: The MRR values between the ending month and the starting month are compared and the growth is calculated by subtracting the sum of the ending mrr minus the sum of the starting mrr
# 4. I'll know it's right because: I can check closing minus starting
# 5. What changes next time (my inputs): the starting and ending month

def growth(start, end):
    end = pd.read_csv(end)
    start = pd.read_csv(start)
    gr = end["mrr"].sum() - start["mrr"].sum()
    return gr

print()
print("3. GROWTH")
print(f"H1 (Dec-Jun): {growth(DEC, JUN)}")
print(f"Q2 (Mar-Jun): {growth(MAR, JUN)}")

# Step 4
# 1. The answer looks like: two numbers indicating the new mrr generated from the ending to the starting period 
# 2. The information is in: the MRR column of the starting and ending month csv files
# 3. What happens to the data: the mrr which is classified as new (only exists in the ending file and not the starting file) is summed and displayed 
# 4. I'll know it's right because: I'm not sure
# 5. What changes next time (my inputs): The months will change

def new_mrr(starting, ending):
    start = pd.read_csv(starting)
    end = pd.read_csv(ending)
    start_mrr = start.groupby("customer_id")["mrr"].sum()
    ending_mrr = end.groupby("customer_id")["mrr"].sum()
    both = pd.merge(start_mrr, ending_mrr, on="mrr", how="outer", indicator=True)
    new = both[both["_merge"] == "right_only"]
    new = new["mrr"].sum()
    return new

print()
print("4. NEW MRR")
print(f"H1 (Dec-Jun): {new_mrr(DEC, JUN)}")
print(f"Q2 (Mar-Jun): {new_mrr(MAR, JUN)}") 