DEALS = [
    {"name": "Acadia Software",    "amount": 18500},
    {"name": "Blue Harbor Foods",  "amount": 4200},
    {"name": "Cobalt Mining Co",   "amount": 156000},
    {"name": "Delta Logistics",    "amount": 47500},
    {"name": "Echo Media Group",   "amount": 8900},
    {"name": "Foothills Energy",   "amount": 92300},
    {"name": "Glacier Insurance",  "amount": 3100},
    {"name": "Harborview Clinics", "amount": 61000},
    {"name": "Ironwood Labs",      "amount": 50000},
]

# E1
name = DEALS[5]["name"]
amount = DEALS[5]["amount"]
print(f"{name}: ${amount:,}")

# E2
amts = [18500, 4200, 156000, 47500]
first = amts[0]
last = amts[len(amts) - 1]
print(f"First Item: {first:,}, Last Item: {last:,}")

# E3
name = DEALS[2]["name"]
amount = DEALS[2]["amount"]
print(f"{name}: ${amount:,}")

# E4
third = DEALS[2]["amount"]
sixth = DEALS[5]["amount"]
total = third + sixth
print(f"Combined Total: ${total:,.2f}")

# E5
count = len(DEALS)
final = DEALS[-1]["name"]
print(f"Total Count: {count}, Name of the Final Deal: {final}")
