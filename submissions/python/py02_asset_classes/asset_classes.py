import pandas as pd
import yfinance as yf

INDICES = {
    "S&P 500": "^GSPC",
    "NASDAQ 100": "^NDX",
    "Dow Jones": "^DJI",
    "Russell 2000": "^RUT",
    "CBOE VIX": "^VIX"
}


def get_quote(symbol):
    ticker = yf.Ticker(symbol)

    last = ticker.fast_info["lastPrice"]
    previous_close = ticker.fast_info["previousClose"]

    change = last - previous_close
    percent = (change / previous_close) * 100

    return last, change, percent


rows = []

for name, symbol in INDICES.items():
    last, change, percent = get_quote(symbol)

    rows.append({
        "Index": name,
        "Last": round(last, 2),
        "1D Change": round(change, 2),
        "1D %": round(percent, 2)
    })

df = pd.DataFrame(rows)

df = df.sort_values("1D %", ascending=False)

print(df.to_string(index=False))

def color_sign(v):
    return "color: green" if v >= 0 else "color: red"

styled = (df.style
          .map(color_sign, subset=["1D Change", "1D %"])
          .format({"Last": "{:,.2f}", "1D Change": "{:+,.2f}", "1D %": "{:+.2f}%"})
          .hide(axis="index"))

with open("idynamics-analyst-training/submissions/python/py02_asset_classes/asset_classes.html", "w") as f: 
    f.write(styled.to_html())