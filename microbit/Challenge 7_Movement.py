from microbit import *

while True:
    readingX = accelerometer.get_x()
    if readingX > 100:
        display.show("R")
    elif readingX < -100:
        display.show("L")
    else:
        display.show("-")
