import numpy as np


#delay, in all the functions, has to be given in amount of samples, not ms!


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


def createCombFiltersParams(reverbTime, combDelays, samplingFreq):
    combeDelaysNrs = np.size(combDelays)
    combFilterParams = np.zeros(combeDelaysNrs)
    for n in np.arange(combeDelaysNrs):
        combFilterParams[n] = 10**(-3*combDelays[n]/(reverbTime*samplingFreq))
    return combFilterParams


def applyReverb(inputSignal, sampleFreq, strength):
    inputSignal = inputSignal/max(inputSignal)
    mixingParams = np.array([0.3, 0.25, 0.25, 0.20])  # they need sum to 1
    combDelays = np.array([1553, 1613, 1493, 1153])  # they need to be large and have mutually prime numbers
    allPassDelays = np.array([223, 443])  # they need to be small
    allPassParams = np.array([-0.7, -0.7])  # they need to not be close to 1

    if strength == 1:
        reverbTime = 0.7
        combFilterParams = createCombFiltersParams(reverbTime, combDelays, sampleFreq)
        return reverb(inputSignal, mixingParams, combDelays, combFilterParams, allPassDelays, allPassParams)

    elif strength == 2:
        return inputSignal

    elif strength == 3:
        reverbTime = 1.2
        combFilterParams = createCombFiltersParams(reverbTime, combDelays, sampleFreq)
        return reverb(inputSignal, mixingParams, combDelays, combFilterParams, allPassDelays, allPassParams)


