# stats.py
# Contains all the code needed to generate graphs for one store's stats

import matplotlib.pyplot as plt

def generateGraph(data, label):
    plt.plot(data)
    plt.ylabel(label)
    plt.show()
