#!/usr/bin/python3

from os import system
import time
import smbus
import sys
from gpiozero import LED
from random import randint
import logging

logging.basicConfig(filename='/home/pi/mylog1.log', filemode='w', format='%(lev$
logging.info('tsl_2561.py started')

BUS = 1
TSL2561_ADDR = 0x39
t = time.ctime()

i2cBus = smbus.SMBus(BUS)

i2cBus.write_byte_data(TSL2561_ADDR, 0x80, 0x03)
i2cBus.write_byte_data(0x39, 0x01 | 0x80, 0x02)

spot_main = LED(22)
spot_gallery = LED(27)
spot_aux = LED(17)
logging.info('variables set')

def time_in_seconds(time):
    """
    extracts from time argument current time,
    converts it to seconds and returns it as int
    """
    t1 = time.split()
    t2 = t1[3].split(':')
    return int(t2[0])* 3600 + int(t2[1])*60 + int(t2[2])

def month(time):
    """
    extracts from time argument current month
    and returns it as string
    """
    tm1 = time.split()
    return  tm1[1]


def read_sensor():
    """
    reads out tsl2561 Sensor and returns visble
    component
    """
    LSB = i2cBus.read_byte_data(TSL2561_ADDR, 0x8C)
    MSB = i2cBus.read_byte_data(TSL2561_ADDR, 0x8D)
    Ambient = (MSB << 8) + LSB

    LSB = i2cBus.read_byte_data(TSL2561_ADDR, 0x8E)
    MSB = i2cBus.read_byte_data(TSL2561_ADDR, 0x8F)
    Infrared = (MSB << 8) + LSB
	Visible = Ambient - Infrared
    return Visible
logging.info('functions defined')

print('light_control.py was started at: ',time.ctime())
tx = time_in_seconds(time.ctime())
time.sleep(0.5)
print('light_control.py was started at: ', tx, 'seconds')

while True:
    print('Visible: ',read_sensor(), 'at: ',time.ctime())
    print('Visible: ',read_sensor(), 'at: ',time_in_seconds(time.ctime()),'seco$
    time.sleep(120)
    if read_sensor() < 100:
        time.sleep(0.5)
        logging.info('below 100')
        spot_gallerys.on()
        logging.info('spot_gallery.on')
        time.sleep(72900 - tx)
        spot_main.on() #20:15
        logging.info('spot_main.on')
        time.sleep(300)
        spot_aux.on() #20:20
        logging.info('spot_aux.on')
        time.sleep(randint(300, 600))
        spot_main.off()  #20:28 - 20:30
        logging.info('spot_main.off')
        time.sleep(180)
        spot_aux.off() #20:28 - 20:33
        logging.info('spot_aux.off')
        time.sleep(180 + randint(300, 600))
        spot_gallery.off() #30:34 - 20:46
        logging.info('spot_gallery.off')
        logging.info('relais off')
        break
sys.exit()


