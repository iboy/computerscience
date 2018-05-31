from microbit import *
import neopixel

ring = neopixel.NeoPixel(pin0, 24)

# task get a pixel to flash on and over every .5 secs 
count = 0
while True: 
    ring[0] = [255,0,0]
    ring.show()
    sleep(250)
    ring[0] = [255,255,255]
    ring.show()
    sleep(250)
    