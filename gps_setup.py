################ GPS PARSERING NMEA MESSAGE #################
### FUNCTIONS ###
# UART port configuration 
# Parser NMEA message and obtain any information base on:
# -	Field No, Name of the message, parameters that GPS datasheet provide.
# Calculate and do a valid format of latitude and longitude for uploading to a server.

from machine import UART
import time

def configure_UART_port(UART_number, baudrate):
    uart_GPS = UART(UART_number, baudrate, bits = 8, parity = None, stop = 1, timeout = 300)
    
    return uart_GPS

def read_data_UART(uart_GPS):
    data_UART=""
    data_UART_splited=[]
    
    data_UART = str(uart_GPS.readline('\r\n'))
    data_UART_splited = data_UART.split(',')
    return data_UART_splited

def get_info_UART(data_UART, field_no, name_message):
    info_GPS = ""
    if name_message in data_UART[0]:
        info_GPS = data_UART[field_no]
    return info_GPS
    
def get_info_UART_saved(data_UART, field_no, name_message, save_info):
    if name_message in data_UART[0]:
        info_GPS = data_UART[field_no]
        save_info.append(info_GPS)
    return save_info

def check_info(variable_save, data):
    if data != "":
        variable_save = data
    return variable_save
    

def convert_location(latitude, longitude):
    final_data = []
    
    degrees_latitude = float(latitude[0:2])
    minutes_latitude = float(latitude[2:10])
    total_degrees_latitude = str(round(degrees_latitude + (minutes_latitude)/60, 5))
    if "S" in latitude:
        total_degrees_latitude = "-" + total_degrees_latitude
    final_data.append(total_degrees_latitude)    
    degrees_longitude = float(longitude[0:2])
    minutes_longitude = float(longitude[2:10])
    total_degrees_longitude = str(round(degrees_longitude + (minutes_longitude)/60, 5))
    if "W" in longitude:
        total_degrees_longitude = "-" + total_degrees_longitude
    final_data.append(total_degrees_longitude)     
    location = "location," + total_degrees_latitude + "," + total_degrees_longitude
    final_data.append(location)
    
    return final_data



