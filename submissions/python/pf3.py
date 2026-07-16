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
for deal in DEALS:
    print(f"Name: {deal["name"]}, Amount: ${deal["amount"]:,}")

# E2
total = 0
for deal in DEALS:
    total += deal["amount"]
print(f"Total pipeline: ${total:,}")

# E3
big = 0
biggington = 0
for deal in DEALS:
    if deal["amount"] >= 50000:
        big += 1
        biggington += deal["amount"]
print(f"{big} deals worth ${biggington:,}")

# E4
best = DEALS[0]
for deal in DEALS:
    if deal["amount"] > best["amount"]:
        best = deal
print (f"{best["name"]} ${best['amount']:,}")

# E5
MRR = 42000
first_time = 0
for deal in range(1,7):
    MRR *= 1.04
    print(f"Month {deal}: ${MRR:,.2f}")
    if MRR > 50000 and first_time == 0:
        first_time = deal
print(f"First month to cross $50,000: {first_time}")
