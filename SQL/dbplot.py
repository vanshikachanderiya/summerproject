import sqlite3
import time
import datetime
import random

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('dhtdata.db')
c = conn.cursor()
def graph_data():
    c.execute('SELECT temp, timestamp FROM dht4')
    data = c.fetchall()

    dates = []
    values = []
    
    for row in data:
        dates.append(row[0])
        values.append(row[1])

    plt.plot(values,dates,'-')
    plt.show()

graph_data()
c.close
conn.close()
