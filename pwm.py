import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)

p = GPIO.PWM(11,50)
p.start(7.5)
try :
    while True :
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        time.sleep(2)
        p.ChangeDutyCycle(2.5)
        time.sleep(2)
except KeyboardInterrupt :
    p.stop()
    GPIO.cleanup()
        
