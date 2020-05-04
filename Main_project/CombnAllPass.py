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


def allpassfilter(inputSignal, samplingFreq, filterCoefficient):
    # d = np.int(np.round(delay * samplingFreq))
    signalLenght = np.size(inputSignal)
    outputSignal = np.zeros(signalLenght, dtype='int16')
    # print(d)
    for n in np.arange(signalLenght):
        if n < 1:
            outputSignal[n] = inputSignal[n]
        else:
            outputSignal[n] = filterCoefficient * inputSignal[n] + inputSignal[n - 1] - filterCoefficient * outputSignal[n - 1]

    return outputSignal / max(outputSignal)


def reverb(inputSignal, samplingFreq, mixingParameters, combDelays, combFilterParams, allPassDelays, allPassParams):
    signalLenght = np.size(inputSignal)
    outputSignal = np.zeros(signalLenght, dtype='int16')
    combFiltersNrs = np.size(combDelays)

    for n in np.arange(combFiltersNrs):
        outputSignal = outputSignal + mixingParameters[n] * combfilter(inputSignal, 44100, combFilterParams[n], combDelays[n])

    allPassFilterNrs = np.size(allPassDelays)
    for n in np.arange(allPassFilterNrs):
        outputSignal = allpassfilter(inputSignal, 44100, allPassParams[n])

    return outputSignal / max(outputSignal)

def plainGainFromReverbTime(reverbTime, plainDelay, samplingFreq):
    nDelays = np.size(plainDelay)
    plainGains = np.zeros(nDelays)
    for ii in np.arange(nDelays):
        plainGains[ii] = 10*(-3*plainDelays[ii]/(reverbTime*samplingFreq))
    return plainGains


mixingParams = np.array([0.3, 0.25, 0.25, 0,20])
plainDelays = np.array([1553, 1613, 1493, 1153])
allpassDelays = np.array([223, 443])
apParams = np.array([-0.7, -0.7])
reverbTime = 0.7 # seconds
plainParams = plainGainFromReverbTime(0.7, plainDelays, samplef)

a = reverb(signal, samplef, mixingParams, plainDelays, plainParams, allpassDelays, apParams)

sd.play(a, samplef)
sd.wait()

# sd.play(combfilter(signal, samplef, 0.5, 0.15), samplef)
# sd.wait()
# sd.play(allpassfilter(signal, samplef, 0.5), samplef)
# sd.wait()
# plt.plot(allpassfilter(signal, samplef, 0.5, 0.5))
# plt.show()
