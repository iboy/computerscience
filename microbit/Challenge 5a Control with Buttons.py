from microbit import *

while True: # try it without the while loop
    if button_a.is_pressed():
      display.show("A")
    elif button_b.is_pressed():
      display.show("B")
    elif button_a.is_pressed() and button_b.is_pressed():
      display.scroll("AB")
    else: 
      display.clear()