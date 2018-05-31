from microbit import *

while True:
    readingY = accelerometer.get_y()
    if readingY > 100:
        display.show("F")
    elif readingY < -100:
        display.show("B")
    else:
        display.show("-")