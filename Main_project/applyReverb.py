import sounddevice as sd
import scipy.io.wavfile as wave
import numpy as np
sampleFreq, audioData = wave.read("testfile.wav")