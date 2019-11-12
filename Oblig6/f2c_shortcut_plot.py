import numpy as np
import matplotlib.pyplot as plt

C = []

C_exact = []
F_list = []
F = -20
while F < 120:
    C_not_precise = (F - 30) / 2
    C.append(C_not_precise)
    C_ex = (F - 32) * (5/9)
    
    C_exact.append(C_ex)
    F_list.append(F)
    F += 1
    

plt.plot(F_list, C, label = "upresis")
plt.plot(F_list, C_exact, label = "presis")
plt.xlabel("Fahrenheit")
plt.ylabel("Celsius")
plt.legend()
plt.show()

"""
Kjore eksempel:
Faar plot med to linjer som krysser hverandre
"""