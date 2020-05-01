import sounddevice as sd
import scipy.io.wavfile as wave

samplingFreq, guitarSignal = wave.read("testfile.wav")
sd.play(guitarSignal, samplingFreq)
print(samplingFreq)
wave.write("text.wav",samplingFreq,guitarSignal)
sd.wait()
