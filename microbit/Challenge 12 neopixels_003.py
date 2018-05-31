# Task add code to make button a move the pixel in the other directions.

from microbit import *
import neopixel

# There are 24 LEDs on the zip halo neopixel
# How to define colours
#            Red Green Blue
foreground = [ 0,  0,   255]  # Decimal colors 0-255 - red, green and blue = Blue
background = [16, 16,    16]  # Dim White

ring = neopixel.NeoPixel(pin0, 24)
count = 0
for i in range(0, 24):
    ring[i] = background     # set pixel to background before moving on
    ring.show()
ring[count] = foreground
ring.show()
while True:
    # blue dot circles around a white background

    if button_b.is_pressed():
        ring[count] = foreground     # set pixel to background before moving on
        ring.show()
    if button_b.was_pressed():
        ring[count] = background     # set pixel to background before moving on
        ring.show()
        if  count == 23: 
            count = 0
        else:
            count = count + 1
        print ("b button count ", count)
        
    if button_a.is_pressed():
        ring[count] = foreground     # set pixel to background before moving on
        ring.show()
    if button_a.was_pressed():
        ring[count] = background     # set pixel to background before moving on
        ring.show()
        if  count == 0: 
            count = 23
        else: 
            count = count - 1
        print ("a button count ", count)
    
# I reversed the logic for button A...

   
  