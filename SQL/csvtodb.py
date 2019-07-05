import csv
import sqlite3

con = sqlite3.connect("dhtdata.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS dht4 ('TEMP' REAL, 'HUMIDITY' REAL, 'TIMESTAMP' TEXT)")

with open('data4.csv','r') as infile:
    dr = csv.reader(infile,delimiter = ',')
    for x in dr:
        
        temp = x[0]
        hum = x[1]
        time = x[2]
        cur.execute("INSERT INTO dht4(TEMP,HUMIDITY,TIMESTAMP) VALUES(?,?,?)",(temp,hum,time))
        con.commit()

cur.close()
con.close()
