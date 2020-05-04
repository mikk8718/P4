import numpy as np
import scipy.io.wavfile as wave
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import rfft, irfft, fftfreq, fft

sf, s = wave.read("pitch.wav")
def speedx(sound_array, factor):
    """ Multiplies the sound's speed by some `factor` """
    indices = np.round(np.arange(0, len(sound_array), factor))
    indices = indices[indices < len(sound_array)].astype(int)
    return sound_array[indices.astype(int)]

sd.play(speedx(s, 2), sf)
sd.wait()







