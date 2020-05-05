import sounddevice as sd
import scipy.io.wavfile as wave
import numpy as np



samplef, signal = wave.read("guitar.wav")
sd.play(signal, samplef)
sd.wait()

def combfilter(inputSignal, samplingFreq, filterCoefficient, delay):
    d = np.int(np.round(delay*samplingFreq))
    signalLenght = np.size(inputSignal)
    outputSignal = np.zeros(signalLenght, dtype='int16')

    for n in np.arange(signalLenght):
        if n < d:
            outputSignal[n] = inputSignal[n]
        else:
            outputSignal[n] = inputSignal[n]+filterCoefficient*outputSignal[n-d]

    return outputSignal / max(outputSignal)


def allpassfilter(inputSignal, samplingFreq, filterCoefficient, delay):
    d = np.int(np.round(delay * samplingFreq))
    signalLenght = np.size(inputSignal)
    outputSignal = np.zeros(signalLenght, dtype='int16')
    #print(d)
    for n in np.arange(signalLenght):
        if n < d:
            outputSignal[n] = inputSignal[n]
        else:
            outputSignal[n] = filterCoefficient * inputSignal[n] + inputSignal[n - d] - filterCoefficient * outputSignal[n - d]

    return outputSignal / max(outputSignal)


def reverb(inputSignal, mixingParameters, combDelays, combFilterParams, allPassDelays, allPassParams):
    signalLenght = np.size(inputSignal)
    outputSignal = np.zeros(signalLenght, dtype='int16')
    combFiltersNrs = np.size(combDelays)

    for n in np.arange(combFiltersNrs):
        outputSignal = outputSignal + mixingParameters[n] * combfilter(inputSignal, 44100, combFilterParams[n], combDelays[n])

    allPassFilterNrs = np.size(allPassDelays)
    for n in np.arange(allPassFilterNrs):
        outputSignal = allpassfilter(inputSignal, 44100, allPassParams[n], allPassDelays[n])

    return outputSignal / max(outputSignal)


def plainGainFromReverbTime(reverbTime, plainDelay, samplingFreq):
    nDelays = np.size(plainDelay)
    plainGains = np.zeros(nDelays)
    for ii in np.arange(nDelays):
        plainGains[ii] = 10*(-3*plainDelays[ii]/(reverbTime*samplingFreq))
    return plainGains


mixingParams = np.array([0.3, 0.25, 0.25, 0.20]) # numbers taken from a table in the book
plainDelays = np.array([1553, 1613, 1493, 1153]) # numbers taken from a table in the book (H1-H4)
allpassDelays = np.array([223, 443]) # numbers taken from a table in the book (H5, H6)
apParams = np.array([-0.7, -0.7])
reverbTime = 0.7 # seconds
plainParams = plainGainFromReverbTime(0.7, plainDelays, samplef)

sd.play(reverb(signal, mixingParams, plainDelays, plainParams, allpassDelays, apParams), samplef)
sd.wait()


# sd.play(combfilter(signal, samplef, 0.5, 0.15), samplef)
# sd.wait()
# sd.play(allpassfilter(signal, samplef, 0.5), samplef)
# sd.wait()
# plt.plot(allpassfilter(signal, samplef, 0.5, 0.5))
# plt.show()
