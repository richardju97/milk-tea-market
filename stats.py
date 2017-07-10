# stats.py
# Contains all the code needed to generate graphs for one store's stats

import matplotlib.pyplot as plt

def generateGraph(data1, label1, data2, label2):
    plt.subplot(2, 1, 1)
    plt.plot(data1)
    plt.ylabel(label1)
    plt.xlabel("Days of Operation")
    plt.subplot(2, 1, 2)
    plt.plot(data2)
    plt.ylabel(label2)
    plt.xlabel("Days of Operation")
    plt.show()
