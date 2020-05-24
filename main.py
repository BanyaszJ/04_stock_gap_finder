import yfinance as yf

igny            = yf.Ticker("4IG.BD")
igny_history    = igny.history(period="2d")