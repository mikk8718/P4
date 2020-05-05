import sounddevice as sd
import scipy.io.wavfile as wave
import numpy as np



samplef, signal = wave.read("guitar.wav")
signal = signal/2**15 # normalise

def combfilter(inputSignal, filterCoefficient, delay):
    #d = np.int(np.round(delay*samplingFreq))
    signalLenght = np.size(inputSignal)
    outputSignal = np.zeros(signalLenght)

    for n in np.arange(signalLenght):
        if n < delay:
            outputSignal[n] = inputSignal[n]
        else:
            outputSignal[n] = inputSignal[n]+filterCoefficient*outputSignal[n-delay]

    return outputSignal


def allpassfilter(inputSignal, filterCoefficient, delay):
    #d = np.int(np.round(delay * samplingFreq))
    signalLenght = np.size(inputSignal)
    outputSignal = np.zeros(signalLenght)
    #print(d)
    for n in np.arange(signalLenght):
        if n < delay:
            outputSignal[n] = inputSignal[n]
        else:
            outputSignal[n] = filterCoefficient * inputSignal[n] + inputSignal[n - delay] - filterCoefficient * outputSignal[n - delay]

    return outputSignal


def reverb(inputSignal, mixingParameters, combDelays, combFilterParams, allPassDelays, allPassParams):
    signalLenght = np.size(inputSignal)
    outputSignal = np.zeros(signalLenght)

    combFiltersNrs = np.size(combDelays)
    for n in np.arange(combFiltersNrs):
        outputSignal = outputSignal + mixingParameters[n] * combfilter(inputSignal, combFilterParams[n], combDelays[n])

    allPassFilterNrs = np.size(allPassDelays)
    for n in np.arange(allPassFilterNrs):
        outputSignal = allpassfilter(outputSignal, allPassParams[n], allPassDelays[n])

    return outputSignal

def plainGainFromReverbTime(reverbTime, plainDelay, samplingFreq):
    nDelays = np.size(plainDelay)
    plainGains = np.zeros(nDelays)
    for ii in np.arange(nDelays):
        plainGains[ii] = 10**(-3*plainDelay[ii]/(reverbTime*samplingFreq))
    return plainGains



mixingParams = np.array([0.3, 0.25, 0.25, 0.20])
plainDelays = np.array([1553, 1613, 1493, 1153])
allpassDelays = np.array([223, 443])
apParams = np.array([-0.7, -0.7])
reverbTime = 0.7 # seconds
plainParams = plainGainFromReverbTime(reverbTime, plainDelays, samplef)

sd.play(reverb(signal, mixingParams, plainDelays, plainParams, allpassDelays, apParams), samplef)
#sd.play(signal,samplef)
sd.wait()


# sd.play(combfilter(signal, samplef, 0.5, 0.15), samplef)
# sd.wait()
# sd.play(allpassfilter(signal, samplef, 0.5), samplef)
# sd.wait()
# plt.plot(allpassfilter(signal, samplef, 0.5, 0.5))
# plt.show()
