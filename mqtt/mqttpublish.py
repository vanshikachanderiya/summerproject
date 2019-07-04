#mqtt publish demo
import paho.mqtt.client as mqtt
broker_address = "test.mosquitto.org"
client = mqtt.Client("PI")
client.connect(broker_address,1883,60)
client.publish("core/tests","good")
