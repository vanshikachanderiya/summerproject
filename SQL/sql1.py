import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('sql1.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS iotws(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def dynamic_data_entry():

    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)

    c.execute("INSERT INTO iotws (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))

    conn.commit()

    
for i in range(10):
    create_table()
    dynamic_data_entry()
    time.sleep(1)

c.close
conn.close()

