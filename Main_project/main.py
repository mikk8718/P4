import serial
import scipy.io.wavfile as wave
from applyReverb import applyReverb
from changePitch import pitch
from createTrack import createTrack
from buttonPlay import buttonPlay, buttonStop

data = serial.Serial("COM3", 115200)
variables = {"reverb": 1,
             "pitch" :1,
             "volume" : 1}

def readInput(string):

    if "selectedTrack" in string:
        trackNumber = [int(i) for i in string if i.isdigit()]
        createTrack(trackNumber[0])

    elif "selectedReverb" in string:
        reverbNumber = [int(i) for i in string if i.isdigit()]
        variables["reverb"] = reverbNumber[0]

    elif "selectedPitch" in string:
        pitchNumber = [int(i) for i in string if i.isdigit()]
        variables["pitch"] = pitchNumber[0]

    elif "selectedVol" in string:
        volNumber = [int(i) for i in string if i.isdigit()]
        variables["volume"] = volNumber[0]

    elif "playButton" in string:
        print(variables)
        samplingFreq, signal = wave.read("selectedTrack.wav")

        signal2 = applyReverb(signal, samplingFreq, variables.get("reverb"))
        signal3 = pitch(signal2, variables.get("pitch"))

        buttonPlay(signal3, samplingFreq)

    elif "stopButton" in string:
        buttonStop()

while True:

    line = data.readline()
    string = line.decode("utf-8")
    readInput(string)



