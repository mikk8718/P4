import numpy as np

def pitch(inputSignal, factor):
    if factor == 1:
        indices = np.round(np.arange(0, len(inputSignal)-1, 0.8))
        return inputSignal[indices.astype(int)]
    if factor == 2:
        return inputSignal
    if factor == 3:
        indices = np.round(np.arange(0, len(inputSignal)-1, 1.2))
        return inputSignal[indices.astype(int)]
