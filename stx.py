'Will track your stocks, including profit, loss, when to sell, and average taxes on the stock.'
import time
import yfinance as yf

ticker_1 = input("Ticker 1 ")
symbols = ["TSLA", "NIO", ticker_1]
result = {}
for symbol in symbols:
    data = yf.Ticker(symbol)
    today_data = data.history(period='1d')
    result[symbol] = round((today_data['Close'][0]),2)
print(result)
