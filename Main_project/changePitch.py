import scipy.io.wavfile as wave
import sounddevice as sd
import numpy as np


sf, s = wave.read("pitch.wav")

def pitch(inputSignal, factor):
    indices = np.round(np.arange(0, len(inputSignal)-1, factor))
    return inputSignal[indices.astype(int)]




