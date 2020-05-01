import sounddevice as sd
import scipy.io.wavfile as wave
import numpy as np

sampleFreq, audioData = wave.read("testfile.wav")

def applyEcho (sampleFreq, audioData, echoStr):
    sd.play(audioData, sampleFreq)
    sd.wait()
