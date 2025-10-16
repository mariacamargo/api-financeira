import yfinance as yf

def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.history(period="1d")

        if info.empty:
            return {"error": "Ticker não encontrado."}

        last_quote = info.tail(1).iloc[0]
        return {
            "ticker": ticker.upper(),
            "price": round(last_quote["Close"], 2),
            "open": round(last_quote["Open"], 2),
            "high": round(last_quote["High"], 2),
            "low": round(last_quote["Low"], 2),
            "volume": int(last_quote["Volume"]),
        }
    except Exception as e:
        return {"error": str(e)}
