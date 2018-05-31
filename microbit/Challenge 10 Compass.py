# Micro:bit Compass
# Source: http://microbit-micropython.readthedocs.io/en/latest/tutorials/direction.html

from microbit import *

compass.calibrate()

while True:
    needle = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])