from tkinter import *
import requests
import time

root = Tk()
root.title("Stock Price")


def get_stock_price(ticker_symbol, api):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    price = response['price'][:-3]
    return price


def get_stock_quote(ticker_symbol, api):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    return response


# exchange = stockdata['exchange']
# currency = stockdata['currency']
# open_price = stockdata['open']
# high_price = stockdata['high']
# low_price = stockdata['low']
# close_price = stockdata['close']
# volume = stockdata['volume']
# name = stockdata['name']

def find():
    try:
        ticker = (tickerInput.get()).upper()
        api_key = "28bfdedfe3e746fbba30a04b89c89977"
        stockdata = get_stock_quote(ticker, api_key)
        stock_price = get_stock_price(ticker, api_key)
        name = stockdata['name']
        output = Label(root, text=name + "'s stock price is " + stock_price, font=("Helvetica", 15))
        output.grid(row=1, column=1, columnspan=2, stick=W + E + N + S)
    except KeyError:
        output = Label(root, text="That ticker doesn't exist", font=("Helvetica", 15))
        output.grid(row=1, column=1, columnspan=2, stick=W + E + N + S)

question = Label(root, text="Input Stock Ticker:", font=("Helvetica", 15))
question.grid(row=0, column=0)
tickerInput = Entry(root, font=("Helvetica", 15))
tickerInput.grid(row=0, column=1, stick=W+E+N+S)
tickerButton = Button(root, text="Lookup Stock Price", font=("Helvetica", 15), command=find)
tickerButton.grid(row=0, column=2, stick=W+E+N+S)


root.mainloop()