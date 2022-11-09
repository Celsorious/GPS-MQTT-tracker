############### MQTT SERVER BASED ON UMQTT.SIMPLE ####################
### FUNCTIONS ###
# Create a MQTT client
# Check  the connection of the client and reset the device
# Publish data to MQTT server

import machine
import time
from umqtt.simple import MQTTClient
from random import randint

### MQTT SERVER VARIABLES ###

IO_SERVER = b'io.adafruit.com'
IO_USERNAME = b'celsorious'
IO_KEY = b'aio_kZiY32wmdAv5YnLK5ptpU0D4kgd8'
CLIENT_ID = b'ESP32_GPS'
PORT = 1883 # ENCRYPTED 8883

### MQTT SERVER FUNCTIONS ###

def create_client():
    client = MQTTClient(client_id = CLIENT_ID, server = IO_SERVER, port = PORT, user = IO_USERNAME, password = IO_KEY, ssl = False)
    return client

def check_connection_client(client):
    wait_time_sec = 5
    try:
        client.connect()
    except OSError as error:
        print(error)
        time.sleep(wait_time_sec)
        machine.reset()
               
def publish_info(client, topic, data):
    """Topic is the feed and data de information you want to upload"""
    client.publish(topic, data)
    