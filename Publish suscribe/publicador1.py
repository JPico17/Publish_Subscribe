#Jean Carlo Rodriguez Pico -2214116
import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    client.publish("topic/test", "Mensaje desde publicador 1 (Disney +)")
    time.sleep(5)

