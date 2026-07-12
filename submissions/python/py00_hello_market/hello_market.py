import yfinance as yf

spx = yf.Ticker("^GSPC")
last = spx.fast_info["lastPrice"]
prev = spx.fast_info["previousClose"]
print(f"S&P 500: {last:,.2f}   1D change: {(last - prev) / prev * 100:+.2f}%")