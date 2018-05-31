from microbit import *

while True:
    readingY = accelerometer.get_y()
    if readingY > 100:
        display.show("B")
    elif readingY < -100:
        display.show("F")
    else:
        display.show("-")