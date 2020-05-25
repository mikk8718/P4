import scipy.io.wavfile as wave

#Tracks are read here
samplingFreq1, signal1 = wave.read("torch.wav")
samplingFreq2, signal2 = wave.read("swords.wav")
samplingFreq3, signal3 = wave.read("footsteps.wav")

#Copy is created here
def createTrack(sliderSong):
    if sliderSong == 1:
        wave.write("selectedTrack.wav",samplingFreq1,signal1)
    elif sliderSong == 2:
        wave.write("selectedTrack.wav",samplingFreq2,signal2)
    elif sliderSong == 3:
        wave.write("selectedTrack.wav",samplingFreq3,signal3)
