#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess


GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Suppress bogus warning caused by LED being plugged into the port
GPIO.setwarnings(False)

GPIO.wait_for_edge(26, GPIO.FALLING)

subprocess.call(['poweroff'], shell=False)
