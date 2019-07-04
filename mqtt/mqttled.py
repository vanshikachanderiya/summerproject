import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT,initial=GPIO.LOW)

def blink(pin):
    
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return

def on_connect(client,userdata,flags,rc):
    print("connected with result code"+str(rc))

    client.subscribe('core/temp')
    #client.subscribe('core/humidity')
    
def on_message(client,userdata,msg):
    
    message = int(float(msg.payload))

    print (message)
    if message < 20:
        print("tempreature is high")
        blink(13)
    else:
        print("current tempreature is:"+ str(message))
try :
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("test.mosquitto.org",1883,60)
finally:
    client.loop_forever()
    GPIO.cleanup()   
