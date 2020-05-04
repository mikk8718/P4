import sounddevice as sd
import scipy.io.wavfile as wave
import numpy as np
import matplotlib.pyplot as plt


samplef, signal = wave.read("testfile.wav")


def combfilter(inputSignal, samplingFreq, filterCoefficient, delay):
    d = np.int(np.round(delay*samplingFreq))
    signalLenght = np.size(inputSignal)
    outputSignal = np.zeros(signalLenght, dtype='int16')

    for n in np.arange(signalLenght):
        if n < d:
            outputSignal[n] = inputSignal[n]
        else:
            outputSignal[n] = inputSignal[n]+filterCoefficient*outputSignal[n-d]

    return outputSignal/max(outputSignal)


def allpassfilter(inputSignal, filterCoefficient):
    # d = np.int(np.round(delay * samplingFreq))
    signalLenght = np.size(inputSignal)
    outputSignal = np.zeros(signalLenght, dtype='int16')

    for n in np.arange(signalLenght):
        if n < 1:
            outputSignal[n] = inputSignal[n]
        else:
            outputSignal[n] = filterCoefficient * inputSignal[n] + inputSignal[n - 1] - filterCoefficient * outputSignal[n - 1]

    return outputSignal / max(outputSignal)


# sd.play(combfilter(signal, samplef, 0.5, 0.15), samplef)
# sd.wait()
# sd.play(allpassfilter(signal, 0.5), samplef)
# sd.wait()
plt.plot(allpassfilter(signal, 0.5))
plt.show()
