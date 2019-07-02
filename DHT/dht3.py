import datetime
import sys
import Adafruit_DHT
import csv

try :
    while True:
        row = []
        humidity, tempreature = Adafruit_DHT.read_retry(11,4)
        row.append(tempreature)
        row.append(humidity)
        row.append(str(datetime.datetime.now()))
        print(row)
        with open('data4.csv','a') as writeFile :
            writer = csv.writer(writeFile)
            writer.writerow(row)
finally :
    writeFile.close()
