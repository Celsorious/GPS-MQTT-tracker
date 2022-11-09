### BOOT PROGRAM FOR CONFIGURING SCREEN AND WIFI CONNECTION ###

import network
import main_ssd1306
from wifi_data import ssid, key
from ssd1306_configuration import CHANNEL_I2C, SDA_PIN, SCL_PIN, WIDTH_SCREEN, HEIGHT_SCREEN

### OLED I2C CONFIGURATION ###
i2c = main_ssd1306.configure_I2C(channel = CHANNEL_I2C,SDA_pin = SDA_PIN, SCL_pin = SCL_PIN)
oled = main_ssd1306.configure_screen( width = WIDTH_SCREEN, height = HEIGHT_SCREEN, i2c_configuration = i2c)
main_ssd1306.clean_screen(oled = oled)

### WIFI CONNECTION ###
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        main_ssd1306.message_connection_wifi(oled = oled)
        
        wlan.connect(ssid, key)
        while not wlan.isconnected():
            pass
        
do_connect()

