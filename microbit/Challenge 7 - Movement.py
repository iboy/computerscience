from microbit import *
y = 2
x = 2
while True:
    readingX = accelerometer.get_x()
    readingY = accelerometer.get_y()
    # First get the Y axis tilt and check and set the Y coordinate for the pixel
    if readingY > 100:
        if y == 4:
            y = 0
        else:
            y = y + 1
        #display.show("F")
    elif readingY < -100:
        if y == 0:
            y = 4
        else: 
            y = y - 1
        #display.show("B")
    else:
        # This block means we haven't moved (much) on the Y axis
        y = y
    
    # Next get the X axis tilt and check and set the X coordinate for the pixel
    if readingX > 100:
        #display.show("R")
        if x < 4:
            x = x + 1
        else: 
            x = 0
    elif readingX < -100:
        #display.show("B")
        if x == 0:
            x = 4
        else: 
            x = x - 1
    else:
        #display.show("-")
        # This block means we haven't moved on the X axis
        x = x
    
    # this sets the pixel on the screen
    display.set_pixel(x, y, 9)
    sleep(400) # This adjusts the speed the pixel appears to move. Like a sensitivity setting
    display.clear()
    
    # Extension: extend the program by creating a game
    # with the aim to settle the pixel in the centre.

        
    