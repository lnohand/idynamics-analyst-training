import pandas as pd
import yfinance as yf

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

SMALL = [
    {"name": "Tiny A", "amount": 1000},
    {"name": "Tiny B", "amount": 2000}
]

INDICES = {"S&P 500": 6800.00, "NASDAQ 100": 25000.00, "Dow Jones": 44000.00}

# A1 + A2
biggest = 0
for deal in DEALS:
    if deal["amount"] > 100000:
        print("Enterprise")
    elif deal["amount"]>= 50000:
        print("Mid-Market")
    else:
        print("SMB")
    if deal["amount"] >= 50000:
        biggest += 1
print(f"There are {biggest} deals worth more than $50,000")

# A3
def total_value(deals):
    total = 0
    for deal in deals:
        total += deal["amount"]
    print(total)

total_value(DEALS)
total_value(SMALL)

# A4
def biggest_deal(deals):
    biggest = deals[0]
    for deal in deals:
        if deal["amount"] > biggest["amount"]:
            biggest = deal
    print(f"Largest: {deal["name"]}: ${deal["amount"]:,}")

biggest_deal(DEALS)

# Section B

rows = [
    {"Index": "S&P 500",    "Last": 6800.00,  "1D %": 0.42},
    {"Index": "NASDAQ 100", "Last": 25000.00, "1D %": -0.15},
    {"Index": "Dow Jones",  "Last": 44000.00, "1D %": 0.08},
]

df = pd.DataFrame(rows)

df = df.sort_values("1D %", ascending=False)

print(df.to_string(index=False))

for name, last in INDICES.items():
    print(f"{name}: {last:.2f}")