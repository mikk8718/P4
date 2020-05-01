import sounddevice as sd
import scipy.io.wavfile as wave
import keyboard
import msvcrt
import os

#samplingFreq = 44100
samplingFreq, signal = wave.read("testfile.wav")


def buttonPlay(play):
    if play == 1:
    #    applyEcho(sample, signal, echoStr)
    #    applyPitch(sample, signal, pitchStr)

        sd.play(signal, samplingFreq)
        # sd.wait()

def buttonStop(state):
    if state == 2:
        sd.stop()
        # os.remove("selectedTrack.wav")


buttonPlay(1)
buttonStop(2)



