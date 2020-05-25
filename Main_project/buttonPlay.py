import sounddevice as sd
import os

def buttonPlay(s, sf):
        sd.play(s, sf, loop = True)

def buttonStop():
        sd.stop()
        try:
            os.remove("selectedTrack.wav")
        except:
            print("nothing to delete")

