<<<<<<< HEAD
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
def format_deal(deal):
    print(f"Name: {deal["name"]}, Amount: ${deal["amount"]:,}")

format_deal(DEALS[0])

# E2
def tier(amount):
    if amount >= 100000:
        return "Enterprise"
    elif amount >= 50000:
        return "Mid-Market"
    else:
        return "SMB"
    
print(tier(156000))   
print(tier(50000))   
print(tier(47500))

# E3

for deal in DEALS:
    print(f"Name: {deal["name"]}, Tier: {tier(deal["amount"])}")

# E4, This question was very hard! I liked it!

def total_value(deals):
    piz = 0
    for deal in DEALS:
        piz += deal["amount"]
    return piz
    
print(f"${total_value(DEALS):,}") 

# E5, this question was hellish.

def biggest_deal(deals):
    biggest = DEALS[0]
    for deal in DEALS:
        if deal["amount"] > biggest["amount"]:
            biggest = deal
    return biggest["name"], biggest["amount"]

name, amount = biggest_deal(DEALS)

print(f"{len(DEALS)} deals worth ${amount:,}")
print(f"Largest: {name}, Amount: ${amount:,}, Tier: {tier(amount)}")
=======
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
def format_deal(deal):
    print(f"Name: {deal["name"]}, Amount: ${deal["amount"]:,}")

format_deal(DEALS[0])

# E2
def tier(amount):
    if amount >= 100000:
        return "Enterprise"
    elif amount >= 50000:
        return "Mid-Market"
    else:
        return "SMB"
    
print(tier(156000))   
print(tier(50000))   
print(tier(47500))

# E3

for deal in DEALS:
    print(f"Name: {deal["name"]}, Tier: {tier(deal["amount"])}")

# E4, This question was very hard! I liked it!

def total_value(deals):
    piz = 0
    for deal in DEALS:
        piz += deal["amount"]
    return piz
    
print(f"${total_value(DEALS):,}") 

# E5, this question was hellish.

def biggest_deal(deals):
    biggest = DEALS[0]
    for deal in DEALS:
        if deal["amount"] > biggest["amount"]:
            biggest = deal
    return biggest["name"], biggest["amount"]

name, amount = biggest_deal(DEALS)

print(f"{len(DEALS)} deals worth ${amount:,}")
print(f"Largest: {name}, Amount: ${amount:,}, Tier: {tier(amount)}")
>>>>>>> 5510ebdefad873895ef4734e2639a268cd072a37
        