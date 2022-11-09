############ SSD 1306 CONFIGURATION AND FUNCTIONS BASED ON ssd1306 ###########
### FUNCTIONS ###
# Configure I2C port
# Configure OLED screen
# Print any GPS data providing only the header and the data variable

from ssd1306 import SSD1306_I2C
from machine import I2C, Pin

def configure_I2C(channel, SDA_pin, SCL_pin):
    i2c_configuration = I2C(channel, scl = Pin(SCL_pin), sda = Pin(SDA_pin))
    
    return i2c_configuration

def configure_screen(i2c_configuration, width, height):
    oled = SSD1306_I2C(width, height, i2c_configuration)
    
    return oled

def clean_screen (oled):
    oled.fill(0)
    
def message_connection_wifi(oled):
    oled.text("Connecting to ", 0, 0)
    oled.text("network...", 0, 10)
    oled.show()

def message_connection_GPS(oled):
    oled.text("Getting GPS data", 0, 0)
    oled.text("...", 0, 10)
    oled.show()
    
def message_getting_data(oled, name_data, data, y_init, units):
    oled.text(name_data + data + units, 0, y_init)
    oled.show()


  
############### TESTS ##################
    
#i2c = configure_I2C(channel = 0,SDA_pin = 21, SCL_pin = 22)
#oled = configure_screen( width = 128, height = 64, i2c_configuration = i2c)
#message_connection_wifi(oled = oled)
#message_connection_GPS(oled = oled)
#message_getting_data(name_data = "Pepe", data = "Hola", y_init = 30)



