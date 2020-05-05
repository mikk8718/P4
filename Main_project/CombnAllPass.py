import sounddevice as sd
import scipy.io.wavfile as wave
import numpy as np


#delay, in all the functions, has to be given in amount of samples, not ms.

#Lines 9-10 are for testing purpose, remove when using in main
samplef, signal = wave.read("guitar.wav")
signal = signal/max(signal) #normalizing the signal


def combfilter(inputSignal, filterCoefficient, delay):

    signalLenght = np.size(inputSignal)
    outputSignal = np.zeros(signalLenght)

    for n in np.arange(signalLenght):
        if n < delay:
            outputSignal[n] = inputSignal[n]
        else:
            outputSignal[n] = inputSignal[n]+filterCoefficient*outputSignal[n-delay]

    return outputSignal


def allpassfilter(inputSignal, filterCoefficient, delay):

    signalLenght = np.size(inputSignal)
    outputSignal = np.zeros(signalLenght)

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


def combFiltersParametersFromReverbTime(reverbTime, combDelays, samplingFreq):
    combeDelaysNrs = np.size(combDelays)
    combFilterParams = np.zeros(combeDelaysNrs)
    for n in np.arange(combeDelaysNrs):
        combFilterParams[n] = 10**(-3*combDelays[n]/(reverbTime*samplingFreq))
    return combFilterParams


#Line 66-71 have to be run before the reverb function, in order to initialise the inputs needed for it

mixingParams = np.array([0.3, 0.25, 0.25, 0.20]) # they need sum to 1
combDelays = np.array([1553, 1613, 1493, 1153]) # they need to be large and have mutually prime numbers
allPassDelays = np.array([223, 443]) # they need to be small
allPassParams = np.array([-0.7, -0.7]) # they need to not be close to 1
reverbTime = 0.7 # by making this bigger, the effect seems stronger
combFilterParams = combFiltersParametersFromReverbTime(reverbTime, combDelays, samplef)

