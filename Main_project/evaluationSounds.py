import sounddevice as sd
import scipy.io.wavfile as wave
from Main_project.applyReverb import applyReverb
from Main_project.changePitch import *

sampFreq, signal = wave.read("torch.wav")


#outputSignal1 = applyReverb(signal, sampFreq, 2)
outputSignal2 = pitch(signal, 0.8)
#sd.play(outputSignal, sampFreq)
#sd.wait()
wave.write("lowPitchTorch.wav", sampFreq, outputSignal2)
