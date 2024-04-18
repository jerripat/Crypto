import sqlite3

def postData(name, symbol, price):
    conn = sqlite3.connect('crypto.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS crypto (
        name TEXT,
        symbol TEXT,
        price REAL )''')

    c.execute('''INSERT INTO crypto VALUES (?,?,?)''', (name, symbol, price))
    conn.commit()
   # conn.close()
