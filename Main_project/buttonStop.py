import sounddevice as sd
import os


def buttonStop(state):
    if state == 1:
        sd.stop()
        os.remove("selectedTrack.wav")