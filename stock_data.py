import yfinance as yf

def get_data(ticker):
    ticker = yf.Ticker(ticker+".NS")
    data = ticker.history(period="1y").reset_index()
    opening_prices = data["Open"]
    closing_prices = data["Close"]
    high = data['High']
    low = data['Low']
    volume = data['Volume']
    date = data['Date']

    return {
       'open': opening_prices,
       'close': closing_prices,
       'high': high,
       'low': low,	
       'volume': volume,
       'date': date
   }


get_data("itc")