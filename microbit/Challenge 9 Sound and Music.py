# Microbit Music and Sound

from microbit import *
import music

# 1
# Playing built in tunes and sound FX
# Use code-complete in Mu to see the available built-in elements


#music.play(music.BA_DING)

# 2
# Here we use a list to define a set of notes.
# Each item in the list is a pair of values describing a note: "<Note><Octave> : <duration>"

#tune = ["C4:4", "D4:4", "E4:4", "C4:4", "C4:4", "D4:4", "E4:4", "C4:4","E4:4", "F4:4", "G4:8", "E4:4", "F4:4", "G4:8"]


#music.play(tune)

# 3 
# optionally you can define the octave just once, simplifying the definition

#tune = ["C4:4", "D", "E", "C", "C", "D", "E", "C", "E", "F", "G:8", "E:4", "F", "G:8"]
#music.play(tune)

# 4 
# Sound effects with a program


#while True:
    # for a kind of loop. Range(<from>, <to>, <OPTIONAL step>)
#    if button_a.is_pressed():
#        break
#    for freq in range(880, 1760, 16):
#        music.pitch(freq, 6)  
#   for freq in range(1760, 880, -16):
#        music.pitch(freq, 6)
        
        
# The BBC Micro:Bit can speak
import speech

speech.say("Hello, World")
sleep(2000)
speech.say("I am a DALEK - EXTERMINATE", speed=120, pitch=100, throat=100, mouth=200)