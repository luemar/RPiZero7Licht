# Raspberry
# tsl2561.py
# Sript starts every day at 16:10 by crontab.
# First light=spot_main turned on when sensor tsl2561 reads value <120 lux.
# Second light=spot_aux turned on at prefixed time calculated as subtraction
# of prefixed time - time when lux<120 in seconds (x) inserted as time.sleep(x).
# Third light=spot_gallery turned on and all lights turned off in sequence 
# after variable time.sleep(....).
# Script turned off after third light turned off.
