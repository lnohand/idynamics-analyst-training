import pandas as pd

POSITIONS = [
    {"Ticker": "AAPL", "Sector": "Tech",    "Shares": 120, "Cost": 145.00, "Price": 180.50},
    {"Ticker": "MSFT", "Sector": "Tech",    "Shares":  40, "Cost": 390.00, "Price": 420.00},
    {"Ticker": "TSLA", "Sector": "Auto",    "Shares":  60, "Cost": 250.00, "Price": 210.00},
    {"Ticker": "XOM",  "Sector": "Energy",  "Shares": 200, "Cost":  98.40, "Price": 115.20},
    {"Ticker": "JNJ",  "Sector": "Health",  "Shares":  75, "Cost": 160.00, "Price": 152.75},
    {"Ticker": "PG",   "Sector": "Staples", "Shares":  90, "Cost": 155.00, "Price": 155.00},
]
book = pd.DataFrame(POSITIONS)

# q1: When Price * Shares is written, it performs the multiplication element by element across each column, making a for loop redundant.

# q2
book["Market_Value"] = book["Price"] * book["Shares"]
print(book.to_string(index=False))

# q3
print(book["Market_Value"].sum())

# q4
book["Weight_%"] = (book["Market_Value"] / book["Market_Value"].sum() * 100).round(2)
print(book.to_string(index=False))

# q5
book["Gain_$"] = (book["Price"] - book["Cost"]) * book["Shares"]
print(book.sort_values("Gain_$", ascending=False).to_string(index=False))

# q6
print(book[book["Gain_$"] < 0].to_string(index=False))

# q7: When you write "for row in book", you iterate over the names of the columns which is why the error mentions that you must use int values and not str.
print(book["Gain_$"].sum())