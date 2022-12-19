#!/usr/bin/python3
from time import sleep
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_tsl2561
sensor = adafruit_tsl2561.TSL2561(i2c)

n = 0
while n < 5:
    print('Lux: {}'.format(sensor.lux))
    print('Broadband: {}'.format(sensor.broadband))
    sleep(2)
    n+=1


