#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time, sys

GPIO.setmode(GPIO.BOARD)

GPIO.setup(22, GPIO.OUT)

try:
    while True:
        GPIO.output(22, True)
        time.sleep(2)
        GPIO.output(22, False)
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print "\nBye"
    sys.exit()
