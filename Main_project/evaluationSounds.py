import sounddevice as sd
import scipy.io.wavfile as wave
from Main_project.applyReverb import applyReverb
from Main_project.changePitch import *

sampFreq, signal = wave.read("footsteps.wav")


outputSignal = applyReverb(signal, sampFreq, 1)
#sd.play(outputSignal, sampFreq)
#sd.wait()
wave.write("lowReverbFootsteps.wav", sampFreq, outputSignal)
