import wave
import sounddevice as sd


w = wave.open("testfile.wav")
sd.play(w, 44100)




