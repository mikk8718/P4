import serial
import sounddevice as sd
import scipy.io.wavfile as wave
from createTrack import createTrack
from buttonPlay import buttonPlay, buttonStop

data = serial.Serial("COM3", 115200)

def readInput(string):
    temp = 0

    if "selectedTrack" in string:
        trackNumber = [int(i) for i in string if i.isdigit()]
        print("selectedTrack = {}".format(trackNumber[0]))
        createTrack(trackNumber[0])

    elif "selectedEcho" in string:
        trackNumber = [int(i) for i in string if i.isdigit()]
        print("selectedEcho = {}".format(trackNumber[0]))
        #Insert Echo here

    elif "selectedPitch" in string:
        trackNumber = [int(i) for i in string if i.isdigit()]
        print("selectedPitch = {}".format(trackNumber[0]))
        #Insert Pitch here

    elif "selectedVol" in string:
        trackNumber = [int(i) for i in string if i.isdigit()]
        print("selectedVol = {}".format(trackNumber[0]))


    elif "playButton" in string:
        temp = [int(i) for i in string if i.isdigit()]
        print("playButton = {}".format(temp[0]))
        samplingFreq, signal = wave.read("selectedTrack.wav")

        buttonPlay(signal, samplingFreq)

    elif "stopButton" in string:
        temp = [int(i) for i in string if i.isdigit()]
        print("stopButton = {}".format(temp[0]))
        buttonStop()

while True:

    line = data.readline()
    string = line.decode("utf-8")
    #print(type(string))
    #res = [int(i) for i in string if i.isdigit()]
    #print(string)
    readInput(string)



