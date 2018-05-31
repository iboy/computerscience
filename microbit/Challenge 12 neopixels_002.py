from microbit import *
import neopixel

# There are 24 LEDs on the zip halo neopixel
# How to define colours
#            Red Green Blue
foreground = [ 0,  0,   255]  # Decimal colors 0-255 - red, green and blue
background = [16, 16,    16]

ring = neopixel.NeoPixel(pin0, 24)
count = 0
for i in range(0, 24):
    ring[i] = background     # set pixel to background before moving on
    ring.show()

while True:
    # blue dot circles around a white background

    if button_b.is_pressed():
        ring[count] = foreground     # set pixel to background before moving on
        ring.show()
    if button_b.was_pressed():
        ring[count] = background     # set pixel to background before moving on
        ring.show()
        count = count + 1
 
# This code will generate an error.
# When will it do that? 
# Why does it do it - what is the error message?
    
  