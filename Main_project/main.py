import serial
import re


data = serial.Serial("COM3", 115200)


def readInput(string):
    temp = 0
    if "playButton" in string:
        temp = [int(i) for i in string if i.isdigit()]
        print("playButton = {}".format(temp[0]))


    elif "stopButton" in string:
        temp = [int(i) for i in string if i.isdigit()]
        print("stopButton = {}".format(temp[0]))

    elif "selectedTrack" in string:
        temp = [int(i) for i in string if i.isdigit()]
        print("selectedTrack = {}".format(temp[0]))



while True:

    line = data.readline()
    string = line.decode("utf-8")
    #print(type(string))
    #res = [int(i) for i in string if i.isdigit()]
    #print(string)
    readInput(string)


