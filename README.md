# GPS-MQTT-tracker

The idea of this project is to make the cheapest position tracking for a car based on MQTT server (Adafruit IO) for storing the data.

This IOT application allows you to track more data than location (speed, height...) for about 7 hours thanks to the optimization and battery chosen.

The 3D design makes the device portable and allows the user to hide it in the glove box where the GPS is able to receive the data.

# Functions 
Get any information from NMEA message based on the field number and name of the message, which are provided in the GPS datasheet (http://files.banggood.com/2016/11/BN-220%20GPS+Antenna%20datasheet.pdf).

Location GPS data to CSV format which allow the commmunication with the server.

OLED configuration for printing data and for showing any error such as wifi connection broken or MQTT client log out.

Warning notification when the position of the car changes send it by email.

Visual notification when you exceed the limit speed.

Easy MQTT upload process, only is need it to provided your adafruit IO feed and the data you want to upload.





# Components
-ESP32 dev kit v1

-GPS BN 220

-OLED 0,96"

-Slider switch

-Lipo charger

-3,7V 850 mah

# 3D printed files
https://www.thingiverse.com/thing:5617723/files


