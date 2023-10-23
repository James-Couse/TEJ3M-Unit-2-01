"""
Created by: James Couse
Created on: Oct 23 2023
This module turns the builtin LED on and off.
"""

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = not led.value
    time.sleep(1)
