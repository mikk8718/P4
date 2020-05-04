import numpy as np
import scipy.io.wavfile as wave
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import rfft, irfft, fftfreq, fft

sf, s = wave.read("001_guitar.wav")
#s = s / max(s)
print("He")
fd = rfft(s)
output = fd.copy()
output = irfft(fd)
sd.play(output, sf)
#sd.wait()







