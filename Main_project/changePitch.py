import numpy as np
import scipy.io.wavfile as wave
import sounddevice as sd
import matplotlib.pyplot as plt
import scipy


sf, s = wave.read("testfile.wav")
s = s / max(s)
plt.plot(s)
plt.xlabel("samples[n]")
plt.ylabel("aplitude")
sd.play(s, sf)
plt.show()




