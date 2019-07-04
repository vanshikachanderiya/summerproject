import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
    print("connected with result code"+str(rc))

    client.subscribe('core/tests')
    client.subscribe('core/topic')
def on_message(client,userdata,msg):
    #print(msg.topic +str(msg.payload))
    message = (msg.payload)
    message = message[2:]
    message = message.strip("'")
    print(message)
    if message =="Hello":
        print("received message1,do something")
        #do something
    if message == "World!":
        print("received message2,do something else")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org",1883,60)

client.loop_forever()
    
