import sqlite3
import ttkbootstrap as ttk
from tkinter import *

root = ttk.Window(themename='superhero')
root.title('Crypto')
root.geometry('500x500')

comboCoins = bitcoin_companies = [
    "Bitcoin: BTC",
    "Coinbase: COIN",
    "MicroStrategy: MSTR",
    "Grayscale Bitcoin Trust: GBTC",
    "Square, Inc.: SQ",
    "Riot Blockchain: RIOT"
]
def bindCoins():
    pass

titleLabel = ttk.Label(root, text='Crypto')
titleLabel.pack(padx=10, pady=10)
crptoCombobox = ttk.Combobox(root, bootstyle="success", values=comboCoins,command=bindCoins)
crptoCombobox.pack(padx=10, pady=10)
crptoLabel = ttk.Label(root, text='Coin')
crptoLabel.pack(padx=10, pady=10)




root.mainloop()