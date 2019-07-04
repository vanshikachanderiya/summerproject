import os
import time
import Adafruit_DHT
import serial
import urllib3
http = urllib3.PoolManager()
while 1:
    try :
        humidity, tempreature = Adafruit_DHT.read_retry(11,25)
        print("Humidity = %f" %humidity)
        print("Tempreature = %f" %tempreature)
        print("-----------------------------")

        baseURL = "https://api.thingspeak.com/update?api_key=WGM41TV9OZ0XW5VT"
        url =(baseURL + "&field1=%f&field2=%f" %(humidity,tempreature))
        #url = "https://api.thingspeak.com/update?api_key=WGM41TV9OZ0XW5VT&field1=250&field2=200"
        print(url)
        response = http.request('GET',url)
        print(response.data)
        time.sleep(1)
    except :
          pass
