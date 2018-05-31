from microbit import *
import random

while True:
    display.show(Image.SQUARE_SMALL)
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.show(str(random.randint(1,6)))