import yfinance as yf
import plotly.graph_objects as go

close = yf.Ticker("^GSPC").history(period="1y")["Close"]
fig = go.Figure(go.Scatter(x=close.index, y=close.values, mode="lines", name="S&P 500"))
fig.update_layout(title="S&P 500 — 1 year")
fig.write_html("idynamics-analyst-training/submissions/python/py02_asset_classes/sp500_preview.html", include_plotlyjs="cdn")