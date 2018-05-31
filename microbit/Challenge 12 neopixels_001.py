from microbit import *
import neopixel

# There are 24 LEDs on the zip halo neopixel
# How to define colours
#            Red Green Blue
foreground = [ 0,  0,   255]  # Decimal colors 0-255 - red, green and blue
background = [16, 16,    16]

ring = neopixel.NeoPixel(pin0, 24)

while True:
    # blue dot circles around a white background
    for i in range(0, 24):
        ring[i] = foreground     # set pixel i to foreground
        ring.show()              # actually display it
        sleep(50)                # milliseconds
        ring[i] = background     # set pixel to background before moving on
        ring.show()
  