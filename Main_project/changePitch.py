import scipy.io.wavfile as wave
import sounddevice as sd
import numpy as np
from Main_project.applyReverb import applyReverb

#sf, s = wave.read("guitar.wav") this only for testing

def pitch(inputSignal, factor):
    indices = np.round(np.arange(0, len(inputSignal)-1, factor))
    return inputSignal[indices.astype(int)]

''' This only for testing
s1 = applyReverb(s,sf,1)
s2 = pitch(s1,1.2)
sd.play(s2,sf)
sd.wait()
'''



