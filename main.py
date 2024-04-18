import ttkbootstrap as ttk
from tkinter import *
import Portfolio
import sqlite3
import matplotlib.pyplot as plt

stocks = []  # Initialize stocks as a list

root = ttk.Window(themename="superhero")
root.title("Crypto Portfolio")
root.geometry("400x400")

comboCoins = [
    'Bitcoin:BTC',
    'Ethereum:ETH',
    'Binance Coin:BNB',
    'Solana:SOL',
    'Cardano:ADA',
    'Avalanche:AVAX',
    'Terra:LUNA',
    'Polygon:MATIC',
    'Chainlink:LINK',
    'Polkadot:DOT'
]


def insertData(stock):
    """
    Insert stock data into the 'stocks' table in the database.
    """
    if not isinstance(stock, dict):
        print("Error: Stock data must be a dictionary.")
        return

    conn = sqlite3.connect('crypto.db')
    cursor = conn.cursor()
    #cursor.execute('DROP TABLE IF EXISTS stocks')  # Drop the table if it already exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS stocks
                    (name TEXT, symbol TEXT, price REAL)''')  # Create the table if it doesn't exist
    cursor.execute("INSERT INTO stocks VALUES (?, ?, ?)",
                   (stock['name'], stock['symbol'], stock['price']))  # Insert individual stock
    conn.commit()
    cursor.close()


def set_dict(nme, sym, cur):
    global stocks

    name = nme
    symbol = sym
    price = cur

    stock = {'name': name, 'symbol': symbol, 'price': price}
    stocks.append(stock)
    for stock in stocks:
        print(stock['name'], stock['symbol'], stock['price'])


def get_symbol(e):
    selected_index = crptoCombobox.current()
    selected_item = comboCoins[selected_index]
    name, symbol = selected_item.split(":")
    name = name.strip()
    symbol = symbol.strip()
    quote = Portfolio.fetch_quote(symbol)
    dataText.insert(END, f"{name}: {symbol} - {quote}\n")  # Display name, symbol, and quote in the Text widget
    insertData({'name': name, 'symbol': symbol, 'price': quote})  # Insert individual stock


crptoCombobox = ttk.Combobox(root, bootstyle="success", values=comboCoins, state="readonly")
crptoCombobox.pack(padx=10, pady=30)

dataText = ttk.Text(root, font=("Arial", 14), height=10, width=40)
dataText.pack(padx=10, pady=10)

crptoLabel = ttk.Label(root, text='Coin', bootstyle="success")
crptoLabel.pack(padx=10, pady=10)

crptoCombobox.bind("<<ComboboxSelected>>", get_symbol)


def fetch_prices():
    """
    Fetch price data from the 'stocks' table in the database.
    """
    conn = sqlite3.connect('crypto.db')
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM stocks")
    prices = cursor.fetchall()  # fetch all prices
    conn.close()
    return [price[0] for price in prices]  # Extract prices from list of tuples


# Fetch data from the database
prices_data = fetch_prices()

# Create a plot
plt.plot(prices_data)
plt.xlabel('Index')
plt.ylabel('Price')
plt.title('Cryptocurrency Prices')
plt.show()

root.mainloop()
