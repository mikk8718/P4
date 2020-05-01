import sounddevice as sd
import scipy.io.wavfile as wave

def createTrack(sliderSong):
    selectedTrack = sliderSong
    return selectedTrack

def createTrack2(sliderSong):
    if sliderSong == 1:
        selectedTrack = Soundfile1
    elif sliderSong == 2:
        selectedTrack = Soundfile2
    elif sliderSong == 3:
        selectedTrack = Soundfile3
    return sliderSong
