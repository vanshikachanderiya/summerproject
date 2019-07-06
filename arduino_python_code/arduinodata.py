import serial
import os
import time
#import Adafruit_DHT
import serial
import urllib3
http = urllib3.PoolManager()
ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
time.sleep(3)
while 1:
    try :
        line = ser.readline().decode().strip()
        data = (line.split(","))
        # print(len(data))
        if len(data) is 0:
            continue
        temp = float(data[0])
        hum = float(data[1])
        motion = float(data[2])
        #print(data[0])

        #humidity, tempreature = Adafruit_DHT.read_retry(11,25)
        
##        print("Tempreature = %f" %temp)
##        print("Humidity = %f" %hum)
##        print("Motion =%f" %motion)
##        print("-----------------------------")

        baseURL = "https://api.thingspeak.com/update?api_key=WGM41TV9OZ0XW5VT"
        url =(baseURL + "&field1=%f&field2=%f&field3=%f" %(temp,hum,motion))
        #url = "https://api.thingspeak.com/update?api_key=WGM41TV9OZ0XW5VT&field1=250&field2=200"
        print(url)
        response = http.request('GET',url)
        print(response.data)
        time.sleep(1)
    except :
          pass
