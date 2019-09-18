#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

# We get a bogus warning about the port being in use if
# the LED is already plugged in
GPIO.setwarnings(False)

while True:
    GPIO.output(13,1)
    time.sleep(1)
    GPIO.output(13,0)
    time.sleep(1)
