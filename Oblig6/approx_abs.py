import numpy as np
import matplotlib.pyplot as plt

def f_sum(x):
    summ = 0
    for i in range (1, 5):
        summ += np.cos((2*i - 1) * x) / (2*i - 1)
        
    return np.pi / 2 - (4 / np.pi) * summ

x = np.linspace(-np.pi, np.pi)

plt.plot(x, f_sum(x), label = "Approximation")
plt.plot(x, np.abs(x), label = "Exact")
plt.legend()
plt.xlabel("negative pi to positive pi")
plt.ylabel("lord jesus")
plt.show()

"""
swapped to english to avoid the three norwegian letters of doom
Run example:
See that the approximation isn't that good. get a graph
"""