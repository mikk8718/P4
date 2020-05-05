import numpy as np
import scipy.io.wavfile as wave
import sounddevice as sd

sampleFreq, audioData = wave.read("testfile.wav")
feedBackIsUsed=True
def applyEcho (samp, data):
        dataLenght = np.size(data)
        outputSignal = np.zeros(dataLenght , dtype='int16')
        delay = np.int(np.round(0.15 * samp))
        print(audioData)
        for n in np.arange(dataLenght):
            if n < 0.15:

                outputSignal[n] = data[n]
            else:
                outputSignal[n] = data[n] + 1 * data[n - delay]
        print(outputSignal)
        print(outputSignal/max(outputSignal))
        return outputSignal/max(outputSignal)

signal = applyEcho(sampleFreq,audioData)
sd.play(signal,sampleFreq)
print("played")
sd.wait()