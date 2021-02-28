import paho.mqtt.publish as publish
 
MQTT_SERVER = "192.168.0.3"
MQTT_PATH = "pi\input"
 
publish.single(MQTT_PATH, "{\"android\":\"tes7\"}", hostname=MQTT_SERVER)
