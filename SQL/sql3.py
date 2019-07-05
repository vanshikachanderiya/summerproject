import sqlite3
import time
import datetime
import random

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('sql1.db')
c = conn.cursor()
def graph_data():
    c.execute('SELECT datestamp, value FROM iotws')
    data = c.fetchall()

    dates = []
    values = []
    
    for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[1])

    plt.plot_date(dates,values,'-')
    plt.show()

graph_data()
c.close
conn.close()
