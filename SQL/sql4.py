import sqlite3
import time
import datetime
import random


conn = sqlite3.connect('sq11.db')
c = conn.cursor()
def del_and_update():
    c.execute('DELETE FROM iotws WHERE value = 99')
    conn.commit()

    c.execute('SELECT * FROM iotws')
    data = c.fetchall()
    [print(row) for row in data]


del_and_update()


c.close
conn.close()

