############# IOT SOLUTION FOR TRACKING CAR LOCATION ###########

import gps_setup
import mqtt
import time
import main_ssd1306


############# GLOBAL VARIABLES ##############

### FRECUENCY OF MQTT PUBLISH ###
TIME_BETWEEN_PUBLISH = 13
TIME_actual_publish = 0

### FRECUENCY OF SCREEN REFRESH ###
TIME_REFRESH_SCREEN = 5
TIME_actual_screen = 0

### DATA SAVE FROM GPS NMEA MESSAGE ###
n_satellites = "00"
longitude = ""
latitude = ""
altitude = ""
speed = ""

### CONFIGURATION UART ###
uart_GPS = gps_setup.configure_UART_port(UART_number = 2, baudrate = 9600)

### CONFIGURATION MQTT SERVER ###
client = mqtt.create_client()
mqtt.check_connection_client(client = client)

while True:  
    if uart_GPS.any():
        data_UART = gps_setup.read_data_UART(uart_GPS)

        ### NUM SATELLITES ###
        info_GPS = gps_setup.get_info_UART(data_UART = data_UART, field_no = 7, name_message = 'GNGGA')
        n_satellites = gps_setup.check_info(n_satellites, info_GPS)
        
        if n_satellites != "00":
            ### GETTING LOCATION FROM LATITUDE AND LONGITUDE ###
            info_latitude = gps_setup.get_info_UART(data_UART = data_UART, field_no = 2, name_message = 'GGA') + gps_setup.get_info_UART(data_UART = data_UART, field_no = 3, name_message = 'GGA')
            info_longitude = gps_setup.get_info_UART(data_UART = data_UART, field_no = 4, name_message = 'GGA') + gps_setup.get_info_UART(data_UART = data_UART, field_no = 5, name_message = 'GGA')
            longitude = gps_setup.check_info(longitude, info_longitude)
            latitude = gps_setup.check_info(latitude, info_latitude)
            location = gps_setup.convert_location(latitude = latitude, longitude = longitude)
            
            ### GETTING ALTITUDE ###
            info_altitude = (gps_setup.get_info_UART(data_UART = data_UART, field_no = 9, name_message = 'GGA'))
            altitude = gps_setup.check_info(altitude, info_altitude)
            
            ### GETTING SPEED ###
            info_speed = gps_setup.get_info_UART(data_UART = data_UART, field_no = 7, name_message = 'VTG')
            speed = gps_setup.check_info(speed, info_speed)
            
            ### SHOW DATA ON SSD 1306 ###
            if (time.time() - TIME_actual_screen) > TIME_REFRESH_SCREEN:
                main_ssd1306.clean_screen(oled = oled)
                main_ssd1306.message_getting_data(oled = oled, name_data = "Num sat:", data = n_satellites, y_init = 0, units = "")
                main_ssd1306.message_getting_data(oled = oled, name_data = "Speed:", data = speed, y_init = 13, units = "km/h")
                main_ssd1306.message_getting_data(oled = oled, name_data = "Lat:", data = location[0], y_init = 26, units = "")
                main_ssd1306.message_getting_data(oled = oled, name_data = "Lon:", data = location[1], y_init = 39, units = "")
                main_ssd1306.message_getting_data(oled = oled, name_data = "Height:", data = altitude, y_init = 52, units = "m")
                
                TIME_actual_screen  = time.time()
            
            ### PUBLISHING DATA ON MQTT SERVER ###
            if (time.time() - TIME_actual_publish) > TIME_BETWEEN_PUBLISH:
             
                mqtt.publish_info(client = client, topic = b'FEED/csv', data = location[2])
                mqtt.publish_info(client = client, topic = b'FEED', data = n_satellites)
                mqtt.publish_info(client = client, topic = b'FEED', data = speed)

                mqtt.publish_info(client = client, topic = b'FEED', data = altitude)
            
                TIME_actual_publish  = time.time()
        else:
            main_ssd1306.clean_screen(oled = oled)
            main_ssd1306.message_connection_GPS(oled=oled)
            
