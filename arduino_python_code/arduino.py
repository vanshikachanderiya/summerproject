import serial
ser = serial.Serial('/dev/ttyACM1',9600, timeout=1)
while True:
    line = ser.readline().decode().strip()
    print(line.split("'"))
