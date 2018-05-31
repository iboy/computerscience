from microbit import *
import neopixel

# There are 24 LEDs on the zip halo neopixel
# How to define colours
#              Red Green Blue

pixelColour = [ 34,139,34]  # Decimal colors 0-255 - red, green and blue
# Practice changing the colours
# Use the chart in the powerpoint as a rough guide
ring = neopixel.NeoPixel(pin0, 24)
# lists and arrays usually start counting items from 0. 
# This is called 'zero indexed arrays'
ring[0] = pixelColour     # set pixel 0 to our pixel colour
#change the position of the on LED around the ring..

#ring[24] = pixelColour     # set pixel 24 to our pixel colourwhat happens if you uncomment this line and flash to your microbit.
ring.show()

