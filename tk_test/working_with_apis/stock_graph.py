import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web
from tkinter import *
import requests
from tkinter import messagebox


root = Tk()
root.title("Stock Graphs")
root.iconbitmap("D:/wL/stock.ico")


times = [
    "Past day",
    "Past week",
    "Past month",
    "Past year",
    "Past 5 years",
    "Past 10 years"
]
clicked = StringVar()
clicked.set(times[0])

def get_stock_quote(ticker_symbol, api):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    return response
def get_stock_price(ticker_symbol, api):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    price = response['price'][:-3]
    return price

def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return (current - previous) / previous * 100.0
    except ZeroDivisionError:
        return 0


def find_plot():
    try:
        ticker = (tickerInput.get()).upper()
        api_key = "28bfdedfe3e746fbba30a04b89c89977"
        style.use("ggplot")
        now = dt.datetime.today()
        if clicked.get() == "Past day":
            start = dt.datetime(now.year, now.month, now.day - 1)
        elif clicked.get() == "Past week":
            start = dt.datetime(now.year, now.month, now.day - 7)
        elif clicked.get() == "Past month":
            start = dt.datetime(now.year, now.month - 1, now.day)
        elif clicked.get() == "Past year":
            start = dt.datetime(now.year - 1, now.month, now.day)
        elif clicked.get() == "Past 5 years":
            start = dt.datetime(now.year - 5, now.month, now.day)
        elif clicked.get() == "Past 10 years":
            start = dt.datetime(now.year - 10, now.month, now.day)
        end = dt.datetime(now.year, now.month, now.day)

        stock_price = get_stock_price(ticker, api_key)
        df = web.get_data_yahoo(ticker, start, end)
        df["Adj Close"].plot(label=ticker)

        output = Label(root)
        output.grid(row=2, column=1, stick=W + E + N + S)

        stockdata = get_stock_quote(ticker, api_key)
        name = stockdata['name']
        percentChange = get_change(df["Close"][-1], df["Open"][0])

        output = Label(root, text="Stock Price: " + stock_price + "\nPercent: " + str(round(percentChange, 2)) + "%", font=("Helvetica", 13))
        output.grid(row=2, column=1, stick=W + E + N + S)

        #plt.plot(stock_price, dt.datetime(now.year, now.month, now.day+1), 'ro')
        plt.suptitle(name, fontsize=20, fontweight='bold')
        plt.ylabel("Stock Price")
        plt.legend()
        plt.show()

    except:
        output = Label(root, text="That ticker doesn't exist", font=("Helvetica", 13))
        output.grid(row=2, column=1, stick=W + E + N + S)

def info():
    messagebox.showinfo("Stock Graph Info", "In this app, you can input a stock's ticker and time and it will return a graph showing the rise and fall of the stock over time. You will also get to see the stock's current price and percentage change.\n\nYou can compare stocks by adding more inputs, and click the X on the top right of the graph to refresh onto a new graph.\n\n Enjoy!")

question = Label(root, text="Input Stock Ticker:", font=("Helvetica", 15))
question.grid(row=0, column=0)
tickerInput = Entry(root, font=("Helvetica", 15))
tickerInput.grid(row=0, column=1)
lbl = Label(root, text="Lookup for:", font=("Helvetica", 15))
lbl.grid(row=1, column=0)
timeInput = OptionMenu(root, clicked, *times)
timeInput.grid(row=1, column=1, stick=W+E+N+S)
tickerButton = Button(root, text="Lookup Stock Graph", font=("Helvetica", 15), command=find_plot)
tickerButton.grid(row=2, column=2, stick=W+E+N+S)
infoButton = Button(root, text="Info", font=("Helvetica", 10), width=10, command=info)
infoButton.grid(row=0, column=2)

if __name__ == "__main__":
    root.mainloop()