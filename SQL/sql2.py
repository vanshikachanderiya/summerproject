import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('sql1.db')
c = conn.cursor()
def read_from_db():

    c.execute('SELECT * FROM iotws WHERE unix > 1452554972')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

read_from_db()
c.close
conn.close()
