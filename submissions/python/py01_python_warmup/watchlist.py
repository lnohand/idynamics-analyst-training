import yfinance as yf

def get_quote(symbol):
    """Return (last_price, 1d_change_percent) for one ticker."""
    info = yf.Ticker(symbol).fast_info
    last = info["lastPrice"]
    prev = info["previousClose"]
    return last, (last - prev) / prev * 100

biggest = 0
biggest_change = 0
for symbol in ["AAPL", "MSFT", "NVDA", "AZO", "TSLA"]:
    last, change = get_quote(symbol)
    print(f"{symbol:6} ${last:>10,.2f}   {change:+.2f}%")

    
    if abs(change) > abs(biggest_change):
        biggest = symbol
        biggest_change = change

print(f"Biggest mover: {biggest} {biggest_change:+.2f}%")