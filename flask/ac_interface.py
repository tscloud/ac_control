#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ConfigParser, time
from flask import Flask, render_template
from collections import OrderedDict
app = Flask(__name__)

# OUT pin used to contol whatever
CONTROLPIN = 15
# msg describing current state of pin
pinStateMsg = "on"

@app.route("/")
def main():
    templateData = {
        'startStopBtnMsg' : pinStateMsg
        'pin' : CONTROLPIN
        }
    # Pass the template data into the template main_GPIO.html and return it to the user
    return render_template('main_GPIO.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/toggle")
def action(changePin):
    # Convert the pin from the URL into an integer:
    changePin = int(changePin)
    # Get the device name for the pin being changed:
    deviceName = "A/C unit"
    # simulate button press
    # Read the pin and set it to whatever it isn't (that is, toggle it) and then set it back:
    time.sleep(0.2)
    message = "Toggled " + deviceName + "."

    # Along with the pin dictionary, put the message into the template data dictionary:
    templateData = {
        'startStopBtnMsg' : pinStateMsg
        'pin' : CONTROLPIN
        'message' : message,
    }

    return render_template('main_GPIO.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088, debug=True)
