import numpy as np
import matplotlib.pyplot as plt
k = 4#kgs^-2
gamma = 0.15#s^-1
m = 9#kg
A = 0.3#m

t_array  = np.zeros(101)
y_array = np.zeros(101)
n = 101
T = 25
#oppgave a)
for i in range(len(t_array)):
    t_array[i] = T/n * (i+1)
    y_array[i] = A * np.exp(-gamma * t_array[i]) * np.cos(np.sqrt(k/m*t_array[i]))



#oppgave b)

t = np.linspace(0, 25, 101)
def y(t):
    return A * np.exp(-gamma * t) * np.cos(np.sqrt(k/m*t))



plt.plot(t_array, y_array, label = "bad way to do it")
plt.plot(t, y(t), label = "decent way to do it")
plt.legend()
plt.xlabel("time")
plt.ylabel("oscilation from time")
plt.show()

#helt lik