import serial
import matplotlib.pyplot as plt
from drawnow import *

port = "COM3"
baudRate = 9600
arduinoData = serial.Serial(port, baudRate)

i = 0
tempArray = []
plt.ion()

print("[!]Status port: %s" % arduinoData.isOpen())
print("[!}Port name: %s" % arduinoData.name)


def chart():
    plt.plot(tempArray, 'ro-', label='Graus ºC')
    plt.ylim(-20, 100)
    plt.grid(True)
    plt.ylabel('Temperatura (ºC)')
    plt.xlabel('Tempo (s)')
    plt.legend(loc='upper left')


while True:
    while arduinoData.inWaiting() == 0:
        pass
    arduinoValues = arduinoData.readline()
    temp = float(arduinoValues)
    tempArray.append(temp)
    drawnow(chart)
    plt.pause(.000001)

    print("Graus ªC: %s" % tempArray[i])
    i += 1
