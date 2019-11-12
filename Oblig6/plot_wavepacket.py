import numpy as np
import matplotlib.pyplot as plt

def f(x,t = 0):
    return np.exp(-(x - 3 * t)**2) * np.sin(3 * np.pi * (x - t))

x = np.linspace(-4, 4, 9)

plt.plot(x, f(x, 0), label = "wavepacket")
plt.legend()
plt.xlabel("Space")
plt.ylabel("Wave position in space")
plt.show()

"""
Kjore eksempel:
faar en graf
"""