import sounddevice as sd
import scipy.io.wavfile as wave

#This comment is added in order to let me push :)

#Tracks are read here
samplingFreq1, signal1 = wave.read("torch.wav")
samplingFreq2, signal2 = wave.read("swords.wav")
samplingFreq3, signal3 = wave.read("somesickassfootsteps.wav")

#Copy is created here
def createTrack(sliderSong):
    if sliderSong == 1:
        wave.write("selectedTrack.wav",samplingFreq1,signal1)
    elif sliderSong == 2:
        wave.write("selectedTrack.wav",samplingFreq2,signal2)
    elif sliderSong == 3:
        wave.write("selectedTrack.wav",samplingFreq3,signal3)