#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import ConfigParser, time
from flask import Flask, render_template
from collections import OrderedDict
app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

# OUT pin used to contol whatever
CONTROLPIN = 15

GPIO.setup(CONTROLPIN, GPIO.OUT)
GPIO.output(CONTROLPIN, GPIO.LOW)

def checkPin(pincheck):
    if GPIO.input(pincheck) == GPIO.HIGH:
        msg = "it be ON"
    else:
        msg = "it be OFF"

    return msg

@app.route("/")
def main():
    # check pin state
    pinStateMsg = checkPin(CONTROLPIN)

    templateData = {
        'startStopBtnMsg' : pinStateMsg,
        'pin' : CONTROLPIN
        }
    # Pass the template data into the template main_GPIO.html and return it to the user
    return render_template('main_GPIO.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/toggle")
def action(changePin):
    # Convert the pin from the URL into an integer:
    changePin = int(changePin)
    # Set device name:
    deviceName = "A/C unit"
    # Read the pin and set it to whatever it isn't (that is, toggle it):
    GPIO.output(changePin, not GPIO.input(changePin))

    message = "Toggled " + deviceName + "."

    # check pin state
    pinStateMsg = checkPin(CONTROLPIN)

    templateData = {
        'startStopBtnMsg' : pinStateMsg,
        'pin' : CONTROLPIN,
        'message' : message
    }

    return render_template('main_GPIO.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088, debug=True)
