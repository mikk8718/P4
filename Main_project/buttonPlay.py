import sounddevice as sd
import scipy.io.wavfile as wave
import keyboard
import msvcrt
import os
from tkinter import *


# GUI stuff for debugging
root = Tk()
root.geometry("400x400") #size of the window
###############


#samplingFreq = 44100
samplingFreq, signal = wave.read("testfile.wav")


def buttonPlay():
    #if play == 1: These three lines will be used later
    #    applyEcho(sample, signal, echoStr)
    #    applyPitch(sample, signal, pitchStr)

        sd.play(signal, samplingFreq)
        # sd.wait()

def buttonStop():
    #if state == 2: Will be used
        sd.stop()
        try:
            os.remove("selectedTrack.wav")
        except:
            print("nothing to delete")


# Created a GUI to see if it works and it indeed does so this chunk can and will be deleted later
btnFrame = LabelFrame(root, text="Notes", padx=5, pady=5)
btnFrame.pack(fill=X)
btn1 = Button(btnFrame, text="Play", padx=20, pady=30, command=buttonPlay)  # fg="white", bg="black",
btn1.pack(side=LEFT)
btn2 = Button(btnFrame, text="Stop", padx=20, pady=30, command=buttonStop)
# btn2.grid(row=btnRow, column=1)
btn2.pack(side=LEFT)
root.mainloop()
#################################################################################

# buttonPlay(1)
# buttonStop(2)





