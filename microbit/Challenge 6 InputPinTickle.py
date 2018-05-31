from microbit import *

while True:
    if pin0.is_touched():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)

'''
# this is a snippet of psuedocode to help you understand how if statements help 
# select different paths for your program to follow
if something is True:
    # do one thing
elif some other thing is True:
    # do another thing
else:
    # do yet another thing.
'''