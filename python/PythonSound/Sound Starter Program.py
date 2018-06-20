from subprocess import call
import wave, sys

def soundInfo(fileName):
    sound = wave.open(fileName, 'rb')
    
    channels = sound.getnchannels()
    frequency = sound.getframerate()
    sampleSize = sound.getsampwidth()
    duration = sound.getnframes() / frequency
    
    print("\n-----SOUND DETAILS-----")
    print("Channels: "+str(channels))
    print("Sampling Frequency: "+str(frequency)+" Hz")
    print("Sample Size: "+str(sampleSize)+" Bytes")
    print("Duration: "+str(duration)+" seconds")
    print("Storage Requirements: ", round((sampleSize*frequency*duration*channels)/1000,2),"kB")

def chooseASound():
    possibleSounds = ["dog", "cat", "lion", "duck"]
    sound = input("What sound would you like to play? ")
    sound = sound.lower()
    if sound in possibleSounds:
        print("We have that. Playing the {} sound now.".format(sound))
        file = sound+".wav"
        call(["afplay",file])
    else:
        print("I'm afraid we don't have that sound. The options are \"dog\", \"cat\", \"lion\" or \"duck\".")


choice = ""
while choice != "5":
    #print("\n-----MENU-----\n1. Dog\n2. Cat\n3. Liom\n4. Duck\n5. Quit")
    #choice = input("Enter your choice: ")
    #if choice == "1":
    #    soundInfo("dog.wav")
    #    call(["afplay", "dog.wav"])
    #elif choice == "2":
    #    soundInfo("cat.wav")
    #    call(["afplay", "cat.wav"])
    #elif choice == "3":
    #    soundInfo("lion.wav")
    #    call(["afplay", "lion.wav"])
    #elif choice == "4":
    #    soundInfo("duck.wav")
    #    call(["afplay", "duck.wav"])
    chooseASound()

