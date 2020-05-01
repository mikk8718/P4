import sounddevice as sd
import scipy.io.wavfile as wave
import keyboard
import msvcrt


while True:
    if msvcrt.kbhit():
        key_stroke = msvcrt.getch()
        print(key_stroke)
samplingFreq = 44100


def buttonPlay(play):
    if play == 1:
        samplingFreq, signal = wave.read("0001.wav")
    if play == 2:
        samplingFreq, signal = wave.read("0002.wav")



    sd.play(signal, samplingFreq)
    sd.wait()


def buttonStop():
    sd.stop()


buttonPlay(2)



