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
print(DEALS[2]["amount"] >= 100000)

# E2
if DEALS[5]["amount"] > 50000:
    print ("Big")
else:
    print ("Small")

# E3
amount = DEALS[3]["amount"]
if amount >= 100000:
    print("Enterprise")
elif amount >= 50000:
    print("Mid-Market")
else:
    print("SMB")

# E4
new_amount = DEALS[7]["amount"]
if new_amount >= 50000 and new_amount < 100000:
    print("Mid-Market")
else:
    print("not Mid-Market")

# E5
newer_amount = DEALS[6]["amount"]
if newer_amount >= 100000 or newer_amount < 5000:
    print("Notable")
else:
    print("Ordinary")
