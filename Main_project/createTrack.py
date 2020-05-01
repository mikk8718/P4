import sounddevice as sd
import scipy.io.wavfile as wave

#This comment is added in order to let me push :)


samplingFreq1, signal1 = wave.read("testfile.wav")
samplingFreq2, signal2 = wave.read("testfile.wav")
samplingFreq3, signal3 = wave.read("testfile.wav")

def createTrack(sliderSong):
    if sliderSong == 1:
        wave.write("selectedTrack.wav",samplingFreq1,signal1)
    elif sliderSong == 2:
        wave.write("selectedTrack.wav",samplingFreq2,signal2)
    elif sliderSong == 3:
        wave.write("selectedTrack.wav",samplingFreq3,signal3)

