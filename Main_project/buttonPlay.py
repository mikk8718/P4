import sounddevice as sd
import scipy.io.wavfile as wave
import keyboard
import msvcrt


#samplingFreq = 44100
samplingFreq, signal = wave.read("testfile.wav")


def buttonPlay(play):
    if play == 1:
    #    applyEcho(sample, signal, echoStr)
    #    applyPitch(sample, signal, pitchStr)

        sd.play(signal, samplingFreq)
        sd.wait()


buttonPlay(1)



