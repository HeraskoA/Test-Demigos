import sqlite3

conn = sqlite3.connect("sqlite3")

try:
    conn.execute(
        '''CREATE TABLE rate
                 (pair text PRIMARY KEY, price DECIMAL(10, 5))'''
    )
except sqlite3.OperationalError:
    pass

conn.close()
