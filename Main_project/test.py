import wave
import sounddevice as sd
import scipy.io.wavfile as wave

samplingFreq, guitarSignal = wave.read("testfile.wav")
sd.play(guitarSignal, samplingFreq)
sd.wait()
