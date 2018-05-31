from microbit import *
while True:
    degrees = compass.heading()
    if degrees < 45:
        display.clear()
        display.show("N")
    elif degrees < 135:
        display.clear()
        display.show("E")
    elif  degrees < 225:
        display.clear()
        display.show("S")
    else:
        display.clear()
        display.show("W")
