# Portfolio.py
from prettytable import PrettyTable
import sqlite3
import requests

def fetch_quote(symbol):
    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}&convert=USD'
    headers = {'X-CMC_PRO_API_KEY': 'cb88e221-51ee-4694-9f62-c12319dfefea'}

    response = requests.get(url, headers=headers)
    data = response.json()

    if 'data' in data and symbol in data['data']:
        name = data['data'][symbol]['name']
        quote = data['data'][symbol]['quote']['USD']['price']
        return f'{name}: ${quote:.2f}'
    else:
        return f'Quote not available for {symbol}'

def comboCoins():
    return [
        "Bitcoin:BTC",
        "Ethereum:ETH",
        "Binance Coin:BNB",
        "Solana:SOL",
        "Cardano:ADA",
        "Ripple:XRP",
        "Polkadot:DOT",
        "Dogecoin:DOGE",
        "Avalanche:AVAX",
        "Algorand:ALGO"
    ]


def fetch_stocks():
    """
    Fetch stock data from the 'stocks' table in the database.
    """
    conn = sqlite3.connect('crypto.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stocks")
    stocks = cursor.fetchall()  # fetch all rows
    conn.close()
    return stocks

def create_pretty_table(stocks):
    """
    Create a PrettyTable from the fetched stock data.
    """
    table = PrettyTable()
    table.field_names = ["Name", "Symbol", "Price"]

    for stock in stocks:
        table.add_row(stock)

    return table

# Fetch data from the database
stocks_data = fetch_stocks()

# Create a PrettyTable from the fetched data
stocks_table = create_pretty_table(stocks_data)

# Print the PrettyTable
print(stocks_table)


