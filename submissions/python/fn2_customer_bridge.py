import pandas as pd

DEC = "closes/2025-12/subscriptions_2025-12-31.csv"
JUN = "closes/2026-06/subscriptions_2026-06-30.csv"

subs = pd.read_csv(JUN)
print(subs.head().to_string(index=False))       # the first 5 rows

ids = subs[["customer_id"]]          # keep only the customer_id column (a table with one column)
print(len(ids))                      # how many rows: one per subscription
customers = ids.drop_duplicates()    # remove the repeated customer_ids, keep the first of each
print(len(customers))                # how many rows now: one per customer

# Step 1
# 1. The answer looks like: a table with one column, customer_id, one row per customer.
# 2. The information is in: one month-end list.
# 3. Steps → tools: read the file → keep the customer_id column → remove the repeats (duplicates) → return it.
# 4. I'll know it's right because: December has 38 customers and June 45 (my FN1 Step 1 output).
# 5. What changes next time (my inputs): the file.
def list_customers(file):
    subs = pd.read_csv(file)
    customers = subs[["customer_id"]].drop_duplicates()
    return customers

print("1. CUSTOMER LISTS")
jun = list_customers(JUN)
print(jun.head().to_string(index=False))
dec = list_customers(DEC)
print(f"December: {len(dec)} customers")
print(f"June: {len(jun)} customers")

# Step 2
# 1. The answer looks like: one table, one row per customer from either list, with customer_id and a column that shows whether the customer_id was present in only Dec (left_only), only June (right_only), or both.
# 2. The information is in: the opening and the closing month-end lists.
# 3. Steps → tools: a customer list for each (call list_customer, twice) → both in one table, with labels (month).
# 4. I'll know it's right because: we know there are 9 new customers and 2 churned customers
# 5. What changes next time (my inputs): the file

def combine_lists(opening, closing):
    opening = list_customers(opening)
    closing = list_customers(closing)
    both = pd.merge(opening, closing, how="outer", on="customer_id", indicator=True)
    return both

print()
print("2. BOTH LISTS IN ONE TABLE")
h1 = combine_lists(DEC, JUN)                     # December to June
print(h1.head().to_string(index=False))          # the first 5 rows of the table it gives back


# Step 3
# 1. The answer looks like: one row: period, opening, closing, new, churned (customer counts), check.
# 2. The information is in: the two month-end lists, through my functions list_customers and combine_lists.
# 3. Steps → tools: count each list (call list_customers, then len) → both lists in one table (call combine_lists)
#    → count the new and the churned rows (filter on customer_id, then len) → a row → return it.
# 4. I'll know it's right because: ____
# 5. What changes next time (my inputs): the file

def customer_bridge(period, opening_file, closing_file):
    opening = len(list_customers(opening_file))
    closing = len(list_customers(closing_file))
    both = combine_lists(opening_file, closing_file)
    new = len(both[both["_merge"] == "right_only"])
    churned = len(both[both["_merge"] == "left_only"])

    row = {
    "period" : period,
    "opening": opening,
    "new": new,
    "churned": churned,
    "closing": closing,
    "check": opening + new - churned - closing,
    }
    return row

h1_bridge = customer_bridge("H1 Dec-Jun", DEC, JUN)
print()
print("3. H1 CUSTOMER BRIDGE")
print(pd.DataFrame([h1_bridge]).to_string(index=False))