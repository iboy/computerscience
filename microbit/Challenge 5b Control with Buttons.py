from microbit import *

while True:
    if button_a.is_pressed():
      display.show("A")
    elif button_b.is_pressed():
      display.show("B")
    else: 
      display.clear()
    # Why do we need two if statements?
    # Test it with an elif in the above block
    # and see the difference
    # Note: why do we think that is happening?
    if button_a.is_pressed() and button_b.is_pressed():
      display.scroll("AB")
    else: 
      display.clear()