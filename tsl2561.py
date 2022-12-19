#!/usr/bin/python3
import adafruit_tsl2561
import time
import board
import busio
import sys
import random
import logging
from gpiozero import LED
from os import system

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2561.TSL2561(i2c)
treshold = 62
logging.basicConfig(filename='/home/pi/mylog1.log',\
                    filemode='w',level=logging.DEBUG,\
                    format='%(message)s:%(asctime)s')

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

def sensor_read():
    brightness = sensor.lux
    return brightness

sec_at_start = time_in_seconds(time.ctime())
time.sleep(0.5)
tsl2561_start_time = time.ctime()
print('tsl2561.py started at: ',\
       tsl2561_start_time,'equals:', sec_at_start)
logging.info('tsl2561.py started ')

if sec_at_start >= 71940:
    time.sleep(1)
    spot_gallery.on()
    print('direkt start, gallery_on')
    logging.info('direk start, gallery_on')
    time.sleep(85500-sec_at_start)
    spot_gallery.off()
    print('gallery_off nach direkt start')
    logging.info('gallery_off nach direkt start')
    sys.exit()

else:
    while True:
        print('Brightness =',sensor_read())
        running_time = time.ctime()
	running_sec = time_in_seconds(running_time)
        print('current_running_time: ',running_time)
        logging.info('sensor_read() started')
        time.sleep(20)

        if  sensor_read() < treshold:
            time.sleep(1)
            below_treshold_time = time.ctime()
            print('brightness below treshold at:',\
                  below_treshold_time)
            logging.info('brightness below treshold')


            if month(time.ctime()) == 'Feb' or month(time.ctime())\
               == 'Mar' or month(time.ctime()) == 'Apr':
                spot_main.on()
                logging.info('main on')
                time.sleep(71940 - sec_at_start)
                spot_gallery.on() #19:59
                logging.info('gallery on')
                time.sleep(6540 + random.randint(60, 180))
                spot_aux.on() #21:11 - 21:15
                logging.info('aux on')
                time.sleep(600)
                spot_main.off() #21:21 - 21:25
                logging.info('main off')
                time.sleep(1260 + random.randint(60, 180))
                spot_aux.off() #21:42 - 21:46
                logging.info('aux off')
                time.sleep(7200)
                spot_gallery.off() #23:42 - 23:46
                logging.info('gallery off')


            elif month(time.ctime()) == 'May' or month(time.ctime())\
                 == 'Jun' or month(time.ctime())== 'July':
                time.sleep(1)
                spot_gallery.on()
                logging.info('gallery on')
                time.sleep(78000 - sec_at_start)
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
			
	    elif month(time.ctime()) == 'Aug'or month(time.ctime())\
                 == 'Sep' or month(time.ctime())== 'Oct':
                time.sleep(0.5)
                spot_main.on()
                logging.info('spot_main.on')
                time.sleep(72600 - sec_at_start + (random.randint(120, 300)))
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
                spot_gallery.off() #23:10 +3Min. = 23:13 - 23:18 +10Min. = 2>
                logging.info('spot_gallery.off')

            elif month(time.ctime()) == 'Nov'or month(time.ctime())\
                 == 'Dec' or month(time.ctime())== 'Jan':
                time.sleep(0.5)
                spot_main.on()
                logging.info('spot_main.on')
                time.sleep((67200 - sec_at_start) + (random.randint(180, 300)))
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
            logging.info('program terminated')
        break
sys.exit()
