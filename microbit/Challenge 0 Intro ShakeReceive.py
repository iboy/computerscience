from microbit import *
import radio
radio.on()
radio.config(channel=15)        # Set the channel number to 

count = 0
while True:
    incoming = radio.receive()
    display.clear()
    if incoming == "0":
        display.clear()
        display.show(Image.SKULL)
    if incoming == "1":
        display.clear()
        display.show(Image.PACMAN)
    if incoming == "2":
        display.clear()
        display.show(Image.GHOST)
    if incoming == "3":
        display.clear()
        display.show(Image.DIAMOND)
    if incoming == "4":
        display.clear()
        display.show(Image.HEART)
    if incoming == "5":
        display.clear()
        display.show(Image.RABBIT)
    if incoming == "6":
        display.clear()
        display.show(Image.DUCK)    
    if incoming == "7":
        display.clear()
        display.show(Image.HAPPY)
    if incoming == "8":
        display.clear()
        display.show(Image.XMAS)   
    if incoming == "9":
        display.clear()
        display.show(Image.SILLY)
    if incoming == "10":
        display.clear()
        display.show(Image.HOUSE)
    sleep(1800)
       
        
        
        