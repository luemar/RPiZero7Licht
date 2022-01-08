#!/usr/bin/python3
import time
import board
import busio
import adafruit_tsl2561
from os import system
import smbus
import sys
from gpiozero import LED
import random
import logging

t = time.ctime()
logging.basicConfig(filename='/home/pi/mylog1.log', filemode='w',level=logging.DEBUG, format='%(message)s:%(asctime)s')

spot_main = LED(13)
spot_aux = LED(19)
spot_gallery = LED(26)

def time_in_seconds(time):
    t1 = time.split()
    t2 = t1[3].split(':')
    return int(t2[0])* 3600 + int(t2[1])*60 + int(t2[2])

def month(time):
    tm1 = time.split()
    return  tm1[1]

tx = time_in_seconds(time.ctime())
print('tsl2561.py started at: ',time.ctime(), 'equals:', tx, 'seconds')
time.sleep(0.5)
logging.info('tsl2561.py started ')

def sensor_read ():

    i2c = busio.I2C(board.SCL, board.SDA) # Create the I2C bus
    tsl = adafruit_tsl2561.TSL2561(i2c)  # Create the TSL2561 instance, passing>

    #tsl.enabled = True  # Enable the light sensor
    time.sleep(1)
    tsl.gain = 0  # Set gain 0=1x, 1=16x
    tsl.integration_time = 1 # Set integration time (0=13.7ms, 1=101ms, 2=402ms>

    # Get raw (luminosity) readings individually
    broadband = tsl.broadband
    infrared = tsl.infrared

    # Get raw (luminosity) readings using tuple unpacking
    # broadband, infrared = tsl.luminosity

    # Get computed lux value (tsl.lux can return None or a float)
    lux = tsl.lux
    if lux is None:
        lux = 0
    return lux

#tsl.enabled = False # Disble the light sensor (to save power)

while True:
    time.sleep(120)
    print('Lux =',sensor_read(),'at:',time.ctime(),'equals:',time_in_seconds(ti>
    logging.info('sensor_read() started')

    if sensor_read() < 120:
        time.sleep(5)
        print('below 120')
        logging.info('lux below 120')

        if month(time.ctime()) == 'Feb' or month(time.ctime()) == 'Mar' or mont>
            spot_main.on()
            logging.inf0('main on')
            time.sleep(69600 - tx)
            spot_gallery.on() #19:20
            logging.inf0('gallery on')
            time.sleep(4200 + random.randint(60, 180))
            spot_aux.on() #20:31 - 20:33
            logging.inf0('aux on')
            time.sleep(600)
            spot_main.off() #20:41 - 20:43
            logging.inf0('main off')
            time.sleep(3600 + random.randint(60, 180))
            spot_aux.off() #21:42 - 21:46
            logging.inf0('aux off')
            time.sleep(7200)
            spot_gallery.off() #23:42 - 23:46
            logging.inf0('gallery off')


        elif month(time.ctime()) == 'May' or month(time.ctime()) == 'Jun' or mo>
            time.sleep(1)
            spot_gallery.on()
            logging.info('gallery on')
            time.sleep(78000 - tx)
            spot_main.on() #21:40
            logging.info('main on')
            time.sleep(900 + random.randint(60, 120))
            spot_aux.on() #21:56 - 21:57
            logging.info('aux on')
            time.sleep(1200 + random.randint(60, 180))
            spot_main.off() #22:17 - 22:20
            logging.info('main off')
            time.sleep(3600)
            spot_aux.off() #23:17 - 23:20
            logging.info('aux off')
            time.sleep(1800)
            spot_gallery.off() #23:39 - 23:54
            logging.info('gallery off')
			
	elif month(time.ctime()) == 'Aug'or month(time.ctime()) == 'Sep'or mont>
            time.sleep(0.5)
            spot_main.on()
            logging.info('spot_main.on')
            time.sleep(72600 - tx + (random.randint(120, 300)))
            spot_aux.on() #20:10+2Min - 20:10+5Min.
            logging.info('spot_aux.on')
            time.sleep(4500)
            spot_gallery.on() #21:27 - 21:30
            logging.info('spot_gallery.on')
            time.sleep(random.randint(300, 600))
            spot_main.off()  #21:32 - 21:40
            logging.info('spot_main.off')
            time.sleep(3600)
            spot_aux.off() #22:32 -22:40
            logging.info('spot_aux.off')
            time.sleep(2280 + random.randint(300, 600))
            spot_gallery.off() #23:10 +3Min. = 23:13 - 23:18 +10Min. = 23:28
            logging.info('spot_gallery.off')


        elif month(time.ctime()) == 'Nov'or month(time.ctime()) == 'Dec'or mont>
            time.sleep(0.5)
            spot_main.on()
            logging.info('spot_main.on')
            time.sleep((67200 - tx) + (random.randint(180, 300)))
            spot_aux.on() #18:43 - 18:45
            logging.info('spot_aux.on')
            time.sleep(1500)
            spot_gallery.on() #19:08 - 19:10
            logging.info('spot_gallery.on')
            time.sleep(2700)
            spot_main.off()  #19:53 - 19:55
            logging.info('spot_main.off')
            time.sleep(4500)
            spot_aux.off() #21:08 -21:10
            logging.info('spot_aux.off')
            time.sleep(9000)
            spot_gallery.off() #23:40 - 23:43
        logging.info('spot_gallery.off')
        break
sys.exit()


