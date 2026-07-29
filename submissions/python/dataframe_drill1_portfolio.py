import pandas as pd

rows = [
    {"Ticker": "AAPL", "Sector": "Tech",   "Price": 180.50, "Shares": 50},
    {"Ticker": "MSFT", "Sector": "Tech",   "Price": 420.00, "Shares": 30},
    {"Ticker": "TSLA", "Sector": "Auto",   "Price": 210.00, "Shares": 40},
    {"Ticker": "XOM",  "Sector": "Energy", "Price": 115.20, "Shares": 100},
]

holdings = [
    {"Ticker": "AAPL", "Sector": "Tech", "Price": 180.50, "Shares": 50},
    {"Ticker": "MSFT", "Sector": "Tech", "Price": 420.00, "Shares": 30},
    {"Ticker": "NVDA", "Sector": "Tech",                  "Shares": 10},  # no Price
]
print(pd.DataFrame(holdings).to_string(index=False))
df = pd.DataFrame(rows)
print(df[df["Sector"] == "Tech"].to_string(index=False))

# q1: Each dict is a row in the table and the keys become the name of the columns.

# q2
print(df["Shares"])

# q3
# print(df.sort_values("Shares", ascending=False).to_string(index=False))

# q4
print(df[df["Sector"] == "Energy"].to_string(index=False))

# q5: A price of NaN indicates that we do not have the price on record, it does not mean that the stock has a price of $0.

# q6
HOLDINGS = [{"Ticker": "AAPL", "Shares": 50}, 
            {"Ticker": "MSFT", "Shares": 30},
]
print(pd.DataFrame(HOLDINGS).to_string(index=False))

# q7
row = {"Ticker": "AAPL", "Shares": 50}
df = print(pd.DataFrame([row]).to_string(index=False))