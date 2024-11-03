import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    client.publish("topic/test", "Mensaje desde publicador 3 en Python (Mercado libre)")
    time.sleep(2)
